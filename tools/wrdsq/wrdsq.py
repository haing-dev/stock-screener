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
  tables    libraries:[..]                    table names in each library (metadata)
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

# WRDS Cloud allows 100 processes per user on the login node: numerical libraries must not start 64 threads
for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

VERSION = "1.0.4"
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


LIGHT = {"libraries", "search", "tables", "describe", "datasets", "delete", "export"}


def job(arg):
    spec = decode(arg)
    for d in (ROOT, DATA, JOBS, LOGS, EXPORT, LIB):
        os.makedirs(d, exist_ok=True)
    name = re.sub(r"[^A-Za-z0-9_-]", "_", spec.get("name", "job"))[:40]
    path = os.path.join(JOBS, "%s_%s.json" % (time.strftime("%Y%m%d-%H%M%S"), name))
    json.dump(spec, open(path, "w"), indent=1)
    log = os.path.join(LOGS, os.path.basename(path).replace(".json", ".txt"))
    me = os.path.join(ROOT, "wrdsq.py")
    light = all(st.get("do") in LIGHT for st in spec.get("steps", []))
    if spec.get("head_node"):
        execute(path)
        return
    msgs = []
    # 1) interactive compute node (streams the report)
    if shutil.which("qrsh"):
        err("wrdsq: asking WRDS for an interactive compute node ...")
        p = subprocess.run(["qrsh", "-now", "no", sys.executable, me, "_exec", path], stdout=sys.stdout,
                           stderr=subprocess.PIPE, universal_newlines=True)
        if os.path.exists(log):
            return
        msgs.append("qrsh: " + " ".join((p.stderr or "").split())[-250:])
    # 2) batch compute node (waits in the queue, then prints the report)
    if shutil.which("qsub"):
        err("wrdsq: interactive nodes busy -> submitting a batch job and waiting for it ...")
        p = subprocess.run(["qsub", "-sync", "y", "-b", "y", "-N", "wrdsq_" + name, "-o", log + ".out", "-e", log + ".err",
                            sys.executable, me, "_exec", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           universal_newlines=True)
        if os.path.exists(log):
            sys.stdout.write(open(log).read())
            return
        msgs.append("qsub: " + " ".join(((p.stdout or "") + " " + (p.stderr or "")).split())[-250:])
    # 3) light jobs (metadata, or aggregate SQL + small analysis marked head_ok) may use the login node
    if light or spec.get("head_ok"):
        err("wrdsq: no compute node available; light job, running it on the login node ...")
        execute(path)
        return
    print("=== WRDSQ: no WRDS compute node was available. Nothing ran. The runner will retry. (%s) ===" % " | ".join(msgs))


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


def _has(col, words):
    return " and ".join("position('%s' in lower(%s)) > 0" % (w, col) for w in words)


def s_search(db, st, R):
    libs = st.get("libraries") or sorted(db.list_libraries())
    inlist = ",".join("'%s'" % re.sub(r"[^A-Za-z0-9_]", "", l) for l in libs)
    for term in st["terms"]:
        words = [w for w in re.sub(r"[^A-Za-z0-9_ ]", "", term).lower().split() if w]
        if not words:
            continue
        R.w("-- '%s'" % term)
        lm = [l for l in libs if all(w in l.lower() for w in words)]
        if lm:
            R.w("   libraries: " + ", ".join(lm))
        q = ("select table_schema as s, table_name as t, string_agg(column_name, ',') as c, "
             "bool_or(%s) as tm from information_schema.columns where table_schema in (%s) and ((%s) or (%s)) "
             "group by 1,2 order by 4 desc, 1, 2 limit %d" % (_has("table_name", words), inlist,
                                                           _has("table_name", words), _has("column_name", words), MAX_LINES))
        try:
            df = _sql(db, q)
        except Exception as e:  # noqa: BLE001
            _rollback(db)
            R.w("   search failed: %s" % " ".join(str(e).split())[:200])
            continue
        if not len(df):
            R.w("   (no table or column names match)")
        for _, r in df.iterrows():
            cols = [c for c in str(r["c"]).split(",") if all(w in c.lower() for w in words)]
            R.w("   %s.%s%s" % (r["s"], r["t"], "" if r["tm"] else "  [columns: %s]" % ", ".join(cols[:8])))


def s_tables(db, st, R):
    for lib in st["libraries"]:
        try:
            tabs = sorted(db.list_tables(library=lib))
            R.w("%s (%d): %s" % (lib, len(tabs), ", ".join(tabs[:300]) + (" ..." if len(tabs) > 300 else "")))
        except Exception as e:  # noqa: BLE001
            _rollback(db)
            R.w("%s: cannot list (%s)" % (lib, " ".join(str(e).split())[:150]))


def _sql(db, q):
    """Run SQL with literal % allowed (escaped for the driver)."""
    import pandas as pd
    try:
        from sqlalchemy import text
        return pd.read_sql_query(text(q), db.connection)
    except ImportError:
        return db.raw_sql(q.replace("%", "%%"))


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
            r = _sql(db, "select min(%s) a, max(%s) b, count(*) n from %s.%s" % (c, c, lib, tab))
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
        return _sql(db, q)

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


STEPS = {"libraries": s_libraries, "search": s_search, "tables": s_tables, "describe": s_describe, "pull": s_pull,
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
