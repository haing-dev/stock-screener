"""Download only what changed at SEC.

* Daily filing index: SEC lists every filing of a day in one small file (daily-index/master.YYYYMMDD.idx). Reading
  the days since the last run tells which companies filed anything (-> refresh their profile) and which filed a
  10-K/10-Q/20-F/40-F (-> refresh their financial statements). Everyone else keeps their cached data, with a long
  safety-net age (config cache_days_*_indexed).
* Bulk files: when nearly everything must be refreshed (new data subset version, empty cache), SEC's nightly
  companyfacts.zip and submissions.zip replace ~11,000 single requests with two downloads.
"""
import io
import os
import time
import zipfile
from datetime import date, timedelta

from .config import CACHE_DIR
from .sec import cache_read, cache_write

SYNC_PATH = os.path.join(CACHE_DIR, "sec_sync.json.gz")
META_PATH = os.path.join(CACHE_DIR, "sec_meta.json.gz")
INDEX_URL = "https://www.sec.gov/Archives/edgar/daily-index/{y}/QTR{q}/master.{ymd}.idx"
BULK_FACTS_URL = "https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip"
BULK_SUBS_URL = "https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip"
PERIODIC = {"10-K", "10-Q", "20-F", "40-F", "10-KT", "10-QT", "10-K/A", "10-Q/A", "20-F/A", "40-F/A", "10-KT/A"}
MAX_GAP_DAYS = 75          # longer gap since the last run: the index route is not trusted, ages decide


def _fetch(client, url, timeout=120, stream_to=None):
    """One GET with the SEC client's session and rate limit; None when the file doesn't exist (403/404)."""
    if getattr(client, "fixtures_dir", None):
        try:
            return client.get_bytes(url)
        except Exception:  # noqa: BLE001
            return None
    for attempt in range(3):
        client.limiter.wait()
        try:
            r = client._session().get(url, timeout=timeout, stream=bool(stream_to))
        except Exception:  # noqa: BLE001
            time.sleep(5 * (attempt + 1))
            continue
        if r.status_code == 200:
            if stream_to:
                with open(stream_to, "wb") as f:
                    for chunk in r.iter_content(1 << 20):
                        f.write(chunk)
                return stream_to
            return r.content
        if r.status_code in (403, 404):
            return None
        time.sleep(10 * (attempt + 1))
    return None


def parse_master(text):
    """master.idx -> [(cik, form, date)]"""
    out = []
    for line in text.splitlines():
        p = line.split("|")
        if len(p) < 5 or not p[0].strip().isdigit():
            continue
        d = p[3].strip()
        if len(d) == 8 and d.isdigit():
            d = f"{d[:4]}-{d[4:6]}-{d[6:]}"
        out.append((int(p[0]), p[2].strip().upper(), d))
    return out


def sync_index(client, today, log=print):
    """Read the daily indexes since the last run. Returns {cik: {'any': date, 'periodic': date}} or None when the
    route can't be trusted (first run, long gap) - callers then fall back to cache ages."""
    st = cache_read(SYNC_PATH) or {}
    filings = st.get("filings") or {}
    last = st.get("last_day")
    if not last:
        cache_write(SYNC_PATH, {"last_day": (today - timedelta(days=1)).isoformat(), "filings": {}})
        log("SEC filing index: starting point set (cache ages decide this run)")
        return None
    try:
        last_d = date.fromisoformat(last)
    except ValueError:
        return None
    if (today - last_d).days > MAX_GAP_DAYS:
        cache_write(SYNC_PATH, {"last_day": (today - timedelta(days=1)).isoformat(), "filings": {}})
        log(f"SEC filing index: last run {last} is too long ago (cache ages decide this run)")
        return None
    d, done, n_files, n_rows = last_d + timedelta(days=1), last_d, 0, 0
    while d < today:
        if d.weekday() < 5:
            q = (d.month - 1) // 3 + 1
            raw = _fetch(client, INDEX_URL.format(y=d.year, q=q, ymd=d.strftime("%Y%m%d")))
            if raw is None:
                if (today - d).days <= 3:
                    break        # not published yet: read it next run
            else:
                n_files += 1
                for cik, form, fdate in parse_master(raw.decode("latin-1", "replace")):
                    e = filings.setdefault(str(cik), {})
                    e["any"] = max(e.get("any") or "", fdate)
                    if form in PERIODIC:
                        e["periodic"] = max(e.get("periodic") or "", fdate)
                    n_rows += 1
        done = d
        d += timedelta(days=1)
    cut = (today - timedelta(days=400)).isoformat()
    filings = {k: v for k, v in filings.items() if (v.get("any") or "") >= cut}
    cache_write(SYNC_PATH, {"last_day": done.isoformat(), "filings": filings})
    log(f"SEC filing index: {n_files} daily files read ({n_rows} filings) since {last}")
    return filings


# ------------------------------------------------------------------ bulk files (full refresh)
def needs_bulk(subset_version, n_wanted, n_cached):
    meta = cache_read(META_PATH) or {}
    return meta.get("subset_version") != subset_version or n_cached < 0.5 * max(1, n_wanted)


def mark_bulk_done(subset_version):
    cache_write(META_PATH, {"subset_version": subset_version, "date": date.today().isoformat()})


def bulk_load(client, url, ciks, out_dir, transform, log=print, keep_zip=False):
    """Download one SEC bulk zip and write the subset cache file for each wanted CIK. Returns the CIKs written."""
    want = {int(c) for c in ciks}
    tmp = os.path.join(CACHE_DIR, "bulk")
    os.makedirs(tmp, exist_ok=True)
    path = os.path.join(tmp, url.rsplit("/", 1)[-1])
    t0 = time.time()
    got = _fetch(client, url, timeout=1800, stream_to=path)
    if not got:
        log(f"  bulk file {url.rsplit('/', 1)[-1]} unavailable - downloading company by company instead")
        return set()
    log(f"  {url.rsplit('/', 1)[-1]}: {os.path.getsize(path) / 1e9:.1f} GB in {time.time() - t0:.0f} s")
    import json
    done = set()
    try:
        with zipfile.ZipFile(path) as z:
            for name in z.namelist():
                base = os.path.basename(name)
                if not (base.startswith("CIK") and base.endswith(".json")) or "-submissions-" in base:
                    continue
                try:
                    cik = int(base[3:13])
                except ValueError:
                    continue
                if cik not in want:
                    continue
                with z.open(name) as f:
                    raw = json.load(io.TextIOWrapper(f, encoding="utf-8"))
                cache_write(os.path.join(out_dir, f"{cik}.json.gz"), transform(raw))
                done.add(cik)
    finally:
        if not keep_zip:
            try:
                os.remove(path)
            except OSError:
                pass
    log(f"  {len(done)} of {len(want)} companies written from the bulk file")
    return done
