"""eq_notes_zip_v1 (PC runner job): pack the short notes (.note.md) and catalogs of the General Transcripts folder
of the processed library into one zip under local\\work\\equity, so the inventory step (E0.1 of the equity plan) can
read them in one transfer. Transcript texts are not packed. Prints counts and sizes only."""
import os
import sys
import zipfile

SRC = os.environ.get("EQ_LIB", r"G:\My Drive\Transcripts\Processed Transcripts\General Transcripts")
OUT = os.path.join(os.getcwd(), "work", "equity")
print("=== eq_notes_zip_v1 ===")
if not os.path.isdir(SRC):
    print("LIBRARY NOT FOUND:", SRC)
    print("=== END ===")
    sys.exit(0)
os.makedirs(OUT, exist_ok=True)
z = os.path.join(OUT, "general_notes_20261117.zip")
n = b = 0
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as f:
    for root, dirs, files in os.walk(SRC):
        for fn in sorted(files):
            if fn.endswith(".note.md") or fn == "_catalog.md":
                p = os.path.join(root, fn)
                f.write(p, os.path.relpath(p, SRC).replace("\\", "/"))
                n += 1
                b += os.path.getsize(p)
print("files packed: %d | bytes %d | zip bytes %d" % (n, b, os.path.getsize(z)))
print("zip:", z)
print("=== END ===")
