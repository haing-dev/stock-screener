"""Smoke test of the triage (triage/): real SEC samples, synthetic month-end prices, 13F and Form 4 data.

    python tests/triage_smoke.py            -> checks
    python tests/triage_smoke.py --demo DIR -> also an unencrypted preview site in DIR (python -m http.server)

Prices, owners and insider trades are invented (deterministic): only the mechanics are real.
"""
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


def _setup(tmp):
    import qs.backtest as bt
    import triage.paths as P
    bt.COMP_DIR = os.path.join(tmp, "companies")
    P.TRI = os.path.join(tmp, "tri")
    for k, sub in (("PANEL", "panel"), ("RETURNS", "returns"), ("OWNERS", "owners"), ("INSIDERS", "insiders"),
                   ("OUT", "out")):
        setattr(P, k, os.path.join(P.TRI, sub))
    P.MARK = os.path.join(P.TRI, "mark.json.gz")
    P.SITE = os.path.join(tmp, "site")
    return bt, P


def _shares(fs):
    for tax, tag in (("dei", "EntityCommonStockSharesOutstanding"), ("us-gaap", "WeightedAverageNumberOfDilutedSharesOutstanding"),
                     ("us-gaap", "CommonStockSharesOutstanding"), ("us-gaap", "WeightedAverageNumberOfSharesOutstandingBasic")):
        try:
            ents = fs["facts"][tax][tag]["shares"]
            return max(ents, key=lambda e: e.get("filed", ""))["val"]
        except (KeyError, ValueError, TypeError):
            continue
    return None


def world(seed=5):
    """(facts, filings, sym, grid, univ): real companyfacts samples, synthetic 10-K/10-Q filing histories and
    month-end bars 2018-01 .. 2026-09 with a few deep falls."""
    from qs.pit import filings_subset
    facts = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "tests", "real_samples", "*companyfacts*.json.gz"))):
        with gzip.open(p, "rt", encoding="utf-8") as f:
            fs = json.load(f)
        if fs.get("cik") and int(fs["cik"]) not in facts and _shares(fs):
            facts[int(fs["cik"])] = fs
    rnd = random.Random(seed)
    ciks = sorted(facts)
    sics = ["3571", "3572", "3576", "3577", "3559", "3561", "3585", "3599", "7372", "7373", "7374", "7389", "7370"]
    filings = {}
    for n, c in enumerate(ciks):
        forms, fds, rds, accs = [], [], [], []
        for y in range(2009, 2027):
            for m, form in ((2, "10-K"), (5, "10-Q"), (8, "10-Q"), (11, "10-Q")):
                forms.append(form)
                fds.append(f"{y}-{m:02d}-15")
                rds.append(f"{y - 1 if m == 2 else y}-{12 if m == 2 else m - 2:02d}-28")
                accs.append(f"{c}-{y}-{m}")
        sub = {"cik": c, "name": facts[c].get("entityName"), "sic": sics[n % len(sics)],
               "sicDescription": "test", "tickers": [f"S{c}"], "exchanges": ["Nasdaq"],
               "filings": {"recent": {"form": forms, "filingDate": fds, "reportDate": rds, "accessionNumber": accs,
                                      "items": [""] * len(forms), "primaryDocument": [""] * len(forms)}}}
        filings[c] = filings_subset(sub)
    sym = {c: f"S{c}" for c in ciks}
    mcap0 = {c: math.exp(rnd.uniform(math.log(4e8), math.log(6e10))) for c in ciks}
    price = {c: mcap0[c] / _shares(facts[c]) for c in ciks}
    from triage.panel import nominal_scans
    scans = nominal_scans((2018, 1), date(2026, 9, 30))
    crash = {c: (rnd.randint(60, 190) if rnd.random() < 0.6 else None) for c in ciks}
    grid = []
    for k, d in enumerate(scans):
        bars_d, bars_e = {}, {}
        for c in ciks:
            shock = -0.55 if (crash[c] == k or (c == ciks[0] and k == len(scans) - 1)) else \
                (0.18 if crash[c] and 6 <= k - crash[c] <= 12 else 0.0)
            price[c] *= math.exp(rnd.gauss(0.003, 0.05) + shock)
            bars_d[sym[c]] = [price[c], price[c], 2e6, price[c]]
            bars_e[sym[c]] = [price[c] * 1.002, price[c], 2e6, price[c]]
        for s, px in (("SPY", 400 * math.exp(0.0035 * k)), ("IWM", 180 * math.exp(0.0025 * k))):
            bars_d[s], bars_e[s] = [px, px, 1e7, px], [px, px, 1e7, px]
        e = d + timedelta(days=1)
        grid.append({"ym": d.isoformat(), "d": d.isoformat(), "e": e.isoformat(), "bars_d": bars_d, "bars_e": bars_e})
    univ = {g["d"]: {c: {"tickers": [sym[c]], "type": "CS", "ex": "XNAS", "name": facts[c].get("entityName")}
                     for c in ciks} for g in grid}
    return facts, filings, sym, grid, univ


def owners_and_insiders(P, ciks, grid, rnd):
    """Synthetic 13F conviction rows (8 filers) and Form 4 trades written where the build reads them."""
    from qs.backtest_support import write_json
    from triage.episodes import plus
    os.makedirs(P.OWNERS, exist_ok=True)
    os.makedirs(P.INSIDERS, exist_ok=True)
    rows = []
    quarters = sorted({f"{g['d'][:4]}-{q}" for g in grid for q in ("03-31", "06-30", "09-30", "12-31")})
    for q in quarters:
        for f in range(8):
            for c in rnd.sample(ciks, 6):
                rows.append([f"9{f}", f"Fund {chr(65 + f)}", q, plus(q, rnd.randint(20, 44)), str(c),
                             round(rnd.uniform(0.03, 0.12), 4)])
    write_json(os.path.join(P.OWNERS, "all.json.gz"), {"span": ["2017-01-01", "2026-09-30"], "rows": rows})
    by = {}
    for c in ciks:
        ts = []
        for _ in range(rnd.randint(0, 12)):
            day = date(2018, 1, 1) + timedelta(days=rnd.randint(0, 3150))
            side = rnd.choice(["P", "S", "Splan", "Sex"])
            ts.append([day.isoformat(), (day + timedelta(days=2)).isoformat(), side, rnd.randint(5_000, 3_000_000),
                       "Jane Doe", "Director"])
        by[str(c)] = ts
    write_json(os.path.join(P.INSIDERS, "2026q3.json.gz"), {"q": "2026q3", "end": "2026-09-30", "by_cik": by})


def factors(grid, rnd):
    return {ym: {"Mkt-RF": rnd.gauss(0.006, 0.04), "SMB": rnd.gauss(0, 0.02), "HML": rnd.gauss(0, 0.02),
                      "RMW": rnd.gauss(0, 0.015), "CMA": rnd.gauss(0, 0.015), "UMD": rnd.gauss(0, 0.03), "RF": 0.002}
            for ym in sorted({g["e"][:7] for g in grid})}


def debug_played(out):
    for kind, kd in out["kinds"].items():
        for x in kd["items"]:
            if x["played"] and (x.get("ctrl_ret") is None or x.get("idx_ret") is None):
                print(kind, x["id"], x.get("ctrl_ret"), x.get("idx_ret"), len(x["path"]))


def run(check, demo_dir=None):
    tmp = tempfile.mkdtemp(prefix="tri_smoke_")
    bt, P = _setup(tmp)
    from qs.backtest_support import read_json
    from qs.config import load_config
    import triage.panel as PN
    import triage.returns as RT
    from triage import build as B
    from triage import episodes as E
    from triage import rules as R
    from triage import score as SC
    from triage import site as S
    cfg = load_config()
    rnd = random.Random(11)
    facts, filings, sym, grid, univ = world()
    ciks = sorted(facts)

    orig = PN.contexts_at

    def verified(*a, **k):                    # synthetic prices don't match the companies' public float
        ctxs, subs, extra = orig(*a, **k)
        for ctx in ctxs.values():
            for key in [x for x in ctx if x.endswith("_unverified")]:
                if ctx.get(key[:-len("_unverified")]) is None:
                    ctx[key[:-len("_unverified")]] = ctx[key]
            ctx["val_ok"] = True
        return ctxs, subs, extra
    PN.contexts_at = verified
    bt.run_company_pass(grid, univ, cfg, lambda c: facts.get(c), lambda c: filings.get(c), log=lambda *a: None)
    PN.save_grid(grid, {g["d"]: {str(c): u for c, u in univ[g["d"]].items()} for g in grid})
    PN.build(grid, univ, cfg, {}, log=lambda *a: None)
    months = PN.months()
    check("panel: a file per month", len(months) == len(grid), f"{len(months)} of {len(grid)}")
    p_last = PN.load(months[-1])["companies"]
    check("panel: US companies with prices, fundamentals and universes",
          len(p_last) >= 20 and all(r.get("px") and "u" in r for r in p_last.values()), str(len(p_last)))
    check("panel: 12-month fall and price change measured", sum(1 for r in p_last.values() if r.get("dd") is not None
                                                                and r.get("r12") is not None) >= 20)

    # no look-ahead: an early month's panel is unchanged when every fact filed later is deleted
    from qs.pit import facts_as_of
    cut_ym = months[80]
    cut_d = grid[80]["d"]
    cut = {c: facts_as_of(f, cut_d) for c, f in facts.items()}
    early = PN.load(cut_ym)["companies"]
    shutil.rmtree(bt.COMP_DIR)
    keep_panel = P.PANEL
    P.PANEL = os.path.join(tmp, "panel_cut")
    bt.run_company_pass(grid[:81], univ, cfg, lambda c: cut.get(c), lambda c: filings.get(c), log=lambda *a: None)
    PN.build(grid[:81], univ, cfg, {}, log=lambda *a: None)
    again = PN.load(cut_ym)["companies"]
    check("no look-ahead: panel unchanged after deleting every fact filed later", again == early)
    P.PANEL = keep_panel
    shutil.rmtree(bt.COMP_DIR)
    bt.run_company_pass(grid[:81], univ, cfg, lambda c: facts.get(c), lambda c: filings.get(c), log=lambda *a: None)
    bt.run_company_pass(grid, univ, cfg, lambda c: facts.get(c), lambda c: filings.get(c), log=lambda *a: None)
    import gzip as _gz
    import pickle
    with _gz.open(os.path.join(bt.COMP_DIR, f"{ciks[0]}.pkl.gz"), "rb") as f:
        inc = pickle.load(f)
    check("company pass: a later run adds only the new month-ends", len(inc["dates"]) == len(grid) and "key" in inc)

    y1 = PN.ttm_ebit_asof(ciks[0], "2025-06-30", "3571", cfg, load_facts=lambda c: facts.get(c))
    rec_then = next((PN.load(m)["companies"].get(str(ciks[0])) for m in months if m >= "2025-07-01"), None)
    check("profit trend: year-ago operating income computed point in time",
          y1 is not None and rec_then is not None and abs(y1 - rec_then["ebit"]) <= abs(y1) * 1e-9 + 1, f"{y1} vs {rec_then and rec_then['ebit']}")

    class StubBTP:
        def resolve(self, s, day):
            return {"cik": int(s[1:])} if s.startswith("S") and s[1:].isdigit() else None

        def last_close(self, *a):
            return None
    RT.build(grid, StubBTP(), {}, {}, log=lambda *a: None)
    idx = read_json(os.path.join(P.RETURNS, "index.json.gz"))
    check("returns: index ETF months", len(idx) == len(grid) - 1 and abs(idx[months[0]]["SPY"] - (math.exp(0.0035) - 1)) < 1e-6)
    owners_and_insiders(P, ciks, grid, rnd)
    last = grid[-1]
    mark = {"day": "2026-10-20", "closes": {s: b[1] * 1.03 for s, b in last["bars_d"].items()}}
    opens = {s: b[0] for s, b in last["bars_e"].items()}
    rec_dir = os.path.join(tmp, "record")
    out = B.build(months=months, grid=[{k: g[k] for k in ("ym", "d", "e")} for g in grid], mark=mark, opens=opens,
                  splits={}, divs={}, factors=factors(grid, rnd), record_dir=rec_dir, log=lambda *a: None,
                  today="2026-10-10")
    n = {k: len(v["items"]) for k, v in out["kinds"].items()}
    check("events found in every triage", all(n[k] > 0 for k in R.KINDS), str(n))

    # event rules re-checked from the panel
    ok, bad = 0, []
    for kind, kd in out["kinds"].items():
        for it in kd["items"]:
            i = months.index(it["ym"])
            rec = PN.load(it["ym"])["companies"][str(it["cik"])]
            if E.backend(kind, rec):
                bad.append((kind, it["id"], "backend"))
            if kind == "hidden":
                prev = PN.load(months[i - 1])["companies"].get(str(it["cik"]))
                if not (rec["dd"] <= R.HIDDEN_FALL and prev and prev["dd"] is not None and prev["dd"] > R.HIDDEN_FALL):
                    bad.append((kind, it["id"], "trigger"))
            elif not ((it["p_own"] or 0) >= R.CHEAP_PCTL or (it["p_peer"] or 0) >= R.CHEAP_PCTL):
                bad.append((kind, it["id"], "cheap"))
            ok += 1
        by_cik = {}
        for it in sorted(kd["items"], key=lambda x: x["ym"]):
            j = months.index(it["ym"])
            if it["cik"] in by_cik and j - by_cik[it["cik"]] < R.COOLDOWN:
                bad.append((kind, it["id"], "cooldown"))
            by_cik[it["cik"]] = j
    check("events: trigger crossed, backend met, 6-month cooldown", not bad and ok > 0, str(bad[:3]))

    # calls follow the written rule
    wrong = []
    for kind, kd in out["kinds"].items():
        for it in kd["items"]:
            if it["verdict"] == "tbu":
                continue
            cols = {k: (c[0] if c[1] != "N/A" else None) for k, c in it["factors"].items()}
            s = R.score(kind, cols)
            if abs(s - it["score"]) > 1e-9 or not -1 <= s <= 1:
                wrong.append(it["id"])
            if not it["upgraded"]:
                hard = SC.hard_avoid(kind, PN.load(it["ym"])["companies"][str(it["cik"])])
                if R.call(kind, cols, hard)[0] != it["verdict"]:
                    wrong.append(it["id"])
    check("calls: score = weighted cells, call = the written rule", not wrong, str(wrong[:3]))
    vs = {v for kd in out["kinds"].values() for v in (x["verdict"] for x in kd["items"])}
    check("calls: Buy candidates, Watch and Avoid all occur", {"overdone", "close", "justified"} <= vs, str(vs))
    played = [x for kd in out["kinds"].values() for x in kd["items"] if x["played"]]
    check("outcomes: 12 months of returns for played events", played and all(len(x["path"]) == 13 for x in played))
    openi = [x for kd in out["kinds"].values() for x in kd["items"] if not x["played"] and x.get("path")]
    check("outcomes: open events marked to the latest close", openi and all(x["ret_to"] == "2026-10-20" for x in openi
                                                                             if x["date"] == grid[-1]["d"]))
    if os.environ.get("TRI_DEBUG"):
        debug_played(out)
        print([(k, x["id"], x["verdict"], x["why"]) for k, kd in out["kinds"].items() for x in kd["items"] if x["date"] >= "2026-08-01"])
    check("outcomes: similar stocks and index alongside", sum(1 for x in played if x.get("ctrl_ret") is not None
                                                              and x.get("idx_ret") is not None) == len(played))
    ev0 = next(e for e in E.detect(months[:120], log=lambda *a: None)["hidden"] if e["sim"])
    check("similar stocks: up to 10, never the company itself", len(ev0["sim"]) <= 10 and ev0["cik"] not in ev0["sim"])

    # owners: only 13Fs whose deadline had passed and that were filed by the date
    O = E.Owners([["1", "F", "2024-03-31", "2024-05-10", "5", 0.05], ["2", "G", "2024-03-31", "2024-07-02", "5", 0.04],
                  ["3", "H", "2024-06-30", "2024-07-20", "5", 0.06], ["4", "J", "2023-12-31", "2024-02-10", "5", 0.09]],
                 "2026-09-30", "2017-01-01")
    f = O.funds("5", "2024-06-30")
    check("13F: last quarter past its deadline, filed by the date; later filers kept apart",
          [x[0] for x in f["list"]] == ["1"] and [x[0] for x in f["later"]] == ["3"], str(f))
    # the SEC data-set readers on miniature files in the published column layout
    import io
    import zipfile
    from triage import owners as OW

    def zf(tables):
        b = io.BytesIO()
        with zipfile.ZipFile(b, "w") as z:
            for name, rows in tables.items():
                z.writestr(name, "\n".join("\t".join(r) for r in rows))
        return b
    z13 = zf({"SUBMISSION.tsv": [["ACCESSION_NUMBER", "FILING_DATE", "SUBMISSIONTYPE", "CIK", "PERIODOFREPORT"],
                                 ["A1", "14-MAY-2024", "13F-HR", "777", "31-MAR-2024"],
                                 ["A2", "10-MAY-2024", "13F-HR", "888", "31-MAR-2024"]],
              "COVERPAGE.tsv": [["ACCESSION_NUMBER", "FILINGMANAGER_NAME", "REPORTTYPE", "AMENDMENTTYPE"],
                                ["A1", "PATIENT CAPITAL LLC", "13F HOLDINGS REPORT", ""],
                                ["A2", "VANGUARD GROUP INC", "13F HOLDINGS REPORT", ""]],
              "INFOTABLE.tsv": [["ACCESSION_NUMBER", "NAMEOFISSUER", "TITLEOFCLASS", "CUSIP", "VALUE", "SSHPRNAMT", "SSHPRNAMTTYPE", "PUTCALL"],
                                ["A1", "ACME CORP", "COM", "000111AA1", "20000000", "1000", "SH", ""],
                                ["A1", "OTHER INC", "COM", "000222BB2", "180000000", "1000", "SH", ""],
                                ["A1", "ACME CORP", "CALL", "000111AA1", "90000000", "1000", "SH", "Call"],
                                ["A2", "ACME CORP", "COM", "000111AA1", "900000000", "1000", "SH", ""]]})
    zp = os.path.join(tmp, "t13f.zip")
    open(zp, "wb").write(z13.getvalue())
    rows13, rem = OW.read_13f(zp, {5: {"ticker": "ACME", "name": "Acme Corp", "other_tickers": ""}}, {}, cfg["portal"]["holders"],
                              log=lambda *a: None, figi=lambda cus, **k: {c: "ACME" for c in cus})
    check("13F data set: conviction positions (3%+, options out, index funds out, dollar units from 2023)",
          rows13 == [["777", "Patient Capital", "2024-03-31", "2024-05-14", "5", 0.1]] and rem == 0, str(rows13))
    zin = zf({"SUBMISSION.tsv": [["ACCESSION_NUMBER", "FILING_DATE", "DOCUMENT_TYPE", "ISSUERCIK", "AFF10B5ONE"],
                                 ["B1", "05-MAR-2024", "4", "5", "0"], ["B2", "06-MAR-2024", "4", "5", "1"],
                                 ["B3", "06-MAR-2024", "4", "6", "0"]],
              "REPORTINGOWNER.tsv": [["ACCESSION_NUMBER", "RPTOWNERNAME", "RPTOWNER_RELATIONSHIP", "RPTOWNER_TITLE"],
                                     ["B1", "DOE JANE", "Director", ""], ["B2", "ROE RICK", "Officer", "CEO"]],
              "NONDERIV_TRANS.tsv": [["ACCESSION_NUMBER", "TRANS_DATE", "TRANS_CODE", "TRANS_SHARES", "TRANS_PRICEPERSHARE"],
                                     ["B1", "01-MAR-2024", "P", "1000", "20"], ["B2", "04-MAR-2024", "S", "500", "21"],
                                     ["B1", "01-MAR-2024", "S", "10", "20"]],
              "DERIV_TRANS.tsv": [["ACCESSION_NUMBER", "TRANS_DATE", "TRANS_CODE"], ["B1", "01-MAR-2024", "M"]]})
    with zipfile.ZipFile(zin) as z:
        ins_rows = OW.read_insiders(z, {5})
    check("insider data set: buys, plan sales and same-day exercise sales told apart",
          sorted(r[2] for r in ins_rows.get("5", [])) == ["P", "Sex", "Splan"] and "6" not in ins_rows, str(ins_rows))
    iv = E.insider_view([["2024-05-01", "2024-05-03", "P", 50_000, "A", ""], ["2024-05-02", "2024-05-04", "Splan", 9e6, "B", ""],
                         ["2023-01-01", "2023-01-03", "S", 9e6, "C", ""]], "2024-06-30", 1e8)
    check("insiders: plan sales and old trades left out; materiality vs market cap",
          iv["net"] == 50_000 and iv["colour"] == "g" and iv["plan"] == 9e6)
    check("statistics: factor regression of the Buy candidates", any(
        (kd.get("regression") or {}).get("overdone", {}).get("alpha_m") is not None for kd in out["kinds"].values()))
    check("statistics: per-cell evidence and the $10,000 test", all(kd["evidence"] for kd in out["kinds"].values())
          and any(kd["years"] for kd in out["kinds"].values()))
    import csv
    led = list(csv.DictReader(open(os.path.join(rec_dir, "ledger.csv"), encoding="utf-8")))
    check("live calls written to the ledger (recent events only)", led and all(r["month_end"] >= "2026-08-26" for r in led),
          str(len(led)))
    out2 = B.build(months=months, grid=[{k: g[k] for k in ("ym", "d", "e")} for g in grid], mark=mark, opens=opens,
                   splits={}, divs={}, factors={}, record_dir=rec_dir, log=lambda *a: None, today="2026-10-10")
    led2 = list(csv.DictReader(open(os.path.join(rec_dir, "ledger.csv"), encoding="utf-8")))
    check("ledger: a rebuild adds no duplicate calls", len(led2) == len(led) and out2["live"])

    site_dir = S.build("", allow_plain=True, data=out, out_dir=os.path.join(tmp, "site"), log=lambda *a: None,
                       salt_path=os.path.join(tmp, "salt.json"))
    with open(os.path.join(site_dir, "data", "data.bin"), "rb") as fh:
        back = json.loads(gzip.decompress(fh.read()))
    check("site: data readable, three triages, page code copied",
          set(back["kinds"]) == set(R.KINDS) and os.path.exists(os.path.join(site_dir, "app.js")))
    enc = S.build("pw-test", data=out, out_dir=os.path.join(tmp, "site_enc"), log=lambda *a: None,
                  salt_path=os.path.join(tmp, "salt.json"))
    info = json.load(open(os.path.join(enc, "data", "keyinfo.json")))
    check("site: encrypted with the password (salt, check, AES-GCM)", not info["plain"] and info["salt"] and info["check"])
    PN.contexts_at = orig
    if demo_dir:
        if os.path.exists(demo_dir):
            shutil.rmtree(demo_dir)
        shutil.copytree(site_dir, demo_dir)
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    fails = []

    def check(name, cond, detail=""):
        print(("  ok   " if cond else "  FAIL ") + name + (f"  ({detail})" if detail else ""))
        if not cond:
            fails.append(name)
    demo = sys.argv[sys.argv.index("--demo") + 1] if "--demo" in sys.argv else None
    run(check, demo)
    print("\nTRIAGE SMOKE " + ("PASSED" if not fails else f"FAILED: {fails}"))
    sys.exit(1 if fails else 0)
