"""python -m macro.run [all|fetch|build|site|record]   (all = fetch, build, site, record)"""
import os
import sys
import time


def main(step="all"):
    t0 = time.time()
    steps = ["fetch", "build", "site", "record"] if step == "all" else [step]
    for s in steps:
        print(f"== {s}", flush=True)
        if s == "fetch":
            from . import fetch
            fetch.run()
        elif s == "build":
            from . import engine
            engine.run()
        elif s == "site":
            from . import site
            site.build(os.environ.get("MACRO_PASSWORD") or os.environ.get("PORTAL_PASSWORD", ""), allow_plain=bool(os.environ.get("MACRO_PLAIN")))
        elif s == "record":
            from . import record
            record.run()
        else:
            raise SystemExit(f"unknown step {s}")
    print(f"done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "all")
