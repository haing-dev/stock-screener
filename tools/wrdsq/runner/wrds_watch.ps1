# WRDS runner (Global Macro Book / wrdsq). Runs every 10 minutes as a Windows scheduled task.
# Claude drops job files into Documents\WRDS results\jobs (other projects) or Documents\Screenerdata\runner\jobs (stock
# screener); this script sends them to WRDS Cloud with the SSH key (Windows-encrypted password kept on this PC), saves the
# report to the matching results\ folder, and moves finished jobs to jobs\done. Only metadata and statistics come back
# to Claude; the data stays on WRDS, and exported files go straight to Documents\Screenerdata\data (the user's copy,
# never connected to Claude). Password and key never leave this PC.
$D = Join-Path $HOME "Documents\WRDS results"
$H = "ttdlisa@wrds-cloud.wharton.upenn.edu"
$O = @("-o", "StrictHostKeyChecking=accept-new", "-o", "ConnectTimeout=30", "-o", "NumberOfPasswordPrompts=1", "-o", "PreferredAuthentications=keyboard-interactive,password", "-o", "ServerAliveInterval=60", "-o", "ServerAliveCountMax=5")
$env:SSH_ASKPASS = Join-Path $D "askpass.cmd"; $env:SSH_ASKPASS_REQUIRE = "force"; $env:DISPLAY = "wrds"
# two job folders: Documents\WRDS results (other projects) and Documents\Screenerdata\runner (stock screener); each has
# jobs\, jobs\done\, lib\ and results\. Exported data goes to Documents\Screenerdata\data (never read by Claude).
$S = Join-Path $HOME "Documents\Screenerdata\runner"
$roots = @($D, $S)
foreach ($r in $roots) { New-Item -ItemType Directory -Force (Join-Path $r "jobs"), (Join-Path $r "jobs\done"), (Join-Path $r "results"), (Join-Path $r "lib") | Out-Null }
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
# one-time move of the stock screener's triage files out of WRDS results
foreach ($pat in @("jobs\tri_*.json", "jobs\tri_*.tries", "lib\tri_*.py", "results\tri_*")) {
    foreach ($f in @(Get-ChildItem -Path (Join-Path $D $pat) -File -ErrorAction SilentlyContinue)) {
        $sub = Split-Path -Parent $pat
        Move-Item -Force -Path $f.FullName -Destination (Join-Path (Join-Path $S $sub) $f.Name) -ErrorAction SilentlyContinue
    }
}
try {
    $pending = @($roots | ForEach-Object { Get-ChildItem -Path (Join-Path $_ "jobs") -Filter *.json -File } | Sort-Object LastWriteTime)
    if ($pending.Count -eq 0) { Set-Content -Path $status -Value ("idle, last check {0:yyyy-MM-dd HH:mm}" -f (Get-Date)); return }
    $ok = (& ssh @O $H "echo KEY_LOGIN_OK" 2>&1) -join " "
    if ($ok -notmatch "KEY_LOGIN_OK") {
        Log "login with key failed: $ok"
        Set-Content -Path $status -Value ("LOGIN FAILED {0:yyyy-MM-dd HH:mm}: WRDS may want Duo again. Tell Claude; usually logging in once in PowerShell (ssh $H) and approving Duo fixes it." -f (Get-Date))
        return
    }
    & scp @O (Join-Path $D "wrdsq.py") "${H}:~/wrdsq/wrdsq.py" 2>&1 | Out-Null
    foreach ($r in $roots) { foreach ($f in @(Get-ChildItem -Path (Join-Path $r "lib") -Filter *.py -File)) { & scp @O $f.FullName "${H}:~/wrdsq/lib/" 2>&1 | Out-Null } }
    foreach ($j in $pending) {
        $n = $j.BaseName
        $jobs = $j.DirectoryName; $done = Join-Path $jobs "done"; $res = Join-Path (Split-Path -Parent $jobs) "results"
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
    # downloads: files a job exported (~/wrdsq/export on WRDS) go to Documents\Screenerdata on this PC, then are removed
    # from WRDS (quota). Screenerdata is the user's own copy: it is never connected to Claude (WRDS AI policy).
    $dl = Join-Path $HOME "Documents\Screenerdata\data"
    $exp = @(& ssh @O $H "ls -1 ~/wrdsq/export 2>/dev/null" 2>$null) | Where-Object { $_ -and $_.Trim() }
    if ($exp.Count -gt 0) {
        New-Item -ItemType Directory -Force $dl | Out-Null
        & scp @O "${H}:~/wrdsq/export/*" $dl 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) {
            & ssh @O $H "rm -f ~/wrdsq/export/*" 2>&1 | Out-Null
            Log ("downloaded to Screenerdata: " + ($exp -join ", "))
        } else { Log "download of exports failed, will retry next round" }
    }
    Set-Content -Path $status -Value ("idle, last run {0:yyyy-MM-dd HH:mm}" -f (Get-Date))
}
finally { Remove-Item -Path $lock -ErrorAction SilentlyContinue }
