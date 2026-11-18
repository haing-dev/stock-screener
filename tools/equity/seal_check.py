#!/usr/bin/env python3
"""seal_check: checks a WRDS job before it is sent to the PC runner (plan v0.3 section 8.2, SEAL_LOG.md).

    python3 tools/equity/seal_check.py [JOB.json ...] [--lib DIR ...]

Default jobs: tools/wrdsq/jobs/eq_sc_pull_v1.json, eq_scorecard_v1.json, eq_precheck_v1.json,
eq_sc_cleanup_v1.json; default lib folders:
tools/equity/wrds, tools/wrdsq/lib. Prints PASS or REFUSED per job with the reasons, the lock id and, for a
seal-exempt job, its code hash and input hash. Exit code 0 only if every job passes.

Rules
- Every job: no file in a lib folder may carry the name of a standard-library module, numpy or pandas (it would be
  imported instead of the real one, unchecked).
- Seal-exempt jobs (tools/equity/seal_exempt.json): the job name matches a registered pattern; every python step is
  exactly the template `import <module>\\n<module>.<function>(<args>)`, the whole step text, where the function is
  registered for that job name and <args> fully matches its registered argument list (in order); other steps only
  `datasets` (and `delete` of the registered prefix where the pattern allows it). The module's code hash (the module with its frozen input block
  left out) must match; the block may hold only NAME = json.loads("...") with valid JSON; the module may import no
  lib module.
- Other jobs whose name starts with eq_: no pull or export step; no delete of a scorecard data set; python steps and
  every lib module they import are read as syntax trees. Refused: a direct read (the names sql, db, load, DATA,
  unless passed to eq_reader.read / load_ds / count or to a function of a lib module that is itself checked; any
  read_sql / read_csv / raw_sql / execute call; open, exec, eval, getattr and similar), any dunder attribute, *args /
  **kwargs in a reader call, the keyword exempt=, any keyword a reader function does not accept (count takes none:
  only a named check as a plain string), access to anything in eq_reader except read, load_ds, count and
  SealError, imports outside a short list, importing a seal-exempt module, and a string naming a scorecard data set
  (eq_sc_...) anywhere except as the name given to eq_reader.load_ds. eq_reader.py must equal the registered file.
- Jobs whose name does not start with eq_: refused if any step or imported lib module names a scorecard data set
  (eq_sc_...) or imports a seal-exempt module; otherwise not checked (they are not equity jobs).
Lock id = SHA-256 over the SHA-256 of eq_reader.py, seal_check.py and seal_exempt.json (one per line).
"""
import ast
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
READER = os.path.join(ROOT, "tools", "equity", "wrds", "eq_reader.py")
EXEMPT = os.path.join(ROOT, "tools", "equity", "seal_exempt.json")
ME = os.path.abspath(__file__)
JOBS = os.path.join(ROOT, "tools", "wrdsq", "jobs")
DEFAULT_JOBS = [os.path.join(JOBS, n) for n in ("eq_sc_pull_v1.json", "eq_scorecard_v1.json", "eq_precheck_v1.json",
                                                "eq_sc_cleanup_v1.json")]
DEFAULT_LIBS = [os.path.join(ROOT, "tools", "equity", "wrds"), os.path.join(ROOT, "tools", "wrdsq", "lib")]

META = {"libraries", "tables", "search", "describe", "datasets"}
STDLIB_OK = {"json", "re", "math", "random", "collections", "itertools", "functools", "datetime", "time", "warnings",
             "hashlib", "statistics", "bisect", "heapq", "string", "textwrap", "typing", "dataclasses", "operator",
             "copy", "numpy", "pandas", "decimal", "fractions"}
EXEMPT_MODULE_IMPORTS = STDLIB_OK | {"os", "traceback", "types"}
READ_HELPERS = {"sql", "db", "load", "DATA"}
BAD_NAMES = {"open", "exec", "eval", "compile", "__import__", "globals", "locals", "vars", "getattr", "setattr",
             "delattr", "breakpoint", "input", "memoryview", "__builtins__", "__loader__", "__spec__"}
BAD_ATTRS = {"raw_sql", "read_sql", "read_sql_query", "read_sql_table", "execute", "executemany", "connection",
             "cursor", "read_csv", "read_parquet", "read_pickle", "read_table", "read_excel", "read_json",
             "read_feather", "read_hdf", "read_fwf", "read_stata", "read_sas", "read_spss", "read_orc", "read_xml",
             "read_html", "read_clipboard", "load", "loadtxt", "genfromtxt", "fromfile", "memmap", "system",
             "popen", "f_globals", "f_locals", "f_back", "gi_frame", "cr_frame", "tb_frame"}
READER_FUNCS = {"read", "load_ds", "count", "SealError"}
READER_MAXPOS = {"read": 6, "load_ds": 4, "count": 4}
READER_KW = {"read": {"where"}, "load_ds": set(), "count": set()}
INPUT_BEGIN = "# >>> FROZEN INPUT"
INPUT_END = "# <<< FROZEN INPUT"
DS_MARK = "eq_sc_"


def sha(path_or_bytes):
    b = path_or_bytes if isinstance(path_or_bytes, bytes) else open(path_or_bytes, "rb").read()
    return hashlib.sha256(b).hexdigest()


def split_input(text):
    """(code without the frozen input block, the block). The marker lines stay in the code."""
    lines = text.splitlines(True)
    try:
        i = next(k for k, x in enumerate(lines) if x.startswith(INPUT_BEGIN))
        j = next(k for k, x in enumerate(lines) if x.startswith(INPUT_END))
    except StopIteration:
        return text, ""
    if j < i:
        return text, ""
    return "".join(lines[:i + 1] + lines[j:]), "".join(lines[i + 1:j])


def code_hash(text):
    return sha(split_input(text)[0].encode("utf-8"))


def input_hash(text):
    return sha(split_input(text)[1].encode("utf-8"))


def check_input_block(block):
    """The frozen input block may hold only NAME = json.loads(<string literal>) with valid JSON."""
    errs = []
    try:
        tree = ast.parse(block)
    except SyntaxError as e:
        return ["input block: syntax error %s" % e]
    for node in tree.body:
        ok = (isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name)
              and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute)
              and isinstance(node.value.func.value, ast.Name) and node.value.func.value.id == "json"
              and node.value.func.attr == "loads" and len(node.value.args) == 1 and not node.value.keywords
              and isinstance(node.value.args[0], ast.Constant) and isinstance(node.value.args[0].value, str))
        if not ok:
            errs.append("input block line %d: only NAME = json.loads(\"...\") is allowed" % node.lineno)
            continue
        try:
            json.loads(node.value.args[0].value)
        except ValueError:
            errs.append("input block line %d: not valid JSON" % node.lineno)
    return errs


def lock_id():
    parts = [sha(READER), sha(ME), sha(EXEMPT) if os.path.exists(EXEMPT) else sha(b"")]
    return sha("\n".join(parts).encode()), parts


def load_exempt():
    if not os.path.exists(EXEMPT):
        return []
    return json.load(open(EXEMPT)).get("jobs", [])


def exempt_modules():
    return {e["module"] for e in load_exempt()}


def find_module(name, libs):
    for d in libs:
        p = os.path.join(d, name + ".py")
        if os.path.exists(p):
            return p
    return None


def shadowing(libs):
    std = set(getattr(sys, "stdlib_module_names", ())) | STDLIB_OK | {"numpy", "pandas", "wrds", "sqlalchemy",
                                                                       "psycopg2", "scipy"}
    bad = []
    for d in libs:
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                stem = f.split(".")[0]
                if stem in std and (f.endswith(".py") or os.path.isdir(os.path.join(d, f)) or f.endswith(".pyc")
                                    or f.endswith(".so")):
                    bad.append("lib folder %s holds %s, which shadows the module %s" % (d, f, stem))
    return bad


class Scan(ast.NodeVisitor):
    """Finds forbidden reads in step code or a lib module of a non-exempt equity job."""

    def __init__(self, where, trusted):
        self.where, self.trusted = where, set(trusted)
        self.alias = {}
        self.imports = set()
        self.errs = []
        self.ok_args = set()
        self.ok_str = set()

    def err(self, node, msg):
        self.errs.append("%s line %d: %s" % (self.where, getattr(node, "lineno", 0), msg))

    def visit_Import(self, node):
        for a in node.names:
            top = a.name.split(".")[0]
            self.imports.add(top)
            self.alias[a.asname or top] = top
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        top = (node.module or "").split(".")[0]
        self.imports.add(top)
        if node.level:
            self.err(node, "relative import")
        if top == "eq_reader":
            for a in node.names:
                if a.name not in READER_FUNCS:
                    self.err(node, "from eq_reader import %s" % a.name)
                self.alias[a.asname or a.name] = "eq_reader." + a.name
        elif top in self.trusted:
            self.err(node, "import the module itself, not names from it")
        self.generic_visit(node)

    def _callee(self, func):
        if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
            return self.alias.get(func.value.id), func.attr
        if isinstance(func, ast.Name) and self.alias.get(func.id, "").startswith("eq_reader."):
            return "eq_reader", self.alias[func.id].split(".", 1)[1]
        return None, None

    def visit_Call(self, node):
        mod, fn = self._callee(node.func)
        if mod in self.trusted:
            if mod == "eq_reader":
                if fn not in READER_FUNCS:
                    self.err(node, "eq_reader.%s is not a reader function" % fn)
                if len(node.args) > READER_MAXPOS.get(fn, 0):
                    self.err(node, "too many positional arguments to eq_reader.%s" % fn)
                for k in node.keywords:
                    if k.arg is not None and k.arg != "exempt" and k.arg not in READER_KW.get(fn, set()):
                        self.err(node, "keyword %s= is not accepted by eq_reader.%s" % (k.arg, fn))
                if fn == "count" and len(node.args) >= 2 and not isinstance(node.args[1], ast.Constant):
                    self.err(node, "eq_reader.count takes a named check as a plain string")
                if fn == "load_ds" and len(node.args) >= 2 and isinstance(node.args[1], ast.Constant):
                    self.ok_str.add(id(node.args[1]))
            for a in node.args:
                if isinstance(a, ast.Starred):
                    self.err(node, "*args in a call that receives the read helpers")
            for k in node.keywords:
                if k.arg is None:
                    self.err(node, "**kwargs in a call that receives the read helpers")
                if k.arg == "exempt":
                    self.err(node, "exempt= is allowed only in seal-exempt jobs")
            for a in list(node.args) + [k.value for k in node.keywords]:
                if isinstance(a, ast.Name):
                    self.ok_args.add(id(a))
        self.generic_visit(node)

    def visit_Name(self, node):
        if node.id in BAD_NAMES:
            self.err(node, "'%s' is not allowed" % node.id)
        if node.id in READ_HELPERS and id(node) not in self.ok_args and isinstance(node.ctx, ast.Load):
            self.err(node, "'%s' used outside a reader call (direct read)" % node.id)

    def visit_Attribute(self, node):
        if node.attr in BAD_ATTRS:
            self.err(node, "'.%s' is not allowed (direct read)" % node.attr)
        if node.attr.startswith("__"):
            self.err(node, "dunder attribute '.%s' is not allowed" % node.attr)
        if isinstance(node.value, ast.Name) and self.alias.get(node.value.id) == "eq_reader":
            if isinstance(node.ctx, (ast.Store, ast.Del)):
                self.err(node, "writing to eq_reader is not allowed")
            elif node.attr not in READER_FUNCS:
                self.err(node, "eq_reader.%s is not open to jobs" % node.attr)
        self.generic_visit(node)

    def visit_Constant(self, node):
        if isinstance(node.value, str) and DS_MARK in node.value and id(node) not in self.ok_str:
            self.err(node, "names a scorecard data set (%s...) outside eq_reader.load_ds" % DS_MARK)


def scan(code, where, libs):
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return ["%s: syntax error %s" % (where, e)], set()
    s = Scan(where, {"eq_reader"})
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            s.visit(node)
    s.trusted |= {m for m in s.imports if m not in STDLIB_OK and m != "eq_reader" and find_module(m, libs)}
    s.errs, s.imports = [], set()
    s.visit(tree)
    return s.errs, s.imports


def _module_imports(text):
    mods = set()
    for node in ast.walk(ast.parse(text)):
        if isinstance(node, ast.Import):
            mods |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            mods.add((node.module or "").split(".")[0])
    return mods


def check_exempt(job, entry, pat, libs):
    errs, extra = [], {}
    mod = entry["module"]
    mp = find_module(mod, libs)
    if not mp:
        return ["exempt module %s not found" % mod], extra
    text = open(mp, encoding="utf-8").read()
    ch, ih = code_hash(text), input_hash(text)
    extra = {"module": mp, "code_sha256": ch, "input_sha256": ih}
    if ch != entry["code_sha256"]:
        errs.append("exempt module %s: code SHA-256 %s does not match the registered %s" % (mod, ch[:16],
                                                                                             entry["code_sha256"][:16]))
    errs += check_input_block(split_input(text)[1])
    for m in sorted(_module_imports(text)):
        if m not in EXEMPT_MODULE_IMPORTS:
            errs.append("exempt module imports %s (not allowed)" % m)
    tmpl = re.compile(r"^import %s\n%s\.(\w+)\(([^()]*)\)$" % (mod, mod))
    for i, st in enumerate(job.get("steps", []), 1):
        do = st.get("do")
        if do == "datasets":
            continue
        if do == "delete" and pat.get("delete_prefix"):
            if all(isinstance(n, str) and n.startswith(pat["delete_prefix"]) for n in st.get("names", [])):
                continue
            errs.append("step %d: delete outside %s" % (i, pat["delete_prefix"]))
            continue
        if do != "python":
            errs.append("step %d: '%s' is not allowed in this seal-exempt job" % (i, do))
            continue
        m = tmpl.match(st.get("code", ""))
        if not m:
            errs.append("step %d: not the registered template 'import %s\\n%s.<function>(<args>)'" % (i, mod, mod))
            continue
        fns = pat["functions"]
        if m.group(1) not in fns:
            errs.append("step %d: %s.%s is not registered for jobs named like %s" % (i, mod, m.group(1),
                                                                                    pat["pattern"]))
        elif not re.fullmatch(fns[m.group(1)], m.group(2)):
            errs.append("step %d: arguments (%s) do not match the registered (%s)" % (i, m.group(2)[:80],
                                                                                    fns[m.group(1)]))
    return errs, extra


def check_job(path, libs, verbose=True):
    job = json.load(open(path))
    name = job.get("name", "")
    errs, info, extra = list(shadowing(libs)), [], {}
    exempt = None
    for e in load_exempt():
        for pat in e.get("names", []):
            if re.match(pat["pattern"] + r"$", name):
                exempt = (e, pat)
    if exempt:
        e, pat = exempt
        x, extra = check_exempt(job, e, pat, libs)
        errs += x
        info.append("seal-exempt job (%s, %s): module %s code sha256 %s input sha256 %s"
                    % (e.get("registered_job"), pat["pattern"], e["module"], extra.get("code_sha256", "?"),
                       extra.get("input_sha256", "?")))
        return not errs, errs + info, extra
    exm = exempt_modules()
    if not name.startswith("eq_"):
        blob = json.dumps(job)
        if DS_MARK in blob:
            errs.append("names a scorecard data set (%s...)" % DS_MARK)
        for st in job.get("steps", []):
            if st.get("do") == "python":
                try:
                    imps = _module_imports(st.get("code", ""))
                except SyntaxError:
                    imps = set()
                for m in imps:
                    if m in exm:
                        errs.append("imports the seal-exempt module %s" % m)
                    mp = find_module(m, libs)
                    if mp and DS_MARK in open(mp, encoding="utf-8").read():
                        errs.append("lib module %s names a scorecard data set" % m)
        if errs:
            return False, errs, {}
        return True, ["not an equity job (name %r): checked only for scorecard data sets" % name], {}
    seen = {}
    rp = find_module("eq_reader", libs)

    def check_module(mod, depth=0):
        if mod in seen or depth > 10:
            return
        seen[mod] = True
        if mod == "eq_reader":
            if not rp:
                errs.append("eq_reader.py not found in the lib folders")
            elif sha(rp) != sha(READER):
                errs.append("eq_reader.py in %s differs from the registered reader" % rp)
            return
        if mod in exm:
            errs.append("imports the seal-exempt module %s" % mod)
            return
        if mod in STDLIB_OK:
            return
        mp = find_module(mod, libs)
        if not mp:
            errs.append("import %s: not an allowed module and not in the lib folders" % mod)
            return
        e, imps = scan(open(mp, encoding="utf-8").read(), os.path.basename(mp), libs)
        errs.extend(e)
        for m in sorted(imps):
            check_module(m, depth + 1)

    for i, st in enumerate(job.get("steps", []), 1):
        do = st.get("do")
        if do in META:
            if DS_MARK in json.dumps(st):
                errs.append("step %d: names a scorecard data set" % i)
            continue
        if do == "delete":
            if any(DS_MARK in str(n) for n in st.get("names", [])):
                errs.append("step %d: delete of a scorecard data set" % i)
            continue
        if do in ("pull", "export"):
            errs.append("step %d: '%s' is not allowed in an equity job" % (i, do))
            continue
        if do != "python":
            errs.append("step %d: unknown step type %r" % (i, do))
            continue
        e, imps = scan(st.get("code", ""), "step %d" % i, libs)
        errs.extend(e)
        for m in sorted(imps):
            check_module(m)
    return not errs, errs + info, extra


def main(argv):
    libs, jobs, k = [], [], 0
    while k < len(argv):
        if argv[k] == "--lib":
            libs.append(argv[k + 1])
            k += 2
        else:
            jobs.append(argv[k])
            k += 1
    libs = libs or DEFAULT_LIBS
    jobs = jobs or DEFAULT_JOBS
    lid, parts = lock_id()
    allok = True
    for j in jobs:
        ok, msgs, _ = check_job(j, libs)
        allok &= ok
        print("%s %s" % ("PASS" if ok else "REFUSED", j))
        for m in msgs:
            print("   " + m)
    print("lock id %s  (eq_reader %s, seal_check %s, seal_exempt %s)" % (lid, parts[0][:12], parts[1][:12],
                                                                         parts[2][:12]))
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
