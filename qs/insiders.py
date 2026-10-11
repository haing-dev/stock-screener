"""Insider buying and selling (Forms 3/4/5) from SEC's 'Insider Transactions Data Sets' - information only.

One ZIP per calendar quarter (tab-separated tables). The last three quarters are combined per company: open-market
purchases (code P) and sales (code S) by officers, directors and 10% owners, with the largest buyers and sellers.
Sales under a pre-arranged 10b5-1 trading plan, and sales on the day of an option exercise, are counted separately
(they say little about conviction).
Rebuilt only when SEC posts a new quarter. Output: cache/prices/insiders/insiders.json.gz.
"""
import csv
import io
import os
import re
import zipfile
from collections import defaultdict
from datetime import date, datetime

from .config import CACHE_DIR

INS_DIR = os.path.join(CACHE_DIR, "prices", "insiders")
OUT_PATH = os.path.join(INS_DIR, "insiders.json.gz")
LIST_URL = "https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets"
ZIP_RE = re.compile(r'href="([^"]*?(\d{4})q([1-4])_form345\.zip)"', re.I)
csv.field_size_limit(10 ** 7)


def _d(s):
    s = (s or "").strip()
    for fmt in ("%d-%b-%Y", "%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(s.title() if "b" in fmt else s, fmt).date()
        except ValueError:
            continue
    return None


def _num(s):
    try:
        return float(str(s).replace(",", "").strip() or 0)
    except ValueError:
        return 0.0


def zip_links(html):
    """[(url, 'YYYYqN')] newest first."""
    out = {}
    for href, y, q in ZIP_RE.findall(html or ""):
        url = href if href.startswith("http") else "https://www.sec.gov" + (href if href.startswith("/") else "/" + href)
        out[f"{y}q{q}"] = url
    return [(u, k) for k, u in sorted(out.items(), reverse=True)]


def guessed_links(today, n=6):
    out = []
    y, q = today.year, (today.month - 1) // 3 + 1
    for _ in range(n):
        q -= 1
        if q == 0:
            y, q = y - 1, 4
        for d in ("datastandardsinnovation", "structureddata"):
            out.append((f"https://www.sec.gov/files/{d}/data/insider-transactions-data-sets/{y}q{q}_form345.zip",
                        f"{y}q{q}"))
    return out


def _table(zf, name):
    member = next((n for n in zf.namelist() if os.path.basename(n).upper().startswith(name.upper())), None)
    if member is None:
        return
    with zf.open(member) as raw:
        rd = csv.reader(io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline=""), delimiter="\t",
                        quoting=csv.QUOTE_NONE)
        head = [h.strip().upper() for h in next(rd)]
        for r in rd:
            yield dict(zip(head, r))


def _role(rel, title):
    rel = (rel or "").upper()
    t = (title or "").strip()
    if t:
        return t[:40]
    if "DIRECTOR" in rel:
        return "Director"
    if "TENPERCENTOWNER" in rel.replace(" ", "") or "10%" in rel:
        return "10% owner"
    if "OFFICER" in rel:
        return "Officer"
    return rel.title()[:40]


def scan(zf, wanted, acc):
    """Fold one quarter's open-market trades into acc[issuer_cik] (only companies we screen)."""
    subs = {}
    for r in _table(zf, "SUBMISSION"):
        if (r.get("DOCUMENT_TYPE") or "").strip() not in ("4", "5"):
            continue                      # amendments (4/A) would double count
        try:
            ic = int((r.get("ISSUERCIK") or "0").strip() or 0)
        except ValueError:
            continue
        if ic in wanted:
            subs[r["ACCESSION_NUMBER"]] = (ic, (r.get("AFF10B5ONE") or "").strip() in ("1", "true", "TRUE", "Y"))
    owners = {}
    for r in _table(zf, "REPORTINGOWNER"):
        a = r.get("ACCESSION_NUMBER")
        if a in subs and a not in owners:
            owners[a] = ((r.get("RPTOWNERNAME") or "").strip(), _role(r.get("RPTOWNER_RELATIONSHIP"), r.get("RPTOWNER_TITLE")))
    # option exercises / conversions per filing and day: a sale the same day is monetising pay ('exercise and
    # sell'), not a view on the shares
    exer, trades = set(), []
    for tbl in ("DERIV_TRANS", "NONDERIV_TRANS"):
        for r in _table(zf, tbl):
            a = r.get("ACCESSION_NUMBER")
            if a not in subs:
                continue
            code = (r.get("TRANS_CODE") or "").strip().upper()
            if code in ("M", "X", "C", "O"):
                exer.add((a, (r.get("TRANS_DATE") or "").strip().upper()))
            elif tbl == "NONDERIV_TRANS" and code in ("P", "S"):
                trades.append((a, code, r))
    for a, code, r in trades:
        sh, px = _num(r.get("TRANS_SHARES")), _num(r.get("TRANS_PRICEPERSHARE"))
        if sh <= 0 or px <= 0:
            continue
        ic, plan = subs[a]
        name, role = owners.get(a, ("", ""))
        d = _d(r.get("TRANS_DATE"))
        e = acc[ic]
        same_day = (a, (r.get("TRANS_DATE") or "").strip().upper()) in exer
        side = "buy" if code == "P" else ("plan_sell" if plan else "ex_sell" if same_day else "sell")
        e[side]["n"] += 1
        e[side]["value"] += sh * px
        p = e[side]["who"].setdefault(name, [role, 0.0, ""])
        p[1] += sh * px
        p[2] = max(p[2], d.isoformat() if d else "")


def build(zips, ctxs, log=print):
    wanted = {int(c) for c in ctxs}
    acc = defaultdict(lambda: {k: {"n": 0, "value": 0.0, "who": {}} for k in ("buy", "sell", "plan_sell", "ex_sell")})
    for zf in zips:
        scan(zf, wanted, acc)
    out = {}
    for ic, e in acc.items():
        rec = {}
        for k, v in e.items():
            if not v["n"]:
                continue
            top = sorted(v["who"].items(), key=lambda kv: -kv[1][1])[:4]
            rec[k] = {"n": v["n"], "value": round(v["value"]), "people": len(v["who"]),
                      "top": [[name.title() if name.isupper() else name, role, round(val), last]
                              for name, (role, val, last) in top]}
        if rec:
            out[str(ic)] = rec
    return out


def _fetch(client, url, timeout=300):
    from .holders import _fetch as f
    return f(client, url, timeout)


SCHEMA = 2      # bump to rebuild (2: sales on the day of an option exercise counted apart)


def update(client, state, cfg, log=print, today=None, quarters=3):
    """Rebuild when SEC has posted a new quarter; otherwise keep the stored result."""
    from .sec import cache_read, cache_write
    ic = (cfg.get("portal") or {}).get("insiders") or {}
    if ic.get("enabled") is False:
        return None
    today = today or date.today()
    prev = cache_read(OUT_PATH) or {}
    page = _fetch(client, LIST_URL, timeout=60)
    links = (zip_links(page.decode("utf-8", "replace")) if page else []) or guessed_links(today)
    zips, names = [], []
    for url, q in links:
        if q in names:
            continue
        if not zips and prev.get("latest") == q and prev.get("v") == SCHEMA:
            log(f"Insider trades: {q} already processed")
            return prev
        blob = _fetch(client, url)
        if not blob:
            continue
        zips.append(zipfile.ZipFile(io.BytesIO(blob)))
        names.append(q)
        if len(zips) >= quarters:
            break
    if not zips:
        log("Insider trades: no data set could be downloaded; keeping the previous result")
        return prev or None
    try:
        by_cik = build(zips, state["ctxs"], log)
    finally:
        for z in zips:
            z.close()
    res = {"latest": names[0], "quarters": names, "built": today.isoformat(), "by_cik": by_cik, "v": SCHEMA}
    cache_write(OUT_PATH, res)
    log(f"Insider trades ({', '.join(names)}): open-market trades for {len(by_cik)} companies")
    return res


def load():
    from .sec import cache_read
    return cache_read(OUT_PATH) or {}
