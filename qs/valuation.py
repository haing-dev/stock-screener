"""Price-dependent metrics: market cap, enterprise value and multiples.

Market cap = price x shares. Shares come from SEC filings:
  * single share class: cover-page shares outstanding (dei EntityCommonStockSharesOutstanding) if it is less
    than 9 months old, else the latest weighted diluted share count;
  * several listed share classes (e.g. GOOGL/GOOG): the latest weighted diluted share count, which covers all
    classes. Classes with different economics (e.g. BRK-A/BRK-B) are caught by the sanity check below.
Sanity check: market cap must be within 0.55x-8x of the public float the company itself reported (dei
EntityPublicFloat, as of its last second quarter). Failing it moves the company to 'Check manually'.
Foreign issuers filing 20-F usually trade as ADRs whose ratio to ordinary shares isn't in XBRL, so their
market cap is marked 'unverified' and price-based rules return NO DATA rather than a wrong number.
"""
from datetime import date

from .extract import _d


def _ratio(a, b):
    if a is None or b is None or b == 0:
        return None
    return a / b


def value(m, info, quote, fx, today=None, td=None, listing_type=None):
    """m: metrics; info: universe/profile row; quote: prices record; fx: rate to USD for m['currency'];
    td: the Twelve Data client (for a historical price when the float check needs one); listing_type: Twelve Data
    instrument type of the listed symbol ('Common Stock', 'Depositary Receipt'...).
    Returns a dict of valuation fields (all prefixed for clarity) including 'val_ok' and 'val_issue'."""
    today = today or date.today()
    v = {"price": None, "price_date": None, "market_cap_usd": None, "ev_usd": None, "val_ok": False,
         "val_issue": "", "shares_used": None, "shares_source": None, "adv_usd": None}
    if not quote or not quote.get("ok"):
        v["val_issue"] = (quote or {}).get("reason") or "no price"
        return v
    v["price"], v["price_date"] = quote["price"], quote["price_date"]
    v["price_open"], v["price_source"] = quote.get("open"), quote.get("source") or "Twelve Data"
    if not listing_type and quote.get("listing_type"):
        listing_type = quote["listing_type"]
    if quote.get("avg_volume"):
        v["adv_usd"] = quote["avg_volume"] * quote["price"]
    if fx is None:
        v["val_issue"] = f"no FX rate for {m.get('currency')}"
        return v
    issues = []
    multi = len(common_classes(info.get("all_tickers") or [])) > 1
    dei, dei_date = m.get("dei_shares"), m.get("dei_shares_date")
    dil, dil_date = m.get("diluted_shares_latest"), m.get("diluted_shares_date")
    shares, src = None, None
    eps_sh, eps_date = m.get("eps_shares"), m.get("eps_shares_date")
    if not multi and dei and dei_date and (today - _d(dei_date)).days <= 270:
        shares, src = dei, f"cover page shares ({dei_date})"
    elif dil:
        shares, src = dil, f"weighted diluted shares ({dil_date})" + (" - multiple share classes" if multi else "")
    elif eps_sh and eps_date and (today - _d(eps_date)).days <= 550:
        # share counts tagged only per class (Visa, Clear Secure...): net income / diluted EPS
        shares, src = eps_sh, f"net income / diluted EPS (year ending {eps_date})"
    elif dei:
        shares, src = dei, f"cover page shares ({dei_date}, older than 9 months)"
        issues.append("share count older than 9 months")
    if not shares:
        v["val_issue"] = "no share count in SEC data"
        return v
    # a split after the date of that share count (before the next filing) would put the market cap off by the
    # split ratio: put the count on today's basis with the split list (Massive)
    # (statements filed after a split already restate share counts retroactively, so the FILING date counts for
    # weighted and EPS-implied shares; the cover-page count is dated at the cover date, close to filing)
    sdate = {"cover": dei_date, "weighted": m.get("diluted_shares_filed"),
             "net": m.get("eps_shares_filed")}.get(src.split(" ")[0])
    if m.get("recent_splits") and sdate:
        from .massive import split_factor
        f = split_factor(m["recent_splits"], after=sdate, until=quote.get("price_date"))
        if f != 1.0:
            shares = shares / f
            src += f" x {1 / f:g} for a split since then"
    v["shares_used"], v["shares_source"] = shares, src
    mcap = quote["price"] * shares
    v["market_cap_usd"] = mcap
    form = ((info.get("latest_annual") or {}).get("form") or "")
    lt = str(listing_type or "")
    v["listing_type"] = lt or None
    if form.startswith("20-F"):
        if lt and ("Common" in lt or "Ordinary" in lt) and "Depositary" not in lt:
            pass   # ordinary shares listed directly (InMode, Check Point, Nova...): one share = one share
        else:
            issues.append("foreign issuer (20-F) listed as " + (lt or "an ADR?") + ": ADR ratio unknown, market "
                          "cap unverified")
    pf = m.get("public_float")
    if pf and pf > 0:
        r = mcap / pf
        v["mcap_to_public_float"] = r
        if not 0.55 <= r <= 8:
            # outside the usual range: a big price move since the float date (ZTS, Pool...) or heavy insider
            # ownership (Ubiquiti) - or a wrong share count. Decide with the price ON the float date.
            ok = None
            pf_date = m.get("public_float_date")
            close = m.get("pf_close")
            if not close and td is not None and pf_date and quote.get("symbol"):
                close = td.close_on(quote["symbol"], pf_date)
            if close:
                float_shares = pf / close
                ok = shares >= 0.7 * float_shares and float_shares >= 0.02 * shares
                v["float_check"] = (f"public float ${pf / 1e6:,.0f}M at ${close:.2f} on {pf_date} = "
                                    f"{float_shares / 1e6:,.1f}M shares vs {shares / 1e6:,.1f}M shares used")
            if ok is None:
                issues.append(f"market cap is {r:.1f}x the public float the company reported - share count or "
                              f"share class mismatch likely")
            elif not ok:
                issues.append("share count doesn't fit the public float even at the price on the float date - "
                              "share count or share class mismatch likely")
    elif multi:
        issues.append("multiple share classes and no public float to cross-check the market cap")
    # enterprise value (balance sheet in reporting currency -> USD)
    debt = m.get("bs_debt")
    cash = m.get("bs_cash_and_sti")
    if cash is None:
        issues.append("no balance-sheet cash")
    # long-term marketable securities are cash-like too (one net-debt definition with the leverage rules)
    claims = (debt or 0) + (m.get("bs_minority_interest") or 0) + (m.get("bs_preferred") or 0) - (cash or 0) \
        - (m.get("bs_lt_investments") or 0)
    ev = mcap + claims * fx
    v["ev_usd"] = ev
    ebit = m.get("ttm_operating_income")
    ebitda = m.get("ttm_ebitda")
    rev = m.get("ttm_revenue")
    ni = m.get("ttm_net_income")
    fcf = m.get("ttm_fcf")
    nebit = m.get("normalized_ebit")
    v["ev_ebit"] = (ev / (ebit * fx)) if (ebit and ebit > 0) else None
    v["ev_ebitda"] = (ev / (ebitda * fx)) if (ebitda and ebitda > 0) else None
    v["ev_sales"] = (ev / (rev * fx)) if (rev and rev > 0) else None
    v["pe"] = (mcap / (ni * fx)) if (ni and ni > 0) else None
    v["earnings_yield"] = (ebit * fx / ev) if (ebit is not None and ev and ev > 0) else None
    v["fcf_yield"] = (fcf * fx / mcap) if (fcf is not None and mcap > 0) else None
    v["ev_normalized_ebit"] = (ev / (nebit * fx)) if (nebit and nebit > 0) else None
    liquid = m.get("liquid_assets")
    if liquid:
        ev_cash = mcap + ((debt or 0) - liquid) * fx
        v["ev_incl_lt_investments_usd"] = ev_cash
        v["ev_to_liquid_assets"] = ev_cash / (liquid * fx)
        v["mcap_to_liquid_assets"] = mcap / (liquid * fx)
        burn = m.get("annual_cash_burn")
        if burn is not None and mcap > 0:
            # clinical-stage biotech: the 2-year funding gap against one normal equity raise (10-20% of market cap),
            # and the market value against the cash left after a further year of burn, net of debt
            v["funding_gap_to_mcap"] = max(0.0, 2 * burn - liquid) * fx / mcap
            left = liquid - (debt or 0) - burn
            v["cash_after_burn_usd"] = left * fx
            v["mcap_to_cash_after_burn"] = mcap / (left * fx) if left > 0 else None
    # ---- second-batch screens
    tb, nc, f5 = m.get("tangible_book"), m.get("net_cash"), m.get("fcf_avg_5y")
    v["price_to_tangible_book"] = (mcap / (tb * fx)) if (tb and tb > 0) else None
    v["mcap_to_net_cash"] = (mcap / (nc * fx)) if (nc and nc > 0) else None
    v["fcf_yield_5y"] = (f5 * fx / mcap) if (f5 is not None and mcap > 0) else None
    # insider (affiliate) ownership = 1 - public float / market value, both on the float date: the float the company
    # reported divided by the close on that date gives the non-affiliate shares (Stahl's owner-operators)
    raw, near = m.get("pf_close_raw"), m.get("dei_shares_near_float")
    adj = m.get("pf_close")
    if pf and pf > 0 and raw and near:
        # both as of the float date: the close as printed that day and the cover-page share count of that time
        nd = m.get("dei_shares_near_float_date")
        if m.get("recent_splits"):
            # a split between the float date and that cover date: back to the float date's basis
            from .massive import split_factor
            lo, hi = sorted([str(m.get("public_float_date")), str(nd)])
            f = split_factor(m["recent_splits"], after=lo, until=hi)
            near = near * f if str(nd) >= str(m.get("public_float_date")) else near / f
        float_shares, shares_then = pf / raw, near
        basis = f"{near / 1e6:,.1f}M shares outstanding near {m.get('public_float_date')} (cover page of {nd})"
    elif pf and pf > 0 and adj and shares:
        # Twelve Data: split-adjusted close (today's basis). The cover-page count near the float date is used unless
        # the change since looks like a split (then today's count, already on the new basis)
        r = (shares / near) if near else None
        split_like = r is not None and any(abs(r * k - 1) < 0.04 or abs(r / k - 1) < 0.04 for k in range(2, 11))
        if near and not split_like:
            float_shares, shares_then = pf / adj, near
            basis = f"{near / 1e6:,.1f}M shares on the {m.get('dei_shares_near_float_date')} cover page"
        else:
            float_shares, shares_then = pf / adj, shares
            basis = "today's share count"
    else:
        float_shares = shares_then = basis = None
        if pf and raw and not near:
            v["insider_issue"] = "no cover-page share count near the public-float date"
    if float_shares and shares_then:
        if float_shares <= 1.05 * shares_then:
            v["insider_share"] = max(0.0, 1 - float_shares / shares_then)
            v["insider_basis"] = basis
        else:
            v["insider_issue"] = (f"public float ({float_shares / 1e6:,.1f}M shares on {m.get('public_float_date')}) "
                                  f"exceeds the {shares_then / 1e6:,.1f}M shares outstanding then")
    # fall from the 12-month high (month-end closes from Massive, or Twelve Data's 52-week high)
    highs = [x for x in (m.get("high_12m"), quote.get("fifty_two_week_high"))
             if isinstance(x, (int, float)) and x > 0]
    if highs:
        h = max(highs + [quote["price"]])
        v["high_12m_used"] = h
        v["drawdown_12m"] = quote["price"] / h - 1
    if not names_match(quote.get("name"), info.get("name")):
        issues.append(f"quote name '{quote.get('name')}' doesn't match the SEC name - recycled ticker?")
    v["val_issue"] = "; ".join(issues)
    v["val_ok"] = not issues
    if issues:
        # keep the numbers for display, but never let a doubtful market cap pass or fail a rule
        for k in GATE_INPUTS:
            if v.get(k) is not None:
                v[k + "_unverified"] = v[k]
                v[k] = None
    return v


GATE_INPUTS = ("market_cap_usd", "ev_usd", "ev_ebit", "ev_ebitda", "ev_sales", "pe", "earnings_yield", "fcf_yield",
               "ev_normalized_ebit", "ev_to_liquid_assets", "mcap_to_liquid_assets", "ev_incl_lt_investments_usd",
               "price_to_tangible_book", "mcap_to_net_cash", "fcf_yield_5y", "insider_share")
AUX_SUFFIXES = ("W", "WS", "WT", "U", "UN", "R", "RT", "RW")
STOP = {"inc", "corp", "corporation", "co", "company", "ltd", "plc", "the", "holdings", "group", "class", "common",
        "stock", "shares", "sa", "nv", "ag", "se", "llc", "lp", "de"}


def _norm_name(s):
    import re
    s = re.sub(r"['\u2019`.]", "", str(s or "").lower())      # Moody's -> moodys, D.R. -> dr
    s = re.sub(r"/[a-z]{2}/", " ", s)                        # SEC state suffix /DE/
    return [w for w in re.sub(r"[^a-z0-9 ]", " ", s).split() if w not in STOP]


def names_match(a, b):
    """Loose company-name match (quote vs SEC): a shared word of 3+ letters, or the same name with spaces
    removed / one a prefix of the other (ExxonMobil vs Exxon Mobil). Unknown names count as a match."""
    wa, wb = _norm_name(a), _norm_name(b)
    if not wa or not wb:
        return True
    if {w for w in wa if len(w) >= 3} & {w for w in wb if len(w) >= 3}:
        return True
    ca, cb = "".join(wa), "".join(wb)
    n = min(len(ca), len(cb), 6)
    return ca == cb or (n >= 3 and ca[:n] == cb[:n])


def is_aux_ticker(t):
    """Warrants, units, rights and preferreds listed next to the common stock."""
    t = str(t).upper()
    if "-" in t:
        suf = t.split("-", 1)[1]
        return suf in AUX_SUFFIXES or suf.startswith("P") or len(suf) > 1
    return False


def common_classes(tickers):
    return [t for t in tickers if not is_aux_ticker(t)]


def primary_ticker(tickers):
    """The listed common stock to price: first common-class ticker in the SEC list (the SEC lists the main
    class first), skipping warrants, units, rights and preferreds."""
    cc = common_classes(tickers)
    return cc[0] if cc else (tickers[0] if tickers else None)
