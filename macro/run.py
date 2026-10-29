"""python -m macro.run [all|fetch|build|site|record]   (all = fetch, build, site, record)"""
import os
import sys
import time


def main(step="all"):
    t0 = time.time()
    steps = ["fetch", "build", "site", "record"] if step == "all" else step.split(",")
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
            site.build("", allow_plain=True)          # public page, no password (user, 2026-10-23)
        elif s == "record":
            from . import record
            record.run()
        elif s == "derisk_weekly":                      # research only: de-risking checked weekly vs monthly
            from . import research_derisk
            research_derisk.weekly()
        elif s == "more":                               # research only: wide multi-asset download
            from . import research_data
            research_data.run()
        elif s == "research_fetch":                     # research only: wide instrument universe
            from . import fetch_research
            fetch_research.run()
        elif s == "stocks":                             # research only: sector calls via sensitive stocks
            from . import research_stocks
            research_stocks.run()
        else:
            raise SystemExit(f"unknown step {s}")
    print(f"done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "all")
