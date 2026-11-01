# Macro research playbook (v1, 2026-11-02): definitive workflow

Scope: the "pod model" research program (project "macro tool"). One person who does not code + Claude sessions on a
subscription with usage limits. Everything below is designed around that limit: cheap models for volume, the
scarcest model only on compressed inputs, scripts wherever a model is not needed.

## 1. Session types and model routing
| Session | Model | Does | Never does |
|---|---|---|---|
| E extraction | Sonnet 5.5 (API batch in GitHub Actions preferred; else Sonnet subagents from a Sonnet-orchestrated session) | one document -> claim records + coverage checklist, fixed schema | judge importance, design strategies |
| V verification | scripts (no model) + Opus 5.5 second reader on a 20% sample and on every paper | quote precision 100% check; blind second read; agreement score | change the ledger by hand |
| J judgement | Fable 5.1 | must-catch lists before extraction; adjudicate disagreements; mechanism synthesis; investor x mechanism patterns; pod candidates; register protocol batches; review results; white paper | read raw transcripts in bulk; run code |
| B build/test | Opus 5.5 | data adapters, pods, protocol batches, diagnostics, audits | adopt anything outside TESTING_PROTOCOL |
| M monthly ops | Sonnet 5.5 (or Actions, no model) | paper book run, ledger append, vault counters | design changes |

Why: Anthropic's own guidance is Sonnet for the large majority of execution, Opus for deeper reasoning, and Opus costs
several times more per turn than Sonnet (support.claude.com, "Models, usage, and limits in Claude Code"). Fable is
the scarcest tier: it reads the ledger (kilobytes), not the documents (megabytes).

## 2. Session contract (every session, any model)
1. Read `docs/research/PLAYBOOK.md` (this file) and the research branch `STATUS.md` (counters: listed / extracted /
   quote-checked / second-read / adjudicated per collection; open batches; next stage).
2. Do exactly ONE stage (the user types the stage key: `E next`, `V last`, `J <collection|topic>`, `B batch <n>`,
   `M monthly`). No stage mixes models; no stage skips the ledger.
3. Append-only outputs (claims, trials, ledgers); commit; update `STATUS.md`; end with the next stage key.
4. Hard rules unchanged: no holdout (2011-2026) inspection; no WRDS data into any model; keys stay in secrets.

## 3. Document universe and order
412 documents: 397 transcripts (research branch `transcripts/`, notes in `notes/doc1/`) + 15 quant papers
(to be copied into research branch `papers/`). Order: macro collection (57) and the "Quant & systematic" and
"Macro & markets" categories + all papers first (they feed the Bloomberg pull list before the UBC trip), then energy and
banking, then general, then healthcare, consumer, media. AI / industrial folders: only if the user says so.

## 4. Extraction schema (one JSONL row per claim; vault notes are built from it)
`claim_id, source_id, speaker, position (chunk n of N | page/exhibit), quote (verbatim, <= 40 words), claim
("X means Y because Z"), mechanism (taxonomy id or "new: ..."), asset_class, indicator (exact series/name if given),
horizon, direction, conditions (regime, when it fails), testable (yes/partly/no + why), speaker_confidence,
time_bound (yes/no), related_rule (existing rule id)`.
Per document: 3-line approach summary; approach tags; COVERAGE table = every chunk (transcripts: ~700-word chunks)
or every section/table/exhibit (papers) marked `claims: n` or `nothing actionable: <reason>`. A document without a
complete coverage table is not "read".

## 5. Verification (pre-registered thresholds)
- Precision: every quote found in the source text by `tools/research/quote_check.py` (OCR for scans). Any
  fabricated quote -> that document is re-extracted; two in a collection -> the collection is re-run.
- Recall: blind second read (Opus, no sight of the first extraction) on a random 20% of transcripts and 100% of
  papers; agreement = share of second-reader claims matched by the first reader. Threshold 0.8; below it the
  collection is re-extracted with Opus. Must-catch lists (Fable, written from the Doc 1 notes BEFORE extraction for
  the 30 most important documents): at most 1 miss per document on average.
- Disagreements adjudicated by Fable against the text; adjudications logged.

## 6. Knowledge vault (research branch = Obsidian vault)
`vault/sources/` (one note per document: status, links to transcript/paper, doc1 note, claims), `vault/claims/`
(one note per claim, wiki-linked), `vault/mechanisms/` (taxonomy v1 seeded from docs/research/hf_macro hypotheses,
docs/criteria workbook, gap reviews: slow reaction, risk premium, cycle persistence, overshoot, liquidity/flows,
policy reaction, crowding, seasonality, ...), `vault/pods/`, `vault/tests/`, `vault/data/`, plus Dataview tables:
claims by mechanism, untested claims, investor x mechanism matrix, sources not yet verified. Google Docs Doc 1/2 stay
as readable copies; the vault is the working copy. MSCI/Bloomberg/WRDS data never enter the vault.

## 7. Two-week schedule (calendar days; stage keys in brackets)
- D0 [B]: pipeline (prep, extract runner, quote check, coverage, vault builder, STATUS.md); copy papers in;
  calibrate on 10 documents (tokens, cost or usage, agreement). Decide API vs subscription route from the numbers.
- D1 [J]: must-catch lists (top 30); mechanism taxonomy v1; freeze schema v1 (changes after this = v2, logged).
- D2-D4 [E, V]: extract everything (API batch: 1-2 nights; subscription: ~40/day, usage permitting), quote checks,
  second reads on the sample and papers. Macro + quant + papers done by D3 so [J] can update the Bloomberg list.
- D5-D6 [J]: adjudicate; recall scores; re-extract what fails; Bloomberg pull list v4 issued before the UBC trip.
- D7-D9 [J]: synthesis: mechanism notes, investor x mechanism patterns, recurring approaches, pod candidates (each
  with mechanism, indicator, data, expected correlation to the book), data wishlist with prices.
- D10-D11 [B]: register batch 2 (Bloomberg) and batch 3 (free-data pods) in TESTING_PROTOCOL.md BEFORE running;
  build adapters; add the program-level error budget (protocol section 7).
- D12-D14 [B then J]: run batches; diagnostics; review; white paper update; freeze decision for gm-2.0.
Fallback: if usage does not allow 40/day on the subscription route, switch to the API route or extend to 4 weeks;
the order in section 3 guarantees the macro core is covered first either way.

## 8. Guardrails carried over
TESTING_PROTOCOL.md governs every adoption; selection inflation (~0.25 SR at 32 variants) is reported with every
result; allocation/timing rules are validated only on the live paper record; holdout criterion decided before freeze.
