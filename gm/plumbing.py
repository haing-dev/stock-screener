"""Phase 0 plumbing check: does a plain price-trend book built from our panel track AQR's published TSMOM factors?

Price trend (Hurst-Ooi-Pedersen style): per market the average sign of its 1-, 3- and 12-month excess return, sized
to 40% annual volatility per market (MOP 2012), equal weight across markets within an asset class; asset classes
combined at equal risk. Compared monthly with AQR TSMOM, TSMOM^EQ/FI/FX/CM (aqr_tsmom_factors.xlsx), 1985+.
A high correlation means the data and the signal code are sound; it is not a performance claim.
"""
import os
import pickle

import numpy as np
import pandas as pd

from . import panel as P

CLASSES = {"EQ": "eq_", "FI": ("bd_", "st_"), "FX": "fx_", "CM": "cm_"}


def trend_book(R, classes=CLASSES, horizons=(1, 3, 12), target=0.40):
    lvl = (1 + R.fillna(0)).cumprod().where(R.notna().cummax())
    sig = sum(np.sign(lvl / lvl.shift(h) - 1) for h in horizons) / len(horizons)
    vol = R.rolling(36, min_periods=12).std() * np.sqrt(12)
    pos = (sig * target / vol).shift(0)                   # decided at t
    out = {}
    for c, pre in classes.items():
        cols = [k for k in R.columns if k.startswith(pre)]
        contrib = (pos[cols].shift(1) * R[cols])          # earned over t+1
        n = contrib.notna().sum(axis=1)
        out[c] = contrib.sum(axis=1, min_count=1) / n.where(n > 0)
    df = pd.DataFrame(out)
    sc = df.std()
    df_eq = df / sc * sc.mean()                           # equal risk across classes (full-sample scaling; check only)
    df["ALL"] = df_eq.mean(axis=1, skipna=True)
    return df


def aqr_tsmom():
    x = pd.read_excel(os.path.join(P.RD, "aqr_tsmom_factors.xlsx"), sheet_name=0, header=17)
    x = x.rename(columns={x.columns[0]: "date"}).dropna(subset=["date"])
    x.index = pd.to_datetime(x["date"]).dt.to_period("M")
    return x[["TSMOM", "TSMOM^EQ", "TSMOM^FI", "TSMOM^FX", "TSMOM^CM"]].astype(float)


def main():
    D = pickle.load(open(os.path.join(P.OUT, "panel.pkl"), "rb"))
    aqr = aqr_tsmom()
    pairs = {"ALL": "TSMOM", "EQ": "TSMOM^EQ", "FI": "TSMOM^FI", "FX": "TSMOM^FX", "CM": "TSMOM^CM"}
    sr = lambda s: s.mean() / s.std() * np.sqrt(12)
    for hz in ((12,), (1, 3, 12)):
        ours = trend_book(D["R"], horizons=hz)
        print("price trend %s-month signal vs AQR TSMOM (12-month signal): monthly correlation; Sharpe ours / AQR, gross"
              % "/".join(map(str, hz)))
        for a, b in (("1985-01", "2000-12"), ("2001-01", "2026-12"), ("1985-01", "2026-12")):
            line = []
            for o, q in pairs.items():
                j = pd.concat([ours[o], aqr[q]], axis=1).loc[a:b].dropna()
                if len(j) < 36:
                    line.append("%s n/a" % o)
                    continue
                line.append("%s corr %.2f SR %.2f/%.2f" % (o, j.iloc[:, 0].corr(j.iloc[:, 1]), sr(j.iloc[:, 0]), sr(j.iloc[:, 1])))
            print("  %s..%s  " % (a[:4], b[:4]) + " | ".join(line))
    n = {c: int(sum(1 for k in D["R"].columns if k.startswith(p) and D["R"][k].notna().sum() > 0)) for c, p in CLASSES.items()}
    print("markets with data per class:", n)


if __name__ == "__main__":
    main()
