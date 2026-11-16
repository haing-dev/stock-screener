"""Build a PC-runner job that copies vault notes from a clone of branch macro-vault into the Obsidian vault on the PC.

Why: the vault is the single store (CLAUDE.md), but the cloud session can write to the PC only through the job runner
(Documents\\WRDS results\\local\\jobs) or file by file through the bridge. One generated job carries the files inside
itself (zlib + base64), writes those that differ, never deletes, and prints names and sizes only.

usage: python3 tools/vault/make_sync_job.py <vault clone> <out dir> <job name> <path> [<path> ...]
  <path> is relative to the clone; a folder is taken with everything under it.
  pipeline/<unit>/...  is written to  _data/<unit>/...   (exact inputs and outputs of a unit)
  every other path keeps its place (Fable/, Method/, Sources/, Papers/, Investors/, Mechanisms/).
Then put <out dir>/<job name>.py into local\\jobs on the PC; the report appears in local\\results\\<job name>.txt.
Generated jobs are not committed (they only repeat files that are on branch macro-vault)."""
import base64, os, subprocess, sys, zlib

ROOT = r"G:\My Drive\Transcripts\Processed Transcripts\Macro Transcripts\Obsidian Macro\Macro"
NOTE_DIRS = ("Fable", "Method", "Sources", "Papers", "Investors", "Mechanisms")

JOB = '''"""Vault sync job %(name)s (generated %(when)s from macro-vault %(commit)s): writes %(n)d files into the Obsidian
vault on the PC. Files that already match are left alone; nothing is deleted. Prints names and sizes only."""
import base64, os, sys, zlib
ROOT = os.environ.get("VAULT_ROOT", %(root)r)
FILES = [
%(files)s
]
def main():
    if not os.path.isdir(ROOT):
        print("VAULT NOT FOUND:", ROOT); sys.exit(1)
    w = u = 0
    for rel, b in FILES:
        if rel.startswith("/") or ".." in rel.split("/") or ":" in rel:
            print("REFUSED", rel); sys.exit(1)
        data = zlib.decompress(base64.b64decode(b))
        p = os.path.join(ROOT, *rel.split("/"))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if os.path.exists(p) and open(p, "rb").read() == data:
            u += 1; print("unchanged", len(data), rel); continue
        with open(p, "wb") as f:
            f.write(data)
        w += 1; print("written  ", len(data), rel)
    print("DONE: written %%d, unchanged %%d, of %%d" %% (w, u, len(FILES)))
main()
'''

def target(rel):
    parts = rel.split("/")
    if parts[0] == "pipeline" and len(parts) >= 3:
        return "/".join(["_data"] + parts[1:])
    if parts[0] in NOTE_DIRS:
        return rel
    raise SystemExit("not a vault path: " + rel)

def main():
    clone, out_dir, name = sys.argv[1:4]
    rels = []
    for a in sys.argv[4:]:
        p = os.path.join(clone, a)
        if os.path.isdir(p):
            for d, _, fs in os.walk(p):
                rels += [os.path.relpath(os.path.join(d, f), clone).replace(os.sep, "/") for f in fs if "__pycache__" not in d]
        elif os.path.isfile(p):
            rels.append(a)
        else:
            raise SystemExit("missing: " + a)
    rels = sorted(set(rels))
    commit = subprocess.run(["git", "-C", clone, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    when = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M UTC"], capture_output=True, text=True).stdout.strip()
    rows, total = [], 0
    for r in rels:
        data = open(os.path.join(clone, r), "rb").read(); total += len(data)
        rows.append("    (%r, %r)," % (target(r), base64.b64encode(zlib.compress(data, 9)).decode()))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, name + ".py")
    open(path, "w", encoding="utf-8").write(JOB % dict(name=name, when=when, commit=commit, n=len(rels), root=ROOT, files="\n".join(rows)))
    print("%s: %d files, %d bytes of notes, job %d bytes" % (path, len(rels), total, os.path.getsize(path)))
    for r in rels:
        print("  ", target(r))

if __name__ == "__main__":
    main()
