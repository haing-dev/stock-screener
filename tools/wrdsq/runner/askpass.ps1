# Answers ssh's password prompt for the WRDS runner. The password is stored with Windows DPAPI in
# %USERPROFILE%\.wrds\secret.txt: only this Windows user on this PC can decrypt it. Any other prompt (e.g. Duo) gets no
# answer, so the login fails safely and the runner reports it.
param([string]$prompt = "")
if ($prompt -notmatch "(?i)password") { exit 1 }
$f = Join-Path $env:USERPROFILE ".wrds\secret.txt"
if (-not (Test-Path $f)) { exit 1 }
$s = Get-Content $f | ConvertTo-SecureString
[Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s))
