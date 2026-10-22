"""Who owned and who traded: SEC's bulk data sets, read once per data set and kept compact.

13F (Form 13F data sets, one ZIP per filing window):
  every original 13F-HR filing in the window: filer, period, filing date, its stock portfolio (shares, no options,
  VALUE in thousands of dollars before 2023, dollars after), and each position mapped to a company (CUSIP issuer ->
  ticker via OpenFIGI, else a unique name match; qs/holders.py). Kept: positions of 3%+ of the filer's portfolio
  held by a high conviction owner (triage/rules.py: not an index fund, broker, fund house or quant fund; portfolio
  $100M+; at most 1,000 stocks).
  -> cache/tri/owners/<data set>.json.gz {"span": [first, last filing day], "rows": [[filer_cik, filer, period,
     filed, cik, weight], ...]}

Insiders (Insider Transactions data sets, one ZIP per calendar quarter of filing):
  open-market purchases (P) and sales (S) of the companies in the panel. A sale under a 10b5-1 plan ('Splan') or
  on the day of an option exercise in the same filing ('Sex') is kept apart: it says little about conviction.
  -> cache/tri/insiders/<YYYYqN>.json.gz {cik: [[trade day, filed, side, value $, who, role], ...]}
"""
import csv
import io
import os
import re
import zipfile
from collections import defaultdict
from datetime import date, datetime

from qs import holders as H
from qs import insiders as INS
from qs.backtest_support import read_json, write_json
from qs.sec import cache_read, cache_write

from . import rules as R
from . import paths as P

LIST_13F = ("https://www.sec.gov/data-research/sec-markets-data/form-13f-data-sets", H.LIST_URL)
LIST_INS = (INS.LIST_URL, "https://www.sec.gov/dera/data/financial-statement-and-notes-data-set")
ZIP13F = re.compile(r'href="([^"]+form13f\.zip)"', re.I)
ZIPINS = re.compile(r'href="([^"]+?(\d{4})q([1-4])_form345\.zip)"', re.I)
MON = {m: i + 1 for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split())}
DOLLARS_FROM = "2023-01-03"          # 13F VALUE switched from thousands to dollars on this filing date
csv.field_size_limit(10 ** 7)


def _abs(href):
    return href if href.startswith("http") else "https://www.sec.gov" + (href if href.startswith("/") else "/" + href)


def span_13f(url):
    """Filing days a 13F data set covers: 2023q4 -> Oct-Dec 2023; 01mar2024-31may2024 -> those days."""
    n = url.rsplit("/", 1)[-1].lower()
    m = re.match(r"(\d{4})q(\d)_", n)
    if m:
        y, q = int(m.group(1)), int(m.group(2))
        return [f"{y}-{3 * q - 2:02d}-01", f"{y}-{3 * q:02d}-{[31, 30, 30, 31][q - 1]}"]
    m = re.match(r"(\d{2})([a-z]{3})(\d{4})-(\d{2})([a-z]{3})(\d{4})_", n)
    if m:
        return [f"{m.group(3)}-{MON[m.group(2)]:02d}-{m.group(1)}", f"{m.group(6)}-{MON[m.group(5)]:02d}-{m.group(4)}"]
    return None


def links_13f(client, today):
    for u in LIST_13F:
        page = H._fetch(client, u, timeout=60)
        if page:
            got = sorted({_abs(h) for h in ZIP13F.findall(page.decode("utf-8", "replace"))})
            if got:
                return [(x, span_13f(x)) for x in got if span_13f(x)]
    return [(u, span_13f(u)) for u, _, _ in H.guessed_links(today) if span_13f(u)]


def links_ins(client, today):
    """[(YYYYqN, [candidate urls])] oldest first."""
    page = H._fetch(client, LIST_INS[0], timeout=60)
    got = defaultdict(list)
    if page:
        for h, y, q in ZIPINS.findall(page.decode("utf-8", "replace")):
            got[f"{y}q{q}"].append(_abs(h))
    if not got:
        for u, q in INS.guessed_links(today, n=8):
            got[q].append(u)
    return sorted(got.items())


def _iso(s):
    s = (s or "").strip()
    for fmt in ("%d-%b-%Y", "%Y-%m-%d", "%m/%d/%Y", "%d%b%Y"):
        try:
            return datetime.strptime(s.title() if "b" in fmt else s, fmt).date().isoformat()
        except ValueError:
            continue
    return None


# ------------------------------------------------------------------ 13F
def filings_13f(zf):
    """{accn: (filer name, filer cik, period, filed)} - original 13F-HR holdings reports, the latest per filer and
    period inside the data set."""
    subs = {}
    for r in H._table(zf, "SUBMISSION"):
        if (r.get("SUBMISSIONTYPE") or "").upper() != "13F-HR":
            continue
        subs[r["ACCESSION_NUMBER"]] = (str(r.get("CIK") or "").lstrip("0"), _iso(r.get("PERIODOFREPORT")),
                                       _iso(r.get("FILING_DATE")))
    names = {}
    for r in H._table(zf, "COVERPAGE"):
        a = r.get("ACCESSION_NUMBER")
        if a in subs:
            if "NOTICE" in (r.get("REPORTTYPE") or "").upper():
                subs.pop(a, None)
                continue
            names[a] = (r.get("FILINGMANAGER_NAME") or "").strip()
    best = {}
    for a, (cik, per, fd) in subs.items():
        k = (cik, per)
        if per and fd and (k not in best or fd > best[k][1]):
            best[k] = (a, fd)
    return {a: (names.get(a, ""), cik, per, fd) for (cik, per), (a, fd) in best.items()}


def read_13f(path, name_map, issuer_cache, rules_cfg, api_key="", budget_s=600, log=print, figi=None):
    """Conviction rows of one data set. name_map: {cik: {'ticker', 'name', 'other_tickers'}} of panel companies."""
    with zipfile.ZipFile(path) as zf:
        meta = filings_13f(zf)
        accns = {a: (n, c) for a, (n, c, _, _) in meta.items()}
        unit = {a: (1.0 if (fd or "") >= DOLLARS_FROM else 1000.0) for a, (_, _, _, fd) in meta.items()}
        npos = {}
        by_cusip, by_acc, names = H.scan_values(zf, accns, npos)
        if not by_acc:
            return [], 0
        f = max(unit.values()) if unit else 1.0
        by_cusip = {k: v * f for k, v in by_cusip.items()}
        cusip_cik, remaining = H.map_issuers(names, by_cusip, name_map, issuer_cache, api_key=api_key,
                                             budget_s=budget_s, log=log, figi=figi)
        pos = H.positions(zf, accns, cusip_cik)
    rows = []
    for cik, accs in pos.items():
        for a, (v, _sh) in accs.items():
            name, fc, per, fd = meta[a]
            total = by_acc.get(a, 0) * unit[a]
            if total < R.FUND_MIN_AUM or not total:
                continue
            w = v * unit[a] / total
            if w < R.FUND_MIN_WEIGHT:
                continue
            if npos.get(a, 0) > R.FUND_MAX_POSITIONS or H.is_excluded(name, [name, total, npos.get(a, 0)], rules_cfg):
                continue
            rows.append([fc, H.clean_manager(name), per, fd, str(cik), round(w, 4)])
    return rows, remaining


def update_13f(client, name_map, cfg, since, today, log=print, budget_s=900, max_sets=12):
    """Read every 13F data set whose filing window ends on or after `since` and isn't stored yet (oldest first,
    at most max_sets per run). Returns the number read."""
    P.ensure(P.OWNERS)
    rules_cfg = (cfg.get("portal") or {}).get("holders") or {}
    cache = cache_read(H.MAP_PATH) or {}
    api_key = os.environ.get("OPENFIGI_API_KEY", "").strip()
    n = 0
    for url, sp in sorted(links_13f(client, today), key=lambda x: x[1][1]):
        if sp[1] < since:
            continue
        out = os.path.join(P.OWNERS, url.rsplit("/", 1)[-1].replace(".zip", ".json.gz"))
        old = read_json(out)
        if old and not old.get("unmapped"):
            continue
        if n >= max_sets:
            break
        tmp = os.path.join(P.OWNERS, "_cur.zip")
        blob = H._fetch(client, url, timeout=900)
        if not blob:
            log(f"  13F {url.rsplit('/', 1)[-1]}: not available")
            continue
        with open(tmp, "wb") as fh:
            fh.write(blob)
        rows, rem = read_13f(tmp, name_map, cache, rules_cfg, api_key=api_key, budget_s=budget_s, log=log)
        os.remove(tmp)
        cache_write(H.MAP_PATH, cache)
        write_json(out, {"url": url, "span": sp, "rows": rows, "unmapped": rem})
        n += 1
        log(f"  13F {url.rsplit('/', 1)[-1]}: {len(rows)} conviction positions"
            + (f"; {rem} issuers still to map" if rem else ""))
    return n


def load_13f():
    """(rows, covered-through day): all stored conviction rows, and the last filing day covered without a gap."""
    if not os.path.isdir(P.OWNERS):
        return [], None
    rows, spans = [], []
    for f in sorted(os.listdir(P.OWNERS)):
        if f.endswith(".json.gz") and not f.startswith("_"):
            x = read_json(os.path.join(P.OWNERS, f)) or {}
            rows += x.get("rows") or []
            if x.get("span"):
                spans.append(tuple(x["span"]))
    through = None
    for a, b in sorted(spans):
        if through is None or a <= _plus(through, 1):
            through = max(through or b, b)
        else:
            break
    return rows, through


def first_13f_day():
    spans = []
    for f in os.listdir(P.OWNERS) if os.path.isdir(P.OWNERS) else []:
        if f.endswith(".json.gz") and not f.startswith("_"):
            x = read_json(os.path.join(P.OWNERS, f)) or {}
            if x.get("span"):
                spans.append(x["span"][0])
    return min(spans) if spans else None


def _plus(d, n):
    from datetime import timedelta
    return (date.fromisoformat(d) + timedelta(days=n)).isoformat()


# ------------------------------------------------------------------ insiders
def read_insiders(zf, wanted):
    subs = {}
    for r in INS._table(zf, "SUBMISSION"):
        if (r.get("DOCUMENT_TYPE") or "").strip() not in ("4", "5"):
            continue
        try:
            ic = int((r.get("ISSUERCIK") or "0").strip() or 0)
        except ValueError:
            continue
        if ic in wanted:
            subs[r["ACCESSION_NUMBER"]] = (ic, (r.get("AFF10B5ONE") or "").strip() in ("1", "true", "TRUE", "Y"),
                                           _iso(r.get("FILING_DATE")))
    owners = {}
    for r in INS._table(zf, "REPORTINGOWNER"):
        a = r.get("ACCESSION_NUMBER")
        if a in subs and a not in owners:
            owners[a] = ((r.get("RPTOWNERNAME") or "").strip(),
                         INS._role(r.get("RPTOWNER_RELATIONSHIP"), r.get("RPTOWNER_TITLE")))
    exer, trades = set(), []
    for tbl in ("DERIV_TRANS", "NONDERIV_TRANS"):
        for r in INS._table(zf, tbl):
            a = r.get("ACCESSION_NUMBER")
            if a not in subs:
                continue
            code = (r.get("TRANS_CODE") or "").strip().upper()
            if code in ("M", "X", "C", "O"):
                exer.add((a, (r.get("TRANS_DATE") or "").strip().upper()))
            elif tbl == "NONDERIV_TRANS" and code in ("P", "S"):
                trades.append((a, code, r))
    out = defaultdict(list)
    for a, code, r in trades:
        sh, px = INS._num(r.get("TRANS_SHARES")), INS._num(r.get("TRANS_PRICEPERSHARE"))
        if sh <= 0 or px <= 0:
            continue
        ic, plan, fd = subs[a]
        who, role = owners.get(a, ("", ""))
        td = _iso(r.get("TRANS_DATE")) or fd
        side = "P" if code == "P" else ("Splan" if plan else "Sex" if (a, (r.get("TRANS_DATE") or "").strip().upper())
                                        in exer else "S")
        out[str(ic)].append([td, fd, side, round(sh * px), who.title() if who.isupper() else who, role])
    return dict(out)


def update_insiders(client, wanted, since, today, log=print, max_sets=16):
    P.ensure(P.INSIDERS)
    n = 0
    for q, urls in links_ins(client, today):
        y, qq = int(q[:4]), int(q[5])
        end = f"{y}-{3 * qq:02d}-{[31, 30, 30, 31][qq - 1]}"
        if end < since:
            continue
        out = os.path.join(P.INSIDERS, f"{q}.json.gz")
        if os.path.exists(out):
            continue
        if n >= max_sets:
            break
        blob = None
        for url in urls:
            blob = INS._fetch(client, url)
            if blob:
                break
        if not blob:
            continue
        with zipfile.ZipFile(io.BytesIO(blob)) as zf:
            got = read_insiders(zf, wanted)
        write_json(out, {"q": q, "end": end, "by_cik": got})
        n += 1
        log(f"  insiders {q}: trades for {len(got)} companies")
    return n


def load_insiders():
    """({cik: [trades]}, covered-through day)."""
    if not os.path.isdir(P.INSIDERS):
        return {}, None
    by, ends = defaultdict(list), []
    for f in sorted(os.listdir(P.INSIDERS)):
        if f.endswith(".json.gz"):
            x = read_json(os.path.join(P.INSIDERS, f)) or {}
            for c, ts in (x.get("by_cik") or {}).items():
                by[c] += ts
            ends.append(x.get("end"))
    return dict(by), (max(e for e in ends if e) if ends else None)


# ------------------------------------------------------------------ insiders not yet in a data set (recent events)
def live_insiders(client, cik, d0, d1, log=print):
    """Open-market trades in Form 4s filed in [d0, d1], read filing by filing from EDGAR (the quarterly data sets
    lag by up to a quarter). Same rows as read_insiders. Cached per company and window."""
    import xml.etree.ElementTree as ET
    from qs.sec import SUBMISSIONS_URL, NotFound, doc_url
    path = os.path.join(P.INSIDERS, "live", f"{cik}_{d0}_{d1}.json.gz")
    hit = read_json(path)
    if hit is not None:
        return hit["rows"]
    try:
        sub = client.get_json(SUBMISSIONS_URL.format(cik=int(cik)))
    except NotFound:
        return []
    rec = (sub.get("filings") or {}).get("recent") or {}
    rows = []
    for form, fd, accn, doc in zip(rec.get("form", []), rec.get("filingDate", []), rec.get("accessionNumber", []),
                                   rec.get("primaryDocument", [])):
        if form != "4" or not (d0 <= fd <= d1):
            continue
        xml_doc = doc.split("/")[-1]
        try:
            b = client.get_bytes(doc_url(cik, accn, xml_doc))
            x = ET.fromstring(b)
        except Exception:  # noqa: BLE001 - one unreadable filing doesn't stop the rest
            continue
        if (x.findtext("issuer/issuerCik") or "").lstrip("0") != str(int(cik)):
            continue
        who = x.findtext("reportingOwner/reportingOwnerId/rptOwnerName") or ""
        rel = x.find("reportingOwner/reportingOwnerRelationship")
        role = ""
        if rel is not None:
            role = (rel.findtext("officerTitle") or "").strip()[:40] or \
                ("Director" if (rel.findtext("isDirector") or "").strip() in ("1", "true") else
                 "10% owner" if (rel.findtext("isTenPercentOwner") or "").strip() in ("1", "true") else "Officer")
        plan = (x.findtext("aff10b5One") or "").strip().lower() in ("1", "true")
        ex_days = {(t.findtext("transactionDate/value") or "")[:10] for t in x.iter("derivativeTransaction")
                   if (t.findtext("transactionCoding/transactionCode") or "") in ("M", "X", "C", "O")}
        for t in x.iter("nonDerivativeTransaction"):
            code = t.findtext("transactionCoding/transactionCode")
            if code not in ("P", "S"):
                continue
            try:
                v = float(t.findtext("transactionAmounts/transactionShares/value") or 0) * \
                    float(t.findtext("transactionAmounts/transactionPricePerShare/value") or 0)
            except ValueError:
                continue
            if v <= 0:
                continue
            td = (t.findtext("transactionDate/value") or fd)[:10]
            side = "P" if code == "P" else "Splan" if plan else "Sex" if td in ex_days else "S"
            rows.append([td, fd, side, round(v), who.title() if who.isupper() else who, role])
    P.ensure(os.path.join(P.INSIDERS, "live"))
    write_json(path, {"rows": rows})
    return rows
