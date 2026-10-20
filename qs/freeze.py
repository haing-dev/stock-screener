"""Pre-registration fingerprints: prove later that the screens being evaluated are the ones frozen on a given date.

* rules fingerprint    - every screen's gates (id, name, metric, operator, threshold, rule text, flags) and the
                         rule-bearing parts of config.json, hashed as canonical JSON. Refactors that don't touch a
                         rule leave it unchanged.
* behavior fingerprint - the class every screen gives each real SEC sample in tests/real_samples (financial rules,
                         fixed date), hashed. Any change in how metrics or rules behave changes it.
* file hashes          - SHA-256 of the rule-bearing source files, for reference.

    python -m qs.freeze           # print the current fingerprints
    python -m qs.freeze --write   # write validation/freeze.json (only when deliberately re-registering)
    python -m qs.freeze --check   # exit 1 if the code no longer matches validation/freeze.json
"""
import glob
import gzip
import hashlib
import json
import os
import sys
from datetime import date

from .config import ROOT, load_config

FREEZE_PATH = os.path.join(ROOT, "validation", "freeze.json")
RULE_FILES = ("config.json", "qs/screens.py", "qs/metrics.py", "qs/extract.py", "qs/valuation.py", "qs/industry.py",
              "qs/rules.py", "qs/pipeline.py")
# config keys that never change what a rule decides (secrets placeholders, caching, download settings, display)
CONFIG_SKIP = {"user_agent", "twelvedata_api_key", "massive_api_key", "requests_per_second", "parallel_downloads",
               "cache_days_universe", "cache_days_submissions", "cache_days_facts", "cache_days_submissions_indexed",
               "cache_days_facts_indexed", "portal", "price_history", "price_also"}
BEHAVIOR_DATE = date(2026, 10, 1)


def _h(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, default=str).encode("utf-8")).hexdigest()


def rule_config(cfg):
    return {k: v for k, v in cfg.items() if not k.startswith("_") and k not in CONFIG_SKIP}


def rules_spec(cfg):
    from .screens import SCREENS
    out = []
    for s in SCREENS:
        gates = []
        for g in s.gates:
            try:
                thr = g.threshold(cfg, s.sid)
            except (KeyError, TypeError):
                thr = "?"
            try:
                text = g.rule_text(cfg, s.sid)
            except Exception:  # noqa: BLE001 - a desc that needs a ctx
                text = ""
            gates.append({"gid": g.gid, "name": g.name, "metric": g.metric, "op": g.op, "key": g.key, "threshold": thr,
                          "text": text, "custom": g.fn is not None, "needs_price": g.needs_price,
                          "valuation": g.valuation, "one_ok": g.one_ok, "near": g.near,
                          "defining": getattr(g, "defining", False), "hidden": g.hidden})
        out.append({"sid": s.sid, "title": s.title, "universe": getattr(s.universe, "__name__", str(s.universe)),
                    "strict": s.strict, "warnings": list(s.warnings), "avoid": getattr(s, "avoid", False),
                    "gates": gates})
    return out


def behavior(cfg):
    """{sample file: {screen: class}} for the real SEC samples, financial rules only."""
    from .extract import CompanyData
    from .pipeline import _CD, apply_industry_cycle, build_ctx, metrics_for
    from .screens import SCREENS
    out = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "tests", "real_samples", "*companyfacts*.json.gz"))):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            fs = json.load(f)
        cd = CompanyData(fs)
        name = os.path.basename(path)
        if cd.currency is None:
            out[name] = "no data"
            continue
        res, why = metrics_for(cd, "", {}, cfg, BEHAVIOR_DATE)
        if res is None:
            out[name] = why
            continue
        m, rows, compact = res
        u = {"cik": fs.get("cik") or 0, "ticker": name.split("_")[0].upper(), "name": fs.get("entityName"),
             "exchange": "NYSE", "all_tickers": [name.split("_")[0].upper()]}
        ctx = build_ctx(u, {"sic": ""}, m, compact, _CD(cd.flags, cd.candidates), cfg, {m.get("currency"): (1.0, "x")},
                        BEHAVIOR_DATE)
        apply_industry_cycle({0: ctx}, cfg)
        cls = {}
        for s in SCREENS:
            r = s.evaluate(ctx, cfg, priced=False)
            cls[s.sid] = [r["class"], bool(r.get("star")), sorted(r["failed"]), sorted(r["no_data"])]
        out[name] = cls
    return out


def file_hashes():
    out = {}
    for rel in RULE_FILES:
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            with open(p, "rb") as f:
                out[rel] = hashlib.sha256(f.read()).hexdigest()
    return out


def fingerprints(cfg=None):
    from . import __version__
    cfg = cfg or load_config()
    return {"screener_version": __version__, "rules_sha256": _h([rules_spec(cfg), rule_config(cfg)]),
            "behavior_sha256": _h(behavior(cfg)), "files_sha256": file_hashes()}


def load_freeze():
    try:
        with open(FREEZE_PATH, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def compare(cur=None, frozen=None):
    """'match' | 'rules changed' | 'behavior changed' | 'not registered'."""
    frozen = frozen if frozen is not None else load_freeze()
    if not frozen:
        return "not registered"
    cur = cur or fingerprints()
    if cur["rules_sha256"] != frozen["rules_sha256"]:
        return "rules changed"
    if cur["behavior_sha256"] != frozen["behavior_sha256"]:
        return "behavior changed"
    return "match"


def main(argv):
    cur = fingerprints()
    if "--write" in argv:
        cur["registered_on"] = date.today().isoformat()
        os.makedirs(os.path.dirname(FREEZE_PATH), exist_ok=True)
        with open(FREEZE_PATH, "w", encoding="utf-8") as f:
            json.dump(cur, f, indent=2, sort_keys=True)
            f.write("\n")
        print(f"written {FREEZE_PATH}")
    elif "--check" in argv:
        st = compare(cur)
        print(f"pre-registration check: {st}")
        return 0 if st == "match" else 1
    else:
        print(json.dumps({k: v for k, v in cur.items() if k != "files_sha256"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
