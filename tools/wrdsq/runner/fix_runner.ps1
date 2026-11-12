# fix_runner.ps1 (2026-11-12): make the "WRDS runner" scheduled task tick every 10 minutes again and keep ticking.
# It keeps the task's action as it is and only replaces WHEN it runs and the power settings.
# Writes what it found and what it did to local\task_fix_report.txt (Claude reads that file).
$ErrorActionPreference = "Continue"
$name = "WRDS runner"
$rep = Join-Path $PSScriptRoot "local\task_fix_report.txt"
function Say($t) { Add-Content -Path $rep -Value $t }
Set-Content -Path $rep -Value ("fix_runner {0:yyyy-MM-dd HH:mm:ss}" -f (Get-Date))
try {
    $task = Get-ScheduledTask -TaskName $name -ErrorAction Stop
    $info = $task | Get-ScheduledTaskInfo
    Say ("BEFORE state={0} lastRun={1} lastResult={2} nextRun={3} missed={4}" -f $task.State, $info.LastRunTime, $info.LastTaskResult, $info.NextRunTime, $info.NumberOfMissedRuns)
    foreach ($t in $task.Triggers) {
        Say ("BEFORE trigger {0} start={1} end={2} enabled={3} interval={4} duration={5} stopAtEnd={6}" -f $t.CimClass.CimClassName, $t.StartBoundary, $t.EndBoundary, $t.Enabled, $t.Repetition.Interval, $t.Repetition.Duration, $t.Repetition.StopAtDurationEnd)
    }
    $s0 = $task.Settings
    Say ("BEFORE settings onBatteryStart={0} stopOnBattery={1} startWhenAvailable={2} timeLimit={3} multiple={4} idleOnly={5} networkOnly={6}" -f (-not $s0.DisallowStartIfOnBatteries), $s0.StopIfGoingOnBatteries, $s0.StartWhenAvailable, $s0.ExecutionTimeLimit, $s0.MultipleInstances, $s0.RunOnlyIfIdle, $s0.RunOnlyIfNetworkAvailable)
    Say ("BEFORE action {0} | user {1} logon {2} level {3}" -f (($task.Actions | ForEach-Object { $_.Execute + " " + $_.Arguments }) -join " ; ").Replace($env:USERPROFILE, "~"), "(current user)", $task.Principal.LogonType, $task.Principal.RunLevel)

    $r = (New-ScheduledTaskTrigger -Once -At "00:00" -RepetitionInterval (New-TimeSpan -Minutes 10) -RepetitionDuration (New-TimeSpan -Days 1)).Repetition
    $daily = New-ScheduledTaskTrigger -Daily -At "00:00"
    $daily.Repetition = $r
    $set = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Hours 4)
    try {
        Set-ScheduledTask -TaskName $name -Trigger $daily -Settings $set -ErrorAction Stop | Out-Null
        Say "CHANGED: runs every day from 00:00, repeating every 10 minutes all day; starts on battery; catches up after sleep"
    } catch {
        Say ("CHANGE FAILED: " + $_.Exception.Message)
    }
    Start-ScheduledTask -TaskName $name
    Start-Sleep -Seconds 5
    $task = Get-ScheduledTask -TaskName $name
    $info = $task | Get-ScheduledTaskInfo
    Say ("AFTER state={0} lastRun={1} lastResult={2} nextRun={3}" -f $task.State, $info.LastRunTime, $info.LastTaskResult, $info.NextRunTime)
    foreach ($t in $task.Triggers) {
        Say ("AFTER trigger {0} start={1} interval={2} duration={3}" -f $t.CimClass.CimClassName, $t.StartBoundary, $t.Repetition.Interval, $t.Repetition.Duration)
    }
} catch {
    Say ("ERROR: " + $_.Exception.Message)
}
Say "END"
Write-Host "Done. You can close this window."
