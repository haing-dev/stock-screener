#!/usr/bin/env bash
# Run a command, keep its output in the normal log, and on failure copy the last lines into GitHub
# annotations (visible on the run's summary page and through the API, without opening the raw log).
set -o pipefail
log="$(mktemp)"
"$@" 2>&1 | tee "$log"
status=${PIPESTATUS[0]}
if [ "$status" -ne 0 ]; then
  tail -n 60 "$log" | sed -E 's/(sk-ant-[A-Za-z0-9_-]{6})[A-Za-z0-9_-]+/\1.../g; s/(apiKey=)[^& ]+/\1.../g' > "$log.tail"
  for part in 0 1 2; do
    chunk="$(sed -n "$((part*20+1)),$((part*20+20))p" "$log.tail")"
    [ -z "$chunk" ] && continue
    chunk="${chunk//'%'/'%25'}"; chunk="${chunk//$'\n'/'%0A'}"; chunk="${chunk//$'\r'/}"
    echo "::error title=Failed: $1 $2 (log lines $((part*20+1))-$((part*20+20)) of the last 60)::$chunk"
  done
fi
exit "$status"
