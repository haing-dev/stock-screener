"""Offline checks of the validation code (point-in-time backtest, statistics, report) on the real SEC samples with
synthetic prices. Called by run_tests.py; can also run alone: python tests/validation_smoke.py"""
import glob
import gzip
import json
import math
import os
import random
import shutil
import sys
import tempfile
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def run(check):
    tmp = tempfile.mkdtemp(prefix="qs_val_")
    import qs.backtest as bt
    import qs.backtest_support as bs
    bt.COMP_DIR, bt.FORM_DIR, bt.RET_DIR = (os.path.join(tmp, x) for x in ("companies", "formations", "returns"))
    bs.OUT = os.path.join(tmp, "out")
    from qs.btanalysis import Panel, analyse
    from qs.btprices import holding_return
    from qs.config import load_config
    from qs.pit import facts_as_of, info_as_of, filings_subset, last_filed
    from qs import valreport
    valreport.OUT = bs.OUT
    cfg = load_config()

    # ---------------------------------------------------------------- point-in-time filters
    facts = {}
    for p in glob.glob(os.path.join(ROOT, "tests", "real_samples", "*companyfacts*.json.gz")):
        with gzip.open(p, "rt", encoding="utf-8") as f:
            fs = json.load(f)
        if fs.get("cik") and fs["cik"] not in facts:
            facts[int(fs["cik"])] = fs
    aapl = facts.get(320193)
    cut = facts_as_of(aapl, "2020-01-01")
    ents = [e for t in cut["facts"].values() for u in t.values() for es in u.values() for e in es]
    check("as-of filter keeps only facts filed before the date", ents and max(e["filed"] for e in ents) < "2020-01-01")
    check("last filing date before a date", last_filed(aapl, "2020-01-01") == max(e["filed"] for e in ents))
    sub = {"cik": 1, "name": "X", "sic": "3571", "filings": {"recent": {
        "form": ["10-K", "8-K", "10-K", "10-12B"], "filingDate": ["2024-02-01", "2023-06-01", "2023-02-01", "2022-05-01"],
        "reportDate": ["2023-12-31", "", "2022-12-31", ""], "accessionNumber": ["a1", "a2", "a3", "a4"],
        "items": ["", "1.03", "", ""], "primaryDocument": ["", "", "", ""]}}}
    fsub = filings_subset(sub)
    inf = info_as_of(fsub, "2023-12-31")
    check("profile as of a date: latest annual report before it", (inf["latest_annual"] or {}).get("accn") == "a3")
    check("profile as of a date: later events invisible",
          all(e["date"] < "2023-12-31" for e in inf["events"]) and any(e["accn"] == "a2" for e in inf["events"]))
    check("holding return: 2-for-1 split + dividend", abs(holding_return(100, 55, [("2024-01-10", 1, 2)],
                                                                         [("2024-01-20", 0.5)], "2024-01-01",
                                                                         "2024-02-01") - (55 * 2 + 1.0) / 100 + 1)
          < 1e-12)

    import io
    import zipfile
    from qs.btstats import merge_factors, parse_french

    def _z(text):
        bio = io.BytesIO()
        with zipfile.ZipFile(bio, "w") as zf:
            zf.writestr("x.CSV", text)
        return bio.getvalue()
    ff5 = parse_french(_z("Created by CMPT.\r\n\r\n,Mkt-RF,SMB,HML,RMW,CMA,RF\r\n202401, 1.00, 0.10, -0.20, 0.30,"
                          " 0.00, 0.40\r\n\r\n Annual Factors \r\n,Mkt-RF,SMB,HML,RMW,CMA,RF\r\n2024, 9,9,9,9,9,9\r\n"))
    mom = parse_french(_z("Created.\r\n\r\nMonthly Momentum\r\n,Mom   \r\n202401,   0.57\r\n\r\nAnnual\r\n,Mom\r\n2024, 9\r\n"))
    fm_ = merge_factors(ff5, mom)
    check("Kenneth French files parsed (monthly block only, percent -> decimal)",
          list(fm_) == ["2024-01"] and abs(fm_["2024-01"]["Mkt-RF"] - 0.01) < 1e-12 and abs(fm_["2024-01"]["UMD"] - 0.0057) < 1e-12)

    # ---------------------------------------------------------------- synthetic grid
    rnd = random.Random(3)
    ciks = sorted(facts)
    sym = {c: f"S{c}" for c in ciks}
    price = {c: 50.0 + rnd.random() * 50 for c in ciks}
    grid = []
    d = date(2019, 1, 31)
    months = []
    while d < date(2026, 7, 1):
        months.append(d)
        nxt = (d.replace(day=1) + timedelta(days=40)).replace(day=1)
        d = nxt + timedelta(days=-1 + 31) if False else (nxt.replace(day=28) + timedelta(days=4)).replace(day=1) - \
            timedelta(days=1)
    for me in months:
        bars_d, bars_e = {}, {}
        for c in ciks:
            price[c] *= math.exp(rnd.gauss(0.005, 0.08))
            bars_d[sym[c]] = [price[c], price[c], 1e6, price[c], price[c], price[c]]
            bars_e[sym[c]] = [price[c] * 1.001, price[c], 1e6, price[c], price[c], price[c]]
        e = me + timedelta(days=1)
        grid.append({"ym": me.strftime("%Y-%m"), "d": me.isoformat(), "e": e.isoformat(), "bars_d": bars_d,
                     "bars_e": bars_e})
    univ = {g["d"]: {c: {"tickers": [sym[c]], "type": "CS", "ex": "XNAS", "name": facts[c].get("entityName")}
                     for c in ciks} for g in grid}
    bt.run_company_pass(grid, univ, cfg, lambda c: facts.get(c), lambda c: None, log=lambda *a: None)
    bt.run_formations(grid, univ, cfg, {}, log=lambda *a: None)

    class StubBTP:
        def resolve(self, s, day):
            return {"cik": int(s[1:])}

        def last_close(self, *a):
            return None
    bt.run_returns(grid, StubBTP(), {}, {}, log=lambda *a: None)
    from qs.backtest_support import read_json
    f0 = read_json(os.path.join(bt.FORM_DIR, grid[-2]["ym"] + ".json.gz"))
    check("formation: every screen evaluated", set(f0["screens"]) >= {"core", "fortress", "red_flags"})
    n_eval = sum(len(v) for v in f0["screens"].values())
    check("formation: companies in screen universes", n_eval > 50, str(n_eval))
    late_pass = sum(1 for v in f0["screens"].values() for r in v.values() if r[0] == "PASS")
    check("formation: some passes in the latest month", late_pass > 0, str(late_pass))

    # leakage: the formation of an early month must not change when every later fact is deleted
    g0 = grid[24]
    cut_facts = {c: facts_as_of(fs, g0["d"]) for c, fs in facts.items()}
    tmp2 = tempfile.mkdtemp(prefix="qs_val2_")
    bt.COMP_DIR, bt.FORM_DIR = os.path.join(tmp2, "c"), os.path.join(tmp2, "f")
    bt.run_company_pass(grid[:25], univ, cfg, lambda c: cut_facts.get(c), lambda c: None, log=lambda *a: None)
    bt.run_formations(grid[:25], univ, cfg, {}, log=lambda *a: None)     # same price history up to that month
    a = read_json(os.path.join(tmp, "formations", g0["ym"] + ".json.gz"))
    b = read_json(os.path.join(tmp2, "f", g0["ym"] + ".json.gz"))
    check("no look-ahead: formation unchanged after deleting every fact filed later",
          a["screens"] == b["screens"] and a["grid"] == b["grid"])
    bt.COMP_DIR, bt.FORM_DIR = os.path.join(tmp, "companies"), os.path.join(tmp, "formations")
    shutil.rmtree(tmp2, ignore_errors=True)

    # ---------------------------------------------------------------- prices (Massive fixtures), audit, fidelity
    from qs.massive import Massive
    from qs.btprices import BTPrices
    fx = os.path.join(tmp, "fx", "massive")
    os.makedirs(fx)

    def put(path, obj):
        with open(os.path.join(fx, path.strip("/").replace("/", "_") + ".json"), "w") as fh:
            json.dump(obj, fh)
    put("/v2/aggs/grouped/locale/us/market/stocks/2024-01-31",
        {"results": [{"T": "OLD", "o": 10, "c": 11, "v": 100}, {"T": "NEW", "o": 20, "c": 21, "v": 100}]})
    put("/v2/aggs/grouped/locale/us/market/stocks/2024-02-01",
        {"results": [{"T": "NEW", "o": 22, "c": 23, "v": 100}]})
    put("/v3/reference/tickers", {"results": [
        {"ticker": "OLD", "cik": "0000000111", "type": "CS", "primary_exchange": "XNYS", "active": False,
         "delisted_utc": "2024-03-01T00:00:00Z"},
        {"ticker": "OLD", "cik": "0000000999", "type": "CS", "primary_exchange": "XNAS", "active": True},
        {"ticker": "NEW", "cik": "0000000222", "type": "ETF", "primary_exchange": "ARCX", "active": True}]})
    put("/v3/reference/dividends", {"results": [{"ticker": "OLD", "ex_dividend_date": "2024-02-15",
                                                 "cash_amount": 0.25, "currency": "USD"}]})
    mm = Massive("", os.path.join(tmp, "fxcache"), fixtures_dir=os.path.join(tmp, "fx"), today=date(2024, 6, 1),
                 log=lambda *a: None)
    btp = BTPrices(mm, log=lambda *a: None)
    gr = btp.grid((2024, 1), (2024, 1))
    check("price grid: month-end formation day and next trading day", gr and gr[0]["d"] == "2024-01-31"
          and gr[0]["e"] == "2024-02-01", str([(g["d"], g["e"]) for g in gr]))
    check("ticker reuse: a delisted ticker maps to its old company before the delisting",
          btp.resolve("OLD", "2024-01-31")["cik"] == 111 and btp.resolve("OLD", "2024-06-01")["cik"] == 999)
    u = btp.universe("2024-01-31", gr[0]["bars_d"], ["NYSE", "Nasdaq"]) if gr else {}
    check("universe: stocks of the wanted exchanges only (ETF left out)", set(u) == {111}, str(u))
    check("dividend list", btp.dividends("2024-01-01").get("OLD") == [("2024-02-15", 0.25)])

    from qs import audit, fidelity
    audit.load_facts = lambda c: facts.get(int(c))
    pk = audit.sample(f0, n=40)
    check("audit sample: stratified by screen, distinct companies", len(pk) == len({c for _s, c in pk}) and
          len({s for s, _c in pk}) >= 5, str(len(pk)))
    figs = audit.our_figures(pk[0][1], f0["d"]) if pk else []
    check("audit: figures carry tag, accession and period for the SEC data-set lookup",
          figs and all(x[3] and x[5] and x[6] for x in figs), str(figs[:2]))
    st = audit.star_sheet(f0, n=5)
    check("star review sheet doesn't show the screener's verdict", all("class" not in r for r in st))
    sc = fidelity.score([{"who": "M", "screens": ["core"]}], {"M": set(list(f0["screens"]["core"])[:5])}, f0)
    check("style fidelity: rate and universe rate per screen", "rate" in sc["managers"][0]["screens"]["core"])

    # ---------------------------------------------------------------- statistics and report
    months_p = []
    for g in grid[:-1]:
        f = read_json(os.path.join(bt.FORM_DIR, g["ym"] + ".json.gz"))
        r = read_json(os.path.join(bt.RET_DIR, g["ym"] + ".json.gz"))
        if f and r:
            months_p.append((f, r))
    panel = Panel(months_p)
    fac = {}
    for ym in panel.yms:
        fac[ym] = {k: rnd.gauss(0, 0.03) for k in ("Mkt-RF", "SMB", "HML", "RMW", "CMA", "UMD")}
        fac[ym]["RF"] = 0.001
    res = analyse(panel, fac)

    # forward record: live lists recorded in 'history' replace the reconstructed ones (here: identical copies)
    import qs.validate as V
    from qs import listlog
    V.PREREG_DATE = "2019-01-01"
    hdir = os.path.join(tmp, "history")
    fm = months_p[-3][0]
    snap = {"date": fm["d"], "kind": "screen", "screens": {
        sid: {"pass": [[int(c)] for c, r in res_.items() if r[0] == "PASS" and not r[1]],
              "star": [[int(c)] for c, r in res_.items() if r[0] == "PASS" and r[1]],
              "near": [[int(c)] for c, r in res_.items() if r[0] == "NEAR"]} for sid, res_ in fm["screens"].items()}}
    listlog.write(snap, os.path.join(hdir, "lists", fm["d"][:4]))
    fp, agree = V.forward_panel(panel, hdir, log=lambda *a: None)
    check("forward record: live lists matched to their formation month",
          fp is not None and len(fp.months) == 1 and all(v == [1.0] for v in agree.values() if v), str(agree)[:200])
    V.FORM_DIR, V.RET_DIR, V.OUT = bt.FORM_DIR, bt.RET_DIR, bs.OUT
    V.export_raw(log=lambda *a: None)
    with gzip.open(os.path.join(bs.OUT, "lists.csv.gz"), "rt") as fh:
        n_lines = sum(1 for _ in fh)
    check("raw outputs: monthly lists exported for anyone to recompute", n_lines > 100, str(n_lines))
    check("statistics: a verdict for every screen", all("verdict" in v for v in res["screens"].values()))
    check("statistics: random prices give no 'edge'", not any(v["verdict"] == "edge" for v in res["screens"].values()),
          ", ".join(f"{k}={v['verdict']}" for k, v in res["screens"].items()))
    os.makedirs(bs.OUT, exist_ok=True)
    with open(os.path.join(bs.OUT, "stats.json"), "w") as fh:
        json.dump(res, fh, default=str)
    path = valreport.write_report(cfg)
    txt = open(path, encoding="utf-8").read()
    check("report written with the verdict table", "| Screen | Verdict |" in txt)
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    fails = []

    def check(name, cond, detail=""):
        print(("  ok   " if cond else "  FAIL ") + name + (f"  ({detail})" if detail else ""))
        if not cond:
            fails.append(name)
    run(check)
    print("\nVALIDATION SMOKE " + ("PASSED" if not fails else f"FAILED: {fails}"))
