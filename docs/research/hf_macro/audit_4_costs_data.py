"""Audit 4: costs/turnover; Yahoo dating error in non-US index and FX files (country proxies); misc data checks."""
import os
import re
import numpy as np
import pandas as pd
from audit_lib import *  # noqa

RD = "/home/claude/stock-screener/cache/macro/raw/research"
r5, e5, W5 = cand()
r0 = live()

# ---------------------------------------------------------------- costs
print("== costs")
Wl = X.W_from(X.e41, X.live_def)
for nm, W in (("live 4.1", Wl), ("candidate 5.0", W5)):
    t = W.reindex(grid).fillna(0).diff().abs().sum(axis=1)[grid >= Per("1975-02")]
    print(f"  {nm:14s} one-way turnover {t.sum() / (len(t) / 12) * 100:.0f}% of book per year")
Ws = W5[[c for c in W5.columns if c.startswith("sec_")]]
ts = Ws.diff().abs().sum(axis=1)[grid >= Per("1975-02")]
print(f"  of which sector tilt {ts.sum() / (len(ts) / 12) * 100:.0f}%/yr")
for c_ in (0.001, 0.003, 0.005):
    rc = cand(cost=c_)[0]
    rl = run(Wl, cost=c_)
    rcd = cand(cost=c_, drift_cost=True)[0]
    print(f"  cost {c_*100:.1f}%: candidate {stats(rc)['cagr']:.2f}% (with drift rebalancing {stats(rcd)['cagr']:.2f}%) | live {stats(rl)['cagr']:.2f}%")
# sector proxies before ETFs: what share of the tilt's months is pre-ETF (French industry proxies, not tradeable)?
src = P["src"]
pre_etf = (src != "etf").sum(axis=1)
m = (grid >= Per("1975-02"))
print(f"  months 1975+ with >= 10 of 20 sectors on French proxies: {int((pre_etf[m] >= 10).sum())} of {int(m.sum())}")
tilt_ret = (W5[[c for c in W5.columns if c.startswith('sec_')]].shift(1).fillna(0) *
            R0[[c for c in W5.columns if c.startswith('sec_')]].fillna(0)).sum(axis=1)
for a, b in (("1975-02", "2000-12"), ("2001-01", "2026-10"), ("2006-07", "2026-10")):
    mm = (grid >= Per(a)) & (grid <= Per(b))
    print(f"  sector tilt active return {a}..{b}: {tilt_ret[mm].mean()*1200:+.2f}%/yr gross")
# KBE / KRE identical before the ETFs (both = French 'Banks')
same = (R0["sec_KBE"] == R0["sec_KRE"]) & R0["sec_KBE"].notna()
print(f"  months where KBE and KRE returns are identical (shared proxy): {int(same.sum())} (to {grid[same.values][-1]})")

# ---------------------------------------------------------------- Yahoo dating
print("\n== Yahoo monthly bars stamped at local midnight -> UTC date in the PREVIOUS month")


def y_auth(sym):
    p = os.path.join(RD, "Y_" + re.sub(r"[^A-Za-z0-9]", "_", sym) + ".csv")
    s = pd.read_csv(p)
    s = s[pd.to_numeric(s["value"], errors="coerce").notna()]
    d = pd.to_datetime(s["date"])
    return pd.Series(s["value"].astype(float).values, index=d.dt.to_period("M")).groupby(level=0).last().reindex(grid)


def y_fix(sym):
    p = os.path.join(RD, "Y_" + re.sub(r"[^A-Za-z0-9]", "_", sym) + ".csv")
    s = pd.read_csv(p)
    s = s[pd.to_numeric(s["value"], errors="coerce").notna()]
    d = pd.to_datetime(s["date"])
    last = d.iloc[-1]
    d = d.where(d == last, d + pd.Timedelta(days=2))          # bar stamped 31st 15:00 UTC = next month's bar
    return pd.Series(s["value"].astype(float).values, index=d.dt.to_period("M")).groupby(level=0).last().reindex(grid)


# documented anchors: KOSPI closed 1996 at 651.22; Nikkei closed 1984 at 11,542.60 and Jan-1985 at 11,992.34
print(f"  ^KS11 value for 1996-12: author {y_auth('^KS11').get(Per('1996-12'))}, fixed {y_fix('^KS11').get(Per('1996-12'))} (true Dec-1996 close 651.22)")
print(f"  ^N225 value for 1985-01: author {y_auth('^N225').get(Per('1985-01'))}, fixed {y_fix('^N225').get(Per('1985-01'))} (true Jan-1985 close 11992.34)")
for sym in ("KRW=X", "JPY=X", "INR=X"):
    a, f = y_auth(sym), y_fix(sym)
    mm = grid >= Per("2005-01")
    print(f"  {sym}: author has {int(a[mm].isna().sum())} missing months since 2005 (each October), fixed {int(f[mm].isna().sum())}")

FXd = {"KRW": "DEXKOUS", "BRL": "DEXBZUS", "INR": "DEXINUS", "MXN": "DEXMXUS"}


def fred_me(sid):
    s = pd.read_csv(os.path.join(RD, sid + ".csv"))
    s = s[pd.to_numeric(s["value"], errors="coerce").notna()]
    d = pd.to_datetime(s["date"])
    return pd.Series(s["value"].astype(float).values, index=d.dt.to_period("M")).groupby(level=0).last().reindex(grid)


def country(yf, etf, idx, cur):
    parts = [yf(etf).pct_change(fill_method=None)]
    if idx:
        p = yf(idx)
        if cur:
            fx = yf(cur + "=X").combine_first(fred_me(FXd[cur]) if cur in FXd else
                                               X.R.get("__none__", pd.Series(np.nan, index=grid)))
            if cur == "JPY":
                fx = yf("JPY=X").combine_first(
                    pd.read_csv("/home/claude/stock-screener/cache/macro/raw/EXJPUS.csv").pipe(
                        lambda s: pd.Series(s["value"].astype(float).values,
                                            index=pd.to_datetime(s["date"]).dt.to_period("M")).groupby(level=0).last().reindex(grid)))
            p = p / fx
        parts.append(p.pct_change(fill_method=None) + 0.02 / 12)
    s = pd.Series(np.nan, index=grid)
    for q in parts:
        s = s.combine_first(q)
    s[s.abs() > 3] = np.nan
    return s


COUNTRY = {"korea": ("EWY", "^KS11", "KRW"), "brazil": ("EWZ", "^BVSP", "BRL"), "japan": ("EWJ", "^N225", "JPY"),
           "hongkong": ("EWH", "^HSI", None), "india": ("INDA", "^BSESN", "INR"), "mexico": ("EWW", "^MXX", "MXN")}
Rfix = R0.copy()
for k, (etf, idx, cur) in COUNTRY.items():
    a = country(y_auth, etf, idx, cur)
    f = country(y_fix, etf, idx, cur)
    ok = a.notna() & f.notna() & (grid < Per("2012-01"))
    lead = pd.concat([a, f.shift(-1)], axis=1).dropna()
    print(f"  eq_{k:8s}: author vs fixed same-month corr {a[ok].corr(f[ok]):.2f}; author(t) vs fixed(t+1) corr "
          f"{lead.iloc[:, 0].corr(lead.iloc[:, 1]):.2f}; panel matches author rebuild: "
          f"{np.allclose(R0['eq_' + k].dropna(), a.reindex(R0['eq_' + k].dropna().index), equal_nan=True)}")
    Rfix["eq_" + k] = f

# rerun Exp 2's country-momentum rule with fixed dates (fully invested, 1997-2011 | 2012-2026 | 1997-2026)
import exp_loc as L  # noqa  (already imported via exp_combo)
WS = (("1997-02", "2011-12"), ("2012-01", "2026-10"), ("1997-02", "2026-10"))


def W_top_R(Rm, k=3):
    C_ = L.C
    lv_ = {c: lvl(Rm[c]).where(Rm[c].notna().cummax()) for c in C_}
    M12 = pd.DataFrame({c: lv_[c].shift(1) / lv_[c].shift(12) - 1 for c in C_})
    UP = pd.DataFrame({c: (lv_[c] > lv_[c].rolling(10, min_periods=10).mean()) for c in C_}).fillna(False)
    W = pd.DataFrame(0.0, index=grid, columns=C_)
    nxt = Rm[C_].shift(-1).notna()
    for t in range(T):
        mrow = M12.iloc[t].dropna()
        okc = [c for c in mrow.index if UP[c].iloc[t] and (nxt[c].iloc[t] if t + 1 < T else True)]
        top = list(mrow[okc].sort_values(ascending=False).index[:k])
        if not top:
            W.iloc[t, 0] = 1.0
        else:
            for c in top:
                W.iloc[t, C_.index(c)] = 1 / len(top)
    return W


print("\n== Exp 2 'L3 country momentum top 3' (CAGR / worst / Sharpe: 1997-2011 | 2012-2026 | 1997-2026)")
print(line("  as published (author panel)", run(L.V["L3 country momentum top 3"]), WS))
print(line("  author panel, rebuilt here", run(W_top_R(R0), R0), WS))
print(line("  dates fixed", run(W_top_R(Rfix), Rfix), WS))
print(line("  S&P 500", R0["spx"], WS))

# ---------------------------------------------------------------- misc data checks
print("\n== misc")
raw = pd.DataFrame({c: R0[c] for c in R0.columns})
print(f"  entries > 300% set to NaN in rpanel: cannot recount after the fact; |r| > 50% now: "
      f"{int((raw.abs() > 0.5).sum().sum())} cells in {list(raw.columns[(raw.abs() > 0.5).any()])}")
gc = y_auth("GC=F")
print(f"  GC=F missing months 2000-09..2004-11 (filled from the monthly-average estimate): "
      f"{[str(p) for p in grid[(gc.isna() & (grid >= Per('2000-09')) & (grid <= Per('2004-11'))).values]]}")
com = R0["commod"]
dbc = y_auth("DBC").pct_change(fill_method=None)
print(f"  commodities: DBC from {dbc.first_valid_index()}; AQR before. Oct-2026 return is a partial month "
      f"(data to 2026-10-29): spx {R0['spx'].iloc[-1]*100:.2f}%")
print(f"  stats(): Sharpe = mean(r - rf) / std(r) (std of total, not excess, return) - immaterial")
