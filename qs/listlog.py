"""Forward record: an append-only log of every published list (validation/PROTOCOL.md section 7).

After each Screen and Daily run, `python screener.py history-snapshot --kind screen|daily` writes one small file
(history_out/<date>_<kind>.json.gz) and scripts/append_history.sh commits it to the branch 'history', which is
never force-pushed. Each entry: date, run kind, code SHA, config hash, pre-registration check, and per screen the
CIK / ticker / price of every PASS (starred or not) and NEAR company.
"""
import hashlib
import json
import os
import subprocess
from datetime import date

from .config import ROOT

OUT_DIR = os.path.join(ROOT, "history_out")
LISTS = ("PASS", "NEAR")


def code_sha():
    sha = os.environ.get("GITHUB_SHA")
    if sha:
        return sha
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True,
                              timeout=10).stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


def config_hash(cfg):
    from .freeze import rule_config
    return hashlib.sha256(json.dumps(rule_config(cfg), sort_keys=True, default=str).encode()).hexdigest()


def snapshot(state, results, cfg, kind, today=None):
    from .freeze import compare
    today = today or date.today()
    ctxs = state.get("ctxs") or {}
    screens = {}
    for sid, res in results.items():
        rows = {"pass": [], "star": [], "near": []}
        for c, r in res.items():
            ctx = ctxs.get(str(c)) or {}
            row = [int(c), ctx.get("ticker"), ctx.get("price"), ctx.get("price_date")]
            if r["class"] == "PASS":
                rows["star" if r.get("star") else "pass"].append(row)
            elif r["class"] == "NEAR":
                rows["near"].append(row)
        for v in rows.values():
            v.sort(key=lambda x: x[0])
        rows["universe"] = len(res)
        screens[sid] = rows
    try:
        reg = compare()
    except Exception as e:  # noqa: BLE001 - the log must still be written
        reg = f"check failed: {type(e).__name__}"
    return {"date": today.isoformat(), "kind": kind, "screened_on": state.get("screened_on"),
            "screener_version": state.get("screener_version"), "code_sha": code_sha(),
            "config_sha256": config_hash(cfg), "preregistration": reg, "screens": screens}


def write(snap, out_dir=OUT_DIR):
    import gzip
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{snap['date']}_{snap['kind']}.json.gz")
    with gzip.open(path, "wt", encoding="utf-8") as f:
        json.dump(snap, f, sort_keys=True)
    return path


def load_all(folder):
    """Every snapshot under folder (the checked-out 'history' branch), oldest first."""
    import gzip
    out = []
    for root, _dirs, files in os.walk(folder):
        for fn in files:
            if fn.endswith(".json.gz"):
                try:
                    with gzip.open(os.path.join(root, fn), "rt", encoding="utf-8") as f:
                        out.append(json.load(f))
                except (OSError, ValueError):
                    continue
    out.sort(key=lambda s: (s.get("date") or "", s.get("kind") or ""))
    return out
