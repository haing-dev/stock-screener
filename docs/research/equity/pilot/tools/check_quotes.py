"""Check every quote of a claims file against its source text (CLAIM_SPEC_v1 rule 1).

python3 check_quotes.py SOURCE.txt CLAIMS.json [OUT.json]
Writes OUT (default CLAIMS with .checked.json) with a field `found` per claim and prints counts. A quote is found if,
after removing [Lnnn] markers and collapsing whitespace (and normalising curly quotes and dashes) in both texts, it is
a substring of the source. Also reports the file line where the quote starts (line_found) and whether the claimed line is within 2 (line_ok).
"""
import json
import re
import sys

TR = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', "—": "-", "–": "-", " ": " "})


def norm(s):
    s = re.sub(r"\[L\d+\]", " ", s).translate(TR)
    return re.sub(r"\s+", " ", s).strip()


def anchors(src):
    """normalised text and, for each character position, the last [Lnnn] anchor before it"""
    out, pos = [], []
    cur = 0
    for line_no, raw in enumerate(src.splitlines(), 1):
        m = re.match(r"\[L(\d+)\]", raw)
        if m:
            cur = int(m.group(1))
        t = norm(raw)
        if t:
            out.append(t)
            pos.append((sum(len(x) + 1 for x in out[:-1]), cur, line_no))
    return " ".join(out), pos


def main():
    src_path, claims_path = sys.argv[1], sys.argv[2]
    out_path = sys.argv[3] if len(sys.argv) > 3 else claims_path.replace(".json", ".checked.json")
    text, pos = anchors(open(src_path, encoding="utf-8").read())
    claims = json.load(open(claims_path, encoding="utf-8"))
    ok = 0
    for c in claims:
        q = norm(c.get("quote", ""))
        i = text.find(q) if len(q) >= 20 else -1
        c["found"] = i >= 0
        if i >= 0:
            ok += 1
            hit = max((p for p in pos if p[0] <= i), default=(0, 0, 0))
            c["line_found"] = hit[2]
            c["line_ok"] = abs(int(c.get("line") or 0) - hit[2]) <= 2
    json.dump(claims, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("%s: %d claims, %d quotes found verbatim, %d dropped" % (claims_path, len(claims), ok, len(claims) - ok))


if __name__ == "__main__":
    main()
