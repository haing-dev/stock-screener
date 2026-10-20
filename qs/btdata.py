"""Data preparation for the backtest: SEC bulk files -> per-company point-in-time subsets.

  cache/bt/facts/<cik>.json.gz    - extract.facts_subset with 10-Q / cover-page facts kept since 2009
  cache/bt/filings/<cik>.json.gz  - pit.filings_subset: every periodic and event filing over the company's history

Only companies the price universe maps to (any month of the grid, delisted ones included) are written.
"""
import io
import json
import os
import time
import zipfile

from .config import CACHE_DIR
from .extract import facts_subset
from .pit import filings_subset
from .sec import cache_read, cache_write
from .secsync import BULK_FACTS_URL, BULK_SUBS_URL, _fetch

BT_DIR = os.path.join(CACHE_DIR, "bt")
FACTS_DIR = os.path.join(BT_DIR, "facts")
FILINGS_DIR = os.path.join(BT_DIR, "filings")
QUARTERLY_SINCE = "2009-01-01"


def _download(client, url, log):
    os.makedirs(os.path.join(BT_DIR, "bulk"), exist_ok=True)
    path = os.path.join(BT_DIR, "bulk", url.rsplit("/", 1)[-1])
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 3 * 86400:
        return path
    t0 = time.time()
    got = _fetch(client, url, timeout=3600, stream_to=path)
    if not got:
        raise RuntimeError(f"bulk file unavailable: {url}")
    log(f"  {os.path.basename(path)}: {os.path.getsize(path) / 1e9:.1f} GB in {time.time() - t0:.0f} s")
    return path


def _cik_of(base):
    try:
        return int(base[3:13])
    except ValueError:
        return None


def prepare(client, ciks, log=print, refresh=False):
    """Write facts and filings subsets for every wanted CIK. Returns (n_facts, n_filings)."""
    want = {int(c) for c in ciks}
    os.makedirs(FACTS_DIR, exist_ok=True)
    os.makedirs(FILINGS_DIR, exist_ok=True)
    todo_f = {c for c in want if refresh or not os.path.exists(os.path.join(FACTS_DIR, f"{c}.json.gz"))}
    todo_s = {c for c in want if refresh or not os.path.exists(os.path.join(FILINGS_DIR, f"{c}.json.gz"))}
    n_f = n_s = 0
    if todo_f:
        path = _download(client, BULK_FACTS_URL, log)
        with zipfile.ZipFile(path) as z:
            for name in z.namelist():
                base = os.path.basename(name)
                if not (base.startswith("CIK") and base.endswith(".json")):
                    continue
                c = _cik_of(base)
                if c not in todo_f:
                    continue
                with z.open(name) as f:
                    raw = json.load(io.TextIOWrapper(f, encoding="utf-8"))
                cache_write(os.path.join(FACTS_DIR, f"{c}.json.gz"), facts_subset(raw, quarterly_since=QUARTERLY_SINCE))
                n_f += 1
        log(f"  facts written for {n_f} of {len(todo_f)} companies")
    if todo_s:
        path = _download(client, BULK_SUBS_URL, log)
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            pages = {}
            mains = {}
            for name in names:
                base = os.path.basename(name)
                if not (base.startswith("CIK") and base.endswith(".json")):
                    continue
                c = _cik_of(base)
                if c not in todo_s:
                    continue
                if "-submissions-" in base:
                    pages.setdefault(c, []).append(name)
                else:
                    mains[c] = name
            for c, name in mains.items():
                with z.open(name) as f:
                    main = json.load(io.TextIOWrapper(f, encoding="utf-8"))
                pg = []
                for pn in sorted(pages.get(c, [])):
                    with z.open(pn) as f:
                        pg.append(json.load(io.TextIOWrapper(f, encoding="utf-8")))
                cache_write(os.path.join(FILINGS_DIR, f"{c}.json.gz"), filings_subset(main, pg))
                n_s += 1
        log(f"  filing histories written for {n_s} of {len(todo_s)} companies")
    return n_f, n_s


def load_facts(cik):
    return cache_read(os.path.join(FACTS_DIR, f"{int(cik)}.json.gz"))


def load_filings(cik):
    return cache_read(os.path.join(FILINGS_DIR, f"{int(cik)}.json.gz"))
