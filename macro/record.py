"""Live record: once a month has ended, its calls are appended to ledger.csv on branch 'macro-record' (never edited
or force-pushed). Only months from the launch month on are recorded, so every row was written in real time."""
import csv
import gzip
import json
import os
import time

from . import registry as R

LAUNCH = "2026-10"
COLS = ["month", "recorded_at", "version", "equity", "bond", "cash", "commodities", "warning_share", "fed_gate",
        "growth_cut", "defensive", "commod_on", "etf", "momentum_12_1", "action"]


def ledger_path():
    d = os.environ.get("MACRO_RECORD_DIR") or os.path.join("cache", "macro", "record")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, "ledger.csv")


def read(path=None):
    path = path or ledger_path()
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def run(log=print):
    p = os.path.join("cache", "macro", "out", "compass.json.gz")
    if not os.path.exists(p):
        log("record: nothing built")
        return 0
    d = json.load(gzip.open(p, "rt"))
    months = d["months"]
    cur = time.strftime("%Y-%m", time.gmtime())
    path = ledger_path()
    rows = read(path)
    done = {r["month"] for r in rows}
    new = []
    X = d.get("derisk", {})
    al = X.get("alloc", {})
    tilt = X.get("tilt") or {}
    for i, m in enumerate(months):
        if m < LAUNCH or m >= cur or m in done:      # only finished months from launch on, each once
            continue
        base = {"month": m, "recorded_at": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "version": d["version"],
                **{k: (al.get(k) or [""] * len(months))[i] for k in ("equity", "bond", "cash", "commodities")},
                "warning_share": X.get("share", [""] * len(months))[i],
                "fed_gate": int(bool((X.get("fed_gate") or [False] * len(months))[i])),
                "growth_cut": int(bool((X.get("growth_cut") or [False] * len(months))[i])),
                "defensive": (X.get("defensive") or [""] * len(months))[i],
                "commod_on": int(bool((X.get("commod_on") or [False] * len(months))[i]))}
        for it in d["industries"]:
            e = it["etf"]
            new.append({**base, "etf": e, "momentum_12_1": (tilt.get("mom_now") or {}).get(e, "") if i == len(months) - 1 else "",
                        "action": (tilt.get("actions") or {}).get(e, [""] * len(months))[i]})
    if new:
        exists = os.path.exists(path)
        with open(path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
            if not exists:
                w.writeheader()
            w.writerows(new)
    log(f"record: {len(new)} new rows ({len({r['month'] for r in new})} months); ledger {len(rows) + len(new)} rows")
    return len(new)
