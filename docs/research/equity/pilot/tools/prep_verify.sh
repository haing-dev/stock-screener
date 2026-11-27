#!/bin/bash
# prep_verify.sh CODE "Investor name (fund)" SEED  -- after all docs of CODE are extracted in $B/<DOC>/
set -e
B=/tmp/claude-0/-home-claude/c6d39485-a0af-5a90-b220-a415744a715e/scratchpad/pilot3
P=/home/claude/stock-screener/docs/research/equity/pilot
CODE=$1; NAME=$2; SEED=$3
R=$P/batch2/$CODE; mkdir -p $R/claims $R/verify $B/V_$CODE
for f in $B/src/$CODE*.txt; do d=$(basename $f .txt); python3 $P/tools/check_quotes.py $f $B/$d/$d.claims.json $R/claims/$d.checked.json; done
python3 $P/tools/make_verify_set.py $B/src $SEED $R/verify $R/claims/*.checked.json
cp $R/verify/verify_items.json $P/CLAIM_SPEC_v1.1.md $B/V_$CODE/
N=$(python3 -c "import json;print(len(json.load(open('$R/verify/verify_items.json'))))")
python3 - "$NAME" "$N" "$P/BRIEF_VERIFY_v1.1.md" "$B/V_$CODE/BRIEF_VERIFY.md" <<'PY'
import sys
name,n,src,dst=sys.argv[1:]
t=open(src).read()
t=t.replace("from five interviews with Dev Kantesaria (Valley\nForge Capital) and tagged them","from interviews with %s and tagged them"%name)
t=t.replace("(292 items","(%s items"%n).replace("Kantesaria's own words","the investor's own words")
assert "Kantesaria" not in t, "brief still names Kantesaria"
open(dst,"w").write(t)
PY
head -5 $B/V_$CODE/BRIEF_VERIFY.md
