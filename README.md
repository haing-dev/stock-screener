# Stock screener: fourteen screens on SEC filings

Thirteen screens over every NYSE and Nasdaq company, built from what the investors in your interview library
look for. Financials come from SEC filings (10-K, 10-Q, 20-F, 40-F); share prices and FX rates from
Twelve Data. **Every number links back to the filing it came from.**

| # | Screen | What it finds | Main voices |
|---|---|---|---|
| 1 | Core Compounders | Durable, high-return, predictable businesses with pricing power | Kantesaria, Hohn, Dorsey, Terry Smith |
| 2 | Emerging Compounders | Profitable small/mid caps growing 15%+ with operating leverage, little dilution, sensible price | Haley (Alta Fox multibagger study) |
| 3 | Special Situations | Spin-offs, post-bankruptcy companies, recent IPOs - profitable and cheap on EBIT | Greenblatt, Haley, Gaines |
| 4 | Fortress | Earnings that held up in 2020 (and 2009), stable margins, strong balance sheet | Druckenmiller, Hohn, Singer |
| 5a | Healthcare - commercial | Profitable pharma, medtech, tools, services, insurers with durable returns | Terry Smith, Chen, Flynn |
| 5b | Healthcare - pre-revenue & clinical | Biotech/medtech valued near or below its cash, with 2+ years of runway | Johnson (Caligan), Chen, Greenblatt |
| 6 | Capacity-cycle Cyclicals | Good businesses in cyclical industries at low points of their own cycle, cheap on cycle-average earnings | Druckenmiller, Haley, Greenblatt |
| 7 | Owner-Operators | Profitable, high-return companies where insiders own 20%+ (1 - reported public float / market value on the float date) | Stahl, Haley, Watsa |
| 8 | Hard Assets & Royalties | Land, mineral, royalty, water, timber and pipeline owners with capex under 20% of operating cash flow and 30%+ margins | Stahl, Alfred, Einhorn |
| 9 | Asset-Floor Value | Market cap at or below net cash, or price at or below tangible book; not burning cash; usually profitable | Watsa, Greenblatt, Davis |
| 10 | Trough Cyclical Cash | Cyclicals at depressed margins with a 10%+ cycle-average FCF yield, not adding capacity | Einhorn, Druckenmiller |
| 11 | Hidden Earnings | Profitable companies that just sold or spun off a unit, or trade 40%+ below their 12-month high | Einhorn, Stahl, Sandler, Greenblatt |
| 12 | Red Flags (**avoid list**) | Priced at 6x+ sales AND at least two deterioration signals (fading growth, falling margins, losses, dilution, shrinking sales) | Einhorn, Sandler, Marques, Nadella, Cohen |

Screens 7-12 come from the second batch of interviews. On them, a defining rule that couldn't be checked (e.g. an
insider stake that couldn't be measured) keeps a company off the near-miss lists: it goes to 'Check manually' if
nothing fails, else it fails.

## How each company is classified (per screen)

- **PASS** - every rule passes and the data looked clean. Ranked by a composite score.
- **CHECK manually** - nothing fails, but something is missing or doubtful (an untagged figure, a price or
  market-cap check that failed, a revenue tag change...). These are *potential* candidates: the reason is
  written next to each one. **Missing data never silently removes a company.**
- **NEAR miss** - failed exactly one rule by less than 20%.
- **Price too high (rest passes)** - every business rule passes; only the valuation rule fails (Emerging,
  Cyclicals). Revisit when the price drops.
- **Failed 1 rule** - exactly one business rule failed by a wider margin (e.g. FICO: more debt than Core allows)
  and every other rule was verified. Judge whether that rule matters for this company. Not used for a screen's
  defining test (Emerging growth and profitability, Fortress recession tests, Special Situations profit and
  cheapness, Clinical runway/debt/price-vs-cash, Healthcare returns, Cyclicals mid-cycle returns and peak
  margins) or tradeable size/volume.
- **FAIL** - everything else. `All_Companies` shows which rules failed (e.g. `FAIL: G5a G8`; codes on the Rules
  sheet).

All four middle lists are on each screen's "- watch" sheet, so a strong company is never lost to one rule.

**Quality warnings** (a would-be PASS goes to CHECK with the note): Core, Fortress, Healthcare and Emerging -
operating margin over the last 12 months less than half its 10-year median ("temporary or permanent?"); Core,
Fortress, Healthcare - revenue shrinking more than 2%/yr over 3 years ("cyclical dip or structural decline?");
Core - lost money in 2008-09 while sales fell (a cyclical at a good point of its cycle?).

Data-quality checks that move a company from PASS to CHECK: an unexplained revenue jump where the XBRL tag
changes (inside the 10-year window), a changed fiscal year-end, several reporting currencies, a value taken from
a non-standard tag, debt that seems to be missing (an interest bill implying material untagged debt), possible
Chapter 11, income data much older than the balance sheet, a filed annual report that isn't in SEC's XBRL data
yet (common for some foreign 20-F filers), and any failed price check (wrong exchange/currency, stale quote,
share count that doesn't fit the public float even at the price on the float date, ADR ratio unknown, quote name
not matching the SEC name).

Handled automatically (with a note in Flags):
- **Revenue**: when a company puts part of its revenue (or zero) on the preferred tag in some years, the figure
  consistent with neighbouring years is used (Flowserve, Applied Industrial, Hershey); with no revenue tag at all
  revenue = gross profit + cost of sales (Novartis, Sanofi). A profitable company whose revenue can't be found is
  *not screened* (listed with the reason) instead of being treated as 'revenue = 0'.
- **EBIT**: with no operating-income line in the latest year, EBIT = pretax income + interest - other
  non-operating income for every year (J&J, Lilly, ADP, TJX); no pretax tag -> net income + tax (Range Resources).
- **Capex** missing in some years: the company's median capex / revenue from the other years.
- **Interest** not tagged: coverage tested at a worst-case 10% rate on all debt (Apple).
- **Recession tests**: net income is the fallback when revenue/operating income for 2008 isn't in XBRL; an
  operating or net loss in a recession year fails; a company listed then with no 2008-09 data is 'check manually'.
- **Market cap**: share count from net income / diluted EPS when it is only tagged per share class (Visa); foreign
  issuers listed as ordinary shares (not ADRs) are recognised from Twelve Data's listing type; a big price move
  since the public-float date is checked with the price on that date (Zoetis, Pool, Ubiquiti).
- New holding companies whose history sits under the old CIK (ExxonMobil Holdings -> Exxon Mobil Corp); share
  dilution after IPOs/spin-offs is measured only after the listing.
- Companies that can't be screened say why in `All_Companies` (e.g. Canadian 40-F filers without XBRL statements
  such as Canadian National; new registrants after a reorganization such as Expro).

## Web portal (GitHub + Cloudflare)

The screener runs itself in GitHub and publishes a password-protected website (Cloudflare Pages):

| When | What (GitHub Actions) |
|---|---|
| 1st and 16th of each month | **Screen**: every NYSE + Nasdaq company from SEC filings, priced, all fourteen screens. Only companies that filed since the last run are re-downloaded (SEC daily index); a full refresh uses SEC's nightly bulk files |
| Weekday mornings | **Daily prices**: end-of-day open/close for every company (Massive), screens re-applied; skipped when there is no new trading day, and the site is republished only when something changed |
| Every day | **Background**: slow fills within API budgets - 52-week ranges, 10-year month-end prices (Twelve Data, once per company, then extended from Massive), 13F holders and buyers/sellers (quarterly), insider trades (quarterly), and 2-3 line company descriptions by Claude (written once, for listed companies and their peers) |

On the site: one page per screen with a rules table (rule, criteria, rationale, on/off switch; +n = companies that
would join without it), two lists (Pass; Near misses, each with the rule it missed or what to check by hand) and the
same columns everywhere: price vs open, 52-week range, industry, P/E, EV/EBIT, FCF yield, ROIC (10-year median) and
5-year revenue CAGR. Each company has its own page: what it does, valuation against its 10 closest peers and its own
3- and 10-year average multiples (information only), ownership (top 13F holders with the share of each holder's
portfolio, biggest buyers and sellers since the previous quarter, insider open-market buys and sales over 3 quarters),
and a button that builds an Excel file with its income
statement, balance sheet, cash flow and a metrics page (up to 10 years, from SEC filings, built in the browser).
Local preview with demo data: `python tests/demo_portal.py OUT_DIR`, then serve OUT_DIR.

**Secrets** (repository Settings > Secrets and variables > Actions): `SEC_USER_AGENT` (your name and email),
`MASSIVE_API_KEY`, `TWELVEDATA_API_KEY`, and either `ANTHROPIC_API_KEY` (from console.anthropic.com, pay per use) or `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`, uses your Claude
subscription), `PORTAL_PASSWORD`. None of them is ever written to the repository or the site.

**Privacy**: the site's data files are encrypted (AES-256-GCM, key derived from `PORTAL_PASSWORD` with PBKDF2);
the page decrypts them in your browser. Changing the password: update the secret, then run **Daily prices** by hand.

**Run by hand**: Actions > Screen (or Daily prices) > Run workflow. The workbook of each screen run is attached to
that run (Artifacts: screen-results) for 30 days.

**Settings**: `config.json` > `portal` (descriptions per run, Claude model, peer group size, price-history budgets:
Massive requests for 52-week ranges and Twelve Data credits for month-end price history per run). Thresholds are the
same `config.json` keys as before.

Commands used by the workflows: `python screener.py portal-screen | portal-daily | portal-summaries --max N |
portal-export`.

## Setup (once)

1. Python is already installed. Your SEC name/email and your Twelve Data key are in `local_settings.json`
   (private - never share or upload it).
2. Double-click **`0_SETUP_CHECK.bat`**. It checks access to the SEC and Twelve Data, shows your Twelve Data
   plan limits, and compares a few numbers with Apple's and Microsoft's annual reports. Send Claude the output
   if anything says FAIL.

## Run it

| Step | Double-click | What happens |
|---|---|---|
| 1 | `1_TEST_RUN.bat` | All fourteen screens on ~50 well-known companies -> `output\test_results.xlsx` |
| 2 | `2_RUN_ALL_SCREENS.bat` | Every NYSE + Nasdaq company -> `output\screen_results_<date>.xlsx` + `_evidence.csv`. The first run re-downloads SEC data (new format, 30-50 min). |
| 3 | `3_MAKE_AI_PACK.bat` | Pick a screen; downloads the top companies' latest annual reports and builds a blind evidence pack for Claude's review |
| 4 | `4_VERIFY_QUOTES.bat` | Checks every quote in Claude's review word-for-word against the filing |
| - | `CHECK_ONE_COMPANY.bat` | Every rule of every screen for one ticker, with the evidence |

**Twelve Data credits.** Only companies that already pass a screen's financial rules are priced (about 900),
the ones whose result depends on the price first. The free plan allows 8 per minute and 800 per day, so a full
run can spread over two days: run it again the next day and it continues (quotes are cached for 3 days). A paid
plan finishes in one go.

## The workbook

| Sheet | Use it for |
|---|---|
| Read_Me | Run details; counts per screen |
| Overlap | Companies passing several screens - the strongest signals |
| 1 Core ... 12 Red flags (avoid) | Ranked PASS list per screen, with pillar scores and key metrics (on Red flags, PASS = flagged) |
| ... - watch | CHECK manually + NEAR misses, each with the reason |
| Events | Every spin-off / bankruptcy / IPO found, pass or not |
| Industry_Cycle | Each cyclical industry's aggregate margin vs its 10-year range |
| Peak_Margins (check) | Margins far above their own history right after a revenue surge - structural (keep) or cyclical peak (avoid)? (Druckenmiller) |
| Data_Gaps | What's missing for CHECK companies, and candidate XBRL tags found in the filing |
| All_Companies | Every company and its status on each screen |
| Annual_Data | The yearly figures behind each listed company |
| Rules | Every rule, its threshold (config.json key) and the investor insight behind it |
| Industry_Groups | SIC code ranges used by each screen |

`screen_results_<date>_evidence.csv`: every input value with its XBRL tag, period, filing and link.

## Industries

Banks, insurers, brokers, asset managers, real estate, funds, utilities, telecom carriers, broadcasting & cable,
newspapers, ad agencies, airlines and commodity producers are excluded from Core/Emerging/Fortress (see
`config.json` `exclude_sic` and the Industry_Groups sheet); commodity and transport cyclicals are covered by the
Cyclicals screen. Special Situations excludes only balance-sheet businesses (banks, insurers, crypto treasuries,
funds, REITs) - EV/EBIT means nothing for them. Auto-parts retailers and auctions (O'Reilly, AutoZone, Copart)
are screened. To screen a company whose SEC industry code is excluded but doesn't describe the business, add it
to `screen_anyway` in `config.json` (Morningstar and MarketAxess are there). Owner-Operators uses Core's industries;
Hard Assets & Royalties looks only at land, mineral, royalty, water, timber and pipeline codes; Asset-Floor Value,
Hidden Earnings and Red Flags look at every operating company outside banks, insurers, funds and real estate
(Red Flags also leaves out pre-revenue drug developers, which burn cash by design).

Past prices: insider share needs the close on each company's public-float date, and Hidden Earnings needs the
12-month high. With Massive (the portal) both come from Massive's all-stocks daily files (one request per date,
re-downloaded every 12 days so splits are adjusted); a local run uses Twelve Data (its 52-week high, and up to 120
float-date prices per run).

## Rules

All thresholds are in `config.json` (`screens.<name>`; Core uses the top-level keys and `gates`). The Rules
sheet prints each one with its source. Key definitions:
- **ROIC** = operating income x (1 - tax rate) / average invested capital (assets - cash and investments -
  non-interest-bearing current liabilities). **Cash ROIC** uses free cash flow.
- **TTM** = latest fiscal year + latest year-to-date - prior year-to-date (from 10-Qs, same XBRL tag).
- **Market cap** = Twelve Data price x SEC share count (cover page; summed across share classes), checked
  against the public float the company reported. **EV** adds debt, minority interest, preferred; subtracts cash.
- **Recession tests** compare fiscal years ending Mar-2020..Jun-2021 and Sep-2008..Mar-2010 with the year before.
  An operating loss in either window fails. Missing 2008-09 data is 'check manually' for cyclical industries.
- **Cycle position** = where the latest operating margin sits in the company's (and its industry's) own
  10-year range.

## Self-test

`python tests/run_tests.py` runs 162 checks: synthetic companies built to land on each list of each screen,
price/market-cap validation, and real SEC data (Apple, Microsoft, Visa, Mastercard, Costco, Moody's, ADP, ODFL,
S&P Global, Coca-Cola, Intel...) checked against figures in their annual reports, plus a check for each
issue found in the live runs (Lam/D.R. Horton 2009 losses, TSMC late XBRL, FICO, Sandisk, Astera Labs, Allogene,
ExxonMobil Holdings, Flowserve, Applied Industrial, Novartis, TJX, Range Resources, Toll Brothers, Pool...).

## Limitations

- Companies that use their own XBRL tags can miss a figure: they land on CHECK with the reason, never dropped.
- ROIC flatters asset-light software (code is expensed) - Dorsey. Emerging uses gross profit / tangible assets.
- Only currently listed NYSE/Nasdaq SEC filers (survivorship; no non-US-only listings).
- SIC codes are coarse; industry groups are approximations.
- Moats, management, patents, clinical pipelines and AI disruption need the AI + human review (step 3).
- A research filter to decide what to read next - not a buy list, and not financial advice.
