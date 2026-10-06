"""Web portal support: keep the screen state between runs, re-price it daily, and export the (encrypted)
data files the static site in site/ reads.

  state  (cache/state/state.json.gz)  - every screened company's metrics ('ctx') and which screens it belongs to,
                                        written by the 15-day screen run, re-priced by the daily job
  site/data/*.bin                      - gzip'd JSON, AES-GCM encrypted with a key derived from PORTAL_PASSWORD
                                        (PBKDF2-SHA256); the browser decrypts with the same password
"""
import base64
import gzip
import json
import math
import os
import statistics
from collections import Counter, defaultdict
from datetime import date, datetime

from . import __version__
from .config import CACHE_DIR, ROOT
from .report import _fmt_val
from .screens import BY_ID, SCREENS

STATE_PATH = os.path.join(CACHE_DIR, "state", "state.json.gz")
SITE_DATA = os.path.join(ROOT, "site", "data")
PBKDF2_ITER = 250000

# price-dependent fields written by valuation.value() - cleared before every re-pricing
VAL_KEYS = ("price", "price_date", "price_open", "price_source", "market_cap_usd", "ev_usd", "val_ok", "val_issue",
            "shares_used", "shares_source", "adv_usd", "listing_type", "mcap_to_public_float", "float_check",
            "ev_ebit", "ev_ebitda", "ev_sales", "pe", "earnings_yield", "fcf_yield", "ev_normalized_ebit",
            "ev_incl_lt_investments_usd", "ev_to_liquid_assets", "mcap_to_liquid_assets")

# metric: (label, format, which direction is better[, True = only positive values are meaningful, e.g. P/E])
METRICS = {
    "pe": ("P/E", "x", "low", True),
    "ev_ebitda": ("EV/EBITDA", "x", "low", True),
    "ev_ebit": ("EV/EBIT", "x", "low", True),
    "ev_sales": ("EV/Sales", "x", "low", True),
    "ev_normalized_ebit": ("EV / avg EBIT", "x", "low", True),
    "ev_to_liquid_assets": ("EV / cash", "x", "low"),
    "fcf_yield": ("FCF yield", "pct", "high"),
    "roic_median": ("ROIC (10y median)", "pct", "high"),
    "roic_latest": ("ROIC (latest)", "pct", "high"),
    "revenue_cagr": ("Sales growth /yr", "pct", "high"),
    "revenue_cagr_3y": ("Sales growth /yr (3y)", "pct", "high"),
    "gross_margin_latest": ("Gross margin", "pct", "high"),
    "ttm_operating_margin": ("Op. margin (TTM)", "pct", "high"),
    "operating_margin_median": ("Op. margin (10y median)", "pct", "high"),
    "net_debt_to_ebitda": ("Net debt / EBITDA", "x", "low"),
    "net_debt_to_norm_ebitda": ("Net debt / avg EBITDA", "x", "low"),
    "op_margin_percentile_10y": ("Margin in own 10y range", "pct", "low"),
    "cash_runway_years": ("Cash runway (years)", "yrs", "high"),
    "debt_to_liquid_assets": ("Debt / cash", "x", "low"),
    "market_cap_usd": ("Market cap", "usd", None),
    "ttm_revenue_usd": ("Revenue (TTM)", "usd", None),
}
PRICE_METRICS = {"pe", "ev_ebitda", "ev_ebit", "ev_sales", "ev_normalized_ebit", "ev_to_liquid_assets", "fcf_yield",
                 "market_cap_usd"}
SCREEN_METRICS = {
    "core": ["pe", "ev_ebitda", "fcf_yield", "roic_median", "revenue_cagr", "gross_margin_latest"],
    "emerging": ["ev_ebitda", "pe", "ev_sales", "roic_latest", "revenue_cagr_3y", "gross_margin_latest"],
    "special": ["ev_ebit", "pe", "ev_ebitda", "fcf_yield", "roic_latest", "ttm_operating_margin"],
    "fortress": ["pe", "ev_ebitda", "fcf_yield", "roic_median", "operating_margin_median", "net_debt_to_ebitda"],
    "hc_commercial": ["pe", "ev_ebitda", "fcf_yield", "roic_median", "gross_margin_latest", "revenue_cagr"],
    "hc_clinical": ["ev_to_liquid_assets", "market_cap_usd", "cash_runway_years", "debt_to_liquid_assets",
                    "ttm_revenue_usd"],
    "cyclicals": ["ev_normalized_ebit", "ev_ebit", "pe", "roic_median", "op_margin_percentile_10y",
                  "net_debt_to_norm_ebitda"],
}
WARNING_LABELS = {"margin_collapse": "Margins haven't collapsed",
                  "revenue_shrinking": "Revenue isn't shrinking",
                  "lost_money_2009": "No loss in 2008-09 on falling sales"}
STATUS_KEEP = ("PASS", "CHECK", "NEAR", "PRICE", "ONE")


# ------------------------------------------------------------------ json helpers
def _jsonable(o):
    try:
        import numpy as np
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
    except ImportError:  # pragma: no cover
        pass
    if isinstance(o, (set, frozenset)):
        return sorted(o)
    if isinstance(o, (date, datetime)):
        return o.isoformat()
    return str(o)


def _clean(x):
    """NaN/inf -> None (browsers' JSON.parse rejects NaN)."""
    if isinstance(x, float):
        return x if math.isfinite(x) else None
    if isinstance(x, dict):
        return {k: _clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_clean(v) for v in x]
    return x


def write_gz_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        json.dump(obj, f, default=_jsonable)
    os.replace(tmp, path)


def read_gz_json(path):
    try:
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError, EOFError):
        return None


# ------------------------------------------------------------------ state
def classes_of(results):
    return {sid: {str(c): r["class"] for c, r in res.items()} for sid, res in results.items()}


def save_state(results, ctxs, records, run_info, today, path=STATE_PATH):
    state = {
        "version": 1, "screener_version": __version__, "screened_on": today.isoformat(),
        "priced_on": today.isoformat(), "run_info": run_info,
        "ctxs": {str(c): ctx for c, ctx in ctxs.items()},
        "membership": {sid: {str(c): r.get("universe_note", "") for c, r in res.items()}
                       for sid, res in results.items()},
        "classes": classes_of(results),
        "records": {str(c): {k: rec.get(k) for k in ("ticker", "name", "exchange", "sic", "industry", "stage")}
                    for c, rec in records.items()},
    }
    write_gz_json(path, state)
    return state


def load_state(path=STATE_PATH):
    return read_gz_json(path)


def evaluate_state(state, cfg):
    """Apply every screen to the stored companies (same code path as the screen run)."""
    results = {}
    ctxs = state["ctxs"]
    for sid, mem in state["membership"].items():
        s = BY_ID[sid]
        res = {}
        for c, note in mem.items():
            ctx = ctxs.get(c)
            if ctx is None:
                continue
            r = s.evaluate(ctx, cfg, priced=True)
            r["universe_note"] = note
            res[c] = r
        results[sid] = res
    return results


def reprice(state, prices, cfg, today, log=print):
    """Daily job: new end-of-day prices for every stored company, then re-apply the screens."""
    from .prices import td_symbol
    from .valuation import value
    ctxs = state["ctxs"]
    last = {}
    for c, ctx in ctxs.items():
        if ctx.get("price") and ctx.get("price_date"):
            adv = ctx.get("adv_usd")
            last[c] = {"ok": True, "reason": "", "symbol": ctx["ticker"], "name": None, "price": ctx["price"],
                       "open": ctx.get("price_open"), "price_date": ctx["price_date"],
                       "avg_volume": (adv / ctx["price"]) if adv else None, "listing_type": ctx.get("listing_type"),
                       "source": (ctx.get("price_source") or "").replace(" (last known)", "") + " (last known)"}
        for k in list(ctx):
            if k in VAL_KEYS or k.endswith("_unverified"):
                del ctx[k]
    order = sorted(ctxs, key=lambda c: -(ctxs[c].get("latest_revenue_usd") or 0))
    quotes = prices.quotes([(ctxs[c]["ticker"], ctxs[c].get("exchange")) for c in order])
    stale_days = cfg.get("price_max_staleness_days", 7)
    kept = 0
    for c in order:
        q = quotes.get(ctxs[c]["ticker"])
        old = last.get(c)
        if (not q or not q.get("ok")) and old:
            try:
                age = (today - date.fromisoformat(old["price_date"])).days
            except ValueError:
                age = 999
            if age <= stale_days:
                quotes[ctxs[c]["ticker"]] = old     # no new quote today: keep the last good one (up to 7 days)
                kept += 1
    if kept:
        log(f"  {kept} companies keep their last known price (no new quote today)")
    currencies = {ctx.get("currency") for ctx in ctxs.values() if ctx.get("currency")}
    static = {k: v for k, v in (cfg.get("fx_to_usd") or {}).items() if isinstance(v, (int, float))}
    fx = prices.fx_rates(currencies, static)
    foreign = any(str(ctx.get("latest_annual_form") or "").startswith("20-F") for ctx in ctxs.values())
    types = prices.instrument_types() if foreign else {}
    for c in order:
        ctx = ctxs[c]
        rate = (fx.get(ctx.get("currency")) or (ctx.get("fx_rate"), None))[0]
        info = {"all_tickers": ctx.get("all_tickers") or [ctx["ticker"]], "name": ctx.get("name"),
                "latest_annual": {"form": ctx.get("latest_annual_form")}}
        ctx.update(value(ctx, info, quotes.get(ctx["ticker"]), rate, today, td=prices,
                         listing_type=types.get(td_symbol(ctx["ticker"]))))
    results = evaluate_state(state, cfg)
    state["classes"] = classes_of(results)
    state["priced_on"] = today.isoformat()
    log(f"Re-priced {sum(1 for c in ctxs.values() if c.get('price'))}/{len(ctxs)} companies")
    return results


# ------------------------------------------------------------------ peers
def _sic(ctx):
    s = str(ctx.get("sic") or "").strip()
    return s if s.isdigit() and len(s) >= 2 else None


def metric_value(ctx, k):
    """(value, verified?) - doubtful market-cap based figures are kept for display only."""
    v = ctx.get(k)
    if v is None and ctx.get(k + "_unverified") is not None:
        return ctx[k + "_unverified"], False
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
        return None, True
    return v, True


def peer_groups(ctxs, min_size=6):
    """Peers = companies with the same 4-digit SIC code; if fewer than min_size, the 3-digit group, then 2-digit.
    Returns ({group_id: group}, {cik: group_id}). Medians use verified values only (multiples: positive only)."""
    lv = {4: defaultdict(list), 3: defaultdict(list), 2: defaultdict(list)}
    for c, ctx in ctxs.items():
        s = _sic(ctx)
        if not s or ctx.get("events_only"):
            continue
        for n in (4, 3, 2):
            lv[n][s[:n]].append(c)
    assign, groups = {}, {}
    for c, ctx in ctxs.items():
        s = _sic(ctx)
        if not s or ctx.get("events_only"):
            continue
        for n in (4, 3, 2):
            members = lv[n][s[:n]]
            if len(members) >= min_size:
                gid = f"{n}:{s[:n]}"
                assign[c] = gid
                if gid not in groups:
                    groups[gid] = members
                break
    out = {}
    for gid, members in groups.items():
        n, code = gid.split(":")
        names = Counter((ctxs[m].get("industry") or "").strip() for m in members if ctxs[m].get("industry"))
        top = names.most_common(1)[0][0].title() if names else "Industry"
        label = top if n == "4" else f"Broader industry group SIC {code}{'x' * (4 - int(n))} (most common: {top})"
        med = {}
        for k, spec in METRICS.items():
            pos_only = len(spec) > 3 and spec[3]
            vals = []
            for m in members:
                v, ok = metric_value(ctxs[m], k)
                if v is None or not ok:
                    continue
                if pos_only and v <= 0:
                    continue
                vals.append(v)
            if len(vals) >= 3:
                med[k] = statistics.median(vals)
        big = sorted(members, key=lambda m: -(ctxs[m].get("latest_revenue_usd") or 0))[:8]
        out[gid] = {"label": label, "sic": code, "n": len(members), "med": med,
                    "top": [[ctxs[m]["ticker"], ctxs[m].get("name")] for m in big]}
    return out, assign


# ------------------------------------------------------------------ export
def _op_text(op):
    return {">=": "at least", "<=": "at most", ">": "above", "<": "below"}.get(op, op or "")


RULE_UNITS = {"years_with_data": " years of data", "years_total": " years of data",
              "years_since_latest_fy": " years since the last annual report",
              "operating_loss_years": " year(s) with an operating loss", "operating_loss_years_5y":
              " loss year(s) in the last 5", "positive_ebit_years": " profitable years of the last 10",
              "bs_age_days": " days old", "fcf_conversion": " (free cash flow / net income)",
              "net_debt_to_ocf": " (net debt / operating cash flow)",
              "net_debt_to_ebitda": " (net debt / EBITDA)", "net_debt_to_norm_ebitda": " (net debt / cycle-average EBITDA)",
              "interest_coverage": " (EBIT / interest)", "cash_runway_years": " years of cash",
              "debt_to_liquid_assets": " (debt / cash)", "ev_to_liquid_assets": " (EV / cash)",
              "ev_ebitda": " EV/EBITDA", "ev_ebit": " EV/EBIT", "ev_normalized_ebit": " EV / cycle-average EBIT",
              "roic_median": " ROIC, 10-year median", "roic_share_above_floor": " of years with ROIC above 10%",
              "revenue_cagr": " revenue growth a year", "revenue_cagr_3y": " revenue growth a year (3 years)",
              "share_count_cagr_3y": " share-count growth a year", "gross_margin_latest": " gross margin",
              "operating_margin_std": " swing in operating margin (std. dev.)",
              "op_margin_percentile_10y": " of its own 10-year margin range", "market_cap_usd": " market cap",
              "latest_revenue_usd": " revenue", "adv_usd": " traded a day",
              "gross_margin_change_2021_2023": " change in margin 2021-23"}


def _thr_text(thr, fmt):
    if isinstance(thr, (int, float)) and not isinstance(thr, bool):
        if fmt == "mult":
            return f"{thr:.1f}\u00d7" if thr < 100 else f"{thr:.0f}\u00d7"
        if fmt == "years":
            return f"{thr:.1f}"
        if fmt == "pct":
            return f"{thr:.0%}" if abs(thr * 100 - round(thr * 100)) < 1e-9 else f"{thr:.1%}"
    return _fmt_val(thr, fmt)


def rule_label(g, cfg, sid):
    if g.desc:
        return g.desc(cfg, sid) if callable(g.desc) else g.desc
    try:
        thr = g.threshold(cfg, sid)
    except (KeyError, TypeError):
        thr = None
    if thr is None or not g.op:
        return g.name
    unit = RULE_UNITS.get(g.metric, "")
    if g.metric == "ev_ebitda" and g.fmt == "mult":
        unit = " EV/EBITDA"
    return f"{_op_text(g.op)} {_thr_text(thr, g.fmt)}{unit}"


GATE_CODE = {"PASS": "P", "FAIL": "F", "NO DATA": "D", "N/A": "N", "PENDING": "D"}


def screen_payload(s, results, ctxs, cfg):
    gates = [{"id": g.gid, "name": g.name, "rule": rule_label(g, cfg, s.sid), "why": g.insight,
              "hard": not g.one_ok, "valuation": bool(g.valuation), "price": bool(g.needs_price)} for g in s.gates]
    warnings = [{"id": "W:" + w, "name": WARNING_LABELS[w]} for w in s.warnings]
    rows = []
    for c, r in results.items():
        ctx = ctxs[c]
        codes, vals, notes = [], [], {}
        for g in s.gates:
            st, val, thr, note = r["gates"][g.gid]
            codes.append(GATE_CODE.get(st, "D"))
            vals.append("" if val is None else _fmt_val(val, g.fmt))
            if note:
                notes[g.gid] = note
        warn_ids = ["W:" + w for w in s.warnings if ctx.get("warn_" + w)]
        warn_txt = {"W:" + w: ctx["warn_" + w] for w in s.warnings if ctx.get("warn_" + w)}
        holds = [h for h in r.get("holds", []) if h not in warn_txt.values()]
        rows.append({"c": c, "g": "".join(codes), "v": vals, "nt": notes, "h": holds, "w": warn_ids,
                     "wt": warn_txt, "cls": r["class"], "un": r.get("universe_note") or "",
                     "nr": r["failed"][0] if r["class"] == "NEAR" and r.get("failed") else None})
    return {"id": s.sid, "title": s.title, "purpose": s.purpose, "sources": s.sources, "review": s.rubric,
            "gates": gates, "warnings": warnings, "metrics": SCREEN_METRICS.get(s.sid, []), "rows": rows}


def company_payload(c, ctx, summaries, group_id):
    m, unverified = {}, []
    for k in METRICS:
        v, ok = metric_value(ctx, k)
        if v is not None:
            m[k] = v
            if not ok:
                unverified.append(k)
    s = summaries.get(c) or {}
    ev = None
    if ctx.get("event_types"):
        ev = {"types": ctx.get("event_types"), "date": ctx.get("event_date"), "url": ctx.get("event_filing_url")}
    return {"t": ctx["ticker"], "n": ctx.get("name"), "ex": ctx.get("exchange"), "sic": ctx.get("sic"),
            "ind": ctx.get("industry"), "cur": ctx.get("currency"),
            "px": {"o": ctx.get("price_open"), "c": ctx.get("price"), "d": ctx.get("price_date"),
                   "src": ctx.get("price_source")} if ctx.get("price") is not None else None,
            "m": m, "mu": unverified, "vi": ctx.get("val_issue") or "", "pg": group_id,
            "sum": s.get("text"), "sumsrc": s.get("source"), "url": ctx.get("latest_annual_url"),
            "fy": ctx.get("latest_fy"), "flags": ctx.get("flags") or [], "ev": ev,
            "other": ctx.get("other_tickers") or ""}


SALT_PATH = os.path.join(ROOT, "data", "portal_salt.json")


class Sealer:
    """gzip + AES-256-GCM. Key = PBKDF2-SHA256(password, salt). The salt is kept in data/portal_salt.json (public
    by design; committed so 'remember on this device' survives daily rebuilds). Without a password, files are only
    gzip'd (local testing only - export refuses that unless asked)."""

    def __init__(self, password, salt_path=SALT_PATH):
        self.password = password or ""
        info = {}
        if os.path.exists(salt_path):
            try:
                with open(salt_path, encoding="utf-8") as f:
                    info = json.load(f)
            except (OSError, ValueError):
                info = {}
        if self.password:
            if info.get("salt"):
                salt = base64.b64decode(info["salt"])
            else:
                salt = os.urandom(16)
                os.makedirs(os.path.dirname(salt_path), exist_ok=True)
                with open(salt_path, "w", encoding="utf-8") as f:
                    json.dump({"salt": base64.b64encode(salt).decode(), "_note": "public salt for the portal key"}, f)
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=PBKDF2_ITER)
            self.key = kdf.derive(self.password.encode("utf-8"))
            self.info = {"plain": False, "salt": base64.b64encode(salt).decode(), "iter": PBKDF2_ITER,
                         "kdf": "PBKDF2-SHA256", "cipher": "AES-256-GCM"}
        else:
            self.key = None
            self.info = {"plain": True}

    def seal(self, obj):
        raw = gzip.compress(json.dumps(_clean(obj), default=_jsonable, separators=(",", ":")).encode("utf-8"), 9,
                            mtime=0)
        if self.key is None:
            return raw
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        nonce = os.urandom(12)
        return nonce + AESGCM(self.key).encrypt(nonce, raw, None)

    def open(self, blob):
        if self.key is None:
            return json.loads(gzip.decompress(blob))
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        return json.loads(gzip.decompress(AESGCM(self.key).decrypt(blob[:12], blob[12:], None)))


def _write_bytes(path, b):
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(b)
    os.replace(tmp, path)


def export_site(state, results, cfg, summaries, password, out_dir=SITE_DATA, today=None, log=print,
                allow_plain=False, salt_path=SALT_PATH):
    today = today or date.today()
    if not password and not allow_plain:
        raise SystemExit("PORTAL_PASSWORD is not set - refusing to publish unencrypted data.")
    os.makedirs(out_dir, exist_ok=True)
    keyinfo_path = os.path.join(out_dir, "keyinfo.json")
    sealer = Sealer(password, salt_path)
    ctxs = state["ctxs"]
    groups, assign = peer_groups(ctxs, int((cfg.get("portal") or {}).get("peer_min_companies", 6)))
    shown = set()
    for res in results.values():
        shown.update(res)
    companies = {c: company_payload(c, ctxs[c], summaries, assign.get(c)) for c in shown}
    files = {}
    counts = {}
    for s in SCREENS:
        if s.sid not in results:
            continue
        p = screen_payload(s, results[s.sid], ctxs, cfg)
        files[f"screen_{s.sid}"] = p
        counts[s.sid] = {k: sum(1 for r in p["rows"] if r["cls"] == k) for k in ("PASS", "CHECK", "NEAR", "PRICE", "ONE")}
        counts[s.sid]["universe"] = len(p["rows"])
    files["companies"] = {"companies": companies, "peers": groups, "metrics": METRICS}
    gaps = []
    for c, rec in (state.get("records") or {}).items():
        st = rec.get("stage") or ""
        if st == "screened" or st.startswith("not screened: ") and "check by hand" not in st:
            continue
        if c in ctxs and not ctxs[c].get("events_only"):
            continue
        gaps.append({"t": rec.get("ticker"), "n": rec.get("name"), "ind": rec.get("industry"), "why": st})
    excluded = Counter(rec.get("stage") for rec in (state.get("records") or {}).values()
                       if (rec.get("stage") or "").startswith("not screened: ") and "check by hand" not in rec["stage"])
    files["meta"] = {
        "version": __version__, "built": datetime.now().isoformat(timespec="minutes"),
        "screened_on": state.get("screened_on"), "priced_on": state.get("priced_on"),
        "price_day": max((c.get("price_date") or "" for c in ctxs.values()), default=None),
        "screens": [{"id": s.sid, "title": s.title, "counts": counts.get(s.sid, {})} for s in SCREENS if s.sid in counts],
        "universe": len(state.get("records") or {}), "screened": len(ctxs),
        "gaps": sorted(gaps, key=lambda g: str(g["t"])), "excluded": excluded.most_common(),
        "summaries": sum(1 for c in companies.values() if c.get("sum")), "companies": len(companies),
        "run_info": state.get("run_info") or {},
    }
    written = set()
    for name, obj in files.items():
        _write_bytes(os.path.join(out_dir, name + ".bin"), sealer.seal(obj))
        written.add(name + ".bin")
    info = dict(sealer.info, check=base64.b64encode(sealer.seal({"ok": True})).decode())
    with open(keyinfo_path + ".tmp", "w", encoding="utf-8") as f:
        json.dump(info, f)
    os.replace(keyinfo_path + ".tmp", keyinfo_path)
    for f in os.listdir(out_dir):
        if f.endswith(".bin") and f not in written:
            os.remove(os.path.join(out_dir, f))
    log(f"Portal data written to {out_dir}: {len(companies)} companies, {len(groups)} peer groups"
        + ("" if password else "  (NOT encrypted - no PORTAL_PASSWORD set)"))
    return files
