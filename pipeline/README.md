# Argument-map pipeline (transcripts)
Restore into a work dir L0/: copy pipeline/docs -> L0/docs, pipeline/maps -> L0/maps, ledger/ -> L0/ledger,
manifest.json, build.py, pipeline/*.md|csv|txt -> L0/, pipeline/tmp/m01/validate.py -> L0/tmp/m01/.
Queue: maps_queue.txt (tier A by priority). Spec: TRANSCRIPT_MAP_SPEC.md (Sonnet high, 5 transcripts per agent).
Maps render into Sources notes via build.py (section "Argument map").
