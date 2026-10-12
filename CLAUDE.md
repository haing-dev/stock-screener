# Investor research store

355 investor/CEO interview transcripts plus the fact-checked notes built from them (Doc 1: per-video notes, Doc 2: by topic).
The Google Docs remain the readable copy; this folder is the working copy for search and fact-checking.

## Layout
| Path | What |
|---|---|
| `index.jsonl` | one line per transcript: id, speakers, title, channel, date, url, video_id, collection, category, file, notes, words. **Read this first.** |
| `collections.json` | Drive subfolder -> collection (general, healthcare, macro; crypto + real estate not processed), and which collections feed each screener |
| `transcripts/NNN_Speaker.md` | full transcript, header block + text reflowed to ~350-char lines (grep hits = usable context, `path:line` citations) |
| `notes/doc1/NNN.md` | Doc 1 entry for transcript NNN (same id). `000_index.md` = header + index table |
| `notes/doc2/NN_section.md` | Doc 2, one file per top-level section |
| `notes/doc1_full.md`, `notes/doc2_full.md` | the whole docs as of the last sync |
| `scripts/search.py` | ranked full-text search (SQLite FTS5) over transcripts + notes |
| `scripts/ingest.py` | add new transcripts (dedupes by YouTube id / URL) |
| `scripts/build_db.py` | rebuilds `search.db` (not committed; ~2 s, built automatically on first search) |

## Source folders (Oct 2026)
Google Drive `G:\My Drive\Transcripts\` has one subfolder per collection: `YouTube Transcripts` (general investing),
`Healthcare Transcripts`, `Macro Transcripts` (macro + thematic), `Crypto Transcripts` and `Real Estate Transcripts`
(both skipped for now). Files named only by a YouTube id are older copies of titled files and are skipped.
`collections.json` > `screens` lists which collections inform each screener (e.g. hc_clinical: healthcare;
fortress, cyclicals, trough_cash, real_assets, red_flags: general + macro). Store ids: 1-113 (first batches, now
tagged by folder; 43 and 111-113 sit in Crypto, 50 is no longer in Drive = `archive`), 114-135 healthcare,
136-161 macro, 162-211 general (added Oct 10, 2026), 212-253 BG2 tech/AI podcasts (212-216 macro, rest general; added Oct 10, 2026; JSON insights incl. `tech_screen_ideas` kept outside the repo), 254-355 added Oct 12, 2026 (254-258 healthcare, 259-272 macro, 273-355 general: mostly NBIM's "In Good Company" with Nicolai Tangen, plus Rob Vinall / RV Capital, Kantesaria, Klarman, Bessent x3, Kyle Bass, Cullen Roche, Citrone; highlights cuts end with a link to the full episode; per-talk JSON insights incl. `macro_ideas` and `sector_signals` kept outside the repo).

## Look things up (cheapest first)
1. `grep -i <name> index.jsonl` → which ids.
2. `notes/doc1/NNN.md` → the fact-checked summary for that talk.
3. `python3 scripts/search.py "watsa seagram"` (`--speaker Einhorn`, `--kind transcript|notes`, `--collection healthcare`, `--screen hc_clinical`, `-k 20`, quoted phrases, `NEAR(a b, 10)`) → `path:line` hits.
4. Open the transcript at that line to confirm wording. Quote only what the transcript says (captions misspell names: grep loosely).

## Add new transcripts (always do this BEFORE using them anywhere)
1. Get the files (Google Drive or chat attachments) into a folder; each needs the standard header:
   title line, `Channel:`, `URL:`, `Upload date:`, `Transcript source:`.
2. Get the files: with the desktop app linked, stage them from `G:\My Drive\Transcripts` (device tools), or download from the Drive connector into a folder per collection. `python3 scripts/ingest.py <Transcripts-root-or-subfolder> --dry-run`, then without `--dry-run`. The collection comes from the subfolder name (`--collection` overrides); duplicates are skipped.
3. New rows have `notes: "pending"`, `category: "uncategorized"`. Write the Doc 1 entry, save it as `notes/doc1/NNN.md`,
   set `notes`, `category` and `speakers` in `index.jsonl` (and the transcript header).
4. Only then update Doc 1 / Doc 2 in Google Docs, the screener rules, etc. Commit and push this branch.

Setup: Python 3 stdlib; `pip install python-docx` only for .docx ingest.
