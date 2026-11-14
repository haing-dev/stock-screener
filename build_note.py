"""Build single Fable notes for the vault (claim ids linked to quote blocks, code refs to GitHub).
usage: python3 build_note.py <repo_commit> <repo_md_path> "<note title>" "<header line>" [...repeat 3 args]"""
import os, re, sys
V = os.path.dirname(os.path.abspath(__file__)); COMMIT = sys.argv[1]; REPO = "/home/claude/stock-screener/"
GH = "https://github.com/haing-dev/stock-screener/blob/%s/" % COMMIT
N = {}
for d in ("Sources", "Papers"):
    for f in os.listdir(os.path.join(V, d)):
        if f.endswith(".md") and f[:2] in ("MT", "QP"): N[f.split(" - ")[0]] = f[:-3]
bid = lambda i: re.sub(r"[^A-Za-z0-9-]", "-", i)
def linkify(t):
    t = re.sub(r"(?<![\[|#^A-Za-z0-9-])(?:MT\d{3}|QP\d{2})-C\d+-[A-Za-z0-9]+", lambda m: "[[%s#^%s|%s]]" % (N[m.group(0).split("-")[0]], bid(m.group(0)), m.group(0)) if m.group(0).split("-")[0] in N else m.group(0), t)
    t = re.sub(r"(?<![\[|#^A-Za-z0-9/-])(?:MT\d{3}|QP\d{2})(?![-\w])", lambda m: "[[%s|%s]]" % (N[m.group(0)], m.group(0)) if m.group(0) in N else m.group(0), t)
    return t
a = sys.argv[2:]
for k in range(0, len(a), 3):
    body = open(REPO + a[k]).read()
    head = ["---", "tags: [fable, thesis]", "code_commit: %s" % COMMIT[:7], "---", "> %s Source: [repo file](%s%s).\n" % (a[k + 2], GH, a[k])]
    open(os.path.join(V, "Fable", a[k + 1] + ".md"), "w").write("\n".join(head) + linkify(body) + "\n"); print("wrote", a[k + 1])
