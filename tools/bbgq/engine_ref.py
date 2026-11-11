"""engine_ref: the reference fingerprint of the cloud run of the book engine on free data, DESIGN PERIOD ONLY.

python3 tools/bbgq/engine_ref.py            -> tools/bbgq/engine_ref.json (committed) + a short report

Runs gm/ unchanged (panel -> signals -> daily -> BASE and CANDIDATE books, as gm.protocol does) on the repo cache
(cache/macro/raw/research, cache/macro/raw), records which input files the engine opened (audit hook), and writes:
  stats            per config and era (1975-2010, 1990-2010): net and gross Sharpe, mean, volatility, worst drawdown
  book_year_sum    per config, per calendar year <= 2010: sum of monthly net / gross book returns (rounded 1e-10)
  pos_abs_sum      per config, per market: sum over months <= 2010-12 of |position| (rounded 1e-8)
  vol_sum, fam_abs_sum, signal_abs_sum   the same for the volatility estimate, family positions and raw signals
  market_months    per market: months with a return up to 2010-12
  code / configs / libraries / inputs   gm commit and file hashes, config hashes, library versions, input files + hashes
Nothing dated after 2010-12 is printed or stored (gm_engine.fingerprint checks the keys). gm's own console output is
discarded unread (panel.build prints a count over the full sample).
"""
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path[:0] = [REPO, os.path.join(HERE, "lib")]

import gm_engine as GE  # noqa: E402

OUT = os.path.join(HERE, "engine_ref.json")


def main():
    opened = set()

    def hook(ev, args):
        if ev == "open" and args and isinstance(args[0], (str, os.PathLike)):
            opened.add(os.path.abspath(os.fspath(args[0])))

    M = GE.setup()                                   # repo cache, old Bloomberg reader off
    P = M["P"]
    roots = {"research": os.path.abspath(P.RD), "raw": os.path.abspath(P.RAW),
             "gm_data": os.path.abspath(P.MANUAL)}
    sys.addaudithook(hook)
    t0 = time.time()
    res = GE.run(M=M)
    secs = time.time() - t0
    fp = GE.fingerprint(res, M)

    files = {}
    for p in sorted(opened):
        for tag, root in roots.items():
            if p.startswith(root + os.sep) and os.path.isfile(p) and "__pycache__" not in p:
                files["%s/%s" % (tag, os.path.relpath(p, root).replace(os.sep, "/"))] = p
                break                                # research/ lies inside raw/: the first (most specific) wins
    inputs = {rel: {"sha256": hashlib.sha256(open(p, "rb").read()).hexdigest(), "bytes": os.path.getsize(p)}
              for rel, p in sorted(files.items())}
    digest, n = GE.inputs_digest({k: v for k, v in files.items() if not k.startswith("gm_data/")})
    try:
        commit = subprocess.run(["git", "-C", REPO, "log", "-1", "--format=%H", "--", "gm"], capture_output=True,
                                text=True, timeout=30).stdout.strip()
        dirty = subprocess.run(["git", "-C", REPO, "status", "--porcelain", "--", "gm"], capture_output=True,
                               text=True, timeout=30).stdout.strip()
    except Exception:  # noqa: BLE001
        commit, dirty = "unknown", ""
    ref = {"what": "book engine (gm/) on free data: design-period fingerprint (months <= 2010-12 only)",
           "made": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"),
           "engine_helper": GE.VERSION,
           "code": {"gm_commit": commit, "gm_dirty": bool(dirty), "gm_files_sha256": GE.gm_code_hashes()},
           "configs": GE.config_hashes(M), "libraries": GE.lib_versions(),
           "run_seconds": round(secs),
           "inputs": {"digest": digest, "files_in_digest": n, "files": inputs,
                      "note": "research/ and raw/ ship in work\\free\\gm_free_inputs.zip; gm_data/ travels inside "
                              "lib\\gm\\data"},
           "tolerances": GE.TOL, **fp}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(ref, f, indent=1, sort_keys=True)
    print("engine_ref.json written: %d input files (%d MB), run %.0fs, gm commit %s%s" % (
        len(inputs), sum(v["bytes"] for v in inputs.values()) // 10 ** 6, secs, commit[:10],
        " (gm/ has uncommitted changes)" if dirty else ""))
    print("libraries: " + ", ".join("%s %s" % kv for kv in ref["libraries"].items()))
    print("config hashes: " + ", ".join("%s %s" % kv for kv in ref["configs"].items()))
    print("design-period statistics (net of costs; gross Sharpe in brackets)")
    print("%-10s %-10s %5s %7s %8s %7s %8s %8s" % ("config", "era", "n", "SR", "mean%", "vol%", "maxDD%", "(grossSR)"))
    for name, eras in fp["stats"].items():
        for era, d in eras.items():
            x, g = d["net"], d["gross"]
            print("%-10s %-10s %5d %7.3f %8.2f %7.2f %8.1f %8.3f" % (name, era, x["n"], x["sr"], x["mean"] * 100,
                                                                     x["vol"] * 100, x["maxdd"] * 100, g["sr"]))


if __name__ == "__main__":
    main()
