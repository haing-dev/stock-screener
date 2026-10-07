# Investor research store

113 investor/CEO interview transcripts plus the fact-checked notes built from them (Doc 1: per-video notes, Doc 2: by topic).
The Google Docs remain the readable copy; this folder is the working copy for search and fact-checking.

## Layout
| Path | What |
|---|---|
| `index.jsonl` | one line per transcript: id, speakers, title, channel, date, url, video_id, category, file, notes, words. **Read this first.** |
| `transcripts/NNN_Speaker.md` | full transcript, header block + text reflowed to ~350-char lines (grep hits = usable context, `path:line` citations) |
| `notes/doc1/NNN.md` | Doc 1 entry for transcript NNN (same id). `000_index.md` = header + index table |
| `notes/doc2/NN_section.md` | Doc 2, one file per top-level section |
| `notes/doc1_full.md`, `notes/doc2_full.md` | the whole docs as of the last sync |
| `scripts/search.py` | ranked full-text search (SQLite FTS5) over transcripts + notes |
| `scripts/ingest.py` | add new transcripts (dedupes by YouTube id / URL) |
| `scripts/build_db.py` | rebuilds `search.db` (not committed; ~2 s, built automatically on first search) |

## Look things up (cheapest first)
1. `grep -i <name> index.jsonl` → which ids.
2. `notes/doc1/NNN.md` → the fact-checked summary for that talk.
3. `python3 scripts/search.py "watsa seagram"` (`--speaker Einhorn`, `--kind transcript|notes`, `-k 20`, quoted phrases, `NEAR(a b, 10)`) → `path:line` hits.
4. Open the transcript at that line to confirm wording. Quote only what the transcript says (captions misspell names: grep loosely).

## Add new transcripts (always do this BEFORE using them anywhere)
1. Get the files (Google Drive or chat attachments) into a folder; each needs the standard header:
   title line, `Channel:`, `URL:`, `Upload date:`, `Transcript source:`.
2. `python3 scripts/ingest.py <folder> --dry-run`, then without `--dry-run`. Duplicates are skipped.
3. New rows have `notes: "pending"`, `category: "uncategorized"`. Write the Doc 1 entry, save it as `notes/doc1/NNN.md`,
   set `notes`, `category` and `speakers` in `index.jsonl` (and the transcript header).
4. Only then update Doc 1 / Doc 2 in Google Docs, the screener rules, etc. Commit and push this branch.

Setup: Python 3 stdlib; `pip install python-docx` only for .docx ingest.
