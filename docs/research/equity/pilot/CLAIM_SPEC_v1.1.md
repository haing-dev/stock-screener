# Equity investor claims: extraction spec v1.1 (2026-11-27)

v1.1 replaces v1 after the first blind check failed (pilot/verify/SCORE_v1.md): the definitions of rule vs
principle, threshold, value and computable are sharpened (section "Definitions that decide tags"). Logged in
V04_REGISTRATION A13 as a change made after seeing the disagreements.

Gate G2 of plan v0.5 (A10 item 8). One reader extracts claims from one document; a script checks every quote; a
different model re-tags blind (G3). Output: one JSON file per document, a list of claim objects.

## What to extract
Every passage in which the INVESTOR (not the host, not another guest) says how they invest: what they buy, how they
value, what they avoid, when they sell, how they size and build the portfolio, how they research, what mistakes taught
them, and how they describe their own record. Include examples and stories, tagged as such. Skip small talk, biography
without an investing lesson, and market commentary with no bearing on the method (tag it `view` if it is close).
Be exhaustive: a typical one-hour interview gives 40-120 claims.
Some transcripts are auto-captions without speaker labels or punctuation: work out from context who is speaking
(questions and introductions are the host's) and extract only passages that are clearly the investor's; when a
passage's speaker is unclear, leave it out.

## Fields
| Field | Values |
|---|---|
| id | `<DOC>-C<nnn>` in order of appearance (DOC given in the brief, e.g. K065) |
| line | the file line number (1-based, as `grep -n` or the Read tool shows it) where the quote starts |
| quote | VERBATIM text from the document, 8-60 words, one continuous span; do not fix grammar, do not join spans; you may cut at word boundaries only. Leave out `[Lnnn]` markers inside a span |
| speaker | the investor's name as given in the brief (only the investor's words are extracted) |
| kind | `rule` (a general practice he follows), `threshold` (a rule with a number or a clear cut-off), `example` (a company case used to show a rule), `anecdote` (a story without a general practice), `principle` (a belief about markets or business that underlies rules, not itself a practice), `view` (an opinion on a market, sector or company at the time), `mistake` (an error he describes and what he learned) |
| part | `buy` (what qualifies a company), `price` (valuation, when the price is right), `avoid` (what disqualifies), `sell`, `size` (position size, concentration, cash, number of holdings), `process` (research method, time horizon, team), `other` |
| scope | `all` (all holdings), `sector` (name it in `note`), `period` (a market phase), `company` (one company) |
| period_meant | the period the statement is about if not the present (e.g. `2008-09`), else empty |
| computable | `yes` (can be measured from accounts, prices or estimates as stated), `proxy` (only through a stand-in measure), `no` |
| measure | if computable is yes or proxy: a short name of the measure (e.g. `free cash flow yield`, `return on invested capital`, `net debt to EBITDA`, `revenue growth`, `number of holdings`) |
| value | every number in the quote that describes his own practice (selection, price, holding, selling, sizing), as stated with units (e.g. `4%`, `8 to 12`, `30 to 60%`); empty if none |
| direction | for thresholds: `>=`, `<=`, `between`, else empty |
| strength | `always`, `usually`, `sometimes` (how firmly he states it; "we never" = always) |
| note | at most 25 words: anything needed to read the claim (e.g. the company in an example, the sector) |

## Definitions that decide tags
- **rule**: a practice he says he (or his fund) follows: "we buy / we require / we sell when / we never / we hold /
  we look for". Test: it can be rewritten as "his (or her) fund does X" or "...never does X" and names a decision.
- **principle**: a belief about businesses, markets or investors that is not phrased as his own practice ("monopolies
  have pricing power", "the error many people make is...", "sometimes the best thing is to do nothing"). A lesson
  he draws for himself in general words is a principle unless he states what he now does.
- **threshold**: a rule that carries a number for his own selection, price, holding, selling or sizing: a cut-off, a
  target or a typical range ("8 to 12 holdings", "generally 30 to 60% below what it is worth", "cash 0 to 5%").
  How firm it is goes in `strength`, not in the kind. A number in an example or a story is not a threshold.
- **anecdote**: a story or a fact about the past (what happened, what he did once) with no general practice stated.
- **computable** is about a measure of a COMPANY OR ITS STOCK that a screen could use:
  `yes` = measurable from reported accounts, prices or consensus estimates as he states it (free cash flow yield,
  forward free cash flow yield from consensus, organic revenue growth, net debt, market value);
  `proxy` = only through a stand-in (moat, pricing power, durability, management quality, "inflection");
  `no` = not a company measure (team size, watch list, research habits, number of holdings, cash level, his own
  return) or not measurable. Portfolio rules (holdings, cash, position size) are `no` here; `part` = size marks them.

## Rules
1. Quotes are ground truth. A claim whose quote is not found verbatim is dropped by the script.
2. Tag what the quote says, not what you know about the investor.
3. A story about one company is `example` if he draws a general lesson from it in the same passage (put the lesson in
   `note`), otherwise `anecdote`.
4. A number alone is not a threshold: it must be a cut-off he applies ("we want at least ...", "we sell above ...").
5. When unsure between two values, choose the weaker one (`sometimes` over `always`, `proxy` over `yes`, `principle`
   over `rule`, `anecdote` over `example`).
6. Output only the JSON list, UTF-8, in the file named in the brief.
