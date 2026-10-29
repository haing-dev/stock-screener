"""Filter the 731 transcript hypotheses (all_results.csv) and test survivors with a timing placebo + FDR.
Screen (vs the clean live 4.1 book, 0.2% costs, fixed data):
 long-data hypotheses (signal first on before 1990): Sharpe gain > 0.02 in BOTH 1975-2000 and 2001-2026, full CAGR
   gain >= 0, worst-fall change >= -2 pts;
 short-data ones (first on 1990+): Sharpe gain > 0.02 in BOTH 1997-2011 and 2012-2026, same CAGR/worst conditions.
Excluded up front: paper factors (AQR TSMOM / multi-style: hypothetical, gross), Kim-Wright term premium (re-estimated
on the full sample), never-on hypotheses.
Placebo: the hypothesis' on/off runs reshuffled in time (same counts and run lengths), 200 draws; p = share of draws
whose full-window Sharpe gain >= the real one. Benjamini-Hochberg at 10% over ALL screened-eligible hypotheses
(p = 1 for those failing the screen)."""
import importlib
import sys

import lab
lab.COST = 0.002
import harness as H  # noqa
from harness import *  # noqa

df = pd.read_csv("all_results.csv")
mods = {m: importlib.import_module(m) for m in ["hyp_b12", "hyp_b34", "hyp_b56", "hyp_b7"]}
HY = {h["id"]: h for m in mods.values() for h in m.HYP}
bad_words = ("aqr", "TSMOM", "trend\"", "THREEFYTP10", "Kim-Wright", "multi-style")
import inspect


def is_paper(h):
    try:
        src = inspect.getsource(h["cond"]) + str(h.get("asset", "")) + str(h.get("assets", "")) + (inspect.getsource(h["weights"]) if "weights" in h else "")
    except Exception:
        src = str(h)
    return any(w in src for w in ("\"trend\"", "'trend'", "aqr_", "THREEFYTP10", "trend_cm")) or h.get("asset") in ("trend", "trend_cm") or str(h.get("asset", "")).startswith("aqr")


df["paper"] = [is_paper(HY[i]) if i in HY else False for i in df["id"]]
df["first_y"] = pd.to_numeric(df["first"].astype(str).str[:4], errors="coerce")
df["long"] = df["first_y"] < 1990
df["never"] = df["on_share"].fillna(0) == 0
okl = df["long"] & (df["live_A_dsh"] > 0.02) & (df["live_B_dsh"] > 0.02)
oks = ~df["long"] & (df["live_S1_dsh"] > 0.02) & (df["live_S2_dsh"] > 0.02)
okc = (df["live_F_dcagr"] >= 0) & (df["live_F_ddd"] >= -2)
df["screen"] = (okl | oks) & okc & ~df["paper"] & ~df["never"] & (df["error"].fillna("") == "")
print(f"hypotheses: {len(df)}; errors {(df.error.fillna('') != '').sum()}; paper-factor {df.paper.sum()}; never on {df.never.sum()}; "
      f"pass screen {df.screen.sum()}")
print("by kind passing:", df[df.screen].kind.value_counts().to_dict())

rng = np.random.default_rng(29)


def shuffle_runs(c):
    g = c.values.astype(bool)
    runs, cur, n = [], g[0], 0
    for v in g:
        if v == cur:
            n += 1
        else:
            runs.append((cur, n)); cur, n = v, 1
    runs.append((cur, n))
    ons = [x for x in runs if x[0]]; offs = [x for x in runs if not x[0]]
    a_on = [ons[i] for i in rng.permutation(len(ons))]; a_off = [offs[i] for i in rng.permutation(len(offs))]
    seq, i, j, on = [], 0, 0, rng.random() < 0.5
    while i < len(a_on) or j < len(a_off):
        if (on and i < len(a_on)) or j >= len(a_off):
            seq += [True] * a_on[i][1]; i += 1
        else:
            seq += [False] * a_off[j][1]; j += 1
        on = not on
    return pd.Series(seq[:len(g)], index=c.index)


def full_dsh(h, win):
    W = H.books(h)["live"]
    r = run(H.fallback(W, h))
    return stats(r, *win)["sh"] - stats(H.REF["live"], *win)["sh"]


rows = []
for _, row in df[df.screen].iterrows():
    h = dict(HY[row["id"]])
    win = ("1975-02", "2026-10") if row["long"] else ("1997-02", "2026-10")
    real = full_dsh(h, win)
    if "cond" not in h:
        rows.append((row["id"], real, np.nan)); continue
    c0 = h["cond"]().reindex(grid).fillna(False).astype(bool)
    draws = []
    for _ in range(200):
        cs = shuffle_runs(c0)
        h2 = dict(h); h2["cond"] = (lambda cs=cs: cs)
        try:
            draws.append(full_dsh(h2, win))
        except Exception:
            pass
    p = (np.array(draws) >= real).mean() if draws else np.nan
    rows.append((row["id"], real, p))
    print(f"  {row['id']:<6} {row['kind']:<9} dSharpe {real:+.3f}  placebo p {p:.3f}  {row['desc'][:80]}", flush=True)
pl = pd.DataFrame(rows, columns=["id", "dsh_full", "p"])
df = df.merge(pl, on="id", how="left")
df["p"] = df["p"].fillna(1.0)
# Benjamini-Hochberg over all eligible (not paper, not never, no error)
elig = df[~df.paper & ~df.never & (df.error.fillna("") == "")].copy()
m = len(elig)
elig = elig.sort_values("p")
elig["bh"] = elig["p"].values <= (np.arange(1, m + 1) / m) * 0.10
cut = elig["bh"][::-1].cummax()[::-1]
elig["fdr_pass"] = cut
df = df.merge(elig[["id", "fdr_pass"]], on="id", how="left")
df["fdr_pass"] = df["fdr_pass"].fillna(False)
df.to_csv("all_results_scored.csv", index=False)
print(f"\neligible {m}; pass screen {df.screen.sum()}; placebo p < 0.05: {(df.p < 0.05).sum()}; pass FDR 10%: {df.fdr_pass.sum()}")
cols = ["id", "kind", "desc", "source", "on_share", "first", "live_A_dsh", "live_B_dsh", "live_S1_dsh", "live_S2_dsh", "live_F_dcagr", "live_F_ddd", "dsh_full", "p", "fdr_pass"]
pd.set_option("display.width", 300); pd.set_option("display.max_colwidth", 70)
print(df[df.screen].sort_values("p")[cols].round(3).to_string())
