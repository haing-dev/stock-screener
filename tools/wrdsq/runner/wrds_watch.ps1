# WRDS runner (Global Macro Book / wrdsq). Runs every 10 minutes as a Windows scheduled task.
# Claude drops job files into Documents\WRDS results\jobs; this script sends them to WRDS Cloud with the SSH key
# (Windows-encrypted password kept on this PC), saves the report to Documents\WRDS results\results, and moves finished jobs to jobs\done.
# Only metadata and statistics come back; the data stays on WRDS. Password and key never leave this PC.
$D = Join-Path $HOME "Documents\WRDS results"
$H = "ttdlisa@wrds-cloud.wharton.upenn.edu"
$O = @("-o", "StrictHostKeyChecking=accept-new", "-o", "ConnectTimeout=30", "-o", "NumberOfPasswordPrompts=1", "-o", "PreferredAuthentications=keyboard-interactive,password", "-o", "ServerAliveInterval=60", "-o", "ServerAliveCountMax=5")
$env:SSH_ASKPASS = Join-Path $D "askpass.cmd"; $env:SSH_ASKPASS_REQUIRE = "force"; $env:DISPLAY = "wrds"
$jobs = Join-Path $D "jobs"; $done = Join-Path $jobs "done"; $res = Join-Path $D "results"; $lib = Join-Path $D "lib"
New-Item -ItemType Directory -Force $jobs, $done, $res, $lib | Out-Null
$log = Join-Path $D "runner_log.txt"; $status = Join-Path $D "runner_status.txt"; $lock = Join-Path $D "runner.lock"
function Log($m) { Add-Content -Path $log -Value ("{0:yyyy-MM-dd HH:mm} {1}" -f (Get-Date), $m) }
if (Test-Path $lock) {
    if (((Get-Date) - (Get-Item $lock).LastWriteTime).TotalHours -lt 3) { exit }
    # watchdog: a run older than 3 hours is stuck -> stop its ssh session and start over
    Get-CimInstance Win32_Process -Filter "Name='ssh.exe'" | Where-Object { $_.CommandLine -match "wrdsq.py job" } |
        ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
    Log "watchdog: previous run older than 3 hours was stopped"
}
Set-Content -Path $lock -Value (Get-Date)
try {
    $pending = @(Get-ChildItem -Path $jobs -Filter *.json -File | Sort-Object LastWriteTime)
    if ($pending.Count -eq 0) { Set-Content -Path $status -Value ("idle, last check {0:yyyy-MM-dd HH:mm}" -f (Get-Date)); return }
    $ok = (& ssh @O $H "echo KEY_LOGIN_OK" 2>&1) -join " "
    if ($ok -notmatch "KEY_LOGIN_OK") {
        Log "login with key failed: $ok"
        Set-Content -Path $status -Value ("LOGIN FAILED {0:yyyy-MM-dd HH:mm}: WRDS may want Duo again. Tell Claude; usually logging in once in PowerShell (ssh $H) and approving Duo fixes it." -f (Get-Date))
        return
    }
    & scp @O (Join-Path $D "wrdsq.py") "${H}:~/wrdsq/wrdsq.py" 2>&1 | Out-Null
    foreach ($f in @(Get-ChildItem -Path $lib -Filter *.py -File)) { & scp @O $f.FullName "${H}:~/wrdsq/lib/" 2>&1 | Out-Null }
    foreach ($j in $pending) {
        $n = $j.BaseName
        Set-Content -Path $status -Value ("running ${n} since {0:yyyy-MM-dd HH:mm}" -f (Get-Date))
        Log "running ${n}"
        & scp @O $j.FullName "${H}:~/wrdsq/jobs/inbox_${n}.json" 2>&1 | Out-Null
        $out = & ssh @O $H "timeout 3h python3 -u ~/wrdsq/wrdsq.py job @~/wrdsq/jobs/inbox_${n}.json" 2> (Join-Path $res "${n}.progress.txt")
        $txt = ($out -join "`r`n")
        Set-Content -Path (Join-Path $res "${n}.txt") -Value $txt -Encoding UTF8
        if ($txt -match "no WRDS compute node was available") { Log "${n}: no compute node, will retry"; continue }
        if ($txt -notmatch "=== END") {
            $tf = Join-Path $jobs "${n}.tries"; $k = 1; if (Test-Path $tf) { $k = [int](Get-Content $tf) + 1 }
            Set-Content -Path $tf -Value $k
            if ($k -lt 3) { Log "${n}: no complete report (attempt $k), will retry"; continue }
            Log "${n}: no complete report after 3 attempts, giving up"; Remove-Item $tf -ErrorAction SilentlyContinue
        }
        Move-Item -Force -Path $j.FullName -Destination (Join-Path $done $j.Name)
        Log "${n}: finished"
    }
    Set-Content -Path $status -Value ("idle, last run {0:yyyy-MM-dd HH:mm}" -f (Get-Date))
}
finally { Remove-Item -Path $lock -ErrorAction SilentlyContinue }
