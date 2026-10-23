"""Research (not used by the page): do the sector calls work better through the stocks most sensitive to their
sector's moves than through the sector ETF?

Universe: today's large holdings of each sector ETF (Yahoo monthly adjusted closes). Survivorship bias: these
are companies that exist today, so every stock basket looks better than it was. To keep the test fair, the
comparison is always basket vs basket from the same survivors:
  * full basket   = equal weight of all the sector's listed stocks;
  * sensitive     = the third of the sector's stocks with the highest beta to the sector's return relative to the
                    20-sector average, over the trailing 60 months (36 minimum), known at the time.
Portfolios (weights set at the end of month t, earn month t+1, from Aug 2006):
  * ETF tilt         - the live method (overweight 1.5x, underweight 0.5x on the sector ETFs);
  * basket tilt      - the same calls on the full stock baskets;
  * sensitive tilt   - the same calls, but overweights and underweights held through the sensitive stocks.
Each is measured against its own equal-weight benchmark (ETFs: the 20 ETFs; stocks: the 20 full baskets).
Also: long/short spread of called sectors (long overweights, short underweights) via ETFs vs sensitive stocks.
Run: python -m macro.run fetch,build,stocks (network needed: GitHub Actions)."""
import math
import os
import time

import numpy as np
import pandas as pd

from . import engine as E
from . import fetch as FT

STOCKS = {
    "SMH": "NVDA TSM AVGO AMD ASML QCOM TXN INTC MU AMAT LRCX KLAC ADI MRVL",
    "IGV": "MSFT ORCL CRM ADBE NOW INTU PANW CDNS SNPS ADSK WDAY FTNT ANSS PTC",
    "VOX": "GOOGL META NFLX T VZ TMUS DIS CMCSA CHTR EA TTWO OMC IPG",
    "KBE": "JPM BAC WFC C USB PNC TFC COF BK STT NTRS SCHW",
    "KRE": "FITB KEY RF HBAN MTB CFG ZION CMA FHN WBS EWBC SNV WAL BOKF",
    "KIE": "PGR CB TRV ALL AIG MET PRU AFL HIG CINF L WRB MMC AON",
    "ITB": "DHI LEN PHM NVR TOL KBH MTH TMHC HD LOW SHW MAS OC MHK",
    "XRT": "TJX ROST BBY DG DLTR KSS M GPS ANF AEO ULTA BURL DKS TGT",
    "IYT": "UNP CSX NSC UPS FDX ODFL JBHT CHRW EXPD DAL UAL LUV KNX LSTR",
    "XLI": "GE CAT DE HON ETN EMR PH ITW MMM ROK CMI DOV PCAR IR",
    "ITA": "RTX LMT NOC GD BA LHX TDG HWM TXT HII HEI CW",
    "XLE": "XOM CVX COP EOG SLB OXY PSX MPC VLO HAL DVN APA BKR OKE WMB KMI",
    "XLU": "NEE DUK SO D AEP EXC SRE XEL ED PEG WEC EIX ETR DTE",
    "XLP": "PG KO PEP WMT COST PM MO MDLZ CL KMB GIS KHC HSY SYY KR",
    "XLV": "UNH JNJ LLY ABBV MRK PFE TMO ABT DHR BMY AMGN MDT SYK CVS CI",
    "XBI": "VRTX REGN GILD BIIB INCY ALNY EXEL NBIX BMRN SRPT IONS UTHR INSM HALO",
    "XLB": "LIN SHW APD ECL DD DOW NUE FCX PPG IP PKG VMC MLM CF",
    "XME": "FCX NUE STLD CLF AA RS CMC CENX ATI CRS BTU MTRN HL CDE",
    "GDX": "NEM AEM WPM FNV KGC AU GFI RGLD AGI EGO HMY BTG IAG SSRM",
    "IYR": "PLD AMT EQIX CCI PSA SPG O WELL DLR AVB EQR VTR ARE MAA",
}
DIR = os.path.join("cache", "macro", "stocks")


def fetch(log=print):
    os.makedirs(DIR, exist_ok=True)
    syms = sorted({s for v in STOCKS.values() for s in v.split()})
    ok, bad = 0, []
    for s in syms:
        p = os.path.join(DIR, f"{s}.csv")
        if os.path.exists(p):
            ok += 1
            continue
        try:
            rows = FT.yahoo(s)
            pd.DataFrame(rows, columns=["date", "value"]).to_csv(p, index=False)
            ok += 1
        except Exception as e:                     # noqa: BLE001 - a missing stock is reported, not fatal
            bad.append(f"{s}:{str(e)[:40]}")
        time.sleep(0.3)
    log(f"stocks: {ok} fetched, {len(bad)} failed {bad[:12]}")


def _px(sym, grid):
    p = os.path.join(DIR, f"{sym}.csv")
    if not os.path.exists(p):
        return pd.Series(np.nan, index=grid)
    s = pd.read_csv(p, parse_dates=["date"]).dropna()
    m = pd.Series(s["value"].values, index=s["date"].dt.to_period("M")).groupby(level=0).last()
    return m.reindex(grid)


def _stats(r):
    r = r.dropna()
    lv = (1 + r).cumprod()
    return (lv.iloc[-1] ** (12 / len(r)) - 1) * 100


def run(log=print):
    fetch(log)
    out = E.run(log=lambda *a: None)
    grid = pd.PeriodIndex(out["months"], freq="M")
    rets, src, mkt = E.build_returns(E.month_grid())
    rets, src = rets.reindex(grid), src.reindex(grid)
    etf_ret = rets.where(src == "etf")
    ew_all = rets.mean(axis=1)
    sec_rel = rets.sub(ew_all, axis=0)                       # sector return minus the 20-sector average
    sr = {k: pd.DataFrame({s: _px(s, grid).pct_change(fill_method=None) for s in v.split()}) for k, v in STOCKS.items()}
    sr = {k: d.where(d.abs() < 3) for k, d in sr.items()}   # drop bad ticks (> +300% in a month)
    start = pd.Period("2006-08", "M")
    idx = grid[grid >= start]
    T = len(grid)
    pos = {p: i for i, p in enumerate(grid)}
    for h in ("12", "6"):
        acts = pd.DataFrame(out["horizons"][h]["actions"], index=grid)
        res = {"etf": [], "bench_etf": [], "basket": [], "sens": [], "bench_stk": [], "ls_etf": [], "ls_sens": [], "ls_basket": []}
        months = []
        for t in idx:
            i = pos[t]
            if i + 1 >= T:
                break
            nxt = grid[i + 1]
            a = acts.iloc[i]
            full, sens = {}, {}
            for k, d in sr.items():
                cur = d.iloc[i + 1]                          # next month's returns (earned)
                hist = d.iloc[max(0, i - 59): i + 1]         # known at t
                have = [s for s in d.columns if not np.isnan(cur[s]) and hist[s].notna().sum() >= 36]
                if len(have) < 3:
                    continue
                x = sec_rel[k].iloc[max(0, i - 59): i + 1]
                beta = {}
                for s in have:
                    y = hist[s] - ew_all.iloc[max(0, i - 59): i + 1]
                    ok = y.notna() & x.notna()
                    if ok.sum() >= 36 and x[ok].var() > 0:
                        beta[s] = float(np.cov(y[ok], x[ok])[0, 1] / x[ok].var())
                full[k] = float(cur[have].mean())
                if len(beta) >= 3:
                    top = sorted(beta, key=beta.get, reverse=True)[:max(2, len(beta) // 3)]
                    sens[k] = float(cur[top].mean())
                else:
                    sens[k] = full[k]
            ks = [k for k in full if k in sens]
            if len(ks) < 15:
                continue
            w = {k: 1.5 if a[k] == "over" else 0.5 if a[k] == "under" else 1.0 for k in ks}
            ws = sum(w.values())
            res["basket"].append(sum(w[k] * full[k] for k in ks) / ws)
            res["sens"].append(sum(w[k] * (sens[k] if a[k] in ("over", "under") else full[k]) for k in ks) / ws)
            res["bench_stk"].append(float(np.mean([full[k] for k in ks])))
            er = etf_ret.iloc[i + 1]
            ke = [k for k in er.index if not np.isnan(er[k])]
            we = {k: 1.5 if a[k] == "over" else 0.5 if a[k] == "under" else 1.0 for k in ke}
            res["etf"].append(sum(we[k] * er[k] for k in ke) / sum(we.values()))
            res["bench_etf"].append(float(er[ke].mean()))
            ov = [k for k in ks if a[k] == "over"]
            un = [k for k in ks if a[k] == "under"]
            def spread(f):
                if not ov and not un:
                    return 0.0
                lo = np.mean([f[k] for k in ov]) if ov else np.mean([f[k] for k in ks])
                sh = np.mean([f[k] for k in un]) if un else np.mean([f[k] for k in ks])
                return float(lo - sh)
            res["ls_sens"].append(spread(sens))
            res["ls_basket"].append(spread(full))
            res["ls_etf"].append(spread({k: (er[k] if k in ke else full[k]) for k in ks}))
            months.append(str(nxt))
        R = {k: pd.Series(v, index=pd.PeriodIndex(months, freq="M")) for k, v in res.items()}

        def line(name, p, b):
            d = (R[p] - R[b])
            return (f"  {name:<32} {_stats(R[p]):5.1f}%/yr vs its benchmark {_stats(R[b]):5.1f}% -> "
                    f"{_stats(R[p]) - _stats(R[b]):+.1f}%/yr, IR {d.mean() / d.std() * math.sqrt(12):.2f}")

        active = (acts.loc[idx].isin(["over", "under"]).any(axis=1)).mean()
        log(f"== {h}-month calls, {months[0]} to {months[-1]} ({len(months)} months; calls active {active:.0%})")
        log(line("ETF tilt (live method)", "etf", "bench_etf"))
        log(line("Stock baskets, same calls", "basket", "bench_stk"))
        log(line("Most sensitive stocks, same calls", "sens", "bench_stk"))
        for n, k in (("ETFs", "ls_etf"), ("full baskets", "ls_basket"), ("sensitive stocks", "ls_sens")):
            v = R[k][R[k] != 0]
            log(f"  long/short spread via {n:<17} {v.mean() * 1200:+.1f}%/yr in active months (t {v.mean() / v.std() * math.sqrt(len(v)):.2f}, "
                f"{(v > 0).mean():.0%} of {len(v)} months positive)")
    return True
