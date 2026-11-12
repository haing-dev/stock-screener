# Rob Carver: ten answers from pack.json

Conventions. Text in double quotation marks is verbatim from a transcript `quote` field unless marked otherwise.
"Summary" = the machine-written `claim` or `conditions` text. "Digest" = `blog_digest`, cited by post id (B..); its
numbers were not checked against the posts, and a "digest quote" is the digest's own `quote` field (not
script-checked). "(reader)" = my own inference or arithmetic. Not used: MT038, whose speaker is "Rob" and whose
correction (MT038-C16-2) says it is that Rob's first time on the show, while Carver appears in earlier-dated sources,
so attribution to Carver is doubtful (reader); and the items whose corrections say Carver is not the speaker
(MT029-C07-4, MT029-C09-1, MT064-C12-1, MT196-C18-3).

## Q1. Information in a few years of results; decay of trend following

(i) Short records are noise for slow systems: "3 to 5 years ... is an insufficient amount of time" for calibration
testing (MT137-C06-3); "10 years isn't necessarily a lot of time" (MT106-C19-X1). Decay: a half-life of "one or two
decades" is "almost impossible to distinguish" from noise (MT140-C07-4); because performance "is not that high to
begin with, it's actually impossible to tell statistically" (MT140-C08-1), and "you still don't see a statistically
significant difference in returns" (MT093-C16-4). Digest B25: average trend return roughly halved since 2010, called
an environment effect.

(ii) Noise statements: ASSERTED. B19 (digest) gives the sampling formula (i.i.d. returns assumed): a Sharpe of 0.5 on
10 years of monthly data has a 25th percentile near 0.29; the same formula gives a standard error near 0.45 for five
years (reader). Decay: SHOWN descriptively in B25, no significance test. Summary only, not in the quotes: "another 50
years" (MT093-C16-4), "decayed gradually over 50-60 years" (MT140-C07-4).

(iii) Weak: B25 is pre-cost, cohorts of 11 and 7 instruments, one author's data, digest unchecked; the rest is
assertion. Whether the decline is permanent: the pack does not show this.

(iv) 3 to 5 years (MT137-C06-3); one or two decades (MT140-C07-4); halved since 2010 (B25); 0.29 (B19).

## Q2. Sizing by current volatility versus fixed-size positions

(i) Carver sizes each position to "a certain ... amount of risk" (MT064-C16-1) and, "if volatility increases", cuts it
"throughout the life of a trade" (MT044-C10-R2). Fixed sizing gives more skew (MT064-C16-3), but "the additional skew
... does not pay you for the loss in sharp, which is substantial" (MT137-C13-2), "assuming you've got leverage"
(MT044-C10-2).

(ii) SHOWN, digest. B31, 37 futures after costs: Sharpe 0.92 with vol targeting, 0.569 without; t-stat on the
difference 3.59; skew 1.08 against 2.46. B22, about 100 futures: Sharpe 1.18 and 1.15 vol-targeted, 0.88 fixed-size;
CAGR at a 30% vol target 36.0% and 35.2% against 25.7% and 25.1%; robust to costs up to about 8x. B21: gross
instrument Sharpe 0.25 against 0.19. B17: at best about 6bp of Sharpe per 5 units of skew. Podcasts: ASSERTED;
MT137-C13-2 carries the summary condition "theory rather than empirical" and MT064-C16-2 relays a third-party study.

(iii) Moderate: three backtests agree (fixed size loses a quarter to two-fifths of Sharpe; reader), two net of costs,
one with a t-stat. But one author's system, backtests only, digest unchecked, B31 has early look-ahead and
outlier-driven skew, B21 is gross of costs.

(iv) 0.92 against 0.569 (B31); 1.18 and 1.15 against 0.88 (B22).

## Q3. Forecast-scaled versus binary positions; scaling and capping of forecasts

(i) Carver turns every signal into "a scaled number" (MT044-C11-4); positions are a "function of two things. The
strength of the trend and the volatility of the instrument" (MT128-C02-1), whereas some CTAs go "from fully short to
fully long" (MT128-C02-X1). Digest: forecasts are scaled to an average absolute value of 10 and capped at +/-20;
position is proportional to forecast/10 (B04, B01). In the podcasts these figures appear only in summaries
(MT044-C11-4, MT093-C07-1). Scaling amounts to a regression coefficient (MT064-C10-1).

(ii) SHOWN, digest. B04: pooled and capped, returns rise across four forecast buckets (adjacent t-stats 10.4, 13.5,
16.0; first to last 35.7); uncapped, slow rules revert in the tails, the reason given for the cap. B22, continuous
against binary, both vol-targeted: Sharpe 1.18 against 1.15; binary did better on EWMAC512 (CAGR 8.2% against 7.1%).

(iii) Moderate that stronger forecasts precede higher risk-adjusted returns (B04: large pooled t-stats; but
overlapping returns overstate them (digest note), 8 instruments fail individually, one author's data). Weak for the
gain over binary (0.03 Sharpe; reader). The correction to MT044-C10-1 says forecast scaling matters more than
volatility adjustment; risk-matched B22 shows the opposite (reader). Unresolved.

(iv) 35.7 (B04); 10 and +/-20 (B04); 1.18 against 1.15 (B22).

## Q4. Constant total risk versus risk that varies with signal strength

(i) Carver lets total risk move with aggregate forecast strength. Live readings: "about a third of my ... long-term
targets" (MT106-C05-3), "about 50 or 60%" (MT093-C05-1), "just under 10% ... just under half" (MT160-C03-1), "a little
bit higher" when the host's trend barometer rises (MT128-C10-X1). Digest B03: expected risk = target x relative
forecast strength x a correlation factor; fixing risk "throws away the information provided by aggregate forecast
strength" (B03 digest quote). Bounds: forecasts capped at twice the average (B04), an overlay that cuts positions once
expected risk exceeds 2x target (B14), and his remark that thinking "your risk is now 90% ... implies you think your
current expected sharp 0.9" (MT044-C11-3).

(ii) SHOWN in B03 (digest): Sharpe 0.93 floating, 0.64 fixed-risk, 0.87 when only the correlation factor is removed;
forecast strength ranged from below 0.2 to above 1.3; fixed risk also made skew more negative. The podcast lines
describe what the system does (ASSERTED). That low-risk spells were followed by weaker live returns: the pack does not
show this.

(iii) Weak: B03 is one hypothetical backtest of one system, 20 instruments, costs approximate (extra trading ignored),
no significance test, digest unchecked.

(iv) 0.93, 0.64, 0.87 (B03); a third of target (MT106-C05-3).

## Q5. Trading costs: budget, too-expensive tests, realised against expected

(i) Budget: "DO NOT SPEND MORE THAN ONE THIRD OF YOUR EXPECTED PRE-COST RETURNS ON COSTS" (B02 digest quote);
elsewhere the limit is 0.13 Sharpe units a year (B11, B26, B27). Too expensive: an instrument costing more than about
0.01 SR per trade is not traded (B06, B26, B29); a rule is dropped on an instrument when turnover x cost per trade
exceeds 0.13 (B11, B26: all six EWMAC speeds need cost below 0.00283, EWMAC64 only below 0.021). Realised: on a 25%
target "I pay about 1%" (MT026-C10-3), 0.04 SR (reader); "just under ... 100 basis points", "in line with" his
backtest (MT196-C13-2); "exactly in line" (MT106-C07-7), where "within one or two basis points" is summary only.

(ii) Thresholds: ASSERTED; B02's digest calls the one-third rule a heuristic. SHOWN (digest): B11, the limit cut cost
drag but lowered net Sharpe in four of five weighting schemes (pooled 0.651 to 0.587; equal weights 0.657 to 0.726);
B26 (160 instruments): gross Sharpe barely rises with cost (R-squared 0.075). Realised costs: self-reported, no data
shown.

(iii) Weak: heuristic limits stated three different ways, a mixed test, one account, digest unchecked.

(iv) One third (B02); 0.13 and 0.01 (B26); about 1% a year (MT026-C10-3).

## Q6. Skipping small position changes (buffering)

(i) The trade-off is being "close to what your optimal position should be" against "the cost of trading to get there"
(MT137-C13-4); hence "either buffering or smoothing" (MT137-C14-2). His rule, on a vol-adjusted position: "if it was
less than 10%, I wouldn't bother trading" (MT026-C08-2). "in theory" the buffer should be wider for expensive
instruments (MT026-C11-1). Digest B13 (dynamic optimisation): a portfolio-level buffer on tracking error; below 0.0125
do nothing, otherwise trade only the share (x - b)/x; buffer and shadow cost (250) come from assumptions, not
calibration.

(ii) Rule: ASSERTED. Turnover: SHOWN only in B27 (digest), S&P 500 alone: raw to buffered 52.6 to 49.8 for EWMAC4 and
10.16 to 7.04 for EWMAC64, about 5% and 31% lower (reader); dynamic optimisation cuts it roughly half to two-thirds,
yet "isn't completely effective" for expensive instruments (B29 digest quote). B13's buffered 114-instrument system
turns over 51 times a year against 37.5 for a static 34-instrument benchmark, not like-for-like. Net return with
against without a buffer: the pack does not show this.

(iii) Weak: one instrument, widths set by assumption, digest unchecked; B13's digest wording "10% of a 25% average
risk target" is not 0.0125 (reader).

(iv) 10% (MT026-C08-2); 10.16 to 7.04 (B27); 0.0125 (B13).

## Q7. Changing trend forecasts with the level of volatility

(i) "when the market's more volatile ... I trade less momentum" (MT010-C15-2). Digest B24's rule: normalised vol =
about one-month EW vol divided by its own 10-year rolling mean; Q = its percentile; forecast multiplier L = 2 - 1.5Q,
so 2 at the calmest and 0.5 at the most volatile (reader); forecasts capped at +/-20. B06 lists vol attenuation in his
system. He will not vary trend speed with VIX: "a prior towards simplicity" (MT010-C16-4). The article he discusses
trades faster in high VIX (MT010-C15-2, summary); B24 finds fast rules suffer most.

(ii) SHOWN (B24, digest). Net Sharpe before to after: EWMAC2_8 0.43 to 0.52, 16_64 1.01 to 1.07, carry 1.07 to 1.11;
paired p 0.00002 (2_8), 0.018 (16_64), 0.176 (carry). Medium-against-high-vol difference: p about 0.00 for every
EWMAC, rising to 0.01-0.14 with a 3-day lag. Explanation: none established (B24); it persists without costs;
commenters suggested vol mean reversion. Carver: "high volatility could mean one of three different things"
(MT010-C16-2).

(iii) Weak: B24 uses his own data, cut-offs chosen by judgement, pooled daily t-tests ignore overlap, gains of
0.04-0.09 Sharpe (reader), three of seven p above 0.05, lag-sensitive, digest unchecked.

(iv) L = 2 - 1.5Q (B24); 0.43 to 0.52 (B24).

## Q8. Sensitivity of a slow trend system to late execution

(i) "a really good test ... is to see what effect has if you delay your fills by one ... business day or even by two
business days" (MT026-C07-1). "even delaying your trades by a day, which is what I test in my backtester, shouldn't
change your results that much" (MT137-C06-2; summary condition: holding periods of about a month). Reason: when
trading slowly, moving the last price by "quite a large amount won't change the desired position that much"
(MT026-C07-2). If the system is sensitive, the summaries say use hourly data or trade more slowly (MT026-C07-1) and
that something is wrong (MT137-C06-2). Neither consequence, nor the "about 0.01" Sharpe threshold, is in the quotes.
Delays of more than a day are an open question (MT137-C17-X1).

(ii) ASSERTED: he says he runs the test; no result is given. A measured effect of delayed fills: the pack does not
show this. Nearest number: B24 (digest), a 3-day lag on the volatility-regime signal lifted p-values to 0.01-0.14, a
signal lag, not a fill delay (reader).

(iii) Assertion: no numbers, one trader's own backtester, and the only threshold is machine-summary text.

(iv) One or two business days (MT026-C07-1); 0.01 Sharpe (MT026-C07-1, summary only).

## Q9. Drawdowns as a test of a strategy

(i) "your drawdown's going to scale with the performance of your strategy and how long you've been running it for"
(MT218-C05-2); "mathematically ... the longer you run any trading strategy ... the bigger your worst draw down will
get" (MT196-C11-2). Rather than compare with the backtest maximum (summary), ask "what's the probability of getting a
draw down this size in say a 12 year trading period ... about a 30% chance" (MT196-C12-1). His own drawdown was the
largest live and "on a par with the biggest ... in my back test, which go back to 1970" (MT044-C03-3). Summary-only
additions: drawdown adds nothing beyond Sharpe (MT218-C05-2); a 50% drawdown would be a real concern (MT196-C12-1);
remove a strategy only on strong evidence of a structural break (MT218-C05-1, whose quote is an unrelated fragment);
drawdown-based timing does not work (MT218-C12-2). He reports weak mean reversion in trend returns (MT160-C02-1) and
weak positive annual autocorrelation (MT044-C21-2): opposite signs, both weak.

(ii) ASSERTED: the 30% comes from a calculation that is not shown.

(iii) Assertion: an argument plus one probability, no derivation, data or test; he also calls Sharpe inappropriate for
negatively skewed strategies (MT140-C05-2).

(iv) About 30% in 12 years (MT196-C12-1).

## Q10. Instrument diversification multiplier; estimating correlations and volatilities

(i) For the diversification multiplier (per summary) "I get numbers of between four and five" (MT128-C11-2); without
multipliers "my volatility drops from 25% to about 8%" (MT144-C07-3), about 3.1x (reader). Digest: IDM set at 2.5,
below the estimated value (B06); about 2.0 in B27. Correlations on "roughly a 6-month window" with an "exponentially
rolling method" (MT026-C11-2, MT128-C12-X1); volatility on "about a 1-month rolling estimate" (MT128-C12-3); "estimate
them separately and then combine" (MT128-C12-1), vol being more predictable: "R squared of about 0.35" month on month
(MT128-C12-2; the 0.2-0.25 for correlation is summary only). Strategy-return correlations (per summary): "as much data
as possible, 10 years" (MT026-C12-3).

(ii) ASSERTED; statistics quoted without sample or method. SHOWN only for blending current with long-run vol (B05,
digest; 70/30 in B06): R-squared 0.884 against 0.84 on the S&P 500, weight fitted in sample. A test of 6 months
against other windows, or of joint against separate estimation: the pack does not show this.

(iii) Weak: multipliers of 2.0, 2.5, 3.1 and four to five are not reconciled; B06's inputs (146 instruments, average
correlation 0.05) imply about 4.2 at equal weights (reader).

(iv) Four to five (MT128-C11-2); 2.5 (B06); 6 months and 1 month (MT128-C12-3); 0.35 (MT128-C12-2).

## Numbers cited

One per line: number | what it measures | id. "Digest" = blog digest figure, not checked against the post. "Summary
only" = the figure is in the machine summary, not in the verbatim quote. "Reader" = my own arithmetic or count.

Q1
- 3 to 5 years | record length Carver calls insufficient for calibration testing | MT137-C06-3
- 10 years | history that "isn't necessarily a lot of time" to judge performance | MT106-C19-X1
- one or two decades | decay half-life he says cannot be told apart from noise | MT140-C07-4
- 2010 | year since which average trend return is roughly halved | B25 (digest)
- half | size of that fall in average trend return, pre-cost | B25 (digest)
- 11 | instruments in the 1972 start group | B25 (digest)
- 7 | instruments in the 1991 cohort | B25 (digest)
- 0.5 | measured Sharpe in the sampling example | B19 (digest)
- 10 years of monthly data | sample length in that example | B19 (digest)
- 25th | percentile of the Sharpe distribution read off in that example | B19 (digest)
- 0.29 | Sharpe at that percentile; the formula reproduces it (reader), but the same digest line also has "25% -> about 17%", which does not fit | B19 (digest)
- 0.45 | standard error of a 0.5 Sharpe on five years of monthly data | reader arithmetic on the B19 formula
- five years | sample length for that standard error | reader arithmetic on the B19 formula
- 50 years | further time needed to know whether trend has degraded; summary only | MT093-C16-4
- 50-60 years | span over which basic trend following is said to have decayed; summary only | MT140-C07-4

Q2
- 37 | futures in the vol-targeting test | B31 (digest)
- 0.92 | Sharpe with vol targeting, after costs | B31 (digest)
- 0.569 | Sharpe without vol targeting, after costs | B31 (digest)
- 3.59 | t-stat on that Sharpe difference | B31 (digest)
- 1.08 | skew with vol targeting | B31 (digest)
- 2.46 | skew without vol targeting | B31 (digest)
- about 100 | futures in the CAGR-race test | B22 (digest)
- 1.18 | Sharpe, vol-targeted with continuous forecast | B22 (digest)
- 1.15 | Sharpe, vol-targeted with binary forecast | B22 (digest)
- 0.88 | Sharpe of both fixed-size systems | B22 (digest)
- 30% | vol target of the risk-matched CAGR comparison | B22 (digest)
- 36.0% | CAGR at that target, vol-targeted continuous | B22 (digest)
- 35.2% | CAGR at that target, vol-targeted binary | B22 (digest)
- 25.7% | CAGR at that target, fixed-size one-entry-one-stop | B22 (digest)
- 25.1% | CAGR at that target, fixed-size reverse-on-signal | B22 (digest)
- about 8x | cost multiple needed to reverse the B22 result | B22 (digest)
- 0.25 | gross instrument-level Sharpe with dynamic vol control | B21 (digest)
- 0.19 | gross instrument-level Sharpe without it | B21 (digest)
- about 6bp | Sharpe worth paying, at best, for the skew change on the next line | B17 (digest)
- 5 units | that skew change | B17 (digest)
- a quarter to two-fifths | share of Sharpe lost by fixed sizing (38% B31; 24-25% B22; 24% B21) | reader arithmetic on B31, B22, B21
- three | backtests that agree (two net of costs, one with a t-stat) | B31, B22, B21 (reader count)

Q3
- 10 | target average absolute forecast | B04, B01 (digest)
- +/-20 | forecast cap | B04, B01 (digest)
- four | forecast buckets in the test | B04 (digest)
- 10.4 | first adjacent-bucket t-stat, pooled and capped | B04 (digest)
- 13.5 | second adjacent-bucket t-stat | B04 (digest)
- 16.0 | third adjacent-bucket t-stat | B04 (digest)
- 35.7 | first-to-last bucket t-stat | B04 (digest)
- 1.18 | Sharpe, continuous forecast, vol-targeted | B22 (digest)
- 1.15 | Sharpe, binary forecast, vol-targeted | B22 (digest)
- 8.2% | EWMAC512 CAGR, binary | B22 (digest)
- 7.1% | EWMAC512 CAGR, continuous | B22 (digest)
- 8 | instruments that fail the bucket test individually | B04 (digest)
- 0.03 | Sharpe gain of continuous over binary (1.18 - 1.15) | reader arithmetic on B22

Q4
- about a third | live risk as a share of long-term target | MT106-C05-3
- about 50 or 60% | live risk as a share of typical level | MT093-C05-1
- just under 10% | live annualised risk | MT160-C03-1
- just under half | that risk as a share of long-term target | MT160-C03-1
- twice | forecast cap as a multiple of the average forecast | B04 (digest)
- 2x | multiple of target risk above which the overlay cuts positions | B14 (digest)
- 90% | risk level in his remark | MT044-C11-3
- 0.9 | expected Sharpe that risk level would imply | MT044-C11-3
- 0.93 | Sharpe with risk floating with forecast strength | B03 (digest)
- 0.64 | Sharpe with risk fixed at target | B03 (digest)
- 0.87 | Sharpe with only the correlation factor removed | B03 (digest)
- below 0.2 | low end of aggregate forecast strength | B03 (digest)
- above 1.3 | high end of aggregate forecast strength | B03 (digest)
- 20 | instruments in that test | B03 (digest)

Q5
- one third | share of expected pre-cost return that may be spent on costs | B02 (digest)
- 0.13 | annual cost limit in Sharpe units; also the per-rule cut-off | B11, B26, B27 (digest)
- about 0.01 | cost per trade (SR units) above which an instrument is not traded; 0.007-0.01 in B26 | B06, B26, B29 (digest)
- six | EWMAC speeds in the test | B26 (digest)
- 0.00283 | highest cost per trade at which all six speeds pass; equals 0.13 / (42 + 4) (reader), although the digest says roll turnover is ignored | B26 (digest)
- 0.021 | highest cost per trade at which EWMAC64 passes; equals 0.13 / (2.1 + 4) (reader) | B26 (digest)
- 25% | his volatility target | MT026-C10-3
- about 1% | annual trading cost he pays | MT026-C10-3
- 0.04 | that cost in Sharpe units (1% / 25%) | reader arithmetic on MT026-C10-3
- just under 100 basis points | annual realised cost, in line with his backtest | MT196-C13-2
- one or two basis points | change in realised cost from the prior year; summary only | MT106-C07-7
- four of five | weighting schemes with lower net Sharpe under the limit | B11 (digest)
- 0.651 | net Sharpe, pooled weights, no limit | B11 (digest)
- 0.587 | net Sharpe, pooled weights, with the limit | B11 (digest)
- 0.657 | net Sharpe, equal weights, no limit | B11 (digest)
- 0.726 | net Sharpe, equal weights, with the limit | B11 (digest)
- 160 | instruments in the speed-against-cost test | B26 (digest)
- 0.075 | R-squared of gross Sharpe on cost, fastest rule | B26 (digest)
- three | different ways the limit is stated (a third; 0.13 a year; 0.01 a trade) | B02, B26, B06 (reader count)

Q6
- 10% | position change below which he does not trade | MT026-C08-2
- 0.0125 | portfolio tracking-error buffer | B13 (digest)
- 250 | shadow cost | B13 (digest)
- 52.6 | S&P 500 annual turnover, EWMAC4, raw position | B27 (digest)
- 49.8 | the same, buffered | B27 (digest)
- 10.16 | S&P 500 annual turnover, EWMAC64, raw position | B27 (digest)
- 7.04 | the same, buffered | B27 (digest)
- 5% | fall in EWMAC4 turnover from buffering | reader arithmetic on B27
- 31% | fall in EWMAC64 turnover from buffering | reader arithmetic on B27
- half to two-thirds | turnover cut from dynamic optimisation | B27 (digest)
- 114 | instruments in the buffered dynamic system | B13 (digest)
- 51 | its turnover, times a year | B13 (digest)
- 37.5 | turnover of the static benchmark, times a year | B13 (digest)
- 34 | instruments in the static benchmark | B13 (digest)
- 10% of a 25% target | digest's description of the 0.0125 buffer; that product is 0.025 (reader) | B13 (digest)

Q7
- one month | span of the vol estimate | B24 (digest)
- 10-year | window of the rolling mean it is divided by | B24 (digest)
- L = 2 - 1.5Q | forecast multiplier, Q = vol percentile | B24 (digest)
- 2 | multiplier at the calmest (Q = 0) | reader arithmetic on B24
- 0.5 | multiplier at the most volatile (Q = 1) | reader arithmetic on B24
- +/-20 | forecast cap | B24 (digest)
- 0.43 | net Sharpe, EWMAC2_8, before attenuation | B24 (digest)
- 0.52 | net Sharpe, EWMAC2_8, after | B24 (digest)
- 1.01 | net Sharpe, EWMAC16_64, before | B24 (digest)
- 1.07 | net Sharpe, EWMAC16_64, after; also carry before | B24 (digest)
- 1.11 | net Sharpe, carry, after | B24 (digest)
- 0.00002 | paired t-test p, EWMAC2_8 | B24 (digest)
- 0.018 | paired t-test p, EWMAC16_64 | B24 (digest)
- 0.176 | paired t-test p, carry | B24 (digest)
- 0.00 | p of the medium-against-high-vol difference, every EWMAC | B24 (digest)
- 0.01-0.14 | the same p-values with a 3-day lag | B24 (digest)
- 3-day | that lag | B24 (digest)
- 0.04-0.09 | Sharpe gain across the seven rules | reader arithmetic on B24
- three of seven | rules with paired p above 0.05 (8_32 0.059; 64_256 0.086; carry 0.176) | reader count on B24

Q8
- one or two business days | fill delay to test | MT026-C07-1
- a day | delay he tests in his backtester | MT137-C06-2
- about a month | holding period the statement applies to; summary only | MT137-C06-2
- 0.01 | Sharpe change above which a system counts as delay-sensitive; summary only | MT026-C07-1
- 3-day | lag on the vol-regime signal (not a fill delay) | B24 (digest)
- 0.01-0.14 | p-values after that lag | B24 (digest)

Q9
- 12 years | horizon of his drawdown probability | MT196-C12-1
- about 30% | probability of a drawdown of the current size over that horizon | MT196-C12-1
- 1970 | start of his backtest | MT044-C03-3
- 50% | drawdown that would be a real concern; summary only | MT196-C12-1

Q10
- four to five | multiplier needed to offset diversification (object per summary) | MT128-C11-2
- 25% | portfolio volatility with the multipliers | MT144-C07-3
- about 8% | portfolio volatility without the multipliers | MT144-C07-3
- 3.1x | multiplier implied by 25 / 8 | reader arithmetic on MT144-C07-3
- 2.5 | IDM as set, below the estimated value | B06 (digest)
- 2.0 | IDM in B27's backtests | B27 (digest)
- 146 | instruments in his system | B06 (digest)
- 0.05 | average correlation of subsystem returns | B06 (digest)
- 4.2 | equal-weight multiplier those two imply, 1 / sqrt(1/146 + 0.05 x 145/146) | reader arithmetic on B06
- 6 months | correlation window | MT026-C11-2, MT128-C12-X1, MT128-C12-3
- 1 month | volatility window | MT128-C12-3
- 0.35 | R-squared of next month's volatility on last month's | MT128-C12-2
- 0.2-0.25 | the same for correlation; summary only | MT128-C12-2
- 10 years | data used for strategy-return correlations (object per summary) | MT026-C12-3
- 70/30 | weights of recent and ten-year-average vol in the vol estimate | B06 (digest)
- 0.884 | vol-forecast R-squared, blended vol, S&P 500 | B05 (digest)
- 0.84 | vol-forecast R-squared, current vol alone, S&P 500 | B05 (digest)
