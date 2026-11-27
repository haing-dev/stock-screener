"""Smoke test of the A1 data swap code (tools/bbgq/lib/a1_panel.py, job tools/bbgq/jobs/gm_a1_v1.py; gm/CHANGES.md "data:
A1 data rule", 2026-11-27) on MOCK Bloomberg stores and SYNTHETIC free inputs only (no cache, no market data).

The mock store is a real bbgdata store on disk (catalog.csv, design / sealed tables, manifest.json, LOCK written with
bbgdata's own hash functions), read through bbgdata.Panel and bbg_panel.Source exactly as on the PC. Checks:
  extension only     no month where the free series has a value changes; only months before the free start are
                     filled; a Bloomberg series that disagrees with the free one inside the overlap leaves the free value
  correlation gate   a series with overlap correlation below 0.95 is rejected; too few overlap months is rejected
  status             copy (no series id), _CUT file, held-back market, missing ticker: rejected and listed
  seal               the store serves nothing after 2010-11 for a one-day-delay sheet, asof after 2010-12-31 raises,
                     the sealed tables are never read (poisoned, outputs unchanged), free inputs dated after 2010-12
                     raise SealBreach in build, Bloomberg values after 2010 never reach the panel
  panel id           stable for the same inputs; changes with the admitted list, the lock id or the free inputs
  no raw value       every line the job's printing functions write (candidate rows and the registered report on a
                     synthetic book) holds no planted data value and no number with 5 or more decimals
python3 tests/a1_panel_smoke.py      (also run from tests/run_tests.py)
"""
import csv
import hashlib
import io
import json
import os
import re
import shutil
import sys
import tempfile

import numpy as np
import pandas as pd

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path[:0] = [REPO, os.path.join(REPO, "tools", "bbgq", "lib")]

import a1_panel as A1  # noqa: E402
import bbgdata  # noqa: E402
import bbg_panel  # noqa: E402
from gm import config as CF  # noqa: E402
from gm import seal as SL  # noqa: E402

GRID = pd.period_range("1960-01", "2010-12", freq="M")
ME = pd.date_range("1969-12-31", "2010-12-31", freq="ME")
ME_SEALED = pd.date_range("2011-01-31", "2015-12-31", freq="ME")
PLANT = 4321.0                  # Bloomberg mock levels live in [PLANT, PLANT + 4000): never printed


def levels(rng, n, start=PLANT, vol=0.04):
    return start * np.exp(np.cumsum(rng.normal(0, vol, n)))


# ------------------------------------------------------------------------------------------------- mock bbgdata store
def write_store(work, blocks, lock_tag=""):
    """blocks: list of dict(ticker, field, sheet, status, values (Series on ME) or None, file_name, untouched,
    sealed (Series on ME_SEALED) or None). Writes work/bbg as bbgdata.build would (metadata layout and hashes)."""
    root = os.path.join(work, "bbg")
    for p in ("design", "sealed"):
        os.makedirs(os.path.join(root, p), exist_ok=True)
    cols, scol, entries = {}, {}, []
    for i, b in enumerate(blocks):
        sid = "%s|%s" % (b["ticker"], b["field"]) if b["status"] == "ok" else ""
        v = b.get("values")
        if sid and v is not None:
            cols[sid] = v.reindex(ME).astype(float)
            sv = b.get("sealed")
            scol[sid] = (sv.reindex(ME_SEALED) if sv is not None else pd.Series(np.nan, index=ME_SEALED)).astype(float)
        vv = v.dropna() if v is not None else pd.Series(dtype=float)
        e = {k: "" for k in bbgdata.CATALOG_COLUMNS}
        e.update({"file": b.get("file", "1"), "file_name": b.get("file_name", "1_Bloomberg_macro_UBC_6 1.xlsx"),
                  "sheet": b["sheet"], "col": 1 + 3 * i, "label": b["ticker"], "ticker": b["ticker"],
                  "field": b["field"], "per": "M", "kind": "price", "status": b["status"],
                  "first": vv.index[0].strftime("%Y-%m-%d") if len(vv) and sid else "",
                  "count": int(len(vv)) if sid else 0, "n_design": int(len(vv)) if sid else 0, "n_sealed": 0,
                  "series_id": sid, "duplicate_of": "", "live_source": "bloomberg_only", "live_delay_days": 1,
                  "release_sid": "", "revised": 0, "untouched": int(b.get("untouched", 0)), "source": "first",
                  "copy_group": "12" if b["status"] == "copy" else ""})
        entries.append(e)
    mon = pd.DataFrame(cols, index=ME)
    mon.index.name = "date"
    sealed = pd.DataFrame(scol, index=ME_SEALED)
    daily = pd.DataFrame(index=pd.DatetimeIndex([], name="date"))
    tabs = {}
    for part, nm, df in (("design", "monthly", mon), ("design", "daily", daily), ("sealed", "monthly", sealed),
                         ("sealed", "daily", daily)):
        p = os.path.join(root, part, nm + ".pkl")
        df.to_pickle(p)
        tabs["%s/%s.pkl" % (part, nm)] = {"content_sha256": bbgdata.content_sha256(df), "rows": int(df.shape[0]),
                                          "columns": int(df.shape[1])}
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(bbgdata.CATALOG_COLUMNS)
    for e in entries:
        w.writerow([e[k] for k in bbgdata.CATALOG_COLUMNS])
    cb = buf.getvalue().encode("utf-8")
    with open(os.path.join(root, "catalog.csv"), "wb") as f:
        f.write(cb)
    man = {"seal_date": "2010-12-31", "build_time": "mock",
           "workbooks": {"1": {"sha256": hashlib.sha256(("mock" + lock_tag).encode()).hexdigest(), "size": 1,
                               "name": "mock.xlsx", "mtime": "mock"}},
           "config": {"live_sources.csv": "mock", "untouched_markets.csv": "mock"}, "tables": tabs,
           "catalog": {"file": "catalog.csv", "sha256": hashlib.sha256(cb).hexdigest(), "rows": len(entries)},
           "counts": {}, "warnings": []}
    with open(os.path.join(root, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(man, f, indent=1, sort_keys=True)
    lid = bbgdata.lock_id_of(man)
    with open(os.path.join(root, "LOCK"), "w", encoding="utf-8") as f:
        f.write(lid + "\n")
    return lid


def per(s):
    """Month-end DatetimeIndex series -> PeriodIndex on GRID."""
    out = pd.Series(s.values, index=s.index.to_period("M"))
    return out.reindex(GRID)


def scenario(seed=3):
    """Mock store blocks and synthetic free inputs with known answers."""
    rng = np.random.default_rng(seed)
    n = len(ME)
    lv_cl = pd.Series(levels(rng, n), index=ME)                    # SPGSCLP: ok, from 1969-12; free cm_wti 1985-02
    lv_bcom = pd.Series(levels(rng, n), index=ME)                  # BCOMCL: ok, unrelated -> correlation gate fails
    lv_ng = pd.Series(levels(rng, n), index=ME)
    lv_gc = pd.Series(levels(rng, n), index=ME).where(ME >= "2003-06-30")   # starts after the free gold start
    lv_si = pd.Series(levels(rng, n), index=ME).where(ME <= "2002-07-31")   # 23 overlap returns with free silver
    ng1 = pd.Series(levels(rng, n, PLANT + 1000, 0.08), index=ME).where(ME >= "1990-04-30")
    ng2 = ng1 * pd.Series(np.exp(rng.normal(0, 0.01, n)), index=ME)
    ty = pd.Series(levels(rng, n, PLANT + 2000, 0.01), index=ME)
    blocks = [
        {"ticker": "SPGSCLP Index", "field": "PX_LAST", "sheet": "Returns", "status": "ok", "values": lv_cl,
         "sealed": pd.Series(1e9, index=ME_SEALED)},
        {"ticker": "BCOMCL Index", "field": "PX_LAST", "sheet": "Returns", "status": "ok", "values": lv_bcom},
        {"ticker": "SPGSNGP Index", "field": "PX_LAST", "sheet": "Returns", "status": "copy", "values": lv_ng},
        {"ticker": "SPGSHOP Index", "field": "PX_LAST", "sheet": "Returns", "status": "ok", "values": lv_ng,
         "file_name": "1_Bloomberg_macro_UBC_CUT.xlsx"},
        {"ticker": "SPGSGCP Index", "field": "PX_LAST", "sheet": "Returns", "status": "ok", "values": lv_gc},
        {"ticker": "SPGSSIP Index", "field": "PX_LAST", "sheet": "Returns", "status": "ok", "values": lv_si},
        {"ticker": "SPGSCNP Index", "field": "PX_LAST", "sheet": "Returns", "status": "ok", "values": lv_ng,
         "untouched": 1},
        {"ticker": "NG1 Comdty", "field": "PX_LAST", "sheet": "ComFront", "status": "ok", "values": ng1, "file": "5",
         "file_name": "5_Bloomberg_commodities_ext_monthly_5 1.xlsx"},
        {"ticker": "NG2 Comdty", "field": "PX_LAST", "sheet": "ComCurve", "status": "ok", "values": ng2, "file": "5",
         "file_name": "5_Bloomberg_commodities_ext_monthly_5 1.xlsx"},
        {"ticker": "MXJP Index", "field": "EQY_DVD_YLD_12M", "sheet": "EquityValuation", "status": "ok",
         "values": pd.Series(2.0 + rng.normal(0, 0.1, n), index=ME).where(ME >= "1995-01-31")},
        {"ticker": "MXCN Index", "field": "EQY_DVD_YLD_12M", "sheet": "EquityValuation", "status": "ok",
         "values": pd.Series(2.0 + rng.normal(0, 0.1, n), index=ME).where(ME >= "1995-01-31")},
        {"ticker": "TY1 Comdty", "field": "PX_LAST", "sheet": "BondFutures", "status": "ok", "values": ty},
    ]
    # free side (synthetic, design months only, on GRID like free_inputs)
    mk = ["eq_us_spx", "eq_jp_nikkei", "eq_gb_ftse", "bd_us_10y", "bd_de_10y", "fx_eur", "fx_jpy", "fx_gbp",
          "cm_wti", "cm_natgas", "cm_heatoil", "cm_gold", "cm_silver"]
    R = pd.DataFrame(rng.normal(0.003, 0.035, (len(GRID), len(mk))), index=GRID, columns=mk)
    gsci = per(lv_cl).pct_change(fill_method=None)
    R["cm_wti"] = (gsci + rng.normal(0, 0.004, len(GRID))).where(GRID >= pd.Period("1985-02", "M"))
    R.loc[R.index < pd.Period("1994-02", "M"), "cm_natgas"] = np.nan
    gcr = per(lv_gc).pct_change(fill_method=None)
    R["cm_gold"] = R["cm_gold"].where(gcr.isna(), gcr + rng.normal(0, 0.003, len(GRID)))   # agrees where both exist
    R.loc[R.index < pd.Period("2000-09", "M"), "cm_gold"] = np.nan
    R.loc[R.index < pd.Period("2000-09", "M"), "cm_silver"] = np.nan
    R.loc[R.index < pd.Period("1975-01", "M")] = np.nan
    R.loc[GRID >= pd.Period("1975-01", "M"), "bd_us_10y"] = per(ty).pct_change(fill_method=None).reindex(GRID).loc[
        "1975-01":] * 1.0 + rng.normal(0, 0.002, (GRID >= pd.Period("1975-01", "M")).sum())
    S = {k: pd.DataFrame(rng.normal(0, 1, (len(GRID), len(mk))), index=GRID, columns=mk) for k in ("E", "C", "V")}
    S["E"] = np.tanh(S["E"] / 2)
    S["E_sign"] = np.sign(S["E"])
    S["V2"] = S["V"].copy()
    eia_ng = pd.DataFrame({1: per(ng1) * 1.0, 2: per(ng2) * 1.0})
    eia_ng = eia_ng.where(pd.Series(GRID >= pd.Period("1994-01", "M"), index=GRID), axis=0)
    eia_ng = eia_ng * pd.DataFrame(np.exp(rng.normal(0, 0.002, eia_ng.shape)), index=GRID, columns=[1, 2])
    S["C"]["cm_natgas"] = (12 * (eia_ng[1] / eia_ng[2] - 1))
    for key in ("V", "V2"):
        S[key]["eq_jp_nikkei"] = S[key]["eq_jp_nikkei"].where(GRID >= pd.Period("1976-01", "M"))
    eia = {"ng": eia_ng, "cl": pd.DataFrame({1: pd.Series(np.nan, index=GRID), 2: pd.Series(np.nan, index=GRID)})}
    dy0 = pd.DataFrame({"eq_jp_nikkei": pd.Series(0.02 + rng.normal(0, 0.001, len(GRID)), index=GRID)
                        .where(GRID >= pd.Period("1975-01", "M"))})
    days = pd.bdate_range("1970-01-02", "2010-12-31")
    D = pd.DataFrame(rng.normal(0, 0.008, (len(days), 4)), index=days, columns=["eq_us_spx", "bd_us_10y", "fx_eur",
                                                                               "cm_wti"])
    D.loc[:"1994-12-31", "cm_wti"] = np.nan
    gspc = pd.Series(np.exp(np.cumsum(rng.normal(0.0003, 0.01, len(days)))) * 100, index=days)
    free = {"R": R, "D": D, "S": S, "eia": eia, "dy0": dy0, "gspc": gspc}
    return blocks, free


def run(check):
    tmp = tempfile.mkdtemp(prefix="a1_smoke_")
    try:
        _run(check, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _run(check, tmp):
    blocks, free = scenario()
    work = os.path.join(tmp, "w1")
    lid = write_store(work, blocks)
    store = A1.Store(work)
    check("A1 mock store: bbgdata.Panel opens it (lock id = the LOCK file)", store.lock_id == lid)
    rows, rep = A1.evaluate(store, free)
    by = {(r["kind"], r["market"], r["ticker"]): r for r in rows}
    r_cl = by[("er", "cm_wti", "SPGSCLP Index")]
    check("A1 status ok, same root, correlation >= 0.95, months before the free start: ADMITTED",
          r_cl["verdict"] == "admitted" and r_cl["corr"] >= 0.95 and r_cl["ext_last"] == "1985-01", A1.fmt_row(r_cl))
    r_b = by[("er", "cm_wti", "BCOMCL Index")]
    check("A1 correlation gate: an unrelated index (corr < 0.95) is rejected and listed",
          r_b["verdict"] == "rejected" and any("correlation below" in x for x in r_b["reasons"]), A1.fmt_row(r_b))
    r_ng = by[("er", "cm_natgas", "SPGSNGP Index")]
    check("A1 copy: a copy block (no series id) is rejected with its status",
          r_ng["verdict"] == "rejected" and "copy" in r_ng["status"], A1.fmt_row(r_ng))
    r_ho = by[("er", "cm_heatoil", "SPGSHOP Index")]
    check("A1 cut: a block from a _CUT file is rejected", r_ho["verdict"] == "rejected" and
          any("cut file" in x for x in r_ho["reasons"]), A1.fmt_row(r_ho))
    r_cn = by[("er", "cm_corn", "SPGSCNP Index")]
    check("A1 held back: an untouched market is invisible (not in the lock)", r_cn["verdict"] == "rejected" and
          "not in the lock" in r_cn["status"], A1.fmt_row(r_cn))
    r_gc = by[("er", "cm_gold", "SPGSGCP Index")]
    check("A1 extension only: a series starting after the free start adds nothing (rejected, listed)",
          r_gc["verdict"] == "rejected" and r_gc["n_ext"] == 0 and any("nothing to extend" in x for x in r_gc["reasons"]),
          A1.fmt_row(r_gc))
    r_si = by[("er", "cm_silver", "SPGSSIP Index")]
    check("A1 too few overlap months (< 24) is rejected", r_si["verdict"] == "rejected" and
          any("too few overlap" in x for x in r_si["reasons"]), A1.fmt_row(r_si))
    r_n1, r_n2 = by[("contract", "cm_natgas", "NG1 Comdty")], by[("contract", "cm_natgas", "NG2 Comdty")]
    check("A1 block 2: contracts 1-2 from another file / sheet (primary id) admitted, extension 1990-04..1993-12",
          r_n1["verdict"] == "admitted" and r_n2["verdict"] == "admitted" and r_n1["ext_first"] == "1990-04" and
          r_n1["ext_last"] == "1993-12", A1.fmt_row(r_n1))
    r_jp = by[("dy", "eq_jp_nikkei", "MXJP Index")]
    r_cnd = by[("dy", "eq_cn", "MXCN Index")]
    check("A1 block 3: a dividend yield starting after the free one adds nothing; a market without a free yield has "
          "nothing to extend", r_jp["verdict"] == "rejected" and r_cnd["verdict"] == "rejected" and
          any("no free history" in x for x in r_cnd["reasons"]), A1.fmt_row(r_jp) + " / " + A1.fmt_row(r_cnd))
    miss = by[("er", "cm_cattle", "SPGSLCP Index")]
    check("A1 a ticker not in the lock is rejected with that status", miss["status"].startswith("not in the lock"))
    ty = [r for r in rep if r["market"] == "bd_us_10y"][0]
    check("A1 report line R: bond futures vs yield-built return, correlation reported, never admitted",
          ty["verdict"] == "report only" and ty["corr"] is not None and ty["n_overlap"] >= 60, A1.fmt_row(ty))
    check("A1 every candidate of the registered list is evaluated (16 x ER, 8 contracts, 15 dividend yields)",
          len([r for r in rows if r["block"] == 1]) == 31 and len([r for r in rows if r["block"] == 2]) == 8 and
          len([r for r in rows if r["block"] == 3]) == len(__import__("gm.bloomberg").bloomberg.EQ_INDEX))

    # ---- the panel
    a = A1.build(store, free, (1, 2, 3), rows)
    ok = True
    try:
        A1.assert_extension_only(free, a)
    except AssertionError as e:
        ok = str(e)
    check("A1 extension only: assert_extension_only passes on the built panel", ok is True, ok)
    R0, R1 = free["R"], a["R"]
    same_free = bool(np.allclose(R0["cm_wti"].dropna().values, R1["cm_wti"].reindex(R0.index)[R0["cm_wti"].notna()]
                                 .values, rtol=0, atol=0))
    new = R1["cm_wti"].notna() & R0["cm_wti"].isna()
    check("A1 extension only: every free month of cm_wti unchanged; new months only before 1985-02",
          same_free and new.any() and R1.index[new].max() < pd.Period("1985-02", "M"))
    gsci = A1._bbg_er("cm_wti", ["SPGSCLP Index"], store)
    over = R0["cm_wti"].notna() & gsci.reindex(R0.index).notna()
    check("A1 extension only: in overlap months the panel keeps the FREE value although the index differs",
          bool((R1["cm_wti"][over] == R0["cm_wti"][over]).all()) and
          bool((R1["cm_wti"][over] != gsci.reindex(R0.index)[over]).any()))
    check("A1 rejected series change nothing (cm_heatoil, cm_gold, cm_silver identical)",
          all(R0[k].equals(R1[k]) for k in ("cm_heatoil", "cm_gold", "cm_silver")))
    c0, c1 = free["S"]["C"]["cm_natgas"], a["S"]["C"]["cm_natgas"]
    cn = c1.notna() & c0.isna()
    check("A1 block 2: natgas carry extended only before its free start (1990-04..1993-12), free months unchanged",
          cn.any() and str(c1.index[cn].min()) == "1990-04" and c1.index[cn].max() < pd.Period("1994-01", "M") and
          bool((c1[c0.notna()] == c0[c0.notna()]).all()))
    check("A1 the blocks applied: build((2,)) leaves R as free, build((1,)) leaves carry as free",
          A1.build(store, free, (2,), rows)["R"].equals(R0) and
          A1.build(store, free, (1,), rows)["S"]["C"].equals(free["S"]["C"]))

    # ---- seal
    late = SL.check_output({"R": a["R"], "S": a["S"]}) is not None
    check("A1 seal: the panel has no value dated after 2010-12", late and a["R"].index.max() <= pd.Period("2010-12", "M"))
    s_cl = store.series("SPGSCLP Index", "PX_LAST")
    check("A1 seal: a one-day-delay series is served to 2010-11 only (as of 2010-12-31)",
          str(s_cl.index.max()) == "2010-11")
    try:
        bbg_panel.Source(work, asof="2011-01-31")
        refused = False
    except bbgdata.HoldoutSealed:
        refused = True
    check("A1 seal: an as-of date after 2010-12-31 raises HoldoutSealed", refused)
    blocks2 = [dict(b, sealed=pd.Series(-7e9, index=ME_SEALED)) if b["ticker"] == "SPGSCLP Index" else b
               for b in blocks]
    work2 = os.path.join(tmp, "w2")
    write_store(work2, blocks2)
    a2 = A1.build(A1.Store(work2), free, (1, 2, 3))
    check("A1 seal: other values in the sealed tables change nothing (sealed tables never read)",
          a2["R"].equals(a["R"]) and all(a2["S"][k].equals(a["S"][k]) for k in a["S"]))
    late_free = dict(free, R=free["R"].reindex(pd.period_range("1960-01", "2012-12", freq="M")).fillna(0.01))
    try:
        A1.build(store, late_free, (1,), rows)
        breach = False
    except SL.SealBreach:
        breach = True
    check("A1 seal: free inputs dated after 2010-12 make build raise SealBreach (the guard is live)", breach)
    mem = A1.MemoryStore(lid, {("SPGSCLP Index", "PX_LAST"): pd.concat([
        s_cl, pd.Series(9e9, index=pd.period_range("2011-01", "2012-12", freq="M"))])})
    check("A1 seal: Bloomberg values after 2010 are dropped by the store interface",
          mem.series("SPGSCLP Index", "PX_LAST").index.max() <= pd.Period("2010-12", "M"))

    # ---- panel id
    a_again = A1.build(store, free, (1, 2, 3))
    check("A1 panel id: stable for the same inputs", a_again["panel_id"] == a["panel_id"])
    check("A1 panel id: changes with the blocks / admitted list", A1.build(store, free, (1,), rows)["panel_id"] !=
          a["panel_id"])
    check("A1 panel id: changes with the free inputs digest and the lock id",
          A1.build(store, free, (1, 2, 3), rows, free_digest="other")["panel_id"] != a["panel_id"] and
          A1.panel_id("x" * 64, "", a["admitted"], (1, 2, 3)) != a["panel_id"])
    work3 = os.path.join(tmp, "w3")
    write_store(work3, blocks, lock_tag="other workbook")
    check("A1 panel id: a store with another lock id gives another id",
          A1.build(A1.Store(work3), free, (1, 2, 3))["panel_id"] != a["panel_id"])

    # ---- printing: no raw value
    lines = []
    for r in rows + rep:
        lines.append(A1.fmt_row(r))
    arms = [("free", None), ("block 1 alone", A1.build(store, free, (1,), rows)), ("all blocks (A1 panel)", a)]
    A1.report(free, arms, CF.A1_INCUMBENT, out=lines.append)
    txt = "\n".join(lines)
    planted = set()
    for b in blocks:
        v = b.get("values")
        if v is not None:
            for x in v.dropna().values[::7]:
                planted.add("%.4f" % x)
                planted.add("%.6g" % x)
    for x in np.concatenate([free["R"]["cm_wti"].dropna().values[::5], a["R"]["cm_wti"].dropna().values[::5],
                             a["S"]["C"]["cm_natgas"].dropna().values[::5]]):
        planted.add("%.6f" % x)
    hits = [p for p in planted if p in txt]
    check("A1 printing: no planted data value appears in the job's output (candidate rows + registered report)",
          not hits, str(hits[:5]))
    long_dec = re.findall(r"\d\.\d{5,}", txt)
    check("A1 printing: no number with 5 or more decimals in the output", not long_dec, str(long_dec[:5]))
    check("A1 report: k = 1 and k = 0 lines for every arm and era, dSR beside each non-free arm",
          sum(1 for l in lines if re.match(r"^(free|block 1 alone|all blocks \(A1 panel\)) \| k[01] \| ", l)) == 18 and
          any(l.startswith("all blocks (A1 panel) | k1 | 1975-2010") and l.count("|") >= 10 for l in lines),
          "\n".join(l for l in lines if " | k" in l)[:600])
    check("A1 report: differences explained (blocks that differ, series extended)",
          any("series extended: R cm_wti" in l for l in lines))

    # ---- the PC job itself, laid out as on the PC (cwd = local, lib\, work\): a store that is not LOCK_v2 stops it
    # before any value is read (the registered lock id cannot be forged; the code paths after the checks are the
    # functions tested above)
    import subprocess
    loc = os.path.join(tmp, "local")
    lib = os.path.join(loc, "lib")
    os.makedirs(lib)
    shutil.copytree(os.path.join(REPO, "gm"), os.path.join(lib, "gm"),
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    bq = os.path.join(REPO, "tools", "bbgq")
    for rel in ("lib/gm_engine.py", "lib/bbg_panel.py", "lib/bbgdata.py", "lib/a1_panel.py", "live_sources.csv",
                "untouched_markets.csv", "engine_ref.json"):
        shutil.copy(os.path.join(bq, rel), os.path.join(lib, os.path.basename(rel)))
    write_store(os.path.join(loc, "work"), blocks)
    env = dict(os.environ, BBG_WORK=os.path.join(loc, "work"), PYTHONPATH="")
    p = subprocess.run([sys.executable, os.path.join(bq, "jobs", "gm_a1_v1.py")], cwd=loc, env=env,
                       capture_output=True, text=True, timeout=600)
    o = p.stdout
    check("A1 job (PC layout): gm code = the reference, a non-LOCK_v2 store -> STOP before any value is read",
          "PASS gm code vs reference" in o and "FAIL Bloomberg store lock id" in o and
          "STOP: the Bloomberg store is not LOCK_v2 (nothing read)" in o and p.returncode == 0, (o + p.stderr)[-600:])
    check("A1 job output: no planted value, no number with 5+ decimals",
          not [x for x in planted if x in o] and not re.findall(r"\d\.\d{5,}", o))


if __name__ == "__main__":
    fails = []

    def check(name, ok, detail=""):
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)[:400]))
        if not ok:
            fails.append(name)
    run(check)
    print("A1 PANEL SMOKE " + ("PASSED" if not fails else "FAILED: %d" % len(fails)))
    sys.exit(1 if fails else 0)
