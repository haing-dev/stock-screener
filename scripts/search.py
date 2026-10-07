"""Search the store.  python3 scripts/search.py "watsa seagram" [-k 10] [--kind notes|transcript] [--speaker Stahl]
Words are AND-ed (falls back to OR); quote phrases ("free option"); FTS5 syntax (NEAR, OR, prefix*) also works.
Output: path:line  [speaker]  snippet  -> open the file at that line for full context."""
import argparse, os, re, sqlite3, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import ROOT

DB = os.path.join(ROOT, "search.db")


def run(con, q, a):
    sql = ("SELECT path, line, speakers, kind, snippet(p, 0, '[', ']', ' … ', 24) FROM p WHERE p MATCH ? "
           + ("AND kind = ? " if a.kind else "") + "ORDER BY rank LIMIT ?")
    args = [q] + ([a.kind] if a.kind else []) + [a.k * 4 if a.speaker else a.k]
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
    a = ap.parse_args()
    if not os.path.exists(DB):
        subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build_db.py")], check=True)
    con = sqlite3.connect(DB)
    raw = " ".join(a.query)
    if re.search(r'["*()]|\b(AND|OR|NOT|NEAR)\b', raw):
        res = run(con, raw, a)
    else:
        toks = [t for t in re.findall(r"\w+", raw)]
        res = run(con, " AND ".join(toks), a) or run(con, " OR ".join(toks), a)
    for path, line, spk, kind, snip in res:
        print(f"{path}:{line}  [{spk}]  {snip}")
    if not res:
        print("no hits")


if __name__ == "__main__":
    main()
