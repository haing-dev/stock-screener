"""Top institutional holders per company, from SEC Form 13F data sets (information only, never a rule).

Source: SEC 'Form 13F data sets' (https://www.sec.gov/dera/data/form-13f) - one ZIP of tab-separated tables per
3 filing months (windows end Feb, May, Aug, Nov), so a quarter's 13F-HR filings (due 45 days after quarter end) all
land in one ZIP. Tables used: SUBMISSION (accession, CIK, period), COVERPAGE (manager name, amendment type) and
INFOTABLE (CUSIP, value in dollars since 2023, shares, put/call).

CUSIPs are mapped to companies through OpenFIGI (free; OPENFIGI_API_KEY makes it ~60x faster) and cached by issuer
(the first 6 CUSIP characters), so share classes of one company are combined. Without a mapping the issuer name is
matched to the screened company's name when exactly one company matches.

Output (cache/prices/holders/holders.json.gz): {"zip", "period", "by_cik": {cik: {"h": [[manager, value_usd, shares,
share_of_manager_portfolio], ...top 15], "sp": [specialist managers holding it], "n": number of 13F holders}}}.
Index funds are flagged at export (config portal.holders.passive), so the site can show the top 5 active holders.
"""
import csv
import io
import json
import os
import re
import time
import zipfile
from collections import defaultdict
from datetime import date, datetime

from .config import CACHE_DIR

# kept under cache/prices so the existing GitHub cache steps of both workflows carry it between runs
HOLD_DIR = os.path.join(CACHE_DIR, "prices", "holders")
OUT_PATH = os.path.join(HOLD_DIR, "holders.json.gz")
MAP_PATH = os.path.join(HOLD_DIR, "issuer_map.json.gz")
LIST_URL = "https://www.sec.gov/dera/data/form-13f"
ZIP_RE = re.compile(r'href="([^"]*?(\d{2}[a-z]{3}\d{4})-(\d{2}[a-z]{3}\d{4})_form13f\.zip)"', re.I)
FIGI_URL = "https://api.openfigi.com/v3/mapping"
MONTHS = {m: i + 1 for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct",
                                          "nov", "dec"])}
csv.field_size_limit(10 ** 7)


def _d(s):
    """'31aug2026' / '30-JUN-2026' / '2026-06-30' -> date."""
    s = (s or "").strip()
    for fmt in ("%d%b%Y", "%d-%b-%Y", "%Y-%m-%d", "%m/%d/%Y", "%d-%b-%y"):
        try:
            return datetime.strptime(s.title() if "b" in fmt else s, fmt).date()
        except ValueError:
            continue
    return None


def zip_links(html):
    """[(url, window_start, window_end)] newest first, from the SEC listing page."""
    out = {}
    for href, a, b in ZIP_RE.findall(html or ""):
        url = href if href.startswith("http") else "https://www.sec.gov" + (href if href.startswith("/") else "/" + href)
        e = _d(b)
        if e:
            out[url] = (url, _d(a), e)
    return sorted(out.values(), key=lambda x: x[2], reverse=True)


def guessed_links(today):
    """Fallback when the listing page can't be read: the last few 3-month windows, both download folders."""
    out = []
    y, m = today.year, today.month
    for _ in range(6):
        while m not in (2, 5, 8, 11):
            m -= 1
            if m == 0:
                y, m = y - 1, 12
        end_m, end_y = m, y
        start_m, start_y = end_m - 2, end_y
        if start_m <= 0:
            start_m, start_y = start_m + 12, end_y - 1
        last = (date(end_y + (end_m == 12), end_m % 12 + 1, 1) - date.resolution).day
        names = [m_ for m_, i in MONTHS.items()]
        tag = f"01{names[start_m - 1]}{start_y}-{last:02d}{names[end_m - 1]}{end_y}_form13f.zip"
        for d in ("datastandardsinnovation", "structureddata"):
            out.append((f"https://www.sec.gov/files/{d}/data/form-13f-data-sets/{tag}", None, date(end_y, end_m, last)))
        m -= 1
        if m == 0:
            y, m = y - 1, 12
    return out


def _table(zf, name):
    """Rows of one TSV table in the ZIP as dicts (streamed)."""
    member = next((n for n in zf.namelist() if os.path.basename(n).upper().startswith(name.upper())), None)
    if member is None:
        raise KeyError(f"{name} table missing from the 13F ZIP")
    with zf.open(member) as raw:
        rd = csv.reader(io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline=""), delimiter="\t",
                        quoting=csv.QUOTE_NONE)
        head = [h.strip().upper() for h in next(rd)]
        for r in rd:
            yield dict(zip(head, r))


def choose_filings(zf, min_filers=1500):
    """Pick the latest reporting period with enough filers and one holdings filing per manager:
    the latest RESTATEMENT amendment if any, else the latest original 13F-HR. Returns (period, {accn: manager})."""
    subs = {}
    for r in _table(zf, "SUBMISSION"):
        t = (r.get("SUBMISSIONTYPE") or "").upper()
        if t not in ("13F-HR", "13F-HR/A"):
            continue
        subs[r["ACCESSION_NUMBER"]] = (r.get("CIK"), _d(r.get("PERIODOFREPORT")), _d(r.get("FILING_DATE")), t)
    cover = {}
    for r in _table(zf, "COVERPAGE"):
        a = r.get("ACCESSION_NUMBER")
        if a in subs:
            cover[a] = ((r.get("FILINGMANAGER_NAME") or "").strip(), (r.get("AMENDMENTTYPE") or "").upper(),
                        (r.get("REPORTTYPE") or "").upper())
    per_count = defaultdict(set)
    for a, (cik, per, _, _) in subs.items():
        if per:
            per_count[per].add(cik)
    good = [p for p, s in per_count.items() if len(s) >= min_filers]
    if not good:
        good = list(per_count)
    if not good:
        return None, {}
    period = max(good)
    best = {}
    for a, (cik, per, fd, t) in subs.items():
        if per != period:
            continue
        name, amend, rtype = cover.get(a, ("", "", ""))
        if "NOTICE" in rtype:
            continue
        if t == "13F-HR/A" and "RESTATEMENT" not in amend:
            continue                       # 'new holdings' amendments only add a few lines; skipped
        rank = (1 if t == "13F-HR/A" else 0, fd or date.min)
        if cik not in best or rank > best[cik][0]:
            best[cik] = (rank, a, name)
    return period, {a: name for _, a, name in best.values()}


def scan_values(zf, accns):
    """Pass 1: total value per CUSIP and per manager (portfolio size), plus each CUSIP's issuer name."""
    by_cusip, by_mgr, names = defaultdict(float), defaultdict(float), {}
    for r in _table(zf, "INFOTABLE"):
        a = r.get("ACCESSION_NUMBER")
        if a not in accns:
            continue
        v = _num(r.get("VALUE"))
        by_mgr[a] += v
        if (r.get("PUTCALL") or "").strip() or (r.get("SSHPRNAMTTYPE") or "").strip().upper() != "SH":
            continue
        cu = (r.get("CUSIP") or "").strip().upper()
        if len(cu) != 9:
            continue
        by_cusip[cu] += v
        names.setdefault(cu, ((r.get("NAMEOFISSUER") or "").strip(), (r.get("TITLEOFCLASS") or "").strip()))
    return by_cusip, by_mgr, names


def positions(zf, accns, cusip_cik):
    """Pass 2: {cik: {accn: [value, shares]}} for mapped CUSIPs (share classes of one company combined)."""
    out = defaultdict(lambda: defaultdict(lambda: [0.0, 0.0]))
    for r in _table(zf, "INFOTABLE"):
        a = r.get("ACCESSION_NUMBER")
        if a not in accns or (r.get("PUTCALL") or "").strip():
            continue
        if (r.get("SSHPRNAMTTYPE") or "").strip().upper() != "SH":
            continue
        cik = cusip_cik.get((r.get("CUSIP") or "").strip().upper())
        if cik is None:
            continue
        p = out[cik][a]
        p[0] += _num(r.get("VALUE"))
        p[1] += _num(r.get("SSHPRNAMT"))
    return out


def _num(s):
    try:
        return float(str(s).replace(",", "").strip() or 0)
    except ValueError:
        return 0.0


_SUFFIX = re.compile(r"[,.]?\s+(INC|INCORPORATED|LLC|L\.?L\.?C|LP|L\.P|LTD|LIMITED|CORP|CORPORATION|CO|COMPANY|PLC|"
                     r"N\.?A|AG|SA|S\.A|SE|NV|N\.V|AB|ASA|GMBH|LLP|PC|/DE/|/ADV|/MD|/CA|/NY|/IL)\.?$", re.I)
_KEEP_UPPER = {"FMR", "JPMORGAN", "UBS", "BNY", "AQR", "TCI", "RTW", "D1", "DE", "II", "III", "IV", "LP", "AMP",
               "T", "AXA", "BMO", "RBC", "TD", "CIBC", "HSBC", "BNP", "ING", "NN", "DWS", "MFS", "PNC", "USAA",
               "ICONIQ", "PGIM", "SSGA", "TIAA", "CPP", "PSP", "GQG", "ARK", "DFA"}


def clean_manager(name):
    s = re.sub(r"\s+", " ", (name or "").replace("/", " /").strip())
    for _ in range(3):
        s2 = _SUFFIX.sub("", s).strip(" ,.")
        if s2 == s:
            break
        s = s2
    s = s.replace(" /", "").strip()
    words = []
    for w in s.split(" "):
        u = w.upper()
        if u in _KEEP_UPPER or (len(u) <= 3 and not re.search(r"[AEIOUY]", u)):
            words.append(u)
        else:
            words.append(w[:1].upper() + w[1:].lower())
    out = " ".join(words).rstrip(" &,")
    return out.replace("JPMORGAN", "JPMorgan").replace("Blackrock", "BlackRock")


def is_match(name, patterns):
    """True when a manager name contains any of the patterns (case-insensitive, punctuation ignored)."""
    n = " " + re.sub(r"[^A-Z0-9]+", " ", (name or "").upper()) + " "
    return any(" " + re.sub(r"[^A-Z0-9]+", " ", p.upper()).strip() + " " in n for p in patterns if p.strip())


def top_active(entry, shares_out, passive, n=5):
    """Site payload: [[manager, % of the company or None, specialist?], ...] - the top n holders that aren't index
    funds or broker platforms (config portal.holders.passive)."""
    out = []
    sp = set((entry or {}).get("sp") or [])
    for name, value, sh, _port in (entry or {}).get("h") or []:
        if is_match(name, passive):
            continue
        pct = round(sh / shares_out, 4) if shares_out and sh else None
        out.append([name, pct if pct is None or pct < 1 else None, name in sp])
        if len(out) >= n:
            break
    return out


# ------------------------------------------------------------------ CUSIP -> company
def _norm_name(s):
    s = (s or "").upper().replace("&", " AND ")
    s = re.sub(r"[^A-Z0-9 ]", " ", s)
    drop = {"INC", "INCORPORATED", "CORP", "CORPORATION", "CO", "COMPANY", "LTD", "LIMITED", "PLC", "THE", "HLDGS",
            "HOLDINGS", "HOLDING", "GROUP", "GRP", "NEW", "DEL", "COM", "LLC", "LP", "SA", "NV", "AG", "CL", "A", "B",
            "INTL", "INTERNATIONAL", "TECHNOLOGIES", "TECHNOLOGY", "TECH", "SYS", "SYSTEMS", "ADR", "SPONSORED"}
    return " ".join(w for w in s.split() if w not in drop)


def _norm_ticker(t):
    return re.sub(r"[^A-Z0-9]", "", (t or "").upper())


def figi_map(cusips, api_key="", budget_s=900, log=print, session=None):
    """{cusip: ticker or ''} via OpenFIGI. Stops when the time budget runs out (the rest is mapped next run)."""
    import requests
    s = session or requests.Session()
    hdr = {"Content-Type": "application/json"}
    if api_key:
        hdr["X-OPENFIGI-APIKEY"] = api_key
    batch, pause = (100, 6.0 / 25) if api_key else (10, 60.0 / 25)
    out, t0 = {}, time.time()
    todo = list(cusips)
    i = 0
    while i < len(todo) and time.time() - t0 < budget_s:
        chunk = todo[i:i + batch]
        body = [{"idType": "ID_CUSIP", "idValue": c, "exchCode": "US"} for c in chunk]
        try:
            r = s.post(FIGI_URL, data=json.dumps(body), headers=hdr, timeout=60)
        except Exception as e:  # noqa: BLE001
            log(f"  OpenFIGI request failed ({type(e).__name__}); retrying")
            time.sleep(10)
            continue
        if r.status_code == 413 and batch > 5:
            batch = 5                      # older no-key limit: 5 jobs per request
            continue
        if r.status_code == 429:
            time.sleep(max(pause * 5, float(r.headers.get("ratelimit-reset") or 0) or 6))
            continue
        if r.status_code != 200:
            log(f"  OpenFIGI HTTP {r.status_code}; stopping the mapping for this run")
            break
        for c, res in zip(chunk, r.json()):
            tick = ""
            for d in (res.get("data") or []):
                if (d.get("marketSector") or "Equity") == "Equity" and d.get("ticker"):
                    tick = d["ticker"]
                    break
            out[c] = tick
        i += batch
        time.sleep(pause)
    return out


def map_issuers(names, by_cusip, ctxs, cache, api_key="", budget_s=900, min_value=5e6, log=print, figi=None):
    """{cusip: cik}. Cache = {issuer6: {"t": ticker or "", "cik": cik or None}} (persists across runs)."""
    by_tick = {}
    for c, x in ctxs.items():
        for t in [x.get("ticker")] + [s.strip() for s in str(x.get("other_tickers") or "").replace(";", ",").split(",")]:
            if t:
                by_tick.setdefault(_norm_ticker(t), c)
    by_name = defaultdict(set)
    for c, x in ctxs.items():
        n = _norm_name(x.get("name"))
        if n:
            by_name[n].add(c)
    # issuers worth mapping: equity lines above a small value floor, biggest first
    issuers = defaultdict(float)
    rep = {}
    for cu, v in by_cusip.items():
        if v >= min_value:
            i6 = cu[:6]
            issuers[i6] += v
            if i6 not in rep or v > by_cusip[rep[i6]]:
                rep[i6] = cu
    todo = [i6 for i6 in sorted(issuers, key=issuers.get, reverse=True) if i6 not in cache]
    if todo:
        log(f"  mapping {len(todo)} new issuers to tickers (OpenFIGI{' with key' if api_key else ', no key: slower'})")
        got = (figi or figi_map)([rep[i6] for i6 in todo], api_key=api_key, budget_s=budget_s, log=log)
        for i6 in todo:
            cu = rep[i6]
            if cu in got:
                cache[i6] = {"t": got[cu]}
    remaining = sum(1 for i6 in todo if i6 not in cache)
    out = {}
    for cu in by_cusip:
        i6 = cu[:6]
        ent = cache.get(i6)
        cik = None
        if ent and ent.get("t"):
            cik = by_tick.get(_norm_ticker(ent["t"]))
        if cik is None and (not ent or not ent.get("t")):
            # no ticker: fall back to an exact (normalized) name match with exactly one screened company
            cands = by_name.get(_norm_name(names.get(cu, ("",))[0]))
            if cands and len(cands) == 1:
                cik = next(iter(cands))
        if cik is not None:
            out[cu] = cik
    return out, remaining


def build(zf, ctxs, cache, api_key="", budget_s=900, top=15, log=print, figi=None, specialists=()):
    period, accns = choose_filings(zf)
    if not accns:
        raise RuntimeError("no 13F holdings filings found in the ZIP")
    log(f"  13F period {period}: {len(accns)} managers")
    by_cusip, by_mgr, names = scan_values(zf, accns)
    cusip_cik, remaining = map_issuers(names, by_cusip, ctxs, cache, api_key=api_key, budget_s=budget_s, log=log,
                                       figi=figi)
    pos = positions(zf, accns, cusip_cik)
    by_cik = {}
    for cik, mgrs in pos.items():
        ranked = sorted(mgrs.items(), key=lambda kv: kv[1][0], reverse=True)
        h = []
        for a, (v, sh) in ranked[:top]:
            port = by_mgr.get(a) or 0
            h.append([clean_manager(accns[a]), round(v), round(sh), round(v / port, 5) if port else None])
        sp = sorted({clean_manager(accns[a]) for a in mgrs if is_match(accns[a], specialists)})
        by_cik[str(cik)] = {"h": h, "n": len(mgrs), "sp": sp}
    return {"period": period.isoformat() if period else None, "by_cik": by_cik, "unmapped_issuers": remaining}


def _fetch(client, url, timeout=300):
    """One polite GET with the SEC client's session and rate limit. A missing file answers 403 or 404 on SEC's file
    server, so both mean 'not there' here (no long retry loop); None = not found."""
    if getattr(client, "fixtures_dir", None):
        try:
            return client.get_bytes(url)
        except Exception:  # noqa: BLE001
            return None
    for attempt in range(3):
        client.limiter.wait()
        try:
            r = client._session().get(url, timeout=timeout)
        except Exception:  # noqa: BLE001
            time.sleep(5 * (attempt + 1))
            continue
        if r.status_code == 200:
            return r.content
        if r.status_code in (403, 404):
            return None
        time.sleep(10 * (attempt + 1))
    return None


def update(client, state, cfg, log=print, today=None):
    """Download the newest 13F data set (skipped when it was already processed) and rebuild holders.json.gz."""
    from .sec import cache_read, cache_write
    pc = (cfg.get("portal") or {}).get("holders") or {}
    if pc.get("enabled") is False:
        log("13F holders: disabled in config")
        return None
    today = today or date.today()
    prev = cache_read(OUT_PATH) or {}
    page = _fetch(client, LIST_URL, timeout=60)
    links = zip_links(page.decode("utf-8", "replace")) if page else []
    if not links:
        log("  13F listing page unreadable; trying the expected file names")
    links = links or guessed_links(today)
    cache = cache_read(MAP_PATH) or {}
    api_key = os.environ.get("OPENFIGI_API_KEY", "").strip()
    for url, _, end in links[:4]:
        name = url.rsplit("/", 1)[-1]
        if prev.get("zip") == name and prev.get("complete"):
            log(f"13F holders: {name} already processed")
            return prev
        blob = _fetch(client, url)
        if not blob:
            continue
        log(f"13F holders from {name} ({len(blob) / 1e6:.0f} MB)")
        with zipfile.ZipFile(io.BytesIO(blob)) as zf:
            res = build(zf, state["ctxs"], cache, api_key=api_key,
                        budget_s=float(pc.get("figi_budget_seconds", 900)), log=log,
                        specialists=pc.get("specialists") or ())
        res["zip"] = name
        res["complete"] = res.get("unmapped_issuers", 0) == 0
        res["built"] = today.isoformat()
        cache_write(MAP_PATH, cache)
        cache_write(OUT_PATH, res)
        log(f"  holders found for {len(res['by_cik'])} of {len(state['ctxs'])} companies")
        return res
    log("13F holders: no data set could be downloaded; keeping the previous holders")
    return prev or None


def load():
    from .sec import cache_read
    return cache_read(OUT_PATH) or {}
