"""Exploratory test (2026-10-30): do IMF WEO forecast revisions predict country equity / bond excess returns?

Data: Extended IMF WEO forecasts panel (Mendeley, 41 vintages Sep 2006 - Oct 2026; user download, kept in the local
cache as imf_weo_vintages.csv.gz). Revision = change in the forecast for the current and next calendar year versus the
previous vintage (about 6 months earlier). Positions start the month after publication and are held 6 months.
Cross-sectional: rank IC and rank-weighted long/short. Directional: sign of the revision, 36-month vol scaling.
Exploratory only: one sample of 39 vintages, not FDR-adjusted.
"""
import os
import pickle

import numpy as np
import pandas as pd

from . import panel as P

EQ = {"USA": "eq_us_spx", "DEU": "eq_de_dax", "GBR": "eq_gb_ftse", "FRA": "eq_fr_cac", "JPN": "eq_jp_nikkei",
      "CAN": "eq_ca_tsx", "AUS": "eq_au_asx", "HKG": "eq_hk_hsi", "CHN": "eq_cn", "KOR": "eq_kr_kospi", "TWN": "eq_tw",
      "IND": "eq_in", "BRA": "eq_br_ibov", "MEX": "eq_mx_ipc", "ZAF": "eq_za"}
BD = {"USA": "bd_us_10y", "DEU": "bd_de_10y", "GBR": "bd_gb_10y", "JPN": "bd_jp_10y", "CAN": "bd_ca_10y",
      "AUS": "bd_au_10y"}


def revisions(w, code):
    d = w[w.indicator_code == code][["iso3", "publication_date", "target_year", "forecast_value"]]
    d = d.sort_values("publication_date")
    d["rev"] = d["forecast_value"] - d.groupby(["iso3", "target_year"])["forecast_value"].shift(1)
    oy = d["publication_date"].dt.year
    d = d[(d.target_year >= oy) & (d.target_year <= oy + 1)]
    return d.groupby(["publication_date", "iso3"])["rev"].mean().unstack()


def cross_section(R, sig, MAP, sign, hold=6):
    ics, ls = [], []
    for pub in sig.index:
        m0 = pd.Period(pub, "M") + 1
        s = sig.loc[pub].rename(index=MAP).reindex(list(MAP.values())).dropna() * sign
        fwd = R.loc[m0:m0 + hold - 1, s.index].sum(min_count=hold)
        j = pd.concat([s, fwd], axis=1).dropna()
        if len(j) < 5:
            continue
        ics.append(j.iloc[:, 0].rank().corr(j.iloc[:, 1].rank()))
        wt = j.iloc[:, 0].rank()
        wt = (wt - wt.mean()) / (wt - wt.mean()).abs().sum()
        ls.append((wt * j.iloc[:, 1]).sum())
    ics = np.array(ics)
    return len(ics), ics.mean(), ics.mean() / ics.std() * np.sqrt(len(ics))


def directional(R, sig, MAP, sign, hold=6):
    rets = []
    for pub in sig.index:
        m0 = pd.Period(pub, "M") + 1
        s = np.sign(sig.loc[pub].rename(index=MAP).reindex(list(MAP.values()))) * sign
        vol = R.loc[:m0 - 1, s.index].tail(36).std()
        rets.append(((s / vol) * R.loc[m0:m0 + hold - 1, s.index]).mean(axis=1))
    r = pd.concat(rets).groupby(level=0).mean().dropna()
    return len(r), r.mean() / r.std() * np.sqrt(12), r.mean() / r.std() * np.sqrt(len(r))


def main():
    R = pickle.load(open(os.path.join(P.OUT, "panel.pkl"), "rb"))["R"]
    w = pd.read_csv(os.path.join(P.RD, "imf_weo_vintages.csv.gz"), parse_dates=["publication_date"])
    g, p = revisions(w, "NGDP_RPCH"), revisions(w, "PCPIPCH")
    for name, sig, MAP, sign in (("equity, GDP revision up -> long", g, EQ, 1),
                                 ("equity, growth minus inflation revision", g - p, EQ, 1),
                                 ("bonds, GDP revision up -> short", g, BD, -1),
                                 ("bonds, inflation revision up -> short", p, BD, -1),
                                 ("bonds, growth+inflation revision up -> short", g + p, BD, -1)):
        n, ic, t = cross_section(R, sig, MAP, sign)
        m, sr, t2 = directional(R, sig, MAP, sign)
        print("%-46s cross-section IC %.2f (t %.1f, %d vintages) | directional SR %.2f (t %.1f, %d months)"
              % (name, ic, t, n, sr, t2, m))


if __name__ == "__main__":
    main()
