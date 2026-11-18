"""Search patterns for matching library investors to 13F filers and CRSP funds (step E0.4, phase A: no returns).

    python3 tools/equity/match_patterns.py docs/research/equity/inventory/investors.csv > patterns.json

For every person coded as having run money: regular expressions (Postgres, case-insensitive, word starts) built from
the firm names in the notes, and the surname for the fund-manager name field. Hand overrides at the bottom cover
firms whose filing name differs from the name used in conversation."""
import csv
import json
import re
import sys
import unicodedata

GENERIC = set("""capital management partners partner fund funds asset assets investment investments investors advisors
advisers advisor group llc lp inc corp corporation company co the and of formerly associates holdings global
international equity wealth research family office podcast club firm financial""".split())
ABBR = {"capital": "cap", "management": "(mgmt|manag|mgt)", "partners": "(part|ptn)", "investment": "inv",
        "investments": "inv", "advisors": "adv", "advisers": "adv", "asset": "ass", "associates": "ass",
        "fund": "(fund|fd)", "funds": "(fund|fd)", "group": "(group|grp)"}
OVERRIDE = {  # investor name -> extra patterns
    "Chris Davis": [r"\mdavis\M.*\m(sel|adv|n\.?y)"], "Tom Gayner": [r"\mmarkel\M"],
    "Bill Nygren": [r"\mharris\M.*\mass", r"\moakmark\M"], "Alex Fitch": [r"\mharris\M.*\mass", r"\moakmark\M"],
    "Chris Hohn": [r"\mtci\M", r"children.?s inv"], "Jeremy Grantham": [r"\mgrantham\M", r"\mgmo\M"],
    "Joel Greenblatt": [r"\mgotham\M.*\m(ass|cap|fund)"], "Rob Goldstein": [r"\mgotham\M.*\m(ass|cap|fund)"],
    "Tobias Carlisle": [r"\macquirers\M", r"\mdeep value etf"], "Murray Stahl": [r"\mhorizon\M.*\mkinetics", r"\mkinetics\M"],
    "Warren Buffett": [r"\mberkshire hathaway\M"], "Charlie Munger": [r"\mberkshire hathaway\M", r"\mdaily journal\M"],
    "Terry Smith": [r"\mfundsmith\M"], "Howard Marks": [r"\moaktree\M"], "Dan Sundheim": [r"\md1 cap"],
    "Robert Vinall": [r"\mrv cap", r"\mbusiness owner\M"], "Guy Spier": [r"\maquamarine\M"],
    "Samantha McLemore": [r"\mpatient cap", r"\mmiller value\M"], "Bill Miller IV": [r"\mmiller value\M"],
    "Cathie Wood": [r"\mark inv"], "Ken Fisher": [r"\mfisher\M.*\m(inv|ass)"], "Dan Loeb": [r"\mthird point\M"],
    "Paul Singer": [r"\melliott\M.*\m(man|mgmt|inv|ass)"], "Ken Griffin": [r"\mcitadel adv"],
    "Steve Cohen": [r"\mpoint72\M", r"\msac cap"], "Li Lu": [r"\mhimalaya cap"], "Seth Klarman": [r"\mbaupost\M"],
    "Stan Druckenmiller": [r"\mduquesne\M"], "David Tepper": [r"\mappaloosa\M"], "Steve Eisman": [r"\memrys\M"],
    "Paul Tudor Jones": [r"\mtudor inv"], "Prem Watsa": [r"\mfairfax fin"], "Bruce Berkowitz": [r"\mfairholme\M"],
    "Jim Chanos": [r"\mkynikos\M", r"\mchanos\M"], "Leon Cooperman": [r"\momega adv"], "Nick Sleep": [r"\mnomad inv"],
    "Thomas Russo": [r"\mgardner russo\M"], "John Spears": [r"\mtweedy\M"], "Matthew McLennan": [r"\mfirst eagle\M"],
    "Ray Dalio": [r"\mbridgewater ass"], "Pat Dorsey": [r"\mdorsey ass"], "David Einhorn": [r"\mgreenlight cap"],
    "Dmitry Balyasny": [r"\mbalyasny\M"], "Philippe Laffont": [r"\mcoatue\M"], "Thomas Laffont": [r"\mcoatue\M"],
    "Brad Gerstner": [r"\maltimeter\M"], "Alex": [r"\mwhale rock\M"], "Alex Sacerdote": [r"\mwhale rock\M"],
    "Joel Tillinghast": [r"\mfidelity low.?priced"], "Anthony Bolton": [r"\mfidelity\M.*\m(special|china)"],
    "James Anderson": [r"\mbaillie gifford\M", r"\mscottish mortgage\M"], "Paul Marshall": [r"\mmarshall wace\M"],
    "John Armitage": [r"\megerton\M"], "Kelly Granat": [r"\mlone pine\M"], "Mala Gaonkar": [r"\msurgocap\M"],
    "Ben Silver": [r"\mmaverick cap"], "David Tykoczynski": [r"\mmaverick cap"], "Graeme Forster": [r"\morbis\M"],
    "Paul Enright": [r"\mkrano", r"\mviking global\M"], "Henry Ellenbogen": [r"\mdurable cap"],
    "Joseph Shaposhnik": [r"\mrainwater\M", r"\mtcw\M.*\m(new america|concentrated|select)"],
    "Mohnish Pabrai": [r"\mpabrai\M", r"\mdalal street\M"], "Ian Cassel": [r"\mintelligent fanatics\M"],
    "Vitaliy Katsenelson": [r"\minvestment management ass", r"\mima\M"], "Laura Geritz": [r"\mrondure\M"],
    "Paul Black": [r"\mwcm inv"], "Peter Keefe": [r"\mavenir corp"], "Jason Donville": [r"\mdonville\M"],
    "Jesse Gamble": [r"\mdonville\M"], "Harris Kupperman": [r"\mpraetorian\M"], "Bob Robotti": [r"\mrobotti\M"],
    "Dan Rasmussen": [r"\mverdad\M"], "Eddy Elfenbein": [r"\madvisorshares focused eq"], "Pete Muller": [r"\mpdt part"],
    "Ricky Sandler": [r"\meminence cap"], "Carson Block": [r"\mmuddy waters\M"], "Sander Gerber": [r"\mhudson bay cap"],
    "Arnold Van Den Berg": [r"\mcentury man", r"\mvan den berg\M"], "Bill Priest": [r"\mepoch inv"],
    "Fred Martin": [r"\mdisciplined growth\M"], "Andrew Brenton": [r"\mturtle creek\M"], "Jeff Yass": [r"\msusquehanna\M"],
    "Gavin Baker": [r"\matreides\M"], "Arif Karim": [r"\mensemble cap"], "Josh Young": [r"\mbison int"],
}


def toks(firm):
    s = unicodedata.normalize("NFKD", firm).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", " ", s)
    return [w for w in re.sub(r"[^a-z0-9& ]", " ", s).split() if w not in ("&",)]


def pattern(firm):
    w = toks(firm)
    d = [x for x in w if x not in GENERIC]
    if not d:
        return None
    t1 = d[0]
    if len(d) >= 2 and len(t1) < 8:
        return r"\m%s\M.*\m%s" % (re.escape(t1), re.escape(d[1][:5]))
    if len(t1) >= 6:
        return r"\m%s" % re.escape(t1)
    rest = w[w.index(t1) + 1:]
    if rest:
        return r"\m%s\M.*\m%s" % (re.escape(t1), ABBR.get(rest[0], re.escape(rest[0][:4])))
    return None


def main(path):
    out = []
    for p in csv.DictReader(open(path, encoding="utf-8")):
        if p["ran_money"] != "yes":
            continue
        firms = [re.sub(r" \(\d+\)$", "", f).strip() for f in p["firms"].split(";") if f.strip()]
        pats = []
        for f in firms:
            for part in re.split(r",|/| formerly ", f):
                x = pattern(part)
                if x and x not in pats:
                    pats.append(x)
        for x in OVERRIDE.get(p["name"], []):
            if x not in pats:
                pats.append(x)
        w = toks(p["name"])
        sur = w[-1] if len(w) >= 2 and w[-1] not in ("iv", "jr") else (w[-2] if len(w) >= 3 else "")
        out.append({"id": p["id"], "name": p["name"], "firms": firms, "patterns": pats[:6],
                    "surname": sur if len(sur) >= 4 else "", "first": w[0] if w else ""})
    json.dump(out, sys.stdout, indent=0)


if __name__ == "__main__":
    main(sys.argv[1])
