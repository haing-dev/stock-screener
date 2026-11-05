"""PDF -> Layer 0 paper document: one chunk per page, reading order from text blocks (two-column aware).
usage: pdf2chunks.py PDF SOURCE_ID TITLE OUT"""
import re, subprocess, sys, html
from xml.etree import ElementTree as ET

P, SID, TITLE, OUT = sys.argv[1:5]
x = subprocess.run(["pdftotext", "-bbox-layout", P, "-"], capture_output=True, text=True).stdout
x = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", x)
x = re.sub(r"<!DOCTYPE[^>]*>", "", x).replace('xmlns="http://www.w3.org/1999/xhtml"', "")
root = ET.fromstring(x)
chunks = []
for page in root.iter("page"):
    W = float(page.get("width"))
    blocks = []
    for b in page.iter("block"):
        x0, y0, x1, y1 = (float(b.get(k)) for k in ("xMin", "yMin", "xMax", "yMax"))
        lines = [" ".join(w.text or "" for w in l.iter("word")) for l in b.iter("line")]
        blocks.append((x0, y0, x1, y1, "\n".join(lines)))
    wide = sorted([b for b in blocks if b[2] - b[0] > 0.55 * W or (b[0] < 0.45 * W and b[2] > 0.58 * W)], key=lambda b: b[1])
    rest = [b for b in blocks if b not in wide]
    out, prev = [], -1
    for cut in [w[1] for w in wide] + [1e9]:
        seg = [b for b in rest if prev <= b[1] < cut]
        left = sorted([b for b in seg if (b[0] + b[2]) / 2 < W / 2], key=lambda b: b[1])
        right = sorted([b for b in seg if (b[0] + b[2]) / 2 >= W / 2], key=lambda b: b[1])
        out += [b[4] for b in left + right]
        w = [b for b in wide if b[1] == cut]
        out += [b[4] for b in w]
        prev = cut
    chunks.append("\n\n".join(t for t in out if t.strip()))
hdr = ["# " + TITLE, "source_id: " + SID, "type: paper", "file: " + P.split("/Quant/")[-1],
       "chunks: one per PDF page (C01 = page 1). Page images: img/%s-p-NN.png (exhibits, charts)" % SID, "---"]
body = ["\n[C%02d]\n%s" % (i, html.unescape(c)) for i, c in enumerate(chunks, 1)]
open(OUT, "w").write("\n".join(hdr + body) + "\n")
print(SID, len(chunks), "pages", sum(len(c.split()) for c in chunks), "words")
