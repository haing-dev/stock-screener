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
    return period, {a: (name, str(cik)) for cik, (_, a, name) in best.items()}


def scan_values(zf, accns, npos=None):
    """Pass 1: total value per CUSIP and per manager (stock portfolio size, options left out), plus each CUSIP's
    issuer name. npos (a dict) receives the number of different stocks each filing holds."""
    by_cusip, by_mgr, names = defaultdict(float), defaultdict(float), {}
    held = defaultdict(set)
    for r in _table(zf, "INFOTABLE"):
        a = r.get("ACCESSION_NUMBER")
        if a not in accns:
            continue
        v = _num(r.get("VALUE"))
        if (r.get("PUTCALL") or "").strip() or (r.get("SSHPRNAMTTYPE") or "").strip().upper() != "SH":
            continue
        by_mgr[a] += v
        cu = (r.get("CUSIP") or "").strip().upper()
        if len(cu) != 9:
            continue
        held[a].add(cu[:6])
        by_cusip[cu] += v
        names.setdefault(cu, ((r.get("NAMEOFISSUER") or "").strip(), (r.get("TITLEOFCLASS") or "").strip()))
    if npos is not None:
        npos.update({a: len(x) for a, x in held.items()})
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
    """Site payload: [[manager, % of the company or None, specialist?, share of the manager's 13F portfolio, value],
    ...] - the top n holders that aren't index funds or broker platforms (config portal.holders.passive)."""
    out = []
    sp = set((entry or {}).get("sp") or [])
    rows = sorted((entry or {}).get("h") or [], key=lambda x: -(x[3] or 0))
    for name, value, sh, port in rows:
        if is_match(name, passive):
            continue
        pct = round(sh / shares_out, 4) if shares_out and sh else None
        out.append([name, pct if pct is None or pct < 1 else None, name in sp, port, value])
        if len(out) >= n:
            break
    return out


def moves(entry, passive, n=5):
    """Biggest buyers and sellers since the previous quarter, index funds and brokers left out:
    {'buy': [[manager, value change, kind (new/add), share of its portfolio, share change]], 'sell': [...]}"""
    out = {}
    for side in ("buy", "sell"):
        rows = [r for r in (entry or {}).get(side) or [] if not is_match(r[0], passive)][:n]
        if rows:
            out[side] = rows
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
    """{cusip: cik}. Cache = {issuer6: {"t": ticker or ""}} (persists across runs). Only issuers whose name starts
    like one of the screened companies are sent to OpenFIGI (most 13F lines are ETFs, funds and companies we don't
    screen), which keeps the free, rate-limited mapping short."""
    by_tick = {}
    for c, x in ctxs.items():
        for t in [x.get("ticker")] + [s.strip() for s in str(x.get("other_tickers") or "").replace(";", ",").split(",")]:
            if t:
                by_tick.setdefault(_norm_ticker(t), c)
    by_name = defaultdict(set)
    firsts = set()
    for c, x in ctxs.items():
        n = _norm_name(x.get("name"))
        if n:
            by_name[n].add(c)
            firsts.add(n.split()[0])
    issuers = defaultdict(float)
    rep = {}
    for cu, v in by_cusip.items():
        if v < min_value:
            continue
        nm = _norm_name(names.get(cu, ("",))[0])
        if not nm or nm.split()[0] not in firsts:
            continue
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
            cands = by_name.get(_norm_name(names.get(cu, ("",))[0]))
            if cands and len(cands) == 1:
                cik = next(iter(cands))
        if cik is not None:
            out[cu] = cik
    return out, remaining


# ------------------------------------------------------------------ who counts as a 'conviction' holder
MGR_PATH = os.path.join(HOLD_DIR, "managers.json.gz")


def manager_stats(by_acc, npos, accns, today, log=print, max_age_days=365):
    """{manager_cik: [name, 13F stock portfolio $, number of stocks]} - measured once from a 13F data set and kept
    for a year (fund sizes and styles change slowly)."""
    from .sec import cache_read, cache_write
    old = cache_read(MGR_PATH) or {}
    try:
        fresh = old.get("as_of") and (today - date.fromisoformat(old["as_of"])).days <= max_age_days
    except ValueError:
        fresh = False
    if fresh and old.get("by_cik"):
        return old["by_cik"]
    st = {}
    for a, v in by_acc.items():
        name, mcik = accns[a]
        cur = st.get(mcik) or [name, 0.0, 0]
        st[mcik] = [name, cur[1] + v, max(cur[2], npos.get(a, 0))]
    st = {k: [n, round(v), c] for k, (n, v, c) in st.items()}
    cache_write(MGR_PATH, {"as_of": today.isoformat(), "by_cik": st})
    log(f"  fund sizes measured for {len(st)} managers (kept until {today.replace(year=today.year + 1)})")
    return st


def is_excluded(name, stats, rules):
    """Index funds and broker platforms, the largest fund houses ('own everything') and quant / multi-manager funds:
    by name (config lists) or by the 13F itself (more than max_positions stocks, or a huge portfolio across many)."""
    if is_match(name, rules.get("passive") or ()) or is_match(name, rules.get("exclude") or ()):
        return True
    if stats:
        _, aum, n = stats
        if n > rules.get("max_positions", 1000):
            return True
        if aum > rules.get("huge_aum", 250e9) and n > rules.get("huge_aum_positions", 500):
            return True
    return False


def _by_manager(pos_for_company, accns):
    """{accn: [value, shares]} -> {manager_cik: [value, shares, name]} (one filing per manager per quarter)."""
    out = {}
    for a, (v, sh) in pos_for_company.items():
        name, mcik = accns[a]
        cur = out.get(mcik)
        out[mcik] = [v + (cur[0] if cur else 0), sh + (cur[1] if cur else 0), name]
    return out


def build(zf, ctxs, cache, api_key="", budget_s=900, top=10, log=print, figi=None, specialists=(), prev_zf=None,
          moves=8, rules=None, today=None):
    """Top holders per company, plus (with the previous quarter's data set) who bought and who sold or exited, and
    each holder's position as a share of its whole 13F portfolio (conviction)."""
    period, accns = choose_filings(zf)
    if not accns:
        raise RuntimeError("no 13F holdings filings found in the ZIP")
    log(f"  13F period {period}: {len(accns)} managers")
    npos = {}
    by_cusip, by_acc, names = scan_values(zf, accns, npos)
    rules = rules or {}
    stats = manager_stats(by_acc, npos, accns, today or date.today(), log=log)
    min_aum = rules.get("min_manager_aum", 500e6)
    excl = {}

    def excluded(mcik, name):
        if mcik not in excl:
            excl[mcik] = is_excluded(name, stats.get(mcik), rules)
        return excl[mcik]
    cusip_cik, remaining = map_issuers(names, by_cusip, ctxs, cache, api_key=api_key, budget_s=budget_s, log=log,
                                       figi=figi)
    pos = positions(zf, accns, cusip_cik)
    port = defaultdict(float)
    for a, v in by_acc.items():
        port[accns[a][1]] += v
    prev_pos, p_accns, p_period = {}, {}, None
    if prev_zf is not None:
        p_period, p_accns = choose_filings(prev_zf)
        if p_accns and p_period and period and p_period < period:
            prev_pos = positions(prev_zf, p_accns, cusip_cik)
            log(f"  previous quarter {p_period}: {len(p_accns)} managers (for buyers and sellers)")
        else:
            p_period = None
    by_cik = {}
    for cik, accs in pos.items():
        cur = _by_manager(accs, accns)
        ctx = ctxs.get(cik) or ctxs.get(str(cik)) or ctxs.get(int(cik) if str(cik).isdigit() else cik) or {}
        sh_out = ctx.get("shares_used")
        # conviction: the position as a share of the holder's own portfolio, among real active holders of a
        # meaningful stake (fund >= $500M; stake >= 0.25% of the company or >= $250M)
        cand = []
        for mcik, (v, sh, name) in cur.items():
            pv = port.get(mcik) or 0
            if not pv or pv < min_aum or excluded(mcik, name):
                continue
            big = v >= rules.get("min_stake_usd", 250e6)
            if sh_out:
                big = big or sh >= rules.get("min_stake_share", 0.0025) * sh_out
            else:
                big = big or v >= rules.get("min_stake_usd_unknown_shares", 25e6)
            if big:
                cand.append((v / pv, mcik, v, sh, name))
        cand.sort(reverse=True)
        h = [[clean_manager(name), round(v), round(sh), round(ps, 5)] for ps, _, v, sh, name in cand[:top]]
        sp = sorted({clean_manager(name) for (_, _, name) in cur.values() if is_match(name, specialists)})
        ent = {"h": h, "n": len(cur), "sp": sp}
        if p_period:
            prev = _by_manager(prev_pos.get(cik, {}), p_accns)
            px = None
            tv = sum(x[0] for x in cur.values())
            ts = sum(x[1] for x in cur.values())
            if ts:
                px = tv / ts
            chg = []
            for mcik in set(cur) | set(prev):
                c_ = cur.get(mcik)
                p_ = prev.get(mcik)
                csh, psh = (c_[1] if c_ else 0.0), (p_[1] if p_ else 0.0)
                if csh == psh:
                    continue
                if not psh:
                    val, kind = c_[0], "new"
                elif not csh:
                    val, kind = -p_[0], "exit"
                else:
                    val, kind = (csh - psh) * (px or (c_[0] / csh)), "add" if csh > psh else "cut"
                name = (c_ or p_)[2]
                if excluded(mcik, name):
                    continue
                pv = port.get(mcik) or 0
                chg.append([clean_manager(name), round(val), kind, round(c_[0] / pv, 5) if (c_ and pv) else None,
                            round((csh - psh) / psh, 3) if psh else None])
            chg.sort(key=lambda x: x[1])
            ent["buy"] = [x for x in reversed(chg) if x[1] > 0][:moves]
            ent["sell"] = [x for x in chg if x[1] < 0][:moves]
        by_cik[str(cik)] = ent
    return {"period": period.isoformat() if period else None, "prev_period": p_period.isoformat() if p_period else None,
            "by_cik": by_cik, "unmapped_issuers": remaining, "v": SCHEMA}


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


SCHEMA = 2      # bump to rebuild from the stored data set (2: conviction ranking, fund-house / quant exclusions)


def update(client, state, cfg, log=print, today=None):
    """Once per quarter: when SEC posts a new 13F data set, rebuild holders.json.gz from it and the previous one
    (for buyers / sellers). The ZIPs are kept until every issuer is mapped to a ticker, so an unfinished mapping
    continues next run without downloading again; then they are deleted."""
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
    os.makedirs(HOLD_DIR, exist_ok=True)

    def get_zip(url):
        name = url.rsplit("/", 1)[-1]
        path = os.path.join(HOLD_DIR, name)
        if os.path.exists(path) and os.path.getsize(path) > 1e6:
            return path
        blob = _fetch(client, url)
        if not blob:
            return None
        with open(path, "wb") as f:
            f.write(blob)
        return path

    for i, (url, _, end) in enumerate(links[:4]):
        name = url.rsplit("/", 1)[-1]
        if prev.get("zip") == name and prev.get("complete") and prev.get("v") == SCHEMA:
            log(f"13F holders: {name} already processed (next data set expected after the next quarter's filings)")
            return prev
        cur_path = get_zip(url)
        if not cur_path:
            continue
        prev_path = None
        for purl, _, pend in links[i + 1:i + 4]:
            if pend < end:
                prev_path = get_zip(purl)
                if prev_path:
                    break
        log(f"13F holders from {name}" + (f" (changes against {os.path.basename(prev_path)})" if prev_path else ""))
        with zipfile.ZipFile(cur_path) as zf:
            pz = zipfile.ZipFile(prev_path) if prev_path else None
            try:
                res = build(zf, state["ctxs"], cache, api_key=api_key,
                            budget_s=float(pc.get("figi_budget_seconds", 900)), log=log,
                            specialists=pc.get("specialists") or (), prev_zf=pz, rules=pc, today=today)
            finally:
                if pz:
                    pz.close()
        res["zip"] = name
        res["complete"] = res.get("unmapped_issuers", 0) == 0
        res["built"] = today.isoformat()
        cache_write(MAP_PATH, cache)
        cache_write(OUT_PATH, res)
        if res["complete"]:
            for f in os.listdir(HOLD_DIR):
                if f.endswith(".zip"):
                    os.remove(os.path.join(HOLD_DIR, f))
        log(f"  holders found for {len(res['by_cik'])} of {len(state['ctxs'])} companies"
            + ("" if res["complete"] else f"; {res.get('unmapped_issuers')} issuers still to map next run"))
        return res
    log("13F holders: no data set could be downloaded; keeping the previous holders")
    return prev or None


def load():
    from .sec import cache_read
    return cache_read(OUT_PATH) or {}
