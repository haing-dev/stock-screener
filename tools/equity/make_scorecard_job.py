#!/usr/bin/env python3
"""Writes the frozen investor table into tools/equity/wrds/eq_scorecard.py and the job files
tools/wrdsq/jobs/eq_sc_pull_v1.json (pulls) and eq_scorecard_v1.json (build + report) (registration STAGE0_REGISTRATION.md sections 6-8, step E0.4 phase B).

    python3 tools/equity/make_scorecard_job.py [--frozen CSV] [--inventory CSV] [--words CSV]
                                                [--module PY] [--job JSON] [--name eq_scorecard_v1]

--frozen    docs/research/equity/inventory/frozen_investors.csv (phase A2). Columns: id, name, record_kind
            (13f | fund | none), mgrnos (space-separated tfn mgrno), fundnos (space-separated crsp_fundno of all
            share classes), start_ym, end_ym (YYYY-MM, months the investor ran the book; blank = whole period),
            grade (A B C F N), primary_style, region, explicit_max, explicit_mean, own_docs, ran_money
            (yes | no | unclear), role (E0.1 role: investor | allocator | ...), known_mgrnos, known_fundnos
            (every filer and fund matched to the investor, whatever its record kind; left out of the best-scored
            lists); optional shares_record_with (an investor id: same record as that investor, no place of its
            own by record or control). Other columns are ignored.
--inventory docs/research/equity/inventory/inventory.csv (E0.1): doc, technique, technique_depth and words (word
            count of the document) for the foundation list; --words CSV (doc, words) supplies words if the
            inventory has no such column. Without word counts the generator stops.
Only the block between the FROZEN INPUT markers of the module is replaced, so the module's code hash (registered
in tools/equity/seal_exempt.json) does not change. Prints the code hash and the input hash.
"""
import argparse
import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools", "equity"))
import seal_check  # noqa: E402

FROZEN = os.path.join(ROOT, "docs", "research", "equity", "inventory", "frozen_investors.csv")
INVENTORY = os.path.join(ROOT, "docs", "research", "equity", "inventory", "inventory.csv")
MODULE = os.path.join(ROOT, "tools", "equity", "wrds", "eq_scorecard.py")
JOB = os.path.join(ROOT, "tools", "wrdsq", "jobs", "eq_scorecard_v1.json")
PULL_JOB = os.path.join(ROOT, "tools", "wrdsq", "jobs", "eq_sc_pull_v1.json")
COLS = ["id", "name", "record_kind", "mgrnos", "fundnos", "start_ym", "end_ym", "grade", "primary_style", "region",
        "explicit_max", "explicit_mean", "own_docs", "ran_money", "role", "known_mgrnos", "known_fundnos"]
REPORT_PARTS = 4


def die(msg):
    sys.exit("make_scorecard_job: " + msg)


def ym(x, where):
    x = (x or "").strip()
    if not x:
        return None
    m = re.match(r"^(\d{4})-?(\d{2})$", x)
    if not m or not 1 <= int(m.group(2)) <= 12:
        die("%s: month %r is not YYYY-MM" % (where, x))
    return int(m.group(1)) * 100 + int(m.group(2))


def num(x, where, kind=float):
    x = (x or "").strip()
    if x == "":
        return None
    try:
        return kind(x)
    except ValueError:
        die("%s: %r is not a number" % (where, x))


def ids(x, where):
    out = []
    for t in (x or "").split():
        if not re.match(r"^\d+(\.0+)?$", t):
            die("%s: id %r is not a whole number" % (where, t))
        out.append(int(float(t)))
    return sorted(set(out))


def read_frozen(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    if not rows:
        die("%s is empty" % path)
    miss = [c for c in COLS if c not in rows[0]]
    if miss:
        die("%s lacks columns %s" % (path, ", ".join(miss)))
    inv, seen = [], set()
    for r in rows:
        w = "frozen row %s" % r.get("id")
        if not r["id"] or r["id"] in seen:
            die("%s: missing or repeated id" % w)
        seen.add(r["id"])
        kind, grade = r["record_kind"].strip(), r["grade"].strip()
        if kind not in ("13f", "fund", "none"):
            die("%s: record_kind %r" % (w, kind))
        if grade not in ("A", "B", "C", "F", "N"):
            die("%s: grade %r" % (w, grade))
        p = {"id": r["id"].strip(), "name": r["name"].strip(), "record_kind": kind,
             "mgrnos": ids(r["mgrnos"], w), "fundnos": ids(r["fundnos"], w),
             "start_ym": ym(r["start_ym"], w), "end_ym": ym(r["end_ym"], w), "grade": grade,
             "primary_style": (r["primary_style"] or "none").strip() or "none", "region": r["region"].strip(),
             "explicit_max": num(r["explicit_max"], w), "explicit_mean": num(r["explicit_mean"], w),
             "own_docs": num(r["own_docs"], w, int) or 0, "ran_money": r["ran_money"].strip().lower(),
             "role": (r["role"] or "").strip().lower(),
             "known_mgrnos": ids(r["known_mgrnos"], w), "known_fundnos": ids(r["known_fundnos"], w),
             "shares_with": (r.get("shares_record_with") or "").strip() or None}
        if p["role"] not in ("investor", "allocator", "executive", "expert", "host"):
            die("%s: role %r" % (w, p["role"]))
        if kind == "13f" and not p["mgrnos"]:
            die("%s: record_kind 13f without mgrnos" % w)
        if kind == "fund" and not p["fundnos"]:
            die("%s: record_kind fund without fundnos" % w)
        if p["start_ym"] and p["end_ym"] and p["start_ym"] > p["end_ym"]:
            die("%s: start_ym after end_ym" % w)
        if p["ran_money"] not in ("yes", "no", "unclear"):
            die("%s: ran_money %r" % (w, p["ran_money"]))
        inv.append(p)
    for p in inv:
        t = p["shares_with"]
        if t and (t not in seen or t == p["id"]):
            die("frozen row %s: shares_record_with %r is not another investor id" % (p["id"], t))
        if t and [q for q in inv if q["id"] == t][0]["shares_with"]:
            die("frozen row %s: shares_record_with points to an investor that itself shares a record" % p["id"])
    return sorted(inv, key=lambda p: p["id"])


def read_docs(path, words_path):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    words = {}
    if words_path:
        words = {int(r["doc"]): int(float(r["words"])) for r in csv.DictReader(open(words_path, encoding="utf-8"))}
    docs = []
    for r in rows:
        d = int(r["doc"])
        wv = r.get("words")
        wv = int(float(wv)) if wv not in (None, "") else words.get(d)
        if wv is None:
            die("document %d has no word count: add a column 'words' to the inventory or pass --words" % d)
        tech = [t for t in (r.get("technique") or "").split(";") if t.strip()]
        docs.append([d, int(float(r.get("technique_depth") or 0)), len(tech), wv])
    return sorted(docs)


def write_module(path, inv, docs):
    text = open(path, encoding="utf-8").read()
    code, _ = seal_check.split_input(text)
    lines = code.splitlines(True)
    i = next(k for k, x in enumerate(lines) if x.startswith(seal_check.INPUT_BEGIN))
    block = ('INV = json.loads(r"""%s""")\nDOCS = json.loads(r"""%s""")\n'
             % (json.dumps(inv, ensure_ascii=True, sort_keys=True), json.dumps(docs, ensure_ascii=True)))
    errs = seal_check.check_input_block(block)
    if errs:
        die("; ".join(errs))
    new = "".join(lines[:i + 1]) + block + "".join(lines[i + 1:])
    assert seal_check.code_hash(new) == seal_check.code_hash(text)
    open(path, "w", encoding="utf-8").write(new)
    return seal_check.code_hash(new), seal_check.input_hash(new)


def _py(code):
    return {"do": "python", "code": "import eq_scorecard\n" + code}


def pull_job(name):
    """Pulls only (budgets sum to 2.25 h, under the runner's 3-hour watchdog); re-run as v1b, v1c ... until
    pull_status prints ALL PULLS COMPLETE."""
    steps = [_py("eq_scorecard.pull_base(sql, save, out, DATA, budget=900)"),
             _py("eq_scorecard.pull_crsp(sql, save, out, DATA, budget=900)"),
             _py("eq_scorecard.pull_agg(sql, save, out, DATA, budget=3000)"),
             _py("eq_scorecard.pull_hold(sql, load, save, out, DATA, budget=2400)"),
             _py("eq_scorecard.pull_funds(sql, load, save, out, DATA, budget=900)"),
             _py("eq_scorecard.pull_status(load, out, DATA)"),
             {"do": "datasets"}]
    return {"name": name, "steps": steps}


def cleanup_job(name="eq_sc_cleanup_v1"):
    """Run once the result is accepted: deletes the stored eq_sc_ data sets (eq_sc_report kept)."""
    return {"name": name, "steps": [_py("eq_scorecard.cleanup(out, DATA)"), {"do": "datasets"}]}


def job(name):
    """Build and report only."""
    steps = [_py("eq_scorecard.build(load, save, out, DATA)")]
    steps += [_py("eq_scorecard.report(load, out, %d, %d)" % (k, REPORT_PARTS)) for k in range(1, REPORT_PARTS + 1)]
    return {"name": name, "steps": steps}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen", default=FROZEN)
    ap.add_argument("--inventory", default=INVENTORY)
    ap.add_argument("--words", default=None)
    ap.add_argument("--module", default=MODULE)
    ap.add_argument("--job", default=JOB)
    ap.add_argument("--name", default="eq_scorecard_v1")
    ap.add_argument("--pull-job", default=PULL_JOB)
    ap.add_argument("--pull-name", default="eq_sc_pull_v1")
    a = ap.parse_args()
    if not re.match(r"^eq_scorecard_v\d+[a-z]?$", a.name) or not re.match(r"^eq_sc_pull_v\d+[a-z]?$", a.pull_name):
        die("job names must look like eq_scorecard_v1 and eq_sc_pull_v1")
    if not os.path.exists(a.frozen):
        die("%s does not exist (phase A2 writes it)" % a.frozen)
    inv = read_frozen(a.frozen)
    docs = read_docs(a.inventory, a.words)
    ch, ih = write_module(a.module, inv, docs)
    os.makedirs(os.path.dirname(os.path.abspath(a.job)), exist_ok=True)
    json.dump(job(a.name), open(a.job, "w"), indent=1)
    json.dump(pull_job(a.pull_name), open(a.pull_job, "w"), indent=1)
    json.dump(cleanup_job(), open(os.path.join(os.path.dirname(os.path.abspath(a.job)), "eq_sc_cleanup_v1.json"), "w"),
              indent=1)
    kinds = [p["record_kind"] for p in inv]
    print("wrote %s (%d investors: 13f %d, fund %d, none %d; %d documents)" % (a.module, len(inv), kinds.count("13f"),
                                                                             kinds.count("fund"), kinds.count("none"),
                                                                             len(docs)))
    print("wrote %s and %s" % (a.pull_job, a.job))
    print("code sha256 %s" % ch)
    print("input sha256 %s" % ih)


if __name__ == "__main__":
    main()
