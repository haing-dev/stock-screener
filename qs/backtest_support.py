"""Small helpers shared by the validation modules (paths, gzip JSON)."""
import gzip
import json
import os

from .config import CACHE_DIR, ROOT

WORK = os.path.join(CACHE_DIR, "bt", "work")
OUT = os.path.join(ROOT, "validation", "out")


def ensure_dirs(*dirs):
    for d in dirs:
        os.makedirs(d, exist_ok=True)


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        json.dump(obj, f, separators=(",", ":"), default=str)
    os.replace(tmp, path)


def read_json(path):
    try:
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError, EOFError):
        return None
