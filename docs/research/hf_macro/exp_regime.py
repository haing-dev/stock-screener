"""Exp 6 (pre-registered 2026-10-29): multi-asset regime book (Dalio/Prince/Karniol-Tambour four quadrants).
Regimes known at t: growth up = the tool's economy-pressure dial (6m avg) below its level 6 months ago (pressure easing);
inflation up = CPI y/y (lagged 1m) above its level 6 months ago. Assets (1975+): S&P (spx), developed ex-US equity
(intl_eq), 10y and 30y Treasuries, 2y, gold, commodities (AQR futures index + T-bill, DBC later), T-bills.
Books:
 Q-theory   fixed quadrant mixes from the transcripts:
            growth up / inflation down  -> 80% equities (60 US / 20 ex-US) + 20% 10y
            growth up / inflation up    -> 50% equities + 25% commodities + 25% gold
            growth down / inflation up  -> 40% T-bills + 30% gold + 30% commodities   (stagflation)
            growth down / inflation down-> 50% 30y Treasuries + 30% 10y + 20% equities (deflationary bust)
 Q-learn    walk-forward: in each quadrant hold the 2 assets with the best average excess return in past months of
            that quadrant (>= 36 months seen, expanding window; else 60/40)
 RP         risk parity (inverse 36m vol) across spx, intl_eq, t10y, gold, commod; RP-T same with each asset held only
            while above its 10m average (else T-bills)
 C5+Q       candidate 5.0 for the equity share, with the non-equity share allocated by Q-theory's non-equity mix
 C5+RP      50% candidate 5.0 + 50% RP-T
Windows 1975-2000 | 2001-2026 | 1975-2026; and 1966-1974 where data exist."""
from robust5 import *  # noqa

g6 = P["g6"]
gu = (g6 < g6.shift(6)).fillna(False)
iu = (cpi_yy > cpi_yy.shift(6)).fillna(False)
Q = pd.Series(np.select([gu & ~iu, gu & iu, ~gu & iu, ~gu & ~iu], ["G+I-", "G+I+", "G-I+", "G-I-"], default="G-I-"), index=grid)
AS = ["spx", "intl_eq", "t10y", "t30y", "gold", "commod"]
MIX = {"G+I-": {"spx": 0.6, "intl_eq": 0.2, "t10y": 0.2},
       "G+I+": {"spx": 0.35, "intl_eq": 0.15, "commod": 0.25, "gold": 0.25},
       "G-I+": {"gold": 0.3, "commod": 0.3},
       "G-I-": {"t30y": 0.5, "t10y": 0.3, "spx": 0.2}}


def W_q():
    W = pd.DataFrame(0.0, index=grid, columns=AS)
    for q, mix in MIX.items():
        for a, w in mix.items():
            W.loc[Q == q, a] = w
    return W


def W_learn(min_n=36, k=2):
    ex = pd.DataFrame({a: R[a] - rf for a in AS})
    nxt = ex.shift(-1)
    W = pd.DataFrame(0.0, index=grid, columns=AS)
    for t in range(T):
        q = Q.iloc[t]
        past = (Q.iloc[:t] == q).values & nxt.iloc[:t].notna().all(axis=1).values   # rows j < t: return of j+1 <= t, known
        if past.sum() >= min_n:
            mu = nxt.iloc[:t][past].mean().sort_values(ascending=False)
            for a in mu.index[:k]:
                W.iloc[t, AS.index(a)] = 1 / k
        else:
            W.iloc[t, AS.index("spx")] = 0.6
            W.iloc[t, AS.index("t10y")] = 0.4
    return W


def W_rp(trend=False, assets=("spx", "intl_eq", "t10y", "gold", "commod"), n=36):
    vol = pd.DataFrame({a: R[a].rolling(n, min_periods=24).std() for a in assets})
    iv = 1 / vol
    if trend:
        up = pd.DataFrame({a: above_ma(a) for a in assets}).fillna(False)
        iv_all = iv.copy()
        w = iv_all.div(iv_all.sum(axis=1), axis=0) * up.astype(float)
    else:
        w = iv.div(iv.sum(axis=1), axis=0)
    return w.fillna(0.0)


Wc5 = build(e5, D_["D7"], X5 if "X5" in globals() else {"gold": 0.1 * ((cpi_yy > 3) & gold_up), "commod": 0.1 * ((cpi_yy > 3) & com_up)}, "L4")
WINS4 = (("1966-02", "1974-12"), ("1975-02", "2000-12"), ("2001-01", "2026-10"), ("1975-02", "2026-10"))
print("quadrant shares 1975-2026:", Q[grid >= Per("1975-01")].value_counts(normalize=True).round(2).to_dict())
print("== CAGR / worst / Sharpe: 1966-74 | 1975-2000 | 2001-2026 | 1975-2026")
print(line("S&P 500", R["spx"], WINS4))
print(line("60/40 S&P/10y (monthly rebalanced)", run(pd.DataFrame({"spx": 0.6, "t10y": 0.4}, index=grid)), WINS4))
print(line("live 4.1", run(W41), WINS4))
print(line("candidate 5.0", r5, WINS4))
wq = W_q()
print(line("Q-theory quadrant book", run(wq), WINS4))
wl = W_learn()
print(line("Q-learn walk-forward (top 2 per quadrant)", run(wl), WINS4))
print(line("RP risk parity", run(W_rp()), WINS4))
wrpt = W_rp(True)
print(line("RP-T risk parity with trend filter", run(wrpt), WINS4))
# C5 equity + quadrant non-equity
nq = wq.drop(columns=["spx", "intl_eq"])
nq = nq.div(nq.sum(axis=1).replace(0, np.nan), axis=0).fillna(0.0)      # non-equity mix of the quadrant (bills if none)
nq_cash = (wq.drop(columns=["spx", "intl_eq"]).sum(axis=1) == 0)
W2 = Wc5.copy()
nonstock = 1 - Wc5.sum(axis=1)                                          # the T-bill part of candidate 5.0
for a in nq.columns:
    W2[a] = W2.get(a, 0.0) + nonstock * nq[a]
print(line("C5 + quadrant mix for its cash", run(W2), WINS4))
for mix in (0.3, 0.5):
    W3 = Wc5.mul(1 - mix).add(wrpt.mul(mix), fill_value=0.0)
    print(line(f"{1 - mix:.0%} C5 + {mix:.0%} RP-T", run(W3), WINS4))
print("\n== quadrant average monthly excess return % (1975-2026), descriptive")
ex = pd.DataFrame({a: R[a] - rf for a in AS}).shift(-1)
m = grid >= Per("1975-01")
print((ex[m].groupby(Q[m]).mean() * 100).round(2).to_string())
print(f"\ntoday: quadrant {Q.iloc[-1]} (growth {'up' if gu.iloc[-1] else 'down'}, inflation {'up' if iu.iloc[-1] else 'down'})")
