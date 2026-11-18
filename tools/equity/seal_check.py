#!/usr/bin/env python3
"""seal_check: checks an equity job before it is sent to the PC runner (plan v0.3 section 8.2, SEAL_LOG.md).

    python3 tools/equity/seal_check.py [JOB.json ...] [--lib DIR ...]

Default job: tools/wrdsq/jobs/eq_scorecard_v1.json; default lib folders: tools/equity/wrds, tools/wrdsq/lib.
Prints PASS or REFUSED per job with the reasons, the lock id and, for a seal-exempt job, its code hash and input
hash. Exit code 0 only if every job passes.

Rules for a job whose name starts with eq_:
- metadata steps (libraries, tables, search, describe, datasets) and delete always pass;
- pull and export steps are refused (tables are read in python steps through eq_reader; data sets never leave);
- python steps and every lib module they import are read as Python syntax trees. Refused: a direct read of a table
  or a stored data set (the helpers sql, db, load, DATA, or any read_sql / read_csv / raw_sql / execute call,
  open, exec, eval, getattr and similar), imports outside a short list (os, sys, subprocess, sqlalchemy, ... are
  refused), the flag exempt= in an eq_reader call, writing to eq_reader. sql and load may appear only as arguments
  of eq_reader.read / eq_reader.load_ds or of functions of lib modules that are themselves checked by these rules.
  The eq_reader module must be the registered file (same SHA-256);
- a seal-exempt job (tools/equity/seal_exempt.json: name pattern, module, code SHA-256) may hand the helpers to its
  registered module, whose code hash (the module with its frozen input block left out) must match, whose frozen
  input block must hold only JSON literals, and which may import no other lib module.
Jobs whose name does not start with eq_ are not equity jobs and pass unchecked.
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
DEFAULT_JOB = os.path.join(ROOT, "tools", "wrdsq", "jobs", "eq_scorecard_v1.json")
DEFAULT_LIBS = [os.path.join(ROOT, "tools", "equity", "wrds"), os.path.join(ROOT, "tools", "wrdsq", "lib")]

META = {"libraries", "tables", "search", "describe", "datasets", "delete"}
STDLIB_OK = {"json", "re", "math", "random", "collections", "itertools", "functools", "datetime", "time", "warnings",
             "hashlib", "statistics", "bisect", "heapq", "string", "textwrap", "typing", "dataclasses", "operator",
             "copy", "numpy", "pandas", "decimal", "fractions"}
HELPERS = {"sql", "db", "load", "save", "out", "DATA", "LIB", "pd", "np"}
READ_HELPERS = {"sql", "db", "load", "DATA"}          # may only be passed to eq_reader (or the exempt module)
BAD_NAMES = {"open", "exec", "eval", "compile", "__import__", "globals", "locals", "vars", "getattr", "setattr",
             "delattr", "breakpoint", "input", "memoryview", "__builtins__"}
BAD_ATTRS = {"raw_sql", "read_sql", "read_sql_query", "read_sql_table", "execute", "executemany", "connection",
             "cursor", "read_csv", "read_parquet", "read_pickle", "read_table", "read_excel", "read_json",
             "read_feather", "read_hdf", "read_fwf", "read_stata", "read_sas", "read_spss", "read_orc", "read_xml",
             "read_html", "read_clipboard", "load", "loadtxt", "genfromtxt", "fromfile", "memmap", "system",
             "popen", "__dict__", "__globals__", "__code__", "__subclasses__", "__getattribute__", "f_globals",
             "f_locals", "__loader__", "__spec__"}
READER_FUNCS = {"read", "load_ds", "sealed", "SealError", "TABLES", "SEAL_END", "SEAL_START"}
INPUT_BEGIN = "# >>> FROZEN INPUT"
INPUT_END = "# <<< FROZEN INPUT"


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


class Scan(ast.NodeVisitor):
    """Finds forbidden reads in step code or a lib module. trusted = module names whose functions may receive the
    read helpers (eq_reader always; the registered module for an exempt job)."""

    def __init__(self, where, trusted, exempt_job):
        self.where, self.trusted, self.exempt_job = where, set(trusted), exempt_job
        self.alias = {}                       # local name -> module name
        self.imports = set()
        self.errs = []
        self.ok_args = set()                  # ids of Name nodes passed to a trusted call

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
                if a.name not in READER_FUNCS or a.name == "*":
                    self.err(node, "from eq_reader import %s" % a.name)
                self.alias[a.asname or a.name] = "eq_reader." + a.name
        elif top in self.trusted:
            self.err(node, "import the module itself, not names from it")
        self.generic_visit(node)

    def _callee_module(self, func):
        if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
            return self.alias.get(func.value.id), func.attr
        if isinstance(func, ast.Name) and self.alias.get(func.id, "").startswith("eq_reader."):
            return "eq_reader", self.alias[func.id].split(".", 1)[1]
        return None, None

    def visit_Call(self, node):
        mod, fn = self._callee_module(node.func)
        if mod in self.trusted:
            if mod == "eq_reader":
                if fn not in READER_FUNCS:
                    self.err(node, "eq_reader.%s is not a reader function" % fn)
                for k in node.keywords:
                    if k.arg == "exempt" and not self.exempt_job:
                        self.err(node, "exempt= in an eq_reader call (only seal-exempt jobs)")
                    if k.arg is None:
                        self.err(node, "**kwargs in an eq_reader call")
            for a in list(node.args) + [k.value for k in node.keywords]:
                if isinstance(a, ast.Name):
                    self.ok_args.add(id(a))
        self.generic_visit(node)

    def visit_Name(self, node):
        if node.id in BAD_NAMES:
            self.err(node, "'%s' is not allowed" % node.id)
        if node.id in READ_HELPERS and id(node) not in self.ok_args and isinstance(node.ctx, ast.Load):
            self.err(node, "'%s' used outside an eq_reader call (direct read)" % node.id)

    def visit_Attribute(self, node):
        if node.attr in BAD_ATTRS:
            self.err(node, "'.%s' is not allowed (direct read)" % node.attr)
        if isinstance(node.value, ast.Name) and self.alias.get(node.value.id) == "eq_reader":
            if isinstance(node.ctx, (ast.Store, ast.Del)):
                self.err(node, "writing to eq_reader is not allowed")
            elif node.attr not in READER_FUNCS:
                self.err(node, "eq_reader.%s is not a reader function" % node.attr)
        self.generic_visit(node)


def scan(code, where, trusted, exempt_job, libs=()):
    """trusted: modules whose functions may receive the read helpers. Lib modules imported by the code (found in
    libs, and scanned in turn by check_job) are trusted too: inside them the same rules apply."""
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return ["%s: syntax error %s" % (where, e)], set()
    # first pass: aliases from imports, so calls are recognised wherever they occur
    s = Scan(where, trusted, exempt_job)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            s.visit(node)
    s.trusted |= {m for m in s.imports if m not in STDLIB_OK and m != "eq_reader" and find_module(m, libs)}
    s.errs = []
    s.imports = set()
    s.visit(tree)
    return s.errs, s.imports


def find_module(name, libs):
    for d in libs:
        p = os.path.join(d, name + ".py")
        if os.path.exists(p):
            return p
    return None


def check_job(path, libs, verbose=True):
    job = json.load(open(path))
    name = job.get("name", "")
    errs, info = [], []
    if not name.startswith("eq_"):
        return True, ["not an equity job (name %r): not checked" % name], {}
    ex = [e for e in load_exempt() if re.match(e["job_pattern"] + r"$", name)]
    exempt = ex[0] if ex else None
    trusted = {"eq_reader"}
    extra = {}
    if exempt:
        trusted.add(exempt["module"])
        mp = find_module(exempt["module"], libs)
        if not mp:
            errs.append("exempt module %s not found" % exempt["module"])
        else:
            text = open(mp, encoding="utf-8").read()
            ch, ih = code_hash(text), input_hash(text)
            extra = {"module": mp, "code_sha256": ch, "input_sha256": ih}
            if ch != exempt["code_sha256"]:
                errs.append("exempt module %s: code SHA-256 %s does not match the registered %s"
                            % (exempt["module"], ch[:16], exempt["code_sha256"][:16]))
            errs += check_input_block(split_input(text)[1])
            tree = ast.parse(text)
            for node in ast.walk(tree):
                mods = []
                if isinstance(node, ast.Import):
                    mods = [a.name.split(".")[0] for a in node.names]
                elif isinstance(node, ast.ImportFrom):
                    mods = [(node.module or "").split(".")[0]]
                for m in mods:
                    if m not in STDLIB_OK and m != "os":
                        errs.append("exempt module imports %s (not allowed)" % m)
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
        if exempt and mod == exempt["module"]:
            return
        if mod in STDLIB_OK:
            return
        mp = find_module(mod, libs)
        if not mp:
            errs.append("import %s: not an allowed module and not in the lib folders" % mod)
            return
        e, imps = scan(open(mp, encoding="utf-8").read(), os.path.basename(mp), {"eq_reader"}, False, libs)
        errs.extend(e)
        for m in sorted(imps):
            check_module(m, depth + 1)

    for i, st in enumerate(job.get("steps", []), 1):
        do = st.get("do")
        if do in META:
            continue
        if do in ("pull", "export"):
            errs.append("step %d: '%s' is not allowed in an equity job" % (i, do))
            continue
        if do != "python":
            errs.append("step %d: unknown step type %r" % (i, do))
            continue
        e, imps = scan(st.get("code", ""), "step %d" % i, trusted, bool(exempt), libs)
        errs.extend(e)
        for m in sorted(imps):
            check_module(m)
    if exempt:
        info.append("seal-exempt job (%s): module %s code sha256 %s input sha256 %s"
                    % (exempt["job_pattern"], exempt["module"], extra.get("code_sha256", "?"),
                       extra.get("input_sha256", "?")))
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
    jobs = jobs or [DEFAULT_JOB]
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
