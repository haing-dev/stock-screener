/* Excel 3-statement model, loaded only when someone clicks "Generate financial statements" (keeps app.js small).
   Classic script sharing app.js globals (esc, S, ...). */
/* Workbook layout (annual, GS-style): Cover, IS, BS, CF, Metrics. Blue = reported figures (SEC), black = formulas.
   Amounts in millions of the reporting currency; per-share figures in units. The template (mdl.tpl, chosen from the
   industry code) decides which lines and ratios appear; a line the company never reports is left out. 'Other' lines
   balance each statement to its reported total, so the three statements always tie; the Cover lists the checks. */
const TEMPLATES = {
  software: "Software & internet",
  hc_products: "Healthcare products (drugs, devices, tools)",
  biotech: "Clinical-stage biotech & medtech",
  insurer: "Insurance & managed care",
  hc_services: "Healthcare services & distribution",
  resources: "Energy, mining & natural resources",
  homebuilder: "Homebuilding",
  tech_hw: "Technology hardware & semiconductors",
  transport: "Transport",
  consumer: "Retail & consumer",
  industrial: "Industrial & general",
};

function buildModel(Excel, mdl) {
  const wb = new Excel.Workbook();
  wb.creator = "Stock Screener";
  const Y = mdl.years;
  const n = Y.length;
  const cur = mdl.currency || "USD";
  const T = TEMPLATES[mdl.tpl] ? mdl.tpl : "industrial";
  const col = (i) => String.fromCharCode(66 + i);           // year i -> column B, C, ...
  const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  const fye = mdl.fye ? months[Number(mdl.fye.slice(5, 7)) - 1] : "";
  const BLUE = { color: { argb: "FF1F4FBF" } };
  const GREY = { italic: true, color: { argb: "FF5B6977" } };
  const NUM = '#,##0.0;(#,##0.0);"–"', PCT = '0.0%;(0.0%);"–"', MULTF = '0.0"x";(0.0"x");"–"', EPS = '0.00;(0.00);"–"', DAYS = '0;(0);"–"', YRS = '0.0" yrs";(0.0" yrs");"–"';
  const has = (k) => Y.some((y) => y[k] !== undefined && y[k] !== null);
  const val = (i, k) => (Y[i][k] === undefined ? null : Y[i][k]);
  const mil = (v) => (v === undefined || v === null ? null : v / 1e6);
  const raw = (k) => (i) => mil(val(i, k));
  const neg = (k) => (i) => (val(i, k) === null ? null : -Math.abs(val(i, k)) / 1e6);
  const pos = (k) => (i) => (val(i, k) === null ? null : Math.abs(val(i, k)) / 1e6);
  const F = (expr) => ({ f: expr });
  const IFE = (expr) => ({ f: `IFERROR(${expr},"")` });

  /* A sheet is a list of rows; rows are laid out first, so every formula can point at any row of any sheet. */
  class Sheet {
    constructor(name, title) { this.name = name; this.title = title; this.items = []; this.row = {}; }
    add(key, label, fn, opt = {}) { if (opt.show !== false) this.items.push({ t: "row", key, label, fn, opt }); }
    head(text) { this.items.push({ t: "head", text }); }
    gap() { this.items.push({ t: "gap" }); }
    has(key) { return !!this.row[key]; }
  }
  const sheets = [];
  const sheet = (name, title) => { const s = new Sheet(name, title); sheets.push(s); return s; };
  const R = (s, key, i) => (s.row[key] ? `'${s.name}'!${col(i)}${s.row[key]}` : null);   // reference or null
  const X = (s, key, i) => R(s, key, i) || "0";                                          // reference or 0
  const sum = (s, keys, i) => keys.filter((k) => s.has(k)).map((k) => X(s, k, i)).join("+") || "0";
  const ratio = (a, b) => IFE(`${a}/${b}`);
  const yoy = (s, key) => (i) => (i ? IFE(`${X(s, key, i)}/${X(s, key, i - 1)}-1`) : null);
  const avg2 = (s, key, i) => (i ? `AVERAGE(${X(s, key, i)},${X(s, key, i - 1)})` : X(s, key, i));
  const pct = { fmt: PCT, italic: true, indent: 1 };

  /* ================================================================ Income statement */
  const IS = sheet("IS", "Income Statement");
  const ins = T === "insurer";
  IS.add("rev", { insurer: "Revenue (premiums, fees & investment income)", biotech: "Revenue (collaboration, royalty & product)" }[T] || "Revenue",
    raw("revenue"), { bold: true });
  IS.add("rev_g", "% yoy", yoy(IS, "rev"), pct);
  IS.add("prem", "of which premiums earned", raw("premiums"), { indent: 2, italic: true, show: ins && has("premiums") });
  const cogsKey = ins && has("benefits_expense") ? "benefits_expense" : "cost_of_revenue";
  const gross = has(cogsKey) || (!ins && has("gross_profit"));
  const cogsLabel = { resources: "Operating & production costs", insurer: "Medical & benefit costs", hc_services: "Cost of services",
    software: "Cost of revenue (hosting, support, services)", homebuilder: "Cost of homes & land sold", consumer: "Cost of goods sold",
    tech_hw: "Cost of goods sold", hc_products: "Cost of goods sold" }[T] || "Cost of revenue";
  IS.add("cogs", cogsLabel, (i) => {
    if (val(i, cogsKey) !== null) return mil(val(i, cogsKey));
    if (!ins && val(i, "gross_profit") !== null && val(i, "revenue") !== null) return F(`${X(IS, "rev", i)}-${mil(val(i, "gross_profit"))}`);
    return null;
  }, { show: gross });
  const grossOk = (i) => val(i, cogsKey) !== null || (!ins && val(i, "gross_profit") !== null);
  IS.add("gp", ins ? "Revenue less benefit costs" : "Gross profit", (i) => (grossOk(i) ? F(`${X(IS, "rev", i)}-${X(IS, "cogs", i)}`) : null),
    { bold: true, top: true, show: gross });
  IS.add("gm", ins ? "Medical cost ratio (benefit costs / revenue)" : "Gross margin",
    (i) => (grossOk(i) ? (ins ? ratio(X(IS, "cogs", i), X(IS, "rev", i)) : ratio(X(IS, "gp", i), X(IS, "rev", i))) : null), { ...pct, show: gross });
  const opex = [];
  const op = (key, label, fn, show) => { if (show) { IS.add(key, label, fn, { indent: 1 }); opex.push(key); } };
  if (has("selling_marketing") || has("general_admin")) {
    op("sm", "Sales & marketing", raw("selling_marketing"), has("selling_marketing"));
    op("ga", "General & administrative", raw("general_admin"), has("general_admin"));
  } else {
    op("sga", ins ? "Operating & administrative costs" : "Selling, general & administrative", raw("sga"), has("sga"));
  }
  op("rnd", "Research & development", raw("rnd"), has("rnd"));
  op("expl", "Exploration", pos("exploration"), T === "resources" && has("exploration"));
  const ebitOk = (i) => val(i, "x_operating_income") !== null;
  const base = (i) => (gross && grossOk(i) ? X(IS, "gp", i) : X(IS, "rev", i));
  IS.add("oth_op", "Other operating expense, net", (i) => (ebitOk(i) && val(i, "revenue") !== null
    ? F(`${base(i)}-(${sum(IS, opex, i)})-${X(IS, "ebit", i)}`) : null), { indent: 1 });
  IS.add("opex", "Total operating expenses", (i) => (ebitOk(i) ? F(`${sum(IS, [...opex, "oth_op"], i)}`) : null), { top: true });
  IS.add("ebit", "Operating income (EBIT)", raw("x_operating_income"), { bold: true });
  IS.add("om", "Operating margin", (i) => ratio(X(IS, "ebit", i), X(IS, "rev", i)), pct);
  IS.add("da", T === "resources" ? "Depreciation, depletion & amortization" : "Depreciation & amortization", pos("da"), { indent: 1, show: has("da") });
  IS.add("ebitda", "EBITDA", (i) => (val(i, "da") !== null && ebitOk(i) ? F(`${X(IS, "ebit", i)}+${X(IS, "da", i)}`) : null), { bold: true, show: has("da") });
  IS.add("ebitda_m", "EBITDA margin", (i) => (val(i, "da") !== null ? ratio(X(IS, "ebitda", i), X(IS, "rev", i)) : null), { ...pct, show: has("da") });
  IS.gap();
  IS.add("int_exp", "Interest expense", neg("interest_expense"), { indent: 1, show: has("interest_expense") });
  IS.add("int_inc", "Interest income", raw("interest_income"), { indent: 1, show: has("interest_income") });
  IS.add("oth_nonop", "Other non-operating income, net", (i) => (val(i, "pretax_income") !== null && ebitOk(i)
    ? F(`${X(IS, "pretax", i)}-${X(IS, "ebit", i)}-(${sum(IS, ["int_exp", "int_inc"], i)})`) : null), { indent: 1 });
  IS.add("pretax", "Pretax income", raw("pretax_income"), { bold: true, top: true });
  IS.add("tax", "Income tax", (i) => (val(i, "income_tax") === null ? null : -mil(val(i, "income_tax"))), { indent: 1 });
  IS.add("etr", "Effective tax rate", (i) => IFE(`-${X(IS, "tax", i)}/${X(IS, "pretax", i)}`), pct);
  IS.add("oth_ni", "Minority interests, discontinued operations & other", (i) => (val(i, "net_income") !== null && val(i, "pretax_income") !== null
    ? F(`${X(IS, "ni", i)}-${X(IS, "pretax", i)}-${X(IS, "tax", i)}`) : null), { indent: 1 });
  IS.add("ni", "Net income", raw("net_income"), { bold: true, top: true });
  IS.add("ni_g", "% yoy", yoy(IS, "ni"), pct);
  IS.add("nm", "Net margin", (i) => ratio(X(IS, "ni", i), X(IS, "rev", i)), pct);
  IS.gap();
  IS.add("eps", "Diluted EPS (as reported)", (i) => val(i, "eps_diluted"), { fmt: EPS, show: has("eps_diluted") });
  IS.add("sh_rep", "Diluted shares, m (as reported)", raw("diluted_shares"), { show: has("diluted_shares") });
  IS.add("sh", "Diluted shares, m (today's share basis)", raw("shares_basis"), { show: has("shares_basis") });
  IS.add("eps_adj", "EPS on today's share basis", (i) => ratio(X(IS, "ni", i), X(IS, "sh", i)), { fmt: EPS, show: has("shares_basis") });
  IS.gap();
  IS.head("Memo (included above)");
  IS.add("sbc", "Stock-based compensation", pos("sbc"), { indent: 1, italic: true, show: has("sbc") });
  IS.add("imp", "Impairments", pos("impairments"), { indent: 1, italic: true, show: has("impairments") });
  IS.add("restr", "Restructuring charges", pos("restructuring"), { indent: 1, italic: true, show: has("restructuring") });

  /* ================================================================ Balance sheet */
  const BS = sheet("BS", "Balance Sheet");
  const classified = has("assets_current");
  BS.head("Assets");
  const ca = [];
  const line = (s, arr, key, label, k, show = has(k)) => { if (show) { s.add(key, label, raw(k), { indent: 1 }); arr.push(key); } };
  line(BS, ca, "cash", "Cash & equivalents", "cash", true);
  line(BS, ca, "sti", "Short-term investments", "st_investments");
  line(BS, ca, "ar", ins ? "Premiums & other receivables" : "Accounts receivable", "accounts_receivable");
  line(BS, ca, "inv", T === "homebuilder" ? "Inventory (homes, land & lots)" : "Inventory", "inventory");
  if (classified) {
    BS.add("oca", "Other current assets", (i) => (val(i, "assets_current") !== null ? F(`${X(BS, "tca", i)}-(${sum(BS, ca, i)})`) : null), { indent: 1 });
    BS.add("tca", "Total current assets", raw("assets_current"), { bold: true, top: true });
  }
  const nca = [];
  line(BS, nca, "ppe", T === "resources" ? "Property, plant, equipment & mineral interests, net" : "PP&E, net", "ppe_net");
  line(BS, nca, "rou", "Operating lease right-of-use assets", "lease_rou");
  line(BS, nca, "gw", "Goodwill", "goodwill");
  line(BS, nca, "intang", "Intangible assets", "intangibles");
  line(BS, nca, "lti", "Long-term investments", "lt_investments");
  BS.add("onca", classified ? "Other non-current assets" : "Other assets", (i) => {
    if (val(i, "assets") === null) return null;
    if (classified) return val(i, "assets_current") !== null ? F(`${X(BS, "ta", i)}-${X(BS, "tca", i)}-(${sum(BS, nca, i)})`) : null;
    return F(`${X(BS, "ta", i)}-(${sum(BS, [...ca, ...nca], i)})`);
  }, { indent: 1 });
  BS.add("ta", "Total assets", raw("assets"), { bold: true, top: true });
  BS.gap();
  BS.head("Liabilities and equity");
  const clist = [];
  const tlOk = (i) => val(i, "liabilities") !== null || (val(i, "assets") !== null && val(i, "equity") !== null);
  line(BS, clist, "ap", "Accounts payable", "accounts_payable");
  line(BS, clist, "accr", "Accrued liabilities", "accrued_liabilities");
  line(BS, clist, "dr_c", "Deferred revenue, current", "deferred_revenue_current");
  line(BS, clist, "ll_c", "Operating lease liabilities, current", "lease_liab_current");
  const ncl = [];
  if (classified && has("liabilities_current")) {
    BS.add("ocl", "Other current liabilities (incl. short-term debt)", (i) => (val(i, "liabilities_current") !== null
      ? F(`${X(BS, "tcl", i)}-(${sum(BS, clist, i)})`) : null), { indent: 1 });
    BS.add("tcl", "Total current liabilities", raw("liabilities_current"), { bold: true, top: true });
  }
  line(BS, ncl, "dr_nc", "Deferred revenue, non-current", "deferred_revenue_noncurrent");
  line(BS, ncl, "ll_nc", "Operating lease liabilities, non-current", "lease_liab_noncurrent");
  BS.add("oncl", BS.has("tcl") || (classified && has("liabilities_current")) ? "Other non-current liabilities (incl. long-term debt)" : "Other liabilities (incl. debt)", (i) => {
    if (!tlOk(i)) return null;
    if (classified && has("liabilities_current")) return val(i, "liabilities_current") !== null ? F(`${X(BS, "tl", i)}-${X(BS, "tcl", i)}-(${sum(BS, ncl, i)})`) : null;
    return F(`${X(BS, "tl", i)}-(${sum(BS, [...clist, ...ncl], i)})`);
  }, { indent: 1 });
  BS.add("tl", "Total liabilities", (i) => {
    if (val(i, "liabilities") !== null) return mil(val(i, "liabilities"));
    if (val(i, "assets") !== null && val(i, "equity") !== null) return F(`${X(BS, "ta", i)}-${mil(val(i, "equity"))}-${mil(val(i, "minority_interest") || 0)}`);
    return null;
  }, { bold: true, top: true });
  BS.add("pref", "of which preferred stock (memo)", raw("preferred_equity"), { indent: 2, italic: true, show: has("preferred_equity") });
  BS.add("mi", "Non-controlling interest", raw("minority_interest"), { indent: 1, show: has("minority_interest") });
  BS.add("eq", "Shareholders' equity", raw("equity"), { indent: 1 });
  BS.add("re", "of which retained earnings", raw("retained_earnings"), { indent: 2, italic: true, show: has("retained_earnings") });
  BS.add("tle", "Total liabilities & equity", (i) => F(sum(BS, ["tl", "mi", "eq"], i)), { bold: true, top: true });
  BS.add("chk", "Check: assets – liabilities & equity (should be 0)", (i) => (val(i, "assets") !== null ? F(`ROUND(${X(BS, "ta", i)}-${X(BS, "tle", i)},1)`) : null), { italic: true });
  BS.gap();
  BS.head("Memo");
  BS.add("debt", "Total debt", raw("x_total_debt"), { indent: 1 });
  BS.add("netdebt", "Net debt (debt – cash – short-term investments)", (i) => F(`${X(BS, "debt", i)}-${X(BS, "cash", i)}-${X(BS, "sti", i)}`), { indent: 1 });
  BS.add("leases", "Operating lease liabilities (total)", (i) => F(sum(BS, ["ll_c", "ll_nc"], i)), { indent: 1, show: has("lease_liab_current") || has("lease_liab_noncurrent") });
  BS.add("nwc", "Net working capital (current assets ex cash – current liabilities)", (i) => (val(i, "assets_current") !== null && val(i, "liabilities_current") !== null
    ? F(`${X(BS, "tca", i)}-${X(BS, "cash", i)}-${X(BS, "sti", i)}-${X(BS, "tcl", i)}`) : null), { indent: 1, show: classified && has("liabilities_current") });
  BS.add("ic", "Invested capital (screener definition)", raw("x_invested_capital"), { indent: 1, show: has("x_invested_capital") });
  BS.add("bvps", "Book value per share (today's share basis)", (i) => ratio(X(BS, "eq", i), X(IS, "sh", i)), { indent: 1, fmt: EPS, show: has("shares_basis") });

  /* ================================================================ Cash flow */
  const CF = sheet("CF", "Cash Flow Statement");
  CF.head("Operating activities");
  CF.add("ni", "Net income", (i) => F(X(IS, "ni", i)), { indent: 1 });
  CF.add("da", T === "resources" ? "Depreciation, depletion & amortization" : "Depreciation & amortization", (i) => F(X(IS, "da", i)), { indent: 1, show: has("da") });
  CF.add("sbc", "Stock-based compensation", (i) => F(X(IS, "sbc", i)), { indent: 1, show: has("sbc") });
  CF.add("imp", "Impairments", (i) => F(X(IS, "imp", i)), { indent: 1, show: has("impairments") });
  CF.add("wc", "Working capital and other items", (i) => (val(i, "ocf") !== null ? F(`${X(CF, "cfo", i)}-(${sum(CF, ["ni", "da", "sbc", "imp"], i)})`) : null), { indent: 1 });
  CF.add("cfo", "Cash from operations", raw("ocf"), { bold: true, top: true });
  CF.gap();
  CF.head("Investing activities");
  const inv = [];
  const cfl = (arr, key, label, fn, show) => { if (show) { CF.add(key, label, fn, { indent: 1 }); arr.push(key); } };
  cfl(inv, "capex", T === "resources" ? "Capital expenditure (incl. development & acquisition of reserves)" : "Capital expenditure (PP&E)", neg("capex_ppe"), true);
  cfl(inv, "capsw", "Capitalized software", neg("capex_software"), has("capex_software"));
  cfl(inv, "acq", "Acquisitions", neg("acquisitions"), has("acquisitions"));
  CF.add("oinv", "Other investing (incl. securities)", (i) => (val(i, "cfi") !== null ? F(`${X(CF, "cfi", i)}-(${sum(CF, inv, i)})`) : null), { indent: 1 });
  CF.add("cfi", "Cash from investing", raw("cfi"), { bold: true, top: true });
  CF.gap();
  CF.head("Financing activities");
  const fin = [];
  cfl(fin, "dbt_i", "Debt issued", pos("debt_issued"), has("debt_issued"));
  cfl(fin, "dbt_r", "Debt repaid", neg("debt_repaid"), has("debt_repaid"));
  cfl(fin, "bb", "Share buybacks", neg("buybacks"), has("buybacks"));
  cfl(fin, "div", "Dividends paid", neg("dividends"), has("dividends"));
  cfl(fin, "eqi", "Shares issued", pos("equity_issued"), has("equity_issued"));
  CF.add("ofin", "Other financing", (i) => (val(i, "cff") !== null ? F(`${X(CF, "cff", i)}-(${sum(CF, fin, i)})`) : null), { indent: 1 });
  CF.add("cff", "Cash from financing", raw("cff"), { bold: true, top: true });
  CF.add("fx", "Exchange-rate effect", raw("fx_effect"), { indent: 1, show: has("fx_effect") });
  const flowsOk = (i) => val(i, "ocf") !== null && val(i, "cfi") !== null && val(i, "cff") !== null;
  // the company's own net change in cash, when tagged, includes items outside the three sections (cash of
  // discontinued operations, held-for-sale reclassifications): shown as one line so the total matches the filing
  CF.add("oth_cash", "Other cash movements (discontinued operations & other)", (i) => (flowsOk(i) && val(i, "cash_change") !== null
    ? F(`${mil(val(i, "cash_change"))}-(${sum(CF, ["cfo", "cfi", "cff", "fx"], i)})`) : null), { indent: 1, show: has("cash_change") });
  CF.add("chg", "Net change in cash", (i) => (flowsOk(i) ? F(sum(CF, ["cfo", "cfi", "cff", "fx", "oth_cash"], i)) : null), { bold: true, top: true });
  CF.gap();
  CF.head("Cash reconciliation");
  const endCash = (i) => (val(i, "cash_cf_end") !== null ? mil(val(i, "cash_cf_end")) : (val(i, "cash") !== null ? F(X(BS, "cash", i)) : null));
  CF.add("beg", "Cash at beginning of year", (i) => {
    if (i && (val(i - 1, "cash_cf_end") !== null || val(i - 1, "cash") !== null)) return F(X(CF, "end", i - 1));
    return flowsOk(i) && endCash(i) !== null ? F(`${X(CF, "end", i)}-${X(CF, "chg", i)}`) : null;
  }, { indent: 1 });
  CF.add("end", "Cash at end of year (incl. restricted cash)", endCash, { indent: 1, bold: true });
  CF.add("chk_cash", "Check: beginning + change – end (should be 0)", (i) => (i && flowsOk(i) && endCash(i) !== null && endCash(i - 1) !== null
    ? F(`ROUND(${X(CF, "beg", i)}+${X(CF, "chg", i)}-${X(CF, "end", i)},1)`) : null), { indent: 1, italic: true });
  CF.add("rcash", "Restricted cash & other (cash-flow cash – balance-sheet cash)", (i) => (endCash(i) !== null && val(i, "cash") !== null
    ? F(`${X(CF, "end", i)}-${X(BS, "cash", i)}`) : null), { indent: 1, italic: true });
  CF.gap();
  CF.head("Free cash flow");
  CF.add("fcf", "Free cash flow (CFO – capex – capitalized software)", (i) => (val(i, "ocf") !== null ? F(`${X(CF, "cfo", i)}+${X(CF, "capex", i)}+${X(CF, "capsw", i)}`) : null), { bold: true });
  CF.add("fcf_sbc", "Free cash flow after stock-based compensation", (i) => (val(i, "ocf") !== null ? F(`${X(CF, "fcf", i)}-${X(CF, "sbc", i)}`) : null), { indent: 1, show: has("sbc") });
  CF.add("fcf_m", "FCF margin", (i) => ratio(X(CF, "fcf", i), X(IS, "rev", i)), pct);
  CF.add("fcf_ps", "FCF per share (today's share basis)", (i) => ratio(X(CF, "fcf", i), X(IS, "sh", i)), { fmt: EPS, indent: 1, show: has("shares_basis") });
  CF.add("fcf_ni", "FCF / net income", (i) => ratio(X(CF, "fcf", i), X(CF, "ni", i)), { fmt: MULTF, indent: 1 });

  /* ================================================================ Metrics */
  const MT = sheet("Metrics", `Key metrics (${TEMPLATES[T]})`);
  const ISr = (k, i) => X(IS, k, i), BSr = (k, i) => X(BS, k, i), CFr = (k, i) => X(CF, k, i);
  const m = (label, fn, fmt = PCT, show = true) => MT.add(null, label, fn, { fmt, indent: 1, show });
  const bio = T === "biotech";
  MT.head("Growth");
  m("Revenue growth", (i) => (i ? IFE(`${ISr("rev", i)}/${ISr("rev", i - 1)}-1`) : null));
  m("Revenue CAGR, 3 years", (i) => (i >= 3 ? IFE(`(${ISr("rev", i)}/${ISr("rev", i - 3)})^(1/3)-1`) : null));
  m("Revenue CAGR, 5 years", (i) => (i >= 5 ? IFE(`(${ISr("rev", i)}/${ISr("rev", i - 5)})^(1/5)-1`) : null));
  m("EBIT growth", (i) => (i ? IFE(`${ISr("ebit", i)}/${ISr("ebit", i - 1)}-1`) : null), PCT, !bio);
  m("EPS growth (today's share basis)", (i) => (i ? IFE(`${ISr("eps_adj", i)}/${ISr("eps_adj", i - 1)}-1`) : null), PCT, !bio && has("shares_basis"));
  m("FCF per share growth", (i) => (i ? IFE(`${CFr("fcf_ps", i)}/${CFr("fcf_ps", i - 1)}-1`) : null), PCT, !bio && has("shares_basis"));
  m("Diluted share count change", (i) => (i ? IFE(`${ISr("sh", i)}/${ISr("sh", i - 1)}-1`) : null), PCT, has("shares_basis"));
  if (!bio) {
    MT.gap();
    MT.head("Margins");
    m("Gross margin", (i) => ratio(ISr("gp", i), ISr("rev", i)), PCT, gross && !ins);
    m("Operating (EBIT) margin", (i) => ratio(ISr("ebit", i), ISr("rev", i)));
    m("EBITDA margin", (i) => ratio(ISr("ebitda", i), ISr("rev", i)), PCT, has("da"));
    m("Net margin", (i) => ratio(ISr("ni", i), ISr("rev", i)));
    m("FCF margin", (i) => ratio(CFr("fcf", i), ISr("rev", i)));
    MT.gap();
    MT.head("Returns");
    MT.add("taxr", "Tax rate used for NOPAT", (i) => val(i, "x_tax_rate_used"), { fmt: PCT, indent: 1, show: has("x_tax_rate_used") });
    MT.add("nopat", "NOPAT (EBIT × (1 – tax rate))", (i) => F(`${ISr("ebit", i)}*(1-${X(MT, "taxr", i)})`), { indent: 1 });
    m("ROIC (NOPAT / average invested capital)", (i) => IFE(`${X(MT, "nopat", i)}/${avg2(BS, "ic", i)}`), PCT, has("x_invested_capital"));
    m("Cash ROIC (FCF / average invested capital)", (i) => IFE(`${CFr("fcf", i)}/${avg2(BS, "ic", i)}`), PCT, has("x_invested_capital"));
    m("Return on equity", (i) => IFE(`${ISr("ni", i)}/${avg2(BS, "eq", i)}`));
    m("Return on assets", (i) => IFE(`${ISr("ni", i)}/${avg2(BS, "ta", i)}`));
    MT.gap();
    MT.head("Cash conversion and reinvestment");
    m("FCF / net income", (i) => F(CFr("fcf_ni", i)), MULTF);
    m("FCF after stock pay / net income", (i) => ratio(CFr("fcf_sbc", i), ISr("ni", i)), MULTF, has("sbc"));
    m("Cash from operations / net income", (i) => ratio(CFr("cfo", i), ISr("ni", i)), MULTF);
    m("Capex / revenue", (i) => IFE(`-(${CFr("capex", i)}+${CFr("capsw", i)})/${ISr("rev", i)}`));
    m("Capex / D&A", (i) => IFE(`-(${CFr("capex", i)}+${CFr("capsw", i)})/${ISr("da", i)}`), MULTF, has("da"));
    m("Buybacks + dividends / FCF", (i) => IFE(`-(${CFr("bb", i)}+${CFr("div", i)})/${CFr("fcf", i)}`), PCT, has("buybacks") || has("dividends"));
    m("Acquisitions / cash from operations", (i) => IFE(`-${CFr("acq", i)}/${CFr("cfo", i)}`), PCT, has("acquisitions"));
  }
  MT.gap();
  MT.head("Balance sheet");
  m("Net debt / EBITDA", (i) => ratio(BSr("netdebt", i), ISr("ebitda", i)), MULTF, !bio && has("da"));
  m("Net debt / cash from operations", (i) => ratio(BSr("netdebt", i), CFr("cfo", i)), MULTF, !bio);
  m("Interest coverage (EBIT / interest)", (i) => IFE(`${ISr("ebit", i)}/-${ISr("int_exp", i)}`), MULTF, !bio && has("interest_expense"));
  m("Debt / equity", (i) => ratio(BSr("debt", i), BSr("eq", i)), MULTF);
  m("Goodwill & intangibles / total assets", (i) => IFE(`(${BSr("gw", i)}+${BSr("intang", i)})/${BSr("ta", i)}`), PCT, has("goodwill") || has("intangibles"));

  /* industry block */
  const IND = {
    software: () => {
      m("Rule of 40 (revenue growth + FCF margin)", (i) => (i ? IFE(`${ISr("rev", i)}/${ISr("rev", i - 1)}-1+${CFr("fcf", i)}/${ISr("rev", i)}`) : null));
      m("FCF margin after stock pay", (i) => ratio(CFr("fcf_sbc", i), ISr("rev", i)), PCT, has("sbc"));
      m("Stock-based comp / revenue", (i) => ratio(ISr("sbc", i), ISr("rev", i)), PCT, has("sbc"));
      m("Stock-based comp / FCF", (i) => ratio(ISr("sbc", i), CFr("fcf", i)), PCT, has("sbc"));
      m("Sales & marketing / revenue", (i) => ratio(ISr("sm", i), ISr("rev", i)), PCT, has("selling_marketing"));
      m("R&D / revenue", (i) => ratio(ISr("rnd", i), ISr("rev", i)), PCT, has("rnd"));
      m("Deferred revenue / revenue", (i) => IFE(`(${BSr("dr_c", i)}+${BSr("dr_nc", i)})/${ISr("rev", i)}`), PCT, has("deferred_revenue_current"));
      m("Billings growth (revenue + change in deferred revenue)", (i) => (i >= 2 ? IFE(
        `(${ISr("rev", i)}+${BSr("dr_c", i)}+${BSr("dr_nc", i)}-${BSr("dr_c", i - 1)}-${BSr("dr_nc", i - 1)})/(${ISr("rev", i - 1)}+${BSr("dr_c", i - 1)}+${BSr("dr_nc", i - 1)}-${BSr("dr_c", i - 2)}-${BSr("dr_nc", i - 2)})-1`) : null),
        PCT, has("deferred_revenue_current"));
    },
    hc_products: () => {
      m("R&D / revenue", (i) => ratio(ISr("rnd", i), ISr("rev", i)), PCT, has("rnd"));
      m("SG&A / revenue", (i) => ratio(ISr("sga", i), ISr("rev", i)), PCT, has("sga"));
      m("Acquisitions / cash from operations", (i) => IFE(`-${CFr("acq", i)}/${CFr("cfo", i)}`), PCT, has("acquisitions"));
      m("Inventory days (DIO)", (i) => IFE(`${BSr("inv", i)}/${ISr("cogs", i)}*365`), DAYS, has("inventory") && gross);
      m("Receivable days (DSO)", (i) => IFE(`${BSr("ar", i)}/${ISr("rev", i)}*365`), DAYS, has("accounts_receivable"));
    },
    biotech: () => {
      MT.add("liq", "Cash & investments (cash + short- and long-term investments)", (i) => F(sum(BS, ["cash", "sti", "lti"], i)), { indent: 1 });
      MT.add("burn", "Cash burn (– cash from operations – capex)", (i) => (val(i, "ocf") !== null ? F(`MAX(0,-(${CFr("cfo", i)}+${CFr("capex", i)}))`) : null), { indent: 1 });
      m("Runway (years of cash at this burn)", (i) => IFE(`IF(${X(MT, "burn", i)}>0,${X(MT, "liq", i)}/${X(MT, "burn", i)},"cash-flow positive")`), YRS);
      m("R&D share of operating costs", (i) => ratio(ISr("rnd", i), ISr("opex", i)), PCT, has("rnd"));
      m("R&D growth", (i) => (i ? IFE(`${ISr("rnd", i)}/${ISr("rnd", i - 1)}-1`) : null), PCT, has("rnd"));
      m("Shares issued / cash burn", (i) => IFE(`${CFr("eqi", i)}/${X(MT, "burn", i)}`), PCT, has("equity_issued"));
    },
    insurer: () => {
      m("Medical cost ratio (benefit costs / revenue)", (i) => ratio(ISr("cogs", i), ISr("rev", i)), PCT, gross);
      m("Medical cost ratio (benefit costs / premiums)", (i) => ratio(ISr("cogs", i), ISr("prem", i)), PCT, gross && has("premiums"));
      m("Operating cost ratio (operating costs / revenue)", (i) => ratio(ISr("sga", i), ISr("rev", i)), PCT, has("sga"));
      m("Investments / total assets", (i) => IFE(`(${BSr("sti", i)}+${BSr("lti", i)})/${BSr("ta", i)}`), PCT, has("st_investments") || has("lt_investments"));
      m("Debt / (debt + equity)", (i) => IFE(`${BSr("debt", i)}/(${BSr("debt", i)}+${BSr("eq", i)})`));
    },
    hc_services: () => {
      m("Receivable days (DSO)", (i) => IFE(`${BSr("ar", i)}/${ISr("rev", i)}*365`), DAYS, has("accounts_receivable"));
      m("Payable days (DPO)", (i) => IFE(`${BSr("ap", i)}/${ISr("cogs", i)}*365`), DAYS, has("accounts_payable") && gross);
      m("Lease liabilities / EBITDA", (i) => ratio(BSr("leases", i), ISr("ebitda", i)), MULTF, has("lease_liab_noncurrent") && has("da"));
    },
    resources: () => {
      m("DD&A / revenue", (i) => ratio(ISr("da", i), ISr("rev", i)), PCT, has("da"));
      m("Reinvestment rate (capex / cash from operations)", (i) => IFE(`-${CFr("capex", i)}/${CFr("cfo", i)}`));
      m("Capex / DD&A", (i) => IFE(`-${CFr("capex", i)}/${ISr("da", i)}`), MULTF, has("da"));
      m("Exploration / revenue", (i) => ratio(ISr("expl", i), ISr("rev", i)), PCT, has("exploration"));
      m("Impairments / revenue", (i) => ratio(ISr("imp", i), ISr("rev", i)), PCT, has("impairments"));
      m("Shareholder returns / FCF", (i) => IFE(`-(${CFr("bb", i)}+${CFr("div", i)})/${CFr("fcf", i)}`), PCT, has("buybacks") || has("dividends"));
    },
    homebuilder: () => {
      m("Inventory / total assets", (i) => ratio(BSr("inv", i), BSr("ta", i)), PCT, has("inventory"));
      m("Inventory turns (cost of sales / average inventory)", (i) => IFE(`${ISr("cogs", i)}/${avg2(BS, "inv", i)}`), MULTF, has("inventory") && gross);
      m("Book value per share growth", (i) => (i ? IFE(`${BSr("bvps", i)}/${BSr("bvps", i - 1)}-1`) : null), PCT, has("shares_basis"));
      m("Debt / (debt + equity)", (i) => IFE(`${BSr("debt", i)}/(${BSr("debt", i)}+${BSr("eq", i)})`));
    },
    tech_hw: () => {
      m("R&D / revenue", (i) => ratio(ISr("rnd", i), ISr("rev", i)), PCT, has("rnd"));
      m("Inventory days (DIO)", (i) => IFE(`${BSr("inv", i)}/${ISr("cogs", i)}*365`), DAYS, has("inventory") && gross);
      m("Receivable days (DSO)", (i) => IFE(`${BSr("ar", i)}/${ISr("rev", i)}*365`), DAYS, has("accounts_receivable"));
      m("Stock-based comp / revenue", (i) => ratio(ISr("sbc", i), ISr("rev", i)), PCT, has("sbc"));
    },
    transport: () => {
      m("Operating ratio (operating costs / revenue)", (i) => IFE(`1-${ISr("ebit", i)}/${ISr("rev", i)}`));
      m("Lease liabilities / EBITDA", (i) => ratio(BSr("leases", i), ISr("ebitda", i)), MULTF, has("lease_liab_noncurrent") && has("da"));
    },
    consumer: () => {
      m("Inventory turns (cost of sales / average inventory)", (i) => IFE(`${ISr("cogs", i)}/${avg2(BS, "inv", i)}`), MULTF, has("inventory") && gross);
      m("Inventory days (DIO)", (i) => IFE(`${BSr("inv", i)}/${ISr("cogs", i)}*365`), DAYS, has("inventory") && gross);
      m("Payable days (DPO)", (i) => IFE(`${BSr("ap", i)}/${ISr("cogs", i)}*365`), DAYS, has("accounts_payable") && gross);
      m("SG&A / revenue", (i) => ratio(ISr("sga", i), ISr("rev", i)), PCT, has("sga"));
      m("Lease liabilities / EBITDA", (i) => ratio(BSr("leases", i), ISr("ebitda", i)), MULTF, has("lease_liab_noncurrent") && has("da"));
    },
    industrial: () => {
      m("Receivable days (DSO)", (i) => IFE(`${BSr("ar", i)}/${ISr("rev", i)}*365`), DAYS, has("accounts_receivable"));
      m("Inventory days (DIO)", (i) => IFE(`${BSr("inv", i)}/${ISr("cogs", i)}*365`), DAYS, has("inventory") && gross);
      m("Payable days (DPO)", (i) => IFE(`${BSr("ap", i)}/${ISr("cogs", i)}*365`), DAYS, has("accounts_payable") && gross);
      m("Net working capital / revenue", (i) => ratio(BSr("nwc", i), ISr("rev", i)), PCT, classified && has("liabilities_current"));
      m("R&D / revenue", (i) => ratio(ISr("rnd", i), ISr("rev", i)), PCT, has("rnd"));
    },
  };
  MT.gap();
  MT.head(`${TEMPLATES[T]}`);
  IND[T]();
  const px = mdl.px || {};     // {fy: [price, market cap]}: split-adjusted, USD reporters only
  MT.gap();
  if (Object.keys(px).length) {
    MT.head("Valuation at fiscal year end (month-end price, split-adjusted to today)");
    MT.add("price", "Share price (today's share basis)", (i) => (px[Y[i].fy] ? px[Y[i].fy][0] : null), { fmt: EPS, indent: 1 });
    MT.add("mcap", "Market cap", (i) => (px[Y[i].fy] ? px[Y[i].fy][1] / 1e6 : null), { indent: 1 });
    MT.add("ev", "Enterprise value", (i) => (px[Y[i].fy] ? F(`${X(MT, "mcap", i)}+${BSr("netdebt", i)}+${BSr("mi", i)}`) : null), { indent: 1 });
    const pxOk = (i) => !!px[Y[i].fy];
    m("P/E", (i) => (pxOk(i) ? IFE(`IF(${ISr("ni", i)}>0,${X(MT, "mcap", i)}/${ISr("ni", i)},"")`) : null), MULTF, !bio);
    m("EV/EBIT", (i) => (pxOk(i) ? IFE(`IF(${ISr("ebit", i)}>0,${X(MT, "ev", i)}/${ISr("ebit", i)},"")`) : null), MULTF, !bio);
    m("EV/EBITDA", (i) => (pxOk(i) ? IFE(`IF(${ISr("ebitda", i)}>0,${X(MT, "ev", i)}/${ISr("ebitda", i)},"")`) : null), MULTF, !bio && has("da"));
    m("EV/Sales", (i) => (pxOk(i) ? ratio(X(MT, "ev", i), ISr("rev", i)) : null), MULTF);
    m("FCF yield", (i) => (pxOk(i) ? ratio(CFr("fcf", i), X(MT, "mcap", i)) : null), PCT, !bio);
    m("Price / book", (i) => (pxOk(i) ? ratio(X(MT, "mcap", i), BSr("eq", i)) : null), MULTF, T === "homebuilder" || T === "insurer");
    m("Market cap / cash & investments", (i) => (pxOk(i) ? ratio(X(MT, "mcap", i), X(MT, "liq", i)) : null), MULTF, bio);
  } else {
    MT.add(null, cur !== "USD" ? `Valuation history not shown: statements are in ${cur}, prices in USD.`
      : "Valuation history not shown: no month-end price history or verified market cap yet.", null, { italic: true });
  }

  /* ================================================================ lay out, then write */
  sheets.forEach((s) => {
    let r = 6;
    s.items.forEach((it) => { if (it.t === "row" && it.key) s.row[it.key] = r; it.r = r; r++; });
  });
  const cv = wb.addWorksheet("Cover", { views: [{ showGridLines: false }] });
  sheets.forEach((s) => {
    const ws = wb.addWorksheet(s.name, { views: [{ state: "frozen", xSplit: 1, ySplit: 5, showGridLines: false }] });
    ws.getColumn(1).width = 52;
    for (let i = 0; i < n; i++) ws.getColumn(i + 2).width = 12;
    ws.getCell("A1").value = `${mdl.n} (${mdl.t})`;
    ws.getCell("A1").font = { bold: true, size: 13 };
    ws.getCell("A2").value = s.title;
    ws.getCell("A2").font = { bold: true };
    ws.getCell("A3").value = `Fiscal year ends ${fye}; ${cur} millions except per-share data`;
    ws.getCell("A3").font = GREY;
    const hr = ws.getRow(5);
    Y.forEach((y, i) => { hr.getCell(i + 2).value = `FY${y.fy}A`; });
    hr.font = { bold: true };
    hr.eachCell((c) => { c.border = { bottom: { style: "thin" } }; c.alignment = { horizontal: "right" }; });
    s.items.forEach((it) => {
      if (it.t === "gap") return;
      const row = ws.getRow(it.r);
      if (it.t === "head") { row.getCell(1).value = it.text; row.getCell(1).font = { bold: true, color: { argb: "FF14212E" } }; return; }
      const o = it.opt;
      row.getCell(1).value = it.label;
      if (o.indent) row.getCell(1).alignment = { indent: o.indent };
      if (it.fn) {
        for (let i = 0; i < n; i++) {
          const v = it.fn(i);
          if (v === null || v === undefined || (typeof v === "number" && !Number.isFinite(v))) continue;
          const cell = row.getCell(i + 2);
          if (typeof v === "number") { cell.value = v; cell.font = BLUE; } else cell.value = { formula: v.f };
          cell.numFmt = o.fmt || NUM;
        }
      }
      if (o.bold) for (let i = 1; i <= n + 1; i++) { const c = row.getCell(i); c.font = { ...(c.font || {}), bold: true }; }
      if (o.top) for (let i = 1; i <= n + 1; i++) row.getCell(i).border = { top: { style: "thin" } };
      if (o.italic) row.getCell(1).font = GREY;
    });
  });

  /* ================================================================ Cover with the checks */
  cv.getColumn(1).width = 30; cv.getColumn(2).width = 86;
  cv.getCell("A1").value = "Financial statements"; cv.getCell("A1").font = { bold: true, size: 14 };
  const rng = (s, key) => `'${s.name}'!B${s.row[key]}:${col(n - 1)}${s.row[key]}`;
  const chk = (s, key, ok) => (s.row[key] ? { formula: `IF(COUNT(${rng(s, key)})=0,"Not checked: the totals it needs aren't reported",IF(SUMPRODUCT(ABS(${rng(s, key)}))<0.5,"${ok}","Differences – see the '${s.name}' sheet, row ${s.row[key]}"))` } : "Not checked: the totals it needs aren't reported");
  const info = [["Company", `${mdl.n} (${mdl.t})`], ["Industry", mdl.ind || ""], ["Template", `${TEMPLATES[T]}: lines and ratios chosen for this industry; lines the company doesn't report are left out`],
    ["Fiscal year end", fye], ["Currency", `${cur} millions (per-share data in ${cur})`],
    ["Years", `FY${Y[0].fy} – FY${Y[n - 1].fy} (annual, as reported)`], ["Source", "SEC XBRL financial statements (10-K / 20-F). Month-end prices, split-adjusted, for the valuation block."],
    ["Colour code", "Blue = reported figure. Black = formula. 'Other' lines balance each statement to its reported total."],
    ["Generated", new Date().toISOString().slice(0, 10)], ["", ""],
    ["Checks", ""],
    ["Balance sheet balances", chk(BS, "chk", "OK: assets = liabilities + equity every year")],
    ["Cash flow ties to cash", chk(CF, "chk_cash", "OK: beginning cash + net change = ending cash")],
    ["Net income", "Linked: the cash flow statement starts from the income statement's net income"]];
  info.forEach(([a, b], i) => {
    cv.getCell(`A${i + 3}`).value = a; cv.getCell(`A${i + 3}`).font = { bold: true };
    cv.getCell(`B${i + 3}`).value = b; cv.getCell(`B${i + 3}`).alignment = { wrapText: true };
  });
  wb.views = [{ activeTab: 1 }];
  return wb;
}
