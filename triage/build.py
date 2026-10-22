"""Put it together: events -> owners and insiders -> outcomes -> top performer owners -> calls -> statistics.

Output: cache/tri/out/<kind>.json.gz (scored events) and cache/tri/out/site.json (what the site shows).
Live calls: <record dir>/ledger.csv gets one row each time a recent event (month-end within 45 days) gets a call or
a new call, with the time of the build; the workflow pushes it to branch 'triage-record' (append-only), so the
record of calls made before their outcome was known can be checked later.
"""
import csv
import os
import time
from datetime import date, datetime, timezone

from qs.backtest_support import read_json, write_json

from . import __version__
from . import owners as OW
from . import panel as PN
from . import rules as R
from . import score as SC
from . import stats as SS
from .episodes import KINDS, Owners, Returns, detect, insider_view, plus, top_performers
from . import paths as P

LCOLS = ["called_utc", "kind", "id", "cik", "ticker", "name", "call", "score", "month_end", "entry_day"]


def _event_learning(ev, rets):
    """Outcome measured from the event's own entry (whatever the call), for ranking 13F filers."""
    p = rets.path(ev["cik"], ev["rec"].get("sym"), ev["i"])
    if p[0] is None or not p[1]:
        return None
    sims = []
    for c in ev.get("sim") or []:
        q = rets.path(c, (ev.get("sim_sym") or {}).get(c), ev["i"])
        if q[0] is not None and q[1]:
            sims.append(min(q[0][-1], SC.CAP))
    if not sims:
        return None
    return {"y": p[0][-1] - sum(sims) / len(sims), "abs": p[0][-1], "end": p[2]}


def build(months=None, grid=None, mark=None, opens=None, splits=None, divs=None, factors=None, client=None,
          record_dir=None, log=print, today=None):
    today = today or date.today().isoformat()
    months = months or PN.months()
    grid = grid or (read_json(PN.grid_path()) or [])
    e_of = {g["ym"]: g["e"] for g in grid}
    d_of = {g["ym"]: g["d"] for g in grid}
    months = [m for m in months if m in e_of]
    log(f"Triage build over {len(months)} months ({months[0] if months else '-'} .. {months[-1] if months else '-'})")
    events = detect(months, log=log)
    rets = Returns(months, e_of, mark=mark, opens=opens, splits=splits, divs=divs)
    rows, through = OW.load_13f()
    owners = Owners(rows, through, OW.first_13f_day())
    ins, ins_through = OW.load_insiders()
    log(f"  13F covered through {through or '-'} ({len(rows)} conviction positions); insider data sets through "
        f"{ins_through or '-'}")
    allev = []
    for kind in KINDS:
        for ev in events[kind]:
            c, d = str(ev["cik"]), ev["d"]
            ev["kind"] = kind
            ev["fund"] = owners.funds(c, d)
            trades = list(ins.get(c, []))
            covered = bool(ins_through and ins_through >= d)
            if not covered and client is not None and d >= plus(today, -120):
                lo = max(plus(ins_through, 1) if ins_through else plus(d, -R.INSIDER_DAYS), plus(d, -R.INSIDER_DAYS))
                try:
                    trades += OW.live_insiders(client, c, lo, d, log=log)
                    covered = True
                except Exception as e:  # noqa: BLE001 - leave it TBU and retry next run
                    log(f"  live Form 4s for {c}: {e}")
            ev["ins"] = insider_view(trades, d, ev["rec"].get("mc")) if covered else None
            ev["learn"] = _event_learning(ev, rets)
            if ev["learn"] and ev["fund"]:
                allev.append({"y": ev["learn"]["y"], "end": ev["learn"]["end"], "fund": ev["fund"], "cik": c})
    as_of = top_performers(allev)
    names = owners.names
    out = {"version": __version__, "updated": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
           "months": [months[0], months[-1]] if months else None, "mark": (mark or {}).get("day"),
           "rules": {"buy_at": R.BUY_AT, "avoid_at": R.AVOID_AT}, "kinds": {}}
    months_d = [d_of[m] for m in months]
    for kind in KINDS:
        items, series = [], {}
        idx_sym = R.INDEX[kind][0]
        for ev in events[kind]:
            f = ev.get("fund")
            if f:
                tops = as_of(ev["d"][:7] + "-01")
                ev["top"] = [(names.get(fc, fc), tops[fc][0], tops[fc][2], tops[fc][3]) for fc, *_ in f["list"] if fc in tops]
                ev["top_later"] = []
                for fc, nm, _w, fd in f["later"]:
                    t = as_of(fd[:7] + "-01").get(fc)
                    if t:
                        ev["top_later"].append((names.get(fc, nm), t[0], t[2], t[3], fd))
                ev["top_later"].sort(key=lambda t: t[4])
            item, _ = SC.evaluate(kind, ev, ins_through, months_d, rets, idx_sym)
            if item.get("no_entry"):
                continue
            ci = months_d.index(item["call_date"]) if item["call_date"] in months_d else ev["i"]
            if item["upgraded"]:
                ci = next((j for j, dd in enumerate(months_d) if dd >= item["call_date"]), ev["i"])
            series[item["id"]] = rets.series(ev["cik"], ev["rec"].get("sym"), ci, None)
            items.append(item)
        items.sort(key=lambda x: (x["date"], x["name"]), reverse=True)
        SC.write(kind, items)
        summ = SS.summary(kind, items, series, factors or {})
        k = R.KINDS[kind]
        out["kinds"][kind] = {"label": k["label"], "thesis": k["thesis"], "event": k["event"],
                              "backend": k["backend"], "cells": [[a, b, w] for a, b, w in k["cells"]],
                              "hard": [h[1] for h in k["hard"]], "index": R.INDEX[kind][1], "items": items, **summ}
        log(f"  {kind}: {len(items)} events, {sum(1 for x in items if x['played'])} with a full year, "
            + ", ".join(f"{v} {sum(1 for x in items if x['verdict'] == v)}" for v in ("overdone", "close", "justified", "tbu")))
    out["live"] = ledger(out, record_dir, today, log)
    now = as_of(today)
    out["top_performers"] = [[names.get(fc, fc), r_, h, n_, round(rate, 3)] for fc, (r_, sc, h, n_, rate, conc)
                             in sorted(now.items(), key=lambda t: t[1][0])]
    P.ensure(P.OUT)
    write_json(os.path.join(P.OUT, "site.json.gz"), out)
    return out


def ledger(out, record_dir, today, log=print):
    """Append new calls on recent events; return every row with its result so far (from the scored items)."""
    record_dir = record_dir or P.OUT
    os.makedirs(record_dir, exist_ok=True)
    path = os.path.join(record_dir, "ledger.csv")
    rows = list(csv.DictReader(open(path, encoding="utf-8"))) if os.path.exists(path) else []
    latest = {}
    for r in rows:
        latest[(r["kind"], r["id"])] = r["call"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    new = []
    for kind, kd in out["kinds"].items():
        for it in kd["items"]:
            if it["verdict"] not in ("overdone", "close", "justified") or it["date"] < plus(today, -45):
                continue
            if latest.get((kind, it["id"])) == it["verdict"]:
                continue
            new.append({"called_utc": now, "kind": kind, "id": it["id"], "cik": it["cik"], "ticker": it["ticker"],
                        "name": it["name"], "call": it["verdict"], "score": it["score"], "month_end": it["date"],
                        "entry_day": it.get("entry_date") or ""})
    if new or not os.path.exists(path):
        with open(path, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=LCOLS)
            if not rows:
                w.writeheader()
            w.writerows(new)
    by_id = {(k, it["id"]): it for k, kd in out["kinds"].items() for it in kd["items"]}
    res = []
    for r in rows + new:
        it = by_id.get((r["kind"], r["id"])) or {}
        res.append({**r, "ret": it.get("ret"), "ctrl_ret": it.get("ctrl_ret"), "idx_ret": it.get("idx_ret"),
                    "now": it.get("verdict")})
    log(f"  live calls: {len(rows)} before, {len(new)} new")
    return sorted(res, key=lambda r: r["called_utc"], reverse=True)
