"""Live record: once a month has ended, its calls are appended to ledger.csv on branch 'macro-record' (never edited
or force-pushed). Only months from the launch month on are recorded, so every row was written in real time."""
import csv
import gzip
import json
import os
import time

from . import registry as R

LAUNCH = "2026-10"
COLS = ["month", "recorded_at", "version", "stage", "growth", "inflation", "liquidity", "credit", "froth", "internals",
        "horizon", "etf", "action", "p_risk", "p_opp", "base_risk", "base_opp"]


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
    for i, m in enumerate(months):
        if m < LAUNCH or m >= cur or m in done:      # only finished months from launch on, each once
            continue
        for h in map(str, R.SETTINGS["horizons"]):
            hz = d["horizons"][h]
            for it in d["industries"]:
                e = it["etf"]
                a = hz["actions"][e][i]
                od = (hz.get("recent", {}).get(m) or {}).get(e) or [None] * 4
                new.append({"month": m, "recorded_at": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
                            "version": d["version"], "stage": d["stage"][i] or "",
                            **{k: d["pillars"][k][i] for k, _, _ in R.PILLARS},
                            "horizon": h, "etf": e, "action": a or "",
                            **dict(zip(["p_risk", "p_opp", "base_risk", "base_opp"], od))})
    if new:
        exists = os.path.exists(path)
        with open(path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
            if not exists:
                w.writeheader()
            w.writerows(new)
    log(f"record: {len(new)} new rows ({len({r['month'] for r in new})} months); ledger {len(rows) + len(new)} rows")
    return len(new)
