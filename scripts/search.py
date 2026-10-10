"""Search the store.  python3 scripts/search.py "watsa seagram" [-k 10] [--kind notes|transcript] [--speaker Stahl]
       [--collection healthcare] [--screen hc_clinical]   (--screen = the collections that feed that screener)
Words are AND-ed (falls back to OR); quote phrases ("free option"); FTS5 syntax (NEAR, OR, prefix*) also works.
Output: path:line  [speaker]  snippet  -> open the file at that line for full context."""
import argparse, os, re, sqlite3, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import ROOT, collections

DB = os.path.join(ROOT, "search.db")


def run(con, q, a):
    cols = a.cols
    sql = ("SELECT path, line, speakers, kind, snippet(p, 0, '[', ']', ' … ', 24), collection FROM p WHERE p MATCH ? "
           + ("AND kind = ? " if a.kind else "")
           + (f"AND (collection IN ({','.join('?' * len(cols))}) OR collection = '') " if cols else "")
           + "ORDER BY rank LIMIT ?")
    args = [q] + ([a.kind] if a.kind else []) + (list(cols) if cols else []) + [a.k * 4 if a.speaker else a.k]
    out = con.execute(sql, args).fetchall()
    if a.speaker:
        out = [r for r in out if a.speaker.lower() in (r[2] or "").lower()][:a.k]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="+")
    ap.add_argument("-k", type=int, default=10)
    ap.add_argument("--kind", choices=["notes", "transcript"])
    ap.add_argument("--speaker")
    ap.add_argument("--collection", help="general, healthcare, macro (comma-separated for several)")
    ap.add_argument("--screen", help="a screener id (core, hc_clinical...): search the collections that feed it")
    a = ap.parse_args()
    a.cols = None
    if a.collection:
        a.cols = [c.strip() for c in a.collection.split(",") if c.strip()]
    elif a.screen:
        a.cols = collections()["screens"][a.screen]
    if not os.path.exists(DB):
        subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build_db.py")], check=True)
    con = sqlite3.connect(DB)
    raw = " ".join(a.query)
    if re.search(r'["*()]|\b(AND|OR|NOT|NEAR)\b', raw):
        res = run(con, raw, a)
    else:
        toks = [t for t in re.findall(r"\w+", raw)]
        res = run(con, " AND ".join(toks), a) or run(con, " OR ".join(toks), a)
    for path, line, spk, kind, snip, coll in res:
        print(f"{path}:{line}  [{spk}{' / ' + coll if coll else ''}]  {snip}")
    if not res:
        print("no hits")


if __name__ == "__main__":
    main()
