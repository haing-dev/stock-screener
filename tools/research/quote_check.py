"""Quote precision check (v0, 2026-11-02): every quote a reader cites must appear in the source text.
Used on the 15 quant papers: 107/107 found. D0 of docs/research/PLAYBOOK.md generalises this to read claims JSONL
(claim_id, source_id, quote) and the research-branch sources; this copy keeps the matching logic (NFKC, hyphen and
line-break joins, decimal-aware tokens, >=60% word-triple fallback for a 'near' match).
"""
import re, sys, os, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "txt")
Q = {
 "david_harding": ["a very complex process could be partially replicated by a very simple algorithm",
   "the charts not of one market, but of lots of different markets", "providing you were not over-leveraged and you stuck to it",
   "it's not this high short ratio thing", "Forecasting covariance is easy and forecasting return is hard",
   "When too much money is put into something usually it works less well", "one of the ways to compensate for that is to diversify further",
   "There is no fixed system that will work from now to the end of eternity", "trends changed slowly"],
 "david_harding_winton": ["exploit a large number of weak predictive signals", "predictive tools lose their power as markets change",
   "new ones are always needed", "seasonal factors and inventory levels across supply chains", "12.8 per cent, net of fees"],
 "Making-Money-From-Mathematical-Models": ["must be capable of producing empirically falsifiable predictions", "subjected to an unbiased test",
   "ultimately non-parametric and certainly non-stationary",
   "much more realistic to judge the usefulness of models developed some time ago, without prior knowledge",
   "the most ruthlessly honest evaluation"],
 "trendfollowing": ["-0.15", "-0.31", "-0.02", "7.51%", "4.56%", "0.22", "0.72", "0.93"],
 "hsieh_fung_final_paper": ["option-like", "delivers the ex post maximum payout of any trend-following strategy",
   "large and positive during the best and worst", "Currencies appeared to be the instrument of choice, and stock indices attracted the least",
   "no fund had any significant exposure to the stock PTFS", "perform as if they are long 'volatility' and 'market event risk'", "47.9", "-20.4", "13.0"],
 "Economic Trend_": ["For both growth and inflation, we use 12-month changes in GDP growth forecasts and CPI inflation forecasts.",
   "lagged one quarter", "in commodities we use consumption-weighted signals across all themes (i.e., the signals apply to consuming countries of that commodity).",
   "From 1970 through November 1987 risk aversion is represented entirely by 12-month equity market momentum.",
   "allocate equal risk to individual asset views", "3-year trailing covariance matrix", "uses 25 asset class-theme portfolios",
   "gross of fees and transaction costs", "Average Pairwise Correlation: 0.06", "around 0.3 at the asset level and 0.4 for the aggregate composites",
   "one of its worse drawdowns between June 1999 and December 2000"],
 "AQR_Certainly Uncertain": ["-16 percent", "+6 percent", "JLN (t+1) = 0.98 x JLN (t)", "The half-life of shocks to macro uncertainty is around 4 years.",
   "0.6 vs. -0.1 in all other months", "t-stat in excess of seven", "JLN is 0.6 correlated with VIX and 0.5 correlated with realized volatility.",
   "includes economic trends and alternative markets may provide even more robust tail protection, as well as superior average returns.",
   "Timing when you need diversification is a fool's errand.", "below average performance of trend following strategies during that decade"],
 "ValMomEverywhere": ["the return over the past 12 months skipping the most recent month", "in fact stronger when we don't skip the most recent month",
   "the 5-year change in purchasing power parity", "the 5-year change in the yields of 10-year bonds",
   "in proportion to their cross-sectional rank based on the signal minus the cross-sectional average rank",
   "a consistent negative correlation", "within each asset class that averages -0.49",
   "value strategies among bonds can be markedly improved with more thoughtful measures", "of -0.28",
   "the Sharpe ratios to both value and momentum have declined slightly over time", "realized volatility over the full sample"],
 "dissecting-investment-strategies-in-the-cross-section-and-time-series": ["do not therefore account for trading costs", "three on each side",
   "value works well in the cross section, poorly in time series", "carry works about equally well in both",
   "momentum works well in time series, but poorly in the cross section", "with stocks trending higher over the last 25 years, the value factor",
   "was bound to underperform", "the combined portfolio is just the time series portfolio with half of the cross sectional mean hedged out",
   "If a market exhibits a persistent carry premium this will accumulate though the total return and produce a momentum effect",
   "monthly rebalancing and linear signals", "broadly consistent with the daily results", "a Sharpe ratio of close to 2", "has suffered over the last few years"],
 "0902": ["consistently more accurate, but the differences are not statistically significant at the usual levels",
   "will, more often than not, predict a fall in forward rates, due to the fact that unconditionally, the term structure of the forward curve is upward sloping",
   "affected by a credit risk", "persistent blips in the data for December contracts", "49.04", "48.74"],
 "Profiting from Mean-Reverting Yield Curve Trading Strategies": ["trading the yield spread between 10-month and 11-month maturities",
   "by 1990, the 10-year moving average monthly return has fallen below the two benchmarks", "7.3892", "1.2703"],
 "penn_fin_club": ["Very strong presence of outliers as τ nears 0", "A contract for light crude did not trade this day",
   "Strong seasonal pattern for heating oil", "follow a contract over time rather than fixed maturity"],
 "penn_finance_2009": ["Martingale test protects against the 'until it happens' unobserved volatility",
   "compound returns have to exceed 20 during observed period", "A p-value of 1/20 does not overcome adjustments for multiplicity",
   "E(return) - (1/2) Var(return)"],
 "Hard02": ["both stationary and parametric", "simple test of rolling standard deviation through time",
   "many small profits and the occasional large loss", "high Sharpe ratio",
   "the removal of the highest returns from the distribution can increase the Sharpe ratio", "a revival of return as a quality statistic"],
 "Chua et al. - 2010 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns": [
   "one cannot construct a profitable trading strategy to exploit the results in this table",
   "poor (and potentially biased) proxies for expected returns"],
}
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[‐-―−]", "-", s)
    s = re.sub(r"-\s*\n\s*", "-", s)
    s = s.lower()
    s = re.sub(r"(?<=\d)\.(?=\d)", "DOT", s)
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl")
    return [t.replace("DOT", ".") for t in re.findall(r"[a-z0-9τ%+/]+(?:-[a-z0-9τ%+/]+)*|DOT", s)]
tot = ok = part = 0
rows = []
for doc, qs in Q.items():
    toks = norm(open(os.path.join(D, doc + ".txt"), errors="ignore").read())
    joined = " " + " ".join(toks) + " "
    nospace = "".join(toks)
    grams = set(zip(toks, toks[1:], toks[2:]))
    for q in qs:
        qt = norm(q)
        tot += 1
        if " " + " ".join(qt) + " " in joined or (len(qt) <= 2 and "".join(qt) in nospace):
            ok += 1; status = "verbatim"
        else:
            g = list(zip(qt, qt[1:], qt[2:]))
            cov = sum(x in grams for x in g) / len(g) if g else 0
            status = "partial %.0f%%" % (cov * 100)
            part += cov >= 0.6
        if status != "verbatim":
            rows.append((doc[:28], status, q[:80]))
print("quotes checked %d, verbatim %d, near (>=60%% of word triples) %d, not found %d" % (tot, ok, part, tot - ok - part))
for r in rows: print("  %-28s %-12s %s" % r)
