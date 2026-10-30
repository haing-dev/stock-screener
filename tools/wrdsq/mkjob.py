#!/usr/bin/env python3
"""Build the one-line PowerShell command that runs a wrdsq job on WRDS Cloud.

  python3 mkjob.py job.json [--user ttdlisa] [--out wrds_result.txt]
Prints the line. The user pastes it into Windows PowerShell, types the WRDS password, approves Duo, and attaches
the result file (Downloads) to the chat. Job JSON format: see wrdsq.py docstring."""
import argparse
import base64
import json
import zlib

p = argparse.ArgumentParser()
p.add_argument("job")
p.add_argument("--user", default="ttdlisa")
p.add_argument("--out", default="wrds_result.txt")
p.add_argument("--update", action="store_true", help="first copy Downloads\\wrdsq.py to WRDS")
a = p.parse_args()
spec = json.load(open(a.job))
code = base64.urlsafe_b64encode(zlib.compress(json.dumps(spec, separators=(",", ":")).encode(), 9)).decode().rstrip("=")
D = '$HOME\\Documents\\WRDS results'
H = "%s@wrds-cloud.wharton.upenn.edu" % a.user
line = ('New-Item -ItemType Directory -Force "%s" | Out-Null; ' % D +
        'Write-Host "Connecting to WRDS: paste your password, press Enter, approve Duo" -ForegroundColor Cyan; ')
if a.update:
    line += 'scp -o StrictHostKeyChecking=accept-new $HOME\\Downloads\\wrdsq.py %s:~/wrdsq/wrdsq.py; ' % H
line += ('ssh -o StrictHostKeyChecking=accept-new %s "python3 -u ~/wrdsq/wrdsq.py job %s" | Out-File -Encoding utf8 "%s\\%s"; '
         'Write-Host "Done. Result saved in Documents\\WRDS results\\%s" -ForegroundColor Cyan' % (H, code, D, a.out, a.out))
if len(line) > 7000:
    raise SystemExit("Job too long for one pasted line (%d chars): shorten the code or split into two jobs." % len(line))
print(line)
