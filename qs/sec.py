"""Polite SEC EDGAR client: rate-limited, retrying, with a small on-disk cache."""
import gzip
import json
import os
import random
import threading
import time

import requests

TICKERS_URL = "https://www.sec.gov/files/company_tickers_exchange.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"
FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
DOC_URL = "https://www.sec.gov/Archives/edgar/data/{cik}/{accn_nodash}/{doc}"
FILING_INDEX_URL = "https://www.sec.gov/Archives/edgar/data/{cik}/{accn_nodash}/"
XBRL_VIEWER_URL = "https://www.sec.gov/cgi-bin/viewer?action=view&cik={cik}&accession_number={accn}&xbrl_type=v"


def filing_index_url(cik, accn):
    return FILING_INDEX_URL.format(cik=int(cik), accn_nodash=accn.replace("-", ""))


def doc_url(cik, accn, doc):
    return DOC_URL.format(cik=int(cik), accn_nodash=accn.replace("-", ""), doc=doc)


class NotFound(Exception):
    pass


class RateLimiter:
    def __init__(self, per_sec):
        self.min_interval = 1.0 / max(0.5, float(per_sec))
        self.lock = threading.Lock()
        self.next_t = 0.0

    def wait(self):
        with self.lock:
            now = time.monotonic()
            t = max(now, self.next_t)
            self.next_t = t + self.min_interval
        delay = t - time.monotonic()
        if delay > 0:
            time.sleep(delay)


class SECClient:
    def __init__(self, user_agent, per_sec=8, fixtures_dir=None):
        self.ua = user_agent
        self.limiter = RateLimiter(per_sec)
        self.local = threading.local()
        self.fixtures_dir = fixtures_dir

    def _session(self):
        s = getattr(self.local, "s", None)
        if s is None:
            s = requests.Session()
            s.headers.update({"User-Agent": self.ua, "Accept-Encoding": "gzip, deflate"})
            self.local.s = s
        return s

    def _fixture(self, url):
        rel = url.split("://", 1)[1]
        path = os.path.join(self.fixtures_dir, *rel.split("/"))
        if url.endswith("/"):
            path = os.path.join(path, "index.html")
        if not os.path.exists(path):
            raise NotFound(url)
        with open(path, "rb") as f:
            return f.read()

    def get_bytes(self, url):
        if self.fixtures_dir:
            return self._fixture(url)
        last_err = None
        for attempt in range(7):
            self.limiter.wait()
            try:
                r = self._session().get(url, timeout=90)
            except requests.RequestException as e:
                last_err = e
                time.sleep(min(60, 2 ** attempt + random.random()))
                continue
            if r.status_code == 200:
                return r.content
            if r.status_code == 404:
                raise NotFound(url)
            if r.status_code == 403:
                # SEC answers 403 when the User-Agent is missing/generic or the rate limit was exceeded.
                last_err = RuntimeError(
                    "SEC returned 403 Forbidden. Check that config.json 'user_agent' has your name and "
                    "email, and that only one copy of the screener is running. SEC blocks for ~10 "
                    "minutes after too many requests; the screener will wait and retry.")
                time.sleep(min(180, 15 * (attempt + 1)))
                continue
            if r.status_code in (429, 500, 502, 503, 504):
                last_err = RuntimeError(f"HTTP {r.status_code} from SEC")
                time.sleep(min(120, 2 ** attempt * 2))
                continue
            raise RuntimeError(f"HTTP {r.status_code} for {url}")
        raise last_err if last_err else RuntimeError(f"Failed to fetch {url}")

    def get_json(self, url):
        return json.loads(self.get_bytes(url))


def cache_read(path, max_age_days=None):
    if not os.path.exists(path):
        return None
    if max_age_days is not None and (time.time() - os.path.getmtime(path)) > max_age_days * 86400:
        return None
    try:
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError, EOFError):
        return None


def cache_write(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        json.dump(obj, f)
    os.replace(tmp, path)
