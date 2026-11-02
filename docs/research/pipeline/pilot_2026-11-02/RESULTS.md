# Pilot 2026-11-02: 5 Macro Transcripts, Sonnet 5.5 (high) extraction vs Opus 5.5 (high) blind read

| Doc | Words | Sonnet claims | Opus claims | Quotes exact (S / O) | Sonnet found % of Opus | Opus found % of Sonnet | Sonnet tokens | Opus tokens |
|---|---|---|---|---|---|---|---|---|
| MT001 van Eck | 7,080 | 68 | 61 | 100% / 100% | 90 | 88 | 110,778 | 114,173 |
| MT002 Systematic Investor 327 | 10,894 | 61 | 72 | 100% / 100% | 78 | 93 | 108,210 | 108,850 |
| MT003 Welton | 10,738 | 56 | 51 | 100% / 100% | 90 | 88 | 113,910 | 122,510 |
| MT004 Guha | 8,370 | 41 | 44 | 100% / 100% | 86 | 93 | 105,814 | 107,296 |
| MT005 gold/silver history | 3,553 | 30 | 29 | 100% / 100% | 100 | 93 | 94,625 | 93,142 |
| Total | 40,635 | 256 | 257 | 513/513 | 87 pooled | | 533,337 | 545,971 |

- Coverage: every chunk listed by both readers; per-chunk counts consistent.
- Agreement measured mechanically (same or adjacent chunk and quote/claim word overlap); misses inspected by hand:
  mostly finer-grained extra claims, some substantive (MT002: structured-product vol supply, illiquid-market trend bias,
  dispersion by trend speed). Neither reader is complete alone: union of the two is the most complete ledger.
- Token overhead: a trivial routing-test subagent used ~79k tokens, so ~75% of each reader's tokens is fixed per-agent
  overhead (system prompt, tools; mostly cached), and the document work is ~15-45k tokens. Batching several documents
  per agent cuts total tokens roughly 2-3x.
- Wall time: 2-4 minutes per reader, all 10 in parallel finished in ~4 minutes.
