"""LSEG adapter: puts the stage-B LSEG data into the input form of the reference-book engine
(tools/equity/wrds/eq_ref.py), so that both sources go through the same formulas (FIELD_DICTIONARY_v1.0.md).

    import lseg_adapter as A
    fq = A.quarterly_fq(STAGEB_DIR)          # Compustat-like quarterly table (one-quarter cash flow in cfoq)
    snap = A.account_snapshot(fq, panel, months)   # account measures known at each month-end + EY and BP

STAGEB_DIR = output folder of tools/equity/lseg/read_stage_b.py (Q_G1..Q_G5.csv.gz). panel = monthly panel from
read_monthly.py (isin, ym, close, shares, mcap, volume, ret1m). LSEG data stay out of the repo.

Notes found on 2026-11-22 (Q2 file and the monthly panel):
- quarterly cash flow from operations (TR.F.NetCashFlowOp, FQ) is one quarter, not year to date;
- TR.PriceClose in the monthly file is split-adjusted to today's basis while TR.SharesOutstanding is as reported:
  close x shares is wrong before a split. TR.CompanyMarketCap is right. The unadjusted close comes with file 12
  (12_LSEG_monthly_unadjusted_close_v3.xlsx); until then company market value is taken from TR.CompanyMarketCap;
- the monthly panel has repeated rows for some line-months (5,804 groups; 1,095 with differing values): the row with
  the latest date in the month is kept;
- first-reported quarterly values are thin early: in 2010 about two thirds of the quarter rows carry values (rows
  with only a period end otherwise), above 90% from 2022; 28% of quarters have no original announcement date (the
  45-day rule applies).
"""
import glob
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wrds"))
import eq_ref  # noqa: E402

PE = "TR.F.TotRevenue.periodenddate"
MAP = {"saleq": "TR.F.TotRevenue", "cogsq": "TR.F.CostOfOpRev", "gp": "TR.F.GrossProfIndPropTot",
       "oiadpq": "TR.F.EBIT", "niq": "TR.F.NetIncAfterTax", "cfoq": "TR.F.NetCashFlowOp", "atq": "TR.F.TotAssets",
       "ceqq": "TR.F.ComEqTot", "cheq": "TR.F.CashSTInvstTot", "dlcq": "TR.F.STDebtCurrPortOfLTDebt",
       "dlttq": "TR.F.DebtLTTot", "debt": "TR.F.DebtTot", "pstkq": "TR.F.PrefShHoldEq", "mibq": "TR.F.MinIntrEq",
       "actq": "TR.F.TotCurrAssets", "lctq": "TR.F.TotCurrLiab", "cshoq": "TR.F.ComShrOutsTot"}


def quarterly_fq(d):
    q = None                     # v1-v3 groups Q_G*, v4 pieces Q_C* (book items) and Q_R* (other items)
    for f in sorted(glob.glob(os.path.join(d, "Q_*.csv.gz"))):
        x = pd.read_csv(f, low_memory=False)
        x = x[x[PE].notna()].drop_duplicates(["instrument", PE], keep="first").set_index(["instrument", PE])
        q = x if q is None else q.combine_first(x)
    q = q.reset_index()
    fq = pd.DataFrame({"gvkey": q.instrument, "datadate": pd.to_datetime(q[PE], errors="coerce"),
                       "rdq": pd.to_datetime(q.get("TR.F.OriginalAnnouncementDate"), errors="coerce")})
    for k, c in MAP.items():
        fq[k] = pd.to_numeric(q[c], errors="coerce") if c in q else np.nan
    # cost of revenue: from gross profit where the cost line is missing
    fq["cogsq"] = fq.cogsq.where(fq.cogsq.notna(), fq.saleq - fq.gp)
    # short-term debt: total debt - long-term debt where the short-term line is missing
    fq["dlcq"] = fq.dlcq.where(fq.dlcq.notna(), fq.debt - fq.dlttq)
    fq = fq.dropna(subset=["datadate"])
    qd = fq.datadate - pd.Timedelta(days=7)      # 52/53-week years: a period ending 1-7 Jan belongs to December
    qi = qd.dt.year * 4 + (qd.dt.month - 1) // 3
    fq["fyearq"], fq["fqtr"] = qi // 4, qi % 4 + 1
    fq["ajexq"] = 1.0           # LSEG shares as reported: split adjustment from file 12 (not applied yet)
    return fq.drop(columns=["gp", "debt"])


def account_snapshot(fq, panel, months):
    """account measures known at each month-end (eq_ref formulas) joined with company market value -> EY, BP"""
    q = eq_ref.quarterly_table(fq)
    am = eq_ref.account_measures(q)
    q = pd.concat([q[["gvkey", "datadate", "avail"]], am], axis=1).dropna(subset=["avail"]).sort_values("avail")
    ids = sorted(set(q.gvkey))
    grid = pd.DataFrame([(g, m) for g in ids for m in months], columns=["gvkey", "yyyymm"])
    grid["t_end"] = [eq_ref.ym_end(m) for m in grid.yyyymm]
    grid = grid.sort_values("t_end")
    j = pd.merge_asof(grid, q.rename(columns={"avail": "t_end"}), on="t_end", by="gvkey", direction="backward")
    j = j[(j.t_end - j.datadate).dt.days <= eq_ref.CFG["stale_days"]]
    p = panel.rename(columns={"isin": "gvkey", "ym": "yyyymm"})[["gvkey", "yyyymm", "date", "mcap"]]
    p = p.dropna(subset=["mcap"]).sort_values("date").drop_duplicates(["gvkey", "yyyymm"], keep="last")
    j = j.merge(p, on=["gvkey", "yyyymm"], how="left")
    ev = j.mcap + j.netdebt
    j["ey"] = (j.ebit_ttm / ev).where((ev > 0) & j.netdebt_ok.fillna(False).astype(bool))
    j["bp"] = (j.ceq / j.mcap).where(j.mcap > 0)
    return j
