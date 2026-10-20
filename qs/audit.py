"""Independent checks (validation/PROTOCOL.md section 8) that a third party can redo without the screener:

  reconciliation - 300 random firm-years (stratified by screen) from the latest formation: each figure the screener
                   took from XBRL against SEC's Financial Statement Data Sets (num.txt) for the same filing, tag and
                   period, plus a link to the filing and blank columns for a human recheck.
  gates          - the same companies' rule outcomes with their inputs, for the human recheck (>= 98% agreement).
  stars          - 50 starred passes, with the rules that couldn't be checked and the filing to check them in;
                   the sheet doesn't say what the screener concluded.
"""
import csv
import gzip
import hashlib
import io
import os
import random
import zipfile
from datetime import date

from .backtest import FORM_DIR, CompanyStore
from .backtest_support import OUT, read_json
from .btdata import load_facts
from .extract import CompanyData
from .pit import facts_as_of
from .screens import BY_ID, SCREENS
from .sec import filing_index_url

FSDS_URL = "https://www.sec.gov/files/dera/data/financial-statement-data-sets/{y}q{q}.zip"
AUDIT_CONCEPTS = ("revenue", "operating_income", "net_income", "ocf", "capex_ppe", "assets", "equity",
                  "lt_debt_noncurrent", "diluted_shares")
DURATION = {"revenue", "operating_income", "net_income", "ocf", "capex_ppe", "diluted_shares"}


def latest_formation():
    files = sorted(f for f in os.listdir(FORM_DIR) if f.endswith(".json.gz")) if os.path.isdir(FORM_DIR) else []
    return read_json(os.path.join(FORM_DIR, files[-1])) if files else None


def sample(form, n=300, seed="prereg"):
    """[(screen, cik)] - about n / 14 PASS and NEAR companies per screen (others from its universe if short)."""
    rnd = random.Random(int(hashlib.sha256(seed.encode()).hexdigest()[:8], 16))
    per = max(1, n // len(SCREENS))
    out, seen = [], set()
    for s in SCREENS:
        res = form["screens"].get(s.sid) or {}
        good = sorted(c for c, r in res.items() if r[0] in ("PASS", "NEAR") and c not in seen)
        rest = sorted(c for c in res if c not in seen and c not in good)
        rnd.shuffle(good)
        rnd.shuffle(rest)
        pick = (good + rest)[:per]
        for c in pick:
            seen.add(c)
            out.append((s.sid, c))
    return out[:n]


def our_figures(cik, d):
    """[(concept, fy, value, tag, taxonomy, accession, period_end, filed)] for the latest fiscal year known at d."""
    fs = load_facts(cik)
    if not fs:
        return []
    cd = CompanyData(facts_as_of(fs, d))
    if not cd.label_end:
        return []
    y = max(cd.label_end)
    rows = []
    for k in AUDIT_CONCEPTS:
        f = cd.fact(k, y)
        if f is None or getattr(f, "tax", "") == "derived":
            continue
        rows.append((k, y, f.val, f.tag, f.tax, f.accn, f.end, f.filed))
    return rows


def fsds_quarter(filed):
    d = date.fromisoformat(filed[:10])
    return d.year, (d.month - 1) // 3 + 1


def fsds_values(client, wanted, log=print):
    """wanted: {(adsh, tag, ddate, qtrs)} -> {key: value} from SEC's quarterly data sets (num.txt)."""
    from .secsync import _fetch
    by_q = {}
    for adsh, tag, ddate, qtrs, filed in wanted:
        by_q.setdefault(fsds_quarter(filed), set()).add((adsh, tag, ddate, qtrs))
    out = {}
    for (y, q), keys in sorted(by_q.items()):
        raw = _fetch(client, FSDS_URL.format(y=y, q=q), timeout=1200)
        if not raw:
            log(f"  Financial Statement Data Set {y}q{q} unavailable")
            continue
        adshs = {k[0] for k in keys}
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            with z.open("num.txt") as f:
                rd = csv.reader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
                head = next(rd)
                ix = {h: i for i, h in enumerate(head)}
                for r in rd:
                    if r[ix["adsh"]] not in adshs or r[ix["coreg"]]:
                        continue
                    if "segments" in ix and r[ix["segments"]]:
                        continue
                    key = (r[ix["adsh"]], r[ix["tag"]], r[ix["ddate"]], r[ix["qtrs"]])
                    if key in keys:
                        try:
                            out[key] = float(r[ix["value"]])
                        except ValueError:
                            pass
        log(f"  {y}q{q}: {sum(1 for k in keys if k in out)} of {len(keys)} values found")
    return out


def reconciliation(client, form, n=300, log=print):
    d = form["d"]
    rows = []
    for sid, c in sample(form, n):
        for k, y, val, tag, tax, accn, end, filed in our_figures(c, d):
            qtrs = "4" if k in DURATION else "0"
            rows.append({"screen": sid, "cik": c, "ticker": form["companies"][c].get("tk"), "fy": y, "concept": k,
                         "our_value": val, "taxonomy": tax, "tag": tag, "accession": accn, "period_end": end,
                         "filed": filed, "qtrs": qtrs,
                         "filing_url": filing_index_url(int(c), accn) if accn else ""})
    wanted = {(r["accession"], r["tag"], (r["period_end"] or "").replace("-", ""), r["qtrs"], r["filed"] or "")
              for r in rows if r["accession"] and r["filed"]}
    fs = fsds_values(client, wanted, log=log)
    ok = n_cmp = 0
    for r in rows:
        v = fs.get((r["accession"], r["tag"], (r["period_end"] or "").replace("-", ""), r["qtrs"]))
        r["fsds_value"] = v
        if v is not None and r["our_value"] is not None:
            diff = abs(r["our_value"] - v) / max(abs(v), 1e-9)
            r["diff_pct"] = round(100 * diff, 3)
            r["within_2pct"] = diff <= 0.02
            ok += r["within_2pct"]
            n_cmp += 1
        else:
            r["diff_pct"], r["within_2pct"] = None, None
        r["reviewer_value_in_filing"], r["reviewer_agrees"] = "", ""
    return rows, {"values": len(rows), "compared": n_cmp, "within_2pct": ok,
                  "share_within_2pct": (ok / n_cmp) if n_cmp else None}


def gate_sheet(form, picks):
    """The screen's rule outcomes for the sampled companies, re-evaluated from the stored formation (statuses only:
    a reviewer rechecks the inputs in the filing)."""
    out = []
    for sid, c in picks:
        r = (form["screens"].get(sid) or {}).get(c)
        if not r:
            continue
        out.append({"screen": sid, "cik": c, "ticker": form["companies"][c].get("tk"), "class": r[0],
                    "star": r[1], "rules_failed": r[2], "rules_met": r[3], "rules_checked": r[4],
                    "reviewer_agrees": ""})
    return out


def star_sheet(form, n=50, seed="stars"):
    rnd = random.Random(int(hashlib.sha256(seed.encode()).hexdigest()[:8], 16))
    stars = sorted((sid, c) for sid, res in form["screens"].items() for c, r in res.items() if r[0] == "PASS" and r[1])
    rnd.shuffle(stars)
    store = CompanyStore()
    out = []
    for i, (sid, c) in enumerate(stars[:n]):
        vm, info = store.get(int(c), form["d"])
        la = (info or {}).get("latest_annual") or {}
        out.append({"id": i + 1, "screen": BY_ID[sid].title, "cik": c,
                    "annual_report": filing_index_url(int(c), la["accn"]) if la.get("accn") else "",
                    "rules_to_check": "see the screen's rule list (validation/out/rules.csv)",
                    "reviewer_inputs_found": "", "reviewer_rule_passes": ""})
    return out


def write_csv(path, rows):
    if not rows:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    keys = list(rows[0].keys())
    with gzip.open(path, "wt", encoding="utf-8", newline="") if path.endswith(".gz") else \
            open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def rules_csv(cfg, path):
    rows = []
    for s in SCREENS:
        for g in s.gates:
            try:
                text = g.rule_text(cfg, s.sid)
            except Exception:  # noqa: BLE001
                text = ""
            rows.append({"screen": s.title, "rule": g.gid, "name": g.name, "rule_text": text})
    write_csv(path, rows)


def run(client, cfg, log=print):
    form = latest_formation()
    if not form:
        log("No formation yet - run the backtest step first.")
        return None
    rows, summ = reconciliation(client, form, log=log)
    write_csv(os.path.join(OUT, "audit_reconciliation.csv"), rows)
    write_csv(os.path.join(OUT, "audit_gates.csv"), gate_sheet(form, sample(form)))
    write_csv(os.path.join(OUT, "audit_stars.csv"), star_sheet(form))
    rules_csv(cfg, os.path.join(OUT, "rules.csv"))
    summ["formation"] = form["ym"]
    log(f"Reconciliation: {summ['within_2pct']} of {summ['compared']} values within 2% of SEC's data sets")
    return summ
