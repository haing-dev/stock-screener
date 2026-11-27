"""build_card_inputs: the card inputs zip and its lock (gm/CHANGES.md data entry "card inputs (FRED / ALFRED first
release, macro-data branch)", 2026-11-27).

python3 tools/bbgq/build_card_inputs.py [OUT_ZIP]      (default: tools/bbgq/engine_pkg/work/free/gm_card_inputs.zip)

Reads every file of tools/bbgq/lib/card_inputs.FILES from git (`git show <COMMIT>:<path>`, after `git fetch origin
macro-data`), checks its sha256 against the lock, writes a deterministic zip (fixed member times, sorted names) and
docs/research/card_inputs/LOCK_CARD_v1.json (commit, seal date, files, lock id, zip sha256). Prints metadata only:
file names, hashes, first / last dates up to 2010-12-31, row counts, the first-vintage starts, the first-release
break months (entry item 5) and the check that the root CPILFESL / UNRATE files equal their _FR files. No value."""
import hashlib
import io
import json
import os
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(HERE, "lib"))
import card_inputs as CI  # noqa: E402

LOCK_PATH = os.path.join(REPO, "docs", "research", "card_inputs", "LOCK_CARD_v1.json")


def git_bytes(path):
    return subprocess.check_output(["git", "-C", REPO, "show", "%s:%s" % (CI.COMMIT, path)])


def build(out_zip):
    files = {p: git_bytes(p) for p in sorted(CI.FILES)}
    bad = [p for p, b in files.items() if hashlib.sha256(b).hexdigest() != CI.FILES[p]]
    if bad:
        raise SystemExit("files differ from the lock: %s" % ", ".join(bad))
    os.makedirs(os.path.dirname(out_zip), exist_ok=True)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(files):
            zi = zipfile.ZipInfo(p, date_time=(2026, 11, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, files[p])
    data = buf.getvalue()
    with open(out_zip, "wb") as f:
        f.write(data)
    return files, hashlib.sha256(data).hexdigest()


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "engine_pkg", "work", "free", "gm_card_inputs.zip")
    files, zsha = build(out)
    ci = CI.Inputs.from_files(files)
    print("card inputs %s | commit %s | lock id %s | zip %s (sha256 %s)" % (CI.VERSION, CI.COMMIT, ci.lock_id, out,
                                                                          zsha))
    for p in sorted(files):
        if p.endswith(".csv"):
            s = ci._raw[p]
            print("  %-28s %s | %s..%s | %d rows to 2010-12-31" % (p, CI.FILES[p][:16], s.index[0].date(),
                                                                    s.index[-1].date(), len(s)))
    for sid in CI.FIRST:
        f = ci._raw[CI.FIRST[sid]]
        br = "n/a (used as a level only)" if sid == "UNRATE" else (", ".join(str(b) for b in ci.breaks(sid)) or "none")
        print("  first vintage %-9s from %s | first-release breaks (entry item 5): %s" % (sid, f.index[0].date(), br))
    for sid in ("CPILFESL", "UNRATE"):
        a = CI.parse_csv(git_bytes(sid + ".csv"))
        b = ci._raw[CI.FIRST[sid]]
        same = a.index.equals(b.index) and bool((a == b).all())
        print("  root %s.csv equals research/%s_FR.csv up to 2010-12-31: %s" % (sid, sid, "yes" if same else "NO"))
    lock = {"version": "card-v1", "source": CI.SOURCE, "commit": CI.COMMIT, "seal_date": CI.SEAL_DATE,
            "files": CI.FILES, "lock_id": ci.lock_id, "zip_sha256": zsha, "reader": CI.VERSION,
            "entry": "gm/CHANGES.md data: card inputs (FRED / ALFRED first release, macro-data branch)"}
    os.makedirs(os.path.dirname(LOCK_PATH), exist_ok=True)
    with open(LOCK_PATH, "w", encoding="utf-8") as f:
        json.dump(lock, f, indent=1, sort_keys=True)
        f.write("\n")
    print("lock written: %s" % os.path.relpath(LOCK_PATH, REPO))


if __name__ == "__main__":
    main()
