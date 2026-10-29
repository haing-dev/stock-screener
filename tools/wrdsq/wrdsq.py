#!/usr/bin/env python3
"""wrdsq - a small, reusable WRDS job runner that lives on WRDS Cloud (~/wrdsq/).

Why it exists: WRDS forbids loading WRDS Data into AI tools. So an AI assistant WRITES the job, the job RUNS here on
WRDS Cloud, the data STAYS here (~/wrdsq/data), and only metadata and analysis results go back.

Commands (run on WRDS Cloud):
  python3 ~/wrdsq.py install            one time: copies itself to ~/wrdsq/, saves the WRDS password in ~/.pgpass
  python3 ~/wrdsq/wrdsq.py job <CODE>   runs a job (CODE = base64(zlib(JSON)), made by the assistant) on a compute node
  python3 ~/wrdsq/wrdsq.py job @FILE    same, from a JSON file on WRDS Cloud
Report -> stdout (and ~/wrdsq/logs/). Progress -> stderr.

Job JSON: {"name": "short_name", "steps": [ {...}, ... ]}. Step types ("do"):
  libraries                                   accessible libraries
  search    terms:[..], libraries:[..]?       library / table / column names matching the terms (metadata)
  describe  table:"lib.tab", date:"col"?      columns and types; with date: min, max, row count
  pull      name, sql, date:"col"?            runs SQL, saves ~/wrdsq/data/<name>.csv.gz; reports rows/cols/size only
  python    code                              runs analysis code here; helpers: sql(q), load(name), save(name, df),
                                              out(*args) (= print), db, pd, np, DATA, LIB
                                              (~/wrdsq/lib is on sys.path: write helper modules there). Print RESULTS, never data rows.
  datasets                                    stored datasets and storage use (10 GB home quota)
  delete    names:[..]                        delete stored datasets
  export    names:[..]                        copy to ~/wrdsq/export/ for the USER to download to their own computer
"""
import base64
import contextlib
import gzip
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
import zlib

VERSION = "1.0.0"
HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "wrdsq")
DATA = os.path.join(ROOT, "data")
JOBS = os.path.join(ROOT, "jobs")
LOGS = os.path.join(ROOT, "logs")
EXPORT = os.path.join(ROOT, "export")
LIB = os.path.join(ROOT, "lib")          # reusable analysis modules (code only), importable from python steps
QUOTA_GB = 10.0
MAX_OUT = 60000          # characters of report per python step
MAX_LINES = 120          # lines per search term


def err(*a):
    print(*a, file=sys.stderr)
    sys.stderr.flush()


def ascii(s):
    return str(s).encode("ascii", "replace").decode("ascii")


def connect():
    import wrds
    return wrds.Connection(wrds_username=os.environ.get("USER") or None)


def used_gb():
    tot = 0
    for d, _, fs in os.walk(HOME):
        for f in fs:
            try:
                tot += os.path.getsize(os.path.join(d, f))
            except OSError:
                pass
    return tot / 1e9


# ------------------------------------------------------------------------------------------------ install
def install():
    for d in (ROOT, DATA, JOBS, LOGS, EXPORT, LIB):
        os.makedirs(d, exist_ok=True)
    me = os.path.abspath(__file__)
    dst = os.path.join(ROOT, "wrdsq.py")
    if me != dst:
        shutil.copy(me, dst)
    print("wrdsq %s installed in %s" % (VERSION, ROOT))
    pg = os.path.join(HOME, ".pgpass")
    if not os.path.exists(pg):
        print("Type your WRDS password once more so later jobs can run without asking.")
    db = connect()
    if not os.path.exists(pg):
        try:
            db.create_pgpass_file()
        except Exception as e:  # noqa: BLE001
            print("Could not create .pgpass (%s). Jobs will still work but may ask for the password." % e)
    n = len(db.list_libraries())
    db.close()
    print("Connection OK: %d libraries accessible. Storage used: %.2f GB of %.0f GB." % (n, used_gb(), QUOTA_GB))
    print("INSTALL DONE")


# ------------------------------------------------------------------------------------------------ job entry
def decode(arg):
    if arg.startswith("@"):
        return json.load(open(os.path.expanduser(arg[1:])))
    pad = "=" * (-len(arg) % 4)
    return json.loads(zlib.decompress(base64.urlsafe_b64decode(arg + pad)).decode("utf-8"))


def job(arg):
    spec = decode(arg)
    for d in (ROOT, DATA, JOBS, LOGS, EXPORT, LIB):
        os.makedirs(d, exist_ok=True)
    name = re.sub(r"[^A-Za-z0-9_-]", "_", spec.get("name", "job"))[:40]
    path = os.path.join(JOBS, "%s_%s.json" % (time.strftime("%Y%m%d-%H%M%S"), name))
    json.dump(spec, open(path, "w"), indent=1)
    if shutil.which("qrsh") and not spec.get("head_node"):
        err("wrdsq: waiting for a WRDS compute node ...")
        cmd = ["qrsh", "-now", "no", sys.executable, os.path.join(ROOT, "wrdsq.py"), "_exec", path]
        sys.exit(subprocess.call(cmd))
    execute(path)


# ------------------------------------------------------------------------------------------------ steps
class Report(object):
    def __init__(self, name):
        self.buf = io.StringIO()
        self.name = name

    def w(self, s=""):
        s = ascii(s)
        self.buf.write(s + "\n")
        print(s)
        sys.stdout.flush()


def s_libraries(db, st, R):
    libs = sorted(db.list_libraries())
    R.w("%d libraries: %s" % (len(libs), ", ".join(libs)))


def s_search(db, st, R):
    libs = st.get("libraries") or sorted(db.list_libraries())
    inlist = ",".join("'%s'" % re.sub(r"[^A-Za-z0-9_]", "", l) for l in libs)
    for term in st["terms"]:
        t = re.sub(r"[^A-Za-z0-9_ ]", "", term).strip().lower()
        if not t:
            continue
        like = "%" + t.replace(" ", "%") + "%"
        R.w("-- '%s'" % term)
        lm = [l for l in libs if t.replace(" ", "") in l.lower()]
        if lm:
            R.w("   libraries: " + ", ".join(lm))
        q = ("select table_schema as s, table_name as t, string_agg(column_name, ',') as c, "
             "bool_or(lower(table_name) like '%s') as tm from information_schema.columns "
             "where table_schema in (%s) and (lower(table_name) like '%s' or lower(column_name) like '%s') "
             "group by 1,2 order by 4 desc, 1, 2 limit %d" % (like, inlist, like, like, MAX_LINES))
        try:
            df = db.raw_sql(q)
        except Exception as e:  # noqa: BLE001
            _rollback(db)
            R.w("   search failed: %s" % " ".join(str(e).split())[:200])
            continue
        if not len(df):
            R.w("   (no table or column names match)")
        for _, r in df.iterrows():
            cols = [c for c in str(r["c"]).split(",") if t.replace(" ", "") in c.lower()]
            R.w("   %s.%s%s" % (r["s"], r["t"], "" if r["tm"] else "  [columns: %s]" % ", ".join(cols[:8])))


def s_describe(db, st, R):
    lib, tab = st["table"].split(".", 1)
    try:
        d = db.describe_table(library=lib, table=tab)
        R.w("%s: %d columns" % (st["table"], len(d)))
        R.w("   " + ", ".join("%s(%s)" % (r["name"], str(r.get("type", ""))[:12]) for _, r in d.iterrows()))
    except Exception as e:  # noqa: BLE001
        _rollback(db)
        R.w("%s: cannot describe (%s)" % (st["table"], " ".join(str(e).split())[:200]))
        return
    if st.get("date"):
        c = re.sub(r"[^A-Za-z0-9_]", "", st["date"])
        try:
            r = db.raw_sql("select min(%s) a, max(%s) b, count(*) n from %s.%s" % (c, c, lib, tab))
            R.w("   %s: %s .. %s, %s rows" % (c, r["a"].iloc[0], r["b"].iloc[0], r["n"].iloc[0]))
        except Exception as e:  # noqa: BLE001
            _rollback(db)
            R.w("   date range failed: %s" % " ".join(str(e).split())[:200])


def s_pull(db, st, R):
    import pandas as pd
    name = re.sub(r"[^A-Za-z0-9_-]", "_", st["name"])
    if used_gb() > QUOTA_GB * 0.9:
        R.w("pull %s refused: storage above 90%% of the 10 GB quota. Delete datasets first." % name)
        return
    path = os.path.join(DATA, name + ".csv.gz")
    tmp = path + ".part"
    rows, cols, t0 = 0, None, time.time()
    try:
        from sqlalchemy import text
        query = text(st["sql"])
    except Exception:  # noqa: BLE001
        query = st["sql"]
    dmin = dmax = None
    try:
        with gzip.open(tmp, "wt") as f:
            for ch in pd.read_sql_query(query, db.connection, chunksize=int(st.get("chunk", 250000))):
                ch.to_csv(f, index=False, header=(cols is None))
                cols = list(ch.columns)
                rows += len(ch)
                dc = st.get("date")
                if dc and dc in ch and len(ch):
                    lo, hi = str(ch[dc].min()), str(ch[dc].max())
                    dmin = lo if dmin is None or lo < dmin else dmin
                    dmax = hi if dmax is None or hi > dmax else dmax
                err("  %s: %d rows ..." % (name, rows))
        os.replace(tmp, path)
    except Exception as e:  # noqa: BLE001
        _rollback(db)
        if os.path.exists(tmp):
            os.remove(tmp)
        R.w("pull %s FAILED: %s" % (name, " ".join(str(e).split())[:300]))
        return
    R.w("pull %s: %d rows x %d columns, %.1f MB, %.0f s%s" % (
        name, rows, len(cols or []), os.path.getsize(path) / 1e6, time.time() - t0,
        ", %s %s .. %s" % (st["date"], dmin, dmax) if dmin else ""))
    R.w("   columns: " + ", ".join(cols or []))


def s_python(db, st, R):
    import numpy as np
    import pandas as pd

    def load(name, **kw):
        return pd.read_csv(os.path.join(DATA, name + ".csv.gz"), **kw)

    def save(name, df):
        df.to_csv(os.path.join(DATA, re.sub(r"[^A-Za-z0-9_-]", "_", name) + ".csv.gz"), index=False)

    def sql(q):
        return db.raw_sql(q)

    if LIB not in sys.path:
        sys.path.insert(0, LIB)
    ns = {"db": db, "pd": pd, "np": np, "load": load, "save": save, "sql": sql, "DATA": DATA,
          "out": print, "LIB": LIB, "__name__": "wrdsq_step"}
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(st["code"], "<job:%s>" % R.name, "exec"), ns)
    except Exception:  # noqa: BLE001
        _rollback(db)
        buf.write("\nERROR:\n" + traceback.format_exc(limit=4))
    txt = buf.getvalue()
    if len(txt) > MAX_OUT:
        txt = txt[:MAX_OUT] + "\n[output cut at %d characters]" % MAX_OUT
    for line in txt.rstrip().split("\n"):
        R.w(line)


def s_datasets(db, st, R):
    fs = sorted(os.listdir(DATA)) if os.path.isdir(DATA) else []
    for f in fs:
        R.w("   %-40s %8.1f MB  %s" % (f, os.path.getsize(os.path.join(DATA, f)) / 1e6,
                                       time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(os.path.join(DATA, f))))))
    R.w("%d datasets; storage used %.2f GB of %.0f GB" % (len(fs), used_gb(), QUOTA_GB))


def s_delete(db, st, R):
    for n in st["names"]:
        p = os.path.join(DATA, re.sub(r"[^A-Za-z0-9_-]", "_", n) + ".csv.gz")
        if os.path.exists(p):
            os.remove(p)
            R.w("deleted " + n)
        else:
            R.w("not found " + n)


def s_export(db, st, R):
    for n in st["names"]:
        p = os.path.join(DATA, re.sub(r"[^A-Za-z0-9_-]", "_", n) + ".csv.gz")
        if os.path.exists(p):
            shutil.copy(p, EXPORT)
            R.w("ready for you to download: ~/wrdsq/export/%s.csv.gz" % n)
    R.w("To download (on your computer, PowerShell): scp %s@wrds-cloud.wharton.upenn.edu:~/wrdsq/export/* "
        "$HOME\\Downloads\\  -- keep these files on your own computer; do not upload them to AI tools."
        % os.environ.get("USER", "USERNAME"))


STEPS = {"libraries": s_libraries, "search": s_search, "describe": s_describe, "pull": s_pull,
         "python": s_python, "datasets": s_datasets, "delete": s_delete, "export": s_export}


def _rollback(db):
    try:
        db.connection.rollback()
    except Exception:  # noqa: BLE001
        pass


def execute(path):
    spec = json.load(open(path))
    R = Report(spec.get("name", "job"))
    R.w("=== WRDSQ REPORT v%s | job %s | %s | metadata and results only ===" % (
        VERSION, spec.get("name", "job"), time.strftime("%Y-%m-%d %H:%M")))
    t0 = time.time()
    try:
        db = connect()
    except Exception as e:  # noqa: BLE001
        R.w("CONNECTION FAILED: %s" % e)
        return
    for i, st in enumerate(spec.get("steps", []), 1):
        fn = STEPS.get(st.get("do"))
        R.w("\n## %d. %s%s" % (i, st.get("do"), (" " + st["title"]) if st.get("title") else ""))
        err("wrdsq: step %d/%d %s" % (i, len(spec["steps"]), st.get("do")))
        if not fn:
            R.w("unknown step type")
            continue
        try:
            fn(db, st, R)
        except Exception as e:  # noqa: BLE001
            _rollback(db)
            R.w("step failed: %s" % " ".join(str(e).split())[:300])
    db.close()
    R.w("\n=== END (%.0f s) ===" % (time.time() - t0))
    open(os.path.join(LOGS, os.path.basename(path).replace(".json", ".txt")), "w").write(R.buf.getvalue())


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help", "help"):
        print(__doc__)
    elif a[0] == "install":
        install()
    elif a[0] == "job" and len(a) > 1:
        job(a[1])
    elif a[0] == "_exec" and len(a) > 1:
        execute(a[1])
    elif a[0] == "version":
        print(VERSION)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
