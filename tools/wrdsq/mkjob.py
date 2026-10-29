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
a = p.parse_args()
spec = json.load(open(a.job))
code = base64.urlsafe_b64encode(zlib.compress(json.dumps(spec, separators=(",", ":")).encode(), 9)).decode().rstrip("=")
line = ('ssh %s@wrds-cloud.wharton.upenn.edu "python3 ~/wrdsq/wrdsq.py job %s" | Set-Content -Encoding utf8 '
        '"$HOME\\Downloads\\%s"' % (a.user, code, a.out))
if len(line) > 7000:
    raise SystemExit("Job too long for one pasted line (%d chars): shorten the code or split into two jobs." % len(line))
print(line)
