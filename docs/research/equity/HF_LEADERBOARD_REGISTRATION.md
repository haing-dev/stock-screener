# Hedge fund leaderboard (HedgeFollow method, 5 years): registration (2026-11-19)

Requested by the user on 2026-11-18: the top 50 hedge funds by 5-year 13F performance, computed on WRDS the way
hedgefollow.com computes its 3-year table, for US and UK/European filers above $1bn, with their latest activity, and
the numbers checked against the website. A descriptive job: it ranks managers to decide whose transcripts and letters
to look for; it is not evidence for any strategy. It reads US months 2021-2025, which are sealed (plan section 8.2);
it is therefore a logged opening of the seal (`SEAL_LOG.md`), registered here before the job runs.

## Method of the website, established from its own pages (2026-11-19)
From the fund pages' performance data (Jeffrey Gendell / Tontine, read in the browser):
- Each quarter q, the fund's top 20 13F holdings by value at the end of quarter q (ETFs included, options excluded).
- Each holding's PRICE return over quarter q (no dividends: SPY Q4 2023 shown as +11.19%, its price change).
- Manager-weighted (MW) quarter return = sum of weight x return / sum of weights, weights = value at the end of q;
  equal-weighted (EW) = simple mean of the 20 returns.
- The quarters are chained; 3-year return = product of 12 quarters - 1, annualised as (1 + cum)^(1/3) - 1. Check:
  Gendell's 12 published MW quarters compound to +476.52% (79.31%/yr) and EW to +98.25% (25.62%/yr), exactly the
  figures shown on the site.
- Note: the weights are those at the END of the quarter whose return they earn, so the method credits a fund with
  gains it could not have been positioned for at the start of the quarter. It is not investable.

## Our computation (job `eq_hf_v1`, WRDS)
- 13F: `tfn.s34`, first versions (file date = report date), quarter-ends 2020-12 to 2025-12; value = shares x 13F
  price at the quarter-end; top 20 by value. Holdings matched to CRSP by 8-digit CUSIP valid at the quarter-end;
  unmatched holdings are left out and the weights rescaled (the matched share of top-20 value is printed).
- Returns: CRSP `msf_v2` monthly PRICE return (`mthretx`), compounded over the 3 months of the quarter; in a
  delisting month the total return with the delisting return (`mthret`).
- Version HF (the website's method): weights at the end of quarter q, return over q. Quarters Q1 2021 to Q4 2025.
- Version START (what the user described, weights at the time of investment): weights at the end of quarter q-1,
  return over q. Quarters Q1 2021 to Q4 2025.
- Per filer: 5-year (20 quarters) and 3-year (Q1 2023 to Q4 2025) cumulative and annualised return, MW and EW, for
  both versions; Q4 2025 return; S&P 500 (SPY price return, same quarters) as reference.
- Universe: filers whose `s34names` country is the United States, the United Kingdom or a European country, with a
  first-version filing at all 21 quarter-ends 2020-12 to 2025-12, at least 5 holdings at each, and 13F value of at
  least $1bn at 2025-12. Printed: the top 100 by version HF 5-year MW annualised return, with country, 13F value at
  2025-12 and 2026-03, holdings at 2025-12, top-20 weight at 2025-12, all return columns. No holdings, no stock names.
- Ranking to 50 hedge funds: from those 100, filers that are not hedge funds or family offices (banks, insurers,
  pension funds, endowments, broker-dealers, wealth managers, index or ETF sponsors) are removed by name, and the
  removals are listed.
- Check against the website (printed by the job): the version HF quarterly MW and EW returns, Q4 2023 to Q4 2025 (the
  nine quarters both cover), for named validation funds (Tontine/Gendell, Atreides, Whale Rock, Duquesne, Renaissance,
  Slate Path, Spruce House, CAS, Fairmount, Caligan, Greenoaks, Helikon). Compared quarter by quarter with the website.
  Pass: median absolute difference under 1 percentage point per quarter; larger gaps are explained case by case.
- Window: CRSP ends 2025-12 and the WRDS 13F file at 2026-03, so the 5 years are 2021-2025, while the website's
  3 years run to Q3 2026.

## Latest activity (not from WRDS)
For the top 50: the latest 13F (Q3 2026) top holdings and new, added, trimmed and sold-out positions, read from the
public HedgeFollow fund pages in the browser. Nothing stock-level comes from WRDS.

## Job and code (2026-11-19)
Module `tools/equity/wrds/eq_hf.py` (code sha256 04b59fd5b396f7cd...), jobs `eq_hf_pull_v1` (resumable, one SQL
aggregate per quarter-end) and `eq_hf_v1` (report, 3 parts: universe + SPY + validation; ranks 1-125; 126-250).
Smoke test `tests/eq_hf_smoke.py` (invented data; also re-checks the website's Gendell chaining). Registered as the
third seal-exempt job (`seal_exempt.json` entry `hf_leaderboard`); the plan's limit of two (v0.3 section 5.4) is
amended for this user-requested descriptive job. The report prints both weight versions (HF and START) for the
validation funds, so the check settles which one the website uses.

## Correction after the first report (eq_hf_v1, 2026-11-19 08:28 PC)
The check settled the weighting: the website uses the START version (weights from the 13F at the end of the
PREVIOUS quarter, return over the quarter), not the end-of-quarter weights stated above. Atreides: our START MW
equals the website in 8 of 9 quarters (13.3/17.9/-1.1/1.4/30.9/-22.6/24.6/13.2; Q2 2025 41.3 vs 37.0); Duquesne:
7 of 9 (Q2 2024 11.8 vs 10.6, Q4 2025 17.7 vs 14.6). The end-weight version differs in most quarters. So the
ranking is on the START version, which is also what the user asked for (allocation at the time of investment).
Report-only change (`eq_hf` 1.1.0, code 0f78ced5...; pulls unchanged): rank on 5-year START MW, START columns
(5y/3y MW and EW, Q4 2025), end-weight 5y MW kept for reference; validation adds START EW and the name GENDELL.
Job `eq_hf_v2`. The first report (ranked on the end-weight version) is kept in `hf_leaderboard/eq_hf_v1_report.txt`.
