"""Score the blind verification (A10 item 8). Fixed before the verifier's tags were read.

python3 score_verify.py verify_key.json tags.json OUT.md
Pass (all four): rule-like agreement >= 90%, part >= 85%, computable >= 85% (planted items excluded), and at least 9 of
10 planted items caught. Rule-like = kind rule or threshold. A planted anecdote is caught when the verifier does not tag
it rule or threshold; a planted altered threshold is caught when the verifier gives a value and none of its numbers
is an altered number (v1.1, stricter than v1, where an empty value also counted as caught). Also lists the disputes (rule-like disagreements) for the third reading.
"""
import json
import re
import sys


WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
         "eleven": 11, "twelve": 12, "fifteen": 15, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
         "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100, "half": 0.5, "third": 0.333, "quarter": 0.25}


def nums(v):
    """digits and (v1.2, A13 item 10) number words; a verifier copies numbers as stated, often in words"""
    v = v or ""
    out = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", v)]
    out += [float(WORDS[w]) for w in re.findall(r"[a-z]+", v.lower()) if w in WORDS]
    return sorted(out)


def main():
    key = {k["vid"]: k for k in json.load(open(sys.argv[1], encoding="utf-8"))}
    tag = {t["vid"]: t for t in json.load(open(sys.argv[2], encoding="utf-8"))}
    missing = sorted(set(key) - set(tag))
    real = [v for v in key if not key[v]["planted"] and v in tag]
    rl = lambda k: k in ("rule", "threshold")
    a_rule = sum(rl(key[v]["kind"]) == rl(tag[v]["kind"]) for v in real) / len(real)
    a_part = sum(key[v]["part"] == tag[v]["part"] for v in real) / len(real)
    a_comp = sum(key[v]["computable"] == tag[v]["computable"] for v in real) / len(real)
    caught = []
    for v, k in key.items():
        if not k["planted"] or v not in tag:
            continue
        if k["planted"] == "anecdote_as_rule":
            ok = not rl(tag[v]["kind"])
        else:
            got = nums(tag[v].get("value"))
            ok = bool(got) and not (set(got) & set(nums(k["value"])) - set(nums(k.get("true_value"))))  # v1.1 stricter
        caught.append((v, k["planted"], ok, tag[v]["kind"], tag[v].get("value", "")))
    n_caught = sum(c[2] for c in caught)
    disputes = [v for v in real if rl(key[v]["kind"]) != rl(tag[v]["kind"])]
    spk = [v for v in tag if str(tag[v].get("speaker_ok", "yes")).lower() != "yes"]
    ok = a_rule >= 0.90 and a_part >= 0.85 and a_comp >= 0.85 and n_caught >= len(caught) - 1 and not missing  # = 9 of 10; A13 item 9 when fewer plants exist
    L = ["# Blind verification score", "",
         "| Measure | Result | Bar |", "|---|---|---|",
         "| Items scored (not planted) | %d | |" % len(real),
         "| Missing tags | %d | 0 |" % len(missing),
         "| Rule-like agreement | %.1f%% | >= 90%% |" % (100 * a_rule),
         "| Part agreement | %.1f%% | >= 85%% |" % (100 * a_part),
         "| Computable agreement | %.1f%% | >= 85%% |" % (100 * a_comp),
         "| Planted caught | %d of %d | all but one |" % (n_caught, len(caught)),
         "", "**Result: %s**" % ("PASS" if ok else "FAIL"), "",
         "## Planted items", "| vid | type | caught | verifier kind | verifier value |", "|---|---|---|---|---|"]
    L += ["| %s | %s | %s | %s | %s |" % (v, p, "yes" if c else "NO", kd, val) for v, p, c, kd, val in caught]
    L += ["", "## Disputes for the third reading (%d)" % len(disputes), "| vid | id | first | second | quote |",
          "|---|---|---|---|---|"]
    L += ["| %s | %s | %s | %s | %s |" % (v, key[v]["id"], key[v]["kind"], tag[v]["kind"],
                                          key[v]["quote"][:90].replace("|", "/")) for v in disputes]
    L += ["", "Speaker not confirmed by the verifier: %s" % (", ".join("%s (%s)" % (v, key[v]["id"]) for v in spk) or "none")]
    open(sys.argv[3], "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[:14]))


if __name__ == "__main__":
    main()
