"""env_setup_v1: install the Python libraries the jobs need into Documents\\WRDS results\\local\\pylib (a private folder;
nothing is installed system-wide; delete the folder to undo). Prints versions only."""
import os
import subprocess
import sys

target = os.path.join(os.getcwd(), "pylib")
os.makedirs(target, exist_ok=True)
print("=== env_setup_v1 ===")
print("python", sys.version.split()[0], sys.executable)
try:
    print("installed pythons:", subprocess.run(["py", "-0p"], capture_output=True, text=True, timeout=60).stdout.strip().replace("\n", " ; "))
except Exception as e:
    print("py -0p failed", type(e).__name__)
for pkg in ("openpyxl", "numpy", "pandas", "scipy"):
    r = subprocess.run([sys.executable, "-m", "pip", "install", "--disable-pip-version-check", "--no-input", "--only-binary=:all:",
                        "--upgrade", "--target", target, pkg], capture_output=True, text=True, timeout=1800)
    tail = (r.stdout.strip().splitlines() or [""])[-1][:200]
    err = (r.stderr.strip().splitlines() or [""])[-1][:300]
    print("pip", pkg, "exit", r.returncode, "|", tail, "|", err)
sys.path.insert(0, target)
for m in ("openpyxl", "numpy", "pandas", "scipy"):
    try:
        mod = __import__(m)
        print("import", m, getattr(mod, "__version__", "ok"))
    except Exception as e:
        print("import", m, "FAILED", type(e).__name__, str(e)[:150])
print("=== END ===")
