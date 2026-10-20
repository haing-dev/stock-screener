"""Point-in-time views of SEC data for the backtest (validation/PROTOCOL.md section 2).

At a formation date d the screens may only see what had been filed before d:
  * facts_as_of(subset, d)     - companyfacts entries with filing date < d (restatements filed later are invisible;
                                 a restatement filed earlier replaces the original, as it did for an investor then)
  * filings_subset(main, pages) - every periodic and event filing of a company over its whole history (the bulk
                                 submissions file holds the older pages too)
  * info_as_of(filings, d)     - the company profile the live pipeline builds from submissions, rebuilt from the
                                 filings before d (latest annual report, first annual report, Special Situations
                                 events inside the event window)
"""
from datetime import date

from .extract import EVENT_FORMS, submissions_subset

PERIODIC_FORMS = {"10-K", "10-Q", "20-F", "40-F", "10-K/A", "10-Q/A", "20-F/A", "40-F/A", "10-KT", "10-KT/A"}
KEEP_FORMS = PERIODIC_FORMS | set(EVENT_FORMS)
PROFILE_KEYS = ("cik", "name", "entityType", "sic", "sicDescription", "tickers", "exchanges", "fiscalYearEnd",
                "category", "stateOfIncorporation")


def _iso(d):
    return d if isinstance(d, str) else d.isoformat()


def facts_as_of(subset, d):
    """A copy of a facts subset (extract.facts_subset) keeping only entries filed before d."""
    cut = _iso(d)
    out = {k: v for k, v in subset.items() if k != "facts"}
    facts = {}
    for tax, tags in (subset.get("facts") or {}).items():
        for tag, units in tags.items():
            for unit, ents in units.items():
                keep = [e for e in ents if (e.get("filed") or "9999") < cut]
                if keep:
                    facts.setdefault(tax, {}).setdefault(tag, {})[unit] = keep
    out["facts"] = facts
    return out


def last_filed(subset, d=None):
    """Latest filing date among the facts filed before d (None if nothing): a cache key for metrics at d."""
    cut = _iso(d) if d else "9999"
    best = ""
    for tags in (subset.get("facts") or {}).values():
        for units in tags.values():
            for ents in units.values():
                for e in ents:
                    f = e.get("filed") or ""
                    if best < f < cut:
                        best = f
    return best or None


def _rows(block):
    """SEC submissions 'recent'-style columns -> [form, filingDate, reportDate, accn, items, primaryDocument]."""
    forms = block.get("form") or []
    n = len(forms)

    def col(name):
        v = block.get(name) or []
        return v if len(v) == n else list(v) + [""] * (n - len(v))
    out = []
    for f, fd, rd, a, it, doc in zip(forms, col("filingDate"), col("reportDate"), col("accessionNumber"),
                                     col("items"), col("primaryDocument")):
        if f in KEEP_FORMS:
            out.append([f, fd or "", rd or "", a or "", it or "", doc or ""])
    return out


def filings_subset(main, pages=()):
    """main: a company's submissions JSON; pages: its older '-submissions-NNN' JSON pages (flat column blocks)."""
    rows = _rows((main.get("filings") or {}).get("recent") or {})
    for p in pages or ():
        rows += _rows(p)
    seen, uniq = set(), []
    for r in sorted(rows, key=lambda r: (r[1], r[3]), reverse=True):     # newest first, as SEC lists them
        if r[3] in seen:
            continue
        seen.add(r[3])
        uniq.append(r)
    prof = {k: main.get(k) for k in PROFILE_KEYS}
    prof["former_names"] = [f.get("name") for f in (main.get("formerNames") or []) if f.get("name")]
    return {"profile": prof, "filings": uniq}


def info_as_of(fsub, d):
    """The submissions_subset() profile as it would have looked on date d (filings before d only)."""
    cut = _iso(d)
    rows = [r for r in fsub.get("filings") or [] if r[1] and r[1] < cut]
    recent = {"form": [r[0] for r in rows], "filingDate": [r[1] for r in rows], "reportDate": [r[2] for r in rows],
              "accessionNumber": [r[3] for r in rows], "items": [r[4] for r in rows],
              "primaryDocument": [r[5] for r in rows]}
    prof = dict(fsub.get("profile") or {})
    sub = dict(prof)
    sub["formerNames"] = [{"name": n} for n in prof.get("former_names") or []]
    sub["filings"] = {"recent": recent, "files": []}       # the full history is here: no 'older pages' left
    dd = d if isinstance(d, date) else date.fromisoformat(cut)
    return submissions_subset(sub, today=dd)
