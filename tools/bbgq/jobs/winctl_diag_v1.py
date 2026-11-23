"""winctl_diag_v1: find which Windows policy blocks the compiled pandas files in local\\pylib (stdlib only).
Prints: Smart App Control state, Device Guard / code integrity status, the last code-integrity block events (file and
policy names only), and which pylib files are affected. Reads system settings; changes nothing."""
import os, subprocess, sys, time
T0 = time.time()
def run(cmd, limit=4000):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120, shell=isinstance(cmd, str))
        out = (r.stdout or "") + (("\n[stderr] " + r.stderr) if r.stderr.strip() else "")
        return out.strip()[:limit] or "(no output)"
    except Exception as e:  # noqa: BLE001
        return "ERROR %s %s" % (type(e).__name__, str(e)[:300])
print("=== winctl_diag_v1 ===")
print("python:", sys.version.split()[0], sys.executable)
print("\n--- Smart App Control (VerifiedAndReputablePolicyState: 0 off, 1 on/enforce, 2 evaluation) ---")
print(run(["reg", "query", r"HKLM\SYSTEM\CurrentControlSet\Control\CI\Policy", "/v", "VerifiedAndReputablePolicyState"]))
print("\n--- Device Guard / code integrity status ---")
print(run('powershell -NoProfile -Command "Get-CimInstance -Namespace root\\Microsoft\\Windows\\DeviceGuard '
          '-ClassName Win32_DeviceGuard | Select-Object CodeIntegrityPolicyEnforcementStatus,'
          'UsermodeCodeIntegrityPolicyEnforcementStatus,SecurityServicesRunning | Format-List"'))
print("\n--- Active code integrity policies (CiTool; may need admin) ---")
print(run(["CiTool.exe", "--list-policies"], 3000))
print("\n--- Last code-integrity block events (3033/3034/3076/3077/3089) ---")
q = "*[System[(EventID=3033 or EventID=3034 or EventID=3076 or EventID=3077)]]"
ev = run(["wevtutil", "qe", "Microsoft-Windows-CodeIntegrity/Operational", "/q:" + q, "/c:8", "/rd:true", "/f:text"], 12000)
keep = [l for l in ev.splitlines() if any(k in l for k in ("Date:", "Event ID:", "Description", "attempted", "Policy",
                                                           "policy", ".pyd", ".dll", "Smart App", "did not meet", "[stderr]", "ERROR"))]
print("\n".join(keep[:80]) or ev[:3000])
print("\n--- Organisation management (MDM enrolment hints) ---")
print(run(["reg", "query", r"HKLM\SOFTWARE\Microsoft\Enrollments", "/s", "/f", "ProviderID", "/d"], 1500))
print("\n--- pylib compiled files (count, newest dates) ---")
base = os.path.join(os.getcwd(), "pylib")
pyd = []
for root, _, files in os.walk(base):
    for f in files:
        if f.endswith((".pyd", ".dll")):
            p = os.path.join(root, f); pyd.append((os.path.getmtime(p), p))
print("compiled files in pylib:", len(pyd))
for m, p in sorted(pyd)[-5:]:
    print(time.strftime("%Y-%m-%d %H:%M", time.localtime(m)), p.replace(base, "pylib"))
print("=== END === %.0fs" % (time.time() - T0))
