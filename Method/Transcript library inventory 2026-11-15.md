---
tags: [method, equity, inventory]
status: counts from the catalog, heuristic kinds
---
> Source: repo `docs/research/equity/library_inventory_2026-11-15.md` (commit 466ced5). Counts behind [[Equity pod shop plan v0.3]] (script `tools/equity/library_stats.py`).

# Transcript library: inventory numbers (General Transcripts)

Source: `_system/manifest.json` of the processed library (metadata only, no transcript text). Script: `tools/equity/library_stats.py`. Document kinds and the investor list are heuristics from the catalog's speaker and role fields; step E0.1 of the plan replaces them with a coded inventory.

## Whole library

| Folder | Documents | Words (M) | Tokens (M) |
|---|---|---|---|
| AI CEO Interviews | 883 | 4.48 | 6.31 |
| General Transcripts | 695 | 8.27 | 11.25 |
| Healthcare Transcripts | 431 | 1.76 | 2.42 |
| Macro Transcripts | 214 | 2.29 | 3.05 |
| Banking Transcripts | 24 | 0.18 | 0.24 |
| Media & Entertainment Transcripts | 10 | 0.07 | 0.09 |
| Total | 2257 | 17.04 | 23.36 |

## General Transcripts: 695 documents, 8.27M words, 11.25M tokens

Subfolders: (top level) 635; macro nov 26 60.
Words per document: median 11228, 10th percentile 6147, 90th percentile 18443.

By year of the talk: 2005 2; 2015 1; 2017 5; 2018 3; 2019 4; 2020 1; 2021 3; 2022 51; 2023 103; 2024 146; 2025 214; 2026 133; unkn 29.
Dated 2022 or later: 647 of 695.

Channels (44): The Investor’s Podcast 344; Norges Bank Investment Management 86; The Master Investor Podcast with Wilfred Frost 45; Generating Alpha Podcast 40; Bg2 Pod 37; Bloomberg Podcasts 35; Odds on Open 22; Invest Like The Best 13; Capital Allocators with Ted Seides 9; Sohn Conference Foundation 9; The value investing channel 8; Robert Vinall 5; others 42.

## Document kinds (heuristic)

| Kind | Documents |
|---|---|
| investor present | 327 |
| host only, book or case study | 153 |
| company executive or founder | 123 |
| author, academic or other guest | 92 |

## Investors present (heuristic, a few aliases merged)

Distinct names: 239; appearing once: 191; twice or more: 48; three times or more: 27.

| Investors taken (most documents first) | Documents covered | Words (M) | Tokens (M) |
|---|---|---|---|
| 20 | 104 | 1.46 | 1.98 |
| 40 | 146 | 2.01 | 2.73 |
| 60 | 170 | 2.34 | 3.18 |
| 100 | 202 | 2.89 | 3.91 |
| 239 | 327 | 4.06 | 5.50 |

Most frequent: Tobias Carlisle 15; Hari Ramachandra 12; Robert Vinall 8; Howard Marks 8; Joel Greenblatt 7; Ian Cassel 7; Lyn Alden 7; Chris Davis 7; Mohnish Pabrai 6; Dev Kantesaria 6; Chris Bloomstran 5; François Rochon 5; Guy Spier 4; Jeremy Grantham 4; Dan Sundheim 3; Tom Gayner 3; Connor Haley 3; Bill Nygren 3; Cullen Roche 3; Dmitry Balyasny 3; Andrew Brenton 3; Joseph Shaposhnik 3; Gautam Baid 3; Brian Feroldi 3; Murray Stahl 3; Chris Hohn 3; David Einhorn 3; Arnold Van Den Berg 2; Christopher Begg 2; Dan Rasmussen 2; Robert Hagstrom 2; Nima Shayegh 2; Thomas Russo 2; Samantha McLemore 2; James Ferguson 2; Terry Smith 2; Li Lu 2; Nick Sleep 2; Lawrence Cunningham 2; Derek Pilecki 2.

## Technique topics in the tags and one-line summaries (a document can count in several)

Loose = any word match (also catches 'hedge fund', 'multiple times'); strict = whole phrases only.

| Area | Documents (loose) | Documents (strict) |
|---|---|---|
| portfolio construction and sizing | 178 | 117 |
| valuation | 177 | 168 |
| risk management | 127 | 58 |
| analysis and accounting | 114 | 114 |
| screening and idea sourcing | 79 | 22 |
| short selling | 28 | 28 |
| any of these | 440 | 347 |
