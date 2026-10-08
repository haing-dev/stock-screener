/* Stock Screener portal - static page. Data files in data/*.bin are gzip'd JSON, AES-GCM encrypted with a key
   derived from the portal password (PBKDF2-SHA256). Nothing leaves the browser. */
"use strict";

const $ = (s, el = document) => el.querySelector(s);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const store = {
  get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* private mode */ } },
  del(k) { try { localStorage.removeItem(k); } catch (e) { /* ignore */ } },
};

const S = { key: null, info: null, meta: null, comp: null, screens: {}, cur: null, view: "pass", q: "", sort: null, off: {},
  company: null, pvMult: null };

/* ------------------------------------------------------------------ crypto */
const b64 = (s) => Uint8Array.from(atob(s), (c) => c.charCodeAt(0));
const toB64 = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf)));

async function gunzipJSON(buf) {
  const stream = new Blob([buf]).stream().pipeThrough(new DecompressionStream("gzip"));
  return JSON.parse(await new Response(stream).text());
}
async function deriveKey(pw, info) {
  const base = await crypto.subtle.importKey("raw", new TextEncoder().encode(pw), "PBKDF2", false, ["deriveKey"]);
  return crypto.subtle.deriveKey({ name: "PBKDF2", salt: b64(info.salt), iterations: info.iter, hash: "SHA-256" },
    base, { name: "AES-GCM", length: 256 }, true, ["decrypt"]);
}
async function openBlob(buf) {
  if (S.info.plain) return gunzipJSON(buf);
  const u = new Uint8Array(buf);
  const pt = await crypto.subtle.decrypt({ name: "AES-GCM", iv: u.slice(0, 12) }, S.key, u.slice(12));
  return gunzipJSON(pt);
}
async function fetchBin(name) {
  const r = await fetch(`data/${name}.bin`, { cache: "no-cache" });
  if (!r.ok) throw new Error(`data/${name}.bin: HTTP ${r.status}`);
  return openBlob(await r.arrayBuffer());
}
async function tryKey(key) {
  S.key = key;
  try { const c = await openBlob(b64(S.info.check).buffer); return !!(c && c.ok); } catch (e) { return false; }
}

/* ------------------------------------------------------------------ formatting */
function fmt(v, f) {
  if (v === null || v === undefined || Number.isNaN(v)) return "–";
  if (f === "x") return (Math.abs(v) >= 100 ? v.toFixed(0) : v.toFixed(1)) + "×";
  if (f === "pct") return (v * 100).toFixed(Math.abs(v) < 0.1 ? 1 : 0) + "%";
  if (f === "yrs") return v >= 99 ? "cash +" : v.toFixed(1) + " yrs";
  if (f === "usd") {
    const a = Math.abs(v);
    if (a >= 1e12) return "$" + (v / 1e12).toFixed(2) + "T";
    if (a >= 1e9) return "$" + (v / 1e9).toFixed(1) + "B";
    if (a >= 1e6) return "$" + (v / 1e6).toFixed(0) + "M";
    return "$" + v.toFixed(0);
  }
  return String(v);
}
const money = (v) => (v === null || v === undefined ? "–" : "$" + (v >= 1000 ? v.toFixed(0) : v.toFixed(2)));
function niceDate(d) {
  if (!d) return "–";
  const t = new Date(d + (d.length === 10 ? "T12:00:00" : ""));
  return t.toLocaleDateString(undefined, { month: "short", day: "numeric", year: "numeric" });
}

/* ------------------------------------------------------------------ status under the current rule switches */
/* Same classification as the screener: PASS; CHECK (nothing fails but an input is missing or needs a look);
   ONE = only valuation rules fail, a near miss on one rule, or one non-defining rule fails with everything else
   verified; FAIL otherwise. With every rule on this reproduces the screener's own lists.
   The site shows two lists: Pass (PASS) and Near misses (CHECK + ONE), each near miss with its reason. */
function statusOf(row, scr, off) {
  const fails = [], missing = [];
  let ndBiz = 0, ndHard = 0;
  scr.gates.forEach((g, i) => {
    if (off.has(g.id)) return;
    const c = row.g[i];
    if (c === "F") fails.push(g);
    else if (c === "D") { missing.push(g); if (!g.price) ndBiz++; if (g.hard) ndHard++; }
  });
  if (!fails.length) return { s: missing.length || row.h.length ? "CHECK" : "PASS", fails, missing };
  if (scr.strict && ndHard) return { s: "FAIL", fails, missing };
  if (fails.every((g) => g.valuation)) return { s: "ONE", fails, missing, kind: "price" };
  if (fails.length === 1) {
    const g = fails[0];
    if (row.nr && row.nr === g.id) return { s: "ONE", fails, missing, kind: "near" };
    if (!g.hard && ndBiz <= 1) return { s: "ONE", fails, missing, kind: "one" };
  }
  return { s: "FAIL", fails, missing };
}
const VIEWS = [
  { id: "pass", label: "Pass", avoid: "Flagged", set: ["PASS"] },
  { id: "near", label: "Near misses", avoid: "Nearly flagged", set: ["CHECK", "ONE"] },
];
const visibleSet = () => new Set(VIEWS.find((v) => v.id === S.view).set);

/* one line: why a company is a near miss (which rule, and the value or the reason it couldn't be checked) */
function reasonOf(st, row, scr) {
  const idx = (g) => scr.gates.indexOf(g);
  const val = (g) => row.v[idx(g)];
  if (st.s === "PASS" || st.s === "FAIL") return "";
  if (st.s === "ONE") {
    const g = st.fails[0];
    const v = val(g);
    const rule = g.rule.replace(/[()]/g, "");
    if (st.kind === "price") return `Price: ${st.fails.map((x) => x.name).join(", ")}${v ? ` ${v}` : ""}; needs ${rule}`;
    return `Missed: ${g.name}${v ? ` ${v}` : ""}; needs ${rule}`;
  }
  const parts = st.missing.map((g) => `${g.name}: ${row.nt[g.id] || "no data"}`).concat(row.h);
  return "Check manually: " + parts.join("; ");
}

function offFor(sid) {
  if (!S.off[sid]) {
    let saved = [];
    try { saved = JSON.parse(store.get("qs-off-" + sid) || "[]"); } catch (e) { saved = []; }
    S.off[sid] = new Set(saved);
  }
  return S.off[sid];
}
function saveOff(sid) { store.set("qs-off-" + sid, JSON.stringify([...offFor(sid)])); }

/* ------------------------------------------------------------------ boot */
async function boot() {
  try {
    const r = await fetch("data/keyinfo.json", { cache: "no-cache" });
    S.info = await r.json();
  } catch (e) {
    showLock("The portal has no data yet. Run the screen once in GitHub (Actions → Screen → Run workflow).");
    return;
  }
  if (S.info.plain) { await startSafe(); return; }
  const saved = store.get("qs-key");
  if (saved) {
    try {
      const { salt, k } = JSON.parse(saved);
      if (salt === S.info.salt) {
        const key = await crypto.subtle.importKey("raw", b64(k), { name: "AES-GCM" }, true, ["decrypt"]);
        if (await tryKey(key)) { await startSafe(); return; }
      }
    } catch (e) { /* saved key unreadable: ask for the password */ }
    store.del("qs-key");
  }
  showLock("");
}
function showLock(msg) {
  $("#app").hidden = true;
  $("#lock").hidden = false;
  $("#lockMsg").textContent = msg;
  $("#pw").focus();
}
$("#lockForm").addEventListener("submit", async (ev) => {
  ev.preventDefault();
  const btn = $("#unlockBtn");
  btn.disabled = true;
  btn.textContent = "Opening…";
  $("#lockMsg").textContent = "";
  try {
    const key = await deriveKey($("#pw").value.trim(), S.info);
    if (!(await tryKey(key))) {
      $("#lockMsg").textContent = "That password didn't open the data. Check it and try again.";
      return;
    }
    if ($("#remember").checked) {
      const raw = await crypto.subtle.exportKey("raw", key);
      store.set("qs-key", JSON.stringify({ salt: S.info.salt, k: toB64(raw) }));
    }
    $("#pw").value = "";
    await startSafe();
  } catch (e) {
    $("#lockMsg").textContent = "Couldn't open the data: " + e.message;
  } finally {
    btn.disabled = false;
    btn.textContent = "Open portal";
  }
});
$("#lockNow").addEventListener("click", () => {
  store.del("qs-key");
  S.key = null; S.meta = null; S.comp = null; S.screens = {};
  showLock("");
});

async function startSafe() {
  try { await start(); } catch (e) {
    $("#table").innerHTML = `<div class="empty">Couldn't load the portal data (${esc(e.message)}). Reload the page; if it keeps happening, check the latest run in GitHub Actions.</div>`;
  }
}
async function start() {
  if (window.matchMedia("(max-width: 1000px)").matches) $("#rulesBox").open = false;
  $("#lock").hidden = true;
  $("#app").hidden = false;
  $("#table").innerHTML = '<div class="empty">Loading…</div>';
  [S.meta, S.comp] = await Promise.all([fetchBin("meta"), fetchBin("companies")]);
  S.byTicker = {};
  Object.entries(S.comp.companies).forEach(([c, x]) => { S.byTicker[x.t] = c; });
  renderNav();
  renderFreshness();
  await route();
}

/* ------------------------------------------------------------------ navigation: #screen or #screen/TICKER */
function parseHash() {
  const [sid, t] = decodeURIComponent((location.hash || "").slice(1)).split("/");
  return { sid, t };
}
async function route() {
  const { sid, t } = parseHash();
  const want = sid || store.get("qs-screen") || S.meta.screens[0].id;
  const ok = S.meta.screens.some((s) => s.id === want) || want === "gaps";
  await go(ok ? want : S.meta.screens[0].id, t && S.byTicker[t] ? t : null);
}
function renderNav() {
  const nav = $("#screenNav");
  nav.innerHTML = S.meta.screens.map((s) =>
    (s.group ? `<div class="sep"></div><div class="nav-h">${esc(s.group)}</div>` : "") +
    `<button type="button" data-sid="${s.id}"><span>${esc(s.title)}</span><span class="n" data-count="${s.id}">${s.counts.PASS ?? 0}</span></button>`
  ).join("") + `<div class="sep"></div><button type="button" data-sid="gaps"><span>Couldn't screen</span><span class="n">${S.meta.gaps.length}</span></button>`;
  nav.querySelectorAll("button").forEach((b) => b.addEventListener("click", () => { location.hash = b.dataset.sid; }));
}
function renderFreshness() {
  const m = S.meta;
  $("#freshness").innerHTML =
    `<span>Screened ${esc(niceDate(m.screened_on))}</span><span>Prices: close of ${esc(niceDate(m.price_day))}</span>`;
}
async function go(sid, ticker) {
  S.cur = sid;
  store.set("qs-screen", sid);
  document.querySelectorAll("#screenNav button").forEach((b) =>
    b.setAttribute("aria-current", b.dataset.sid === sid ? "page" : "false"));
  $("#main").hidden = true; $("#gapsView").hidden = true; $("#companyView").hidden = true;
  if (sid === "gaps") { $("#gapsView").hidden = false; renderGaps(); return; }
  if (!S.screens[sid]) {
    $("#main").hidden = false;
    $("#table").innerHTML = '<div class="empty">Loading…</div>';
    try {
      S.screens[sid] = await fetchBin("screen_" + sid);
    } catch (e) {
      $("#table").innerHTML = `<div class="empty">Couldn't load this screen's data (${esc(e.message)}). Reload the page to try again.</div>`;
      return;
    }
  }
  if (ticker) { renderCompany(ticker); return; }
  $("#main").hidden = false;
  if (S.lastList !== sid) { S.sort = null; S.lastList = sid; }
  render();
}

/* ------------------------------------------------------------------ screen view */
function render() {
  const scr = S.screens[S.cur];
  const off = offFor(S.cur);
  $("#title").textContent = scr.title;
  $("#purpose").textContent = scr.purpose;
  $("#purpose").classList.toggle("avoid", !!scr.avoid);
  document.title = scr.title + " – Stock Screener";
  renderRules(scr, off);
  renderViews(scr, off);
  renderTable(scr, off);
}

function renderRules(scr, off) {
  const vis = visibleSet();
  const base = scr.rows.map((r) => statusOf(r, scr, off).s);
  const rules = scr.gates.filter((g) => !g.hidden);
  const body = rules.map((r) => {
    const on = !off.has(r.id);
    let gain = 0;
    if (on) {
      const trial = new Set(off); trial.add(r.id);
      scr.rows.forEach((row, i) => { if (!vis.has(base[i]) && vis.has(statusOf(row, scr, trial).s)) gain++; });
    }
    return `<tr class="${on ? "" : "is-off"}">
      <td class="r-name">${esc(r.name)}${r.price ? ' <span class="tag">price</span>' : ""}</td>
      <td class="r-crit">${esc(r.rule)}</td>
      <td class="r-why">${esc(r.why)}</td>
      <td class="r-sw"><button type="button" class="sw" role="switch" aria-checked="${on}" data-id="${esc(r.id)}" aria-label="${esc(r.name)}: ${on ? "on" : "off"}"></button>
        <span class="gain${gain ? " has" : ""}" title="${on ? gain + " more companies would show without this rule" : "rule is off"}">${on ? (gain ? "+" + gain : "") : "off"}</span></td>
    </tr>`;
  }).join("");
  $("#rules").innerHTML = `<table class="rules-tbl"><thead><tr><th>Rule</th><th>Criteria</th><th>Rationale</th><th class="r-sw">On</th></tr></thead><tbody>${body}</tbody></table>`;
  $("#rules").querySelectorAll(".sw").forEach((b) => b.addEventListener("click", () => {
    const id = b.dataset.id;
    if (off.has(id)) off.delete(id); else off.add(id);
    saveOff(S.cur);
    render();
  }));
  $("#resetRules").hidden = off.size === 0;
  const shown = rules.length - rules.filter((r) => off.has(r.id)).length;
  $("#rulesOn").textContent = `${shown} of ${rules.length} on`;
}
$("#resetRules").addEventListener("click", () => { offFor(S.cur).clear(); saveOff(S.cur); render(); });

function renderViews(scr, off) {
  const n = { pass: 0, near: 0 };
  scr.rows.forEach((r) => { const s = statusOf(r, scr, off).s; if (s === "PASS") n.pass++; else if (s === "CHECK" || s === "ONE") n.near++; });
  $("#viewSwitch").innerHTML = VIEWS.map((v) =>
    `<button type="button" role="radio" aria-checked="${v.id === S.view}" data-v="${v.id}">${scr.avoid ? v.avoid : v.label} <span>${n[v.id]}</span></button>`).join("");
  $("#viewSwitch").querySelectorAll("button").forEach((b) => b.addEventListener("click", () => { S.view = b.dataset.v; render(); }));
  const navCount = document.querySelector(`[data-count="${S.cur}"]`);
  if (navCount) navCount.textContent = n.pass;
}
$("#search").addEventListener("input", (e) => { S.q = e.target.value.trim().toLowerCase(); renderTable(S.screens[S.cur], offFor(S.cur)); });

const ORDER = { PASS: 0, CHECK: 1, ONE: 1, FAIL: 2 };
function rangePos(px) {
  if (!px || px.hi == null || px.lo == null || !(px.hi > px.lo)) return null;
  return Math.max(0, Math.min(1, (px.c - px.lo) / (px.hi - px.lo)));
}
function renderTable(scr, off) {
  const vis = visibleSet();
  const M = S.comp.metrics;
  let rows = scr.rows.map((r) => ({ r, st: statusOf(r, scr, off), c: S.comp.companies[r.c] })).filter((x) => x.c);
  rows = S.q ? rows.filter((x) => (x.c.t + " " + x.c.n + " " + (x.c.other || "")).toLowerCase().includes(S.q))
             : rows.filter((x) => vis.has(x.st.s));
  const val = (x, k) => (k === "_t" ? x.c.t : k === "_px" ? (x.c.px && x.c.px.o ? x.c.px.c / x.c.px.o - 1 : null)
    : k === "_rg" ? rangePos(x.c.px) : k === "_ind" ? (x.c.ind || "") : x.c.m[k]);
  if (S.sort) {
    const { k, dir } = S.sort;
    rows.sort((a, b) => {
      const va = val(a, k), vb = val(b, k);
      if (va === undefined || va === null) return 1;
      if (vb === undefined || vb === null) return -1;
      return (va > vb ? 1 : va < vb ? -1 : 0) * dir;
    });
  } else {
    rows.sort((a, b) => ORDER[a.st.s] - ORDER[b.st.s] || (b.c.m.market_cap_usd || 0) - (a.c.m.market_cap_usd || 0));
  }
  const mk = scr.metrics;
  const th = (k, label, cls = "") => {
    const sorted = S.sort && S.sort.k === k;
    const arrow = sorted ? (S.sort.dir > 0 ? " ↑" : " ↓") : "";
    return `<th class="${cls}" aria-sort="${sorted ? (S.sort.dir > 0 ? "ascending" : "descending") : "none"}"><button type="button" data-k="${k}" class="${sorted ? "sorted" : ""}">${esc(label)}${arrow}</button></th>`;
  };
  const head = `<thead><tr>${th("_t", "Company", "c-co")}${th("_px", "Price (vs open)", "c-px num")}${th("_rg", "52-week range", "c-rg")}${th("_ind", "Industry", "c-ind")}` +
    mk.map((k) => th(k, M[k][0], "num")).join("") + "</tr></thead>";
  const shown = rows.slice(0, 400);
  const body = shown.map((x) => rowHTML(x, scr, mk)).join("");
  const empty = S.q ? "No company matches that search in this screen." : scr.avoid ? "No company is flagged with these rules."
    : S.view === "pass" ? "No company passes with these rules. See Near misses, or switch a rule off." : "No near misses with these rules.";
  $("#table").innerHTML = `<table class="list-tbl">${head}<tbody>${body}</tbody></table>` + (shown.length ? "" : `<div class="empty">${empty}</div>`);
  $("#listNote").textContent = `${rows.length} of ${scr.rows.length} companies` +
    (rows.length > shown.length ? ` (first ${shown.length}; search to find others)` : "") + ". Select a company for its page.";
  $("#table").querySelectorAll("thead button").forEach((b) => b.addEventListener("click", () => {
    const k = b.dataset.k;
    const better = k.startsWith("_") ? null : M[k][2];
    S.sort = S.sort && S.sort.k === k ? { k, dir: -S.sort.dir } : { k, dir: better === "high" ? -1 : 1 };
    renderTable(scr, off);
  }));
  $("#table").querySelectorAll("tbody tr").forEach((el) => {
    el.addEventListener("click", (e) => { if (!e.target.closest("a")) location.hash = `${S.cur}/${el.dataset.t}`; });
    el.addEventListener("keydown", (e) => { if (e.key === "Enter") location.hash = `${S.cur}/${el.dataset.t}`; });
  });
}

function pxHTML(px) {
  if (!px) return "–";
  const ch = px.o ? (px.c / px.o - 1) * 100 : null;
  return `<span class="cl">${money(px.c)}</span>` +
    (ch !== null ? ` <span class="chg ${ch >= 0 ? "up" : "dn"}">${ch >= 0 ? "+" : ""}${ch.toFixed(1)}%</span>` : "");
}
function rangeHTML(px) {
  const p = rangePos(px);
  if (p === null) return '<span class="muted">–</span>';
  return `<div class="rg" title="52-week low ${money(px.lo)}, high ${money(px.hi)}"><span>${money(px.lo)}</span>` +
    `<span class="rg-bar"><b style="left:${(p * 100).toFixed(1)}%"></b></span><span>${money(px.hi)}</span></div>`;
}
function rowHTML(x, scr, mk) {
  const c = x.c;
  const reason = x.st.s === "FAIL" ? "Fails: " + x.st.fails.map((g) => g.name).join(", ") : reasonOf(x.st, x.r, scr);
  const cells = mk.map((k) => {
    const u = c.mu.includes(k);
    return `<td class="num" data-label="${esc(S.comp.metrics[k][0])}"><span class="${u ? "u" : ""}" ${u ? `title="Unverified: ${esc(c.vi)}"` : ""}>${u ? "≈" : ""}${fmt(c.m[k], S.comp.metrics[k][1])}</span></td>`;
  }).join("");
  const pill = x.st.s === "CHECK" ? "chk" : x.st.s === "PASS" ? "" : "miss";
  return `<tr tabindex="0" data-t="${esc(c.t)}">
    <td class="c-co"><span class="tk">${esc(c.t)}</span> <span class="nm" title="${esc(c.n)}">${esc(c.n)}</span>${reason ? `<div class="why ${pill}">${esc(reason)}</div>` : ""}</td>
    <td class="c-px num" data-label="Price (vs open)">${pxHTML(c.px)}</td>
    <td class="c-rg" data-label="52-week range">${rangeHTML(c.px)}</td>
    <td class="c-ind" data-label="Industry"><span title="${esc(c.ind)}">${esc(c.ind || "–")}</span></td>
    ${cells}
  </tr>`;
}

/* ------------------------------------------------------------------ company page */
const MULT = { pe: ["P/E", "x"], ev_ebit: ["EV/EBIT", "x"], fcf_yield: ["FCF yield", "pct"], ev_ebitda: ["EV/EBITDA", "x"],
  ev_sales: ["EV/Sales", "x"], pb: ["P/B", "x"] };
const VERDICT = { cheap: "Cheap", expensive: "Expensive", mixed: "Mixed", "in line": "In line" };

function renderCompany(ticker) {
  const cid = S.byTicker[ticker];
  const c = S.comp.companies[cid];
  const scr = S.screens[S.cur];
  const row = scr.rows.find((r) => r.c === cid);
  S.company = cid;
  document.title = `${c.t} – Stock Screener`;
  let status = "";
  if (row) {
    const st = statusOf(row, scr, offFor(S.cur));
    const lab = st.s === "PASS" ? (scr.avoid ? "Flagged" : "Passes") : st.s === "FAIL" ? (scr.avoid ? "Not flagged" : "Fails") : (scr.avoid ? "Nearly flagged" : "Near miss");
    const why = st.s === "FAIL" ? "Fails: " + st.fails.map((g) => g.name).join(", ") : reasonOf(st, row, scr);
    status = `<p class="status s-${st.s}"><b>${esc(scr.title)}: ${lab}.</b> ${esc(why)}</p>`;
  }
  const links = [c.url ? `<a href="${esc(c.url)}" target="_blank" rel="noopener">Latest annual report (SEC)</a>` : "",
    c.ev && c.ev.url ? `<a href="${esc(c.ev.url)}" target="_blank" rel="noopener">${esc(c.ev.types)} filing (${esc(c.ev.date)})</a>` : ""].filter(Boolean).join("");
  const M = S.comp.metrics;
  const keys = ["market_cap_usd", ...scr.metrics];
  const facts = keys.filter((k) => c.m[k] !== undefined).map((k) =>
    `<div class="fact"><span>${esc(M[k][0])}</span><b>${c.mu.includes(k) ? "≈" : ""}${fmt(c.m[k], M[k][1])}</b></div>`).join("");
  $("#companyView").hidden = false;
  $("#companyView").innerHTML = `
    <a class="back" href="#${esc(S.cur)}">← ${esc(scr.title)}</a>
    <header class="co-head">
      <div>
        <h2>${esc(c.t)} <span class="co-name">${esc(c.n)}</span></h2>
        <p class="co-sub">${esc(c.ind || "")}${c.ex ? " · " + esc(c.ex) : ""}${c.other ? " · also " + esc(c.other) : ""}</p>
      </div>
      <div class="co-px">${pxHTML(c.px)}${c.px && c.px.hi != null ? `<div class="co-rg">${rangeHTML(c.px)}</div>` : ""}</div>
    </header>
    ${status}
    <div class="facts">${facts}</div>
    <section class="card">
      <h3>About the company</h3>
      <p>${c.sum ? esc(c.sum) : '<span class="muted">Description not written yet.</span>'}</p>
      ${links ? `<p class="links">${links}</p>` : ""}
    </section>
    <section class="card" id="pvCard">${pvHTML(c)}</section>
    <section class="card">
      <h3>Financial statements</h3>
      ${c.mdl ? `<p class="muted">Income statement, balance sheet, cash flow and a metrics page for up to 10 years, from SEC filings, as an Excel file.</p>
        <button type="button" id="genXlsx" class="btn">Generate financial statements</button> <span id="genMsg" class="muted"></span>`
      : '<p class="muted">No statement data stored for this company.</p>'}
    </section>`;
  window.scrollTo(0, 0);
  bindPv(c);
  const gb = $("#genXlsx");
  if (gb) gb.addEventListener("click", () => generateModel(cid, gb));
}

function pvHTML(c) {
  const pv = c.pv;
  if (!pv) return `<h3>Valuation against peers</h3><p class="muted">Prepared for companies on a Pass or Near-miss list.</p>`;
  const k = pv.mult.includes(S.pvMult) ? S.pvMult : pv.mult[0];
  const f = MULT[k][1];
  const tabs = pv.mult.length > 1 ? `<div class="seg small" role="tablist">${pv.mult.map((m) =>
    `<button type="button" role="tab" aria-selected="${m === k}" data-m="${m}">${MULT[m][0]}</button>`).join("")}</div>` : "";
  const vd = pv.verdict[k] || {};
  const rows = pv.rows.map((r) => {
    const v = r.v[k] || [];
    const avg10 = v[2] != null ? fmt(v[2], f) + (v[3] && v[3] < 10 ? `<sup>${v[3]}y</sup>` : "") : "–";
    return `<tr class="${r.me ? "me" : ""}"><td>${esc(r.t)}<span class="pn">${esc(r.n || "")}</span></td><td>${fmt(r.rev, "usd")}</td>` +
      `<td>${fmt(v[0], f)}</td><td>${fmt(v[1], f)}</td><td>${avg10}</td></tr>`;
  }).join("");
  const peerNote = pv.rows.length > 1 ? `${pv.rows.length - 1} closest companies by industry code and revenue.` : "No peers found.";
  return `<div class="pv-top"><h3>Valuation against peers</h3>${pv.overall ? `<span class="chip v-${pv.overall.replace(" ", "-")}">${VERDICT[pv.overall]} overall</span>` : ""}</div>
    ${tabs}
    <div class="tbl-wrap"><table class="pv-tbl"><thead><tr><th>Company</th><th>Revenue</th><th>Now</th><th>3-yr avg</th><th>10-yr avg</th></tr></thead><tbody>${rows}</tbody></table></div>
    <p class="muted small">${vd.v ? `<b>${MULT[k][0]}: ${VERDICT[vd.v]}</b> against its own history and the peer median (${fmt(vd.peer_med, f)}). ` : ""}${peerNote} Averages use fiscal-year-end prices. For information only, not a rule.</p>`;
}
function bindPv(c) {
  document.querySelectorAll("#pvCard [data-m]").forEach((b) => b.addEventListener("click", () => {
    S.pvMult = b.dataset.m;
    $("#pvCard").innerHTML = pvHTML(c);
    bindPv(c);
  }));
}

/* ------------------------------------------------------------------ Excel model (built in the browser) */
let excelLib = null;
function loadExcel() {
  if (excelLib) return excelLib;
  excelLib = new Promise((res, rej) => {
    const s = document.createElement("script");
    s.src = "vendor/exceljs.min.js";
    s.onload = () => res(window.ExcelJS);
    s.onerror = () => { excelLib = null; rej(new Error("couldn't load the Excel library")); };
    document.head.appendChild(s);
  });
  return excelLib;
}
async function generateModel(cid, btn) {
  const msg = $("#genMsg");
  btn.disabled = true;
  msg.textContent = "Building…";
  try {
    const shards = S.meta.model_shards || 64;
    const [Excel, shard] = await Promise.all([loadExcel(), fetchBin("model_" + String(Number(cid) % shards).padStart(2, "0"))]);
    const mdl = shard[cid];
    if (!mdl) throw new Error("no statement data for this company");
    const wb = buildModel(Excel, mdl);
    const buf = await wb.xlsx.writeBuffer();
    const a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([buf], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" }));
    a.download = `${mdl.t}_financial_statements.xlsx`;
    document.body.appendChild(a);
    a.click();
    setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
    msg.textContent = "Downloaded.";
  } catch (e) {
    msg.textContent = "Couldn't build the file: " + e.message;
  } finally {
    btn.disabled = false;
  }
}

/* Workbook layout (annual, GS-style): Cover, IS, BS, CF, Metrics. Blue = reported figures (SEC), black = formulas.
   Amounts in millions of the reporting currency; per-share figures in units. */
function buildModel(Excel, mdl) {
  const wb = new Excel.Workbook();
  wb.creator = "Stock Screener";
  const Y = mdl.years;
  const n = Y.length;
  const cur = mdl.currency || "USD";
  const col = (i) => String.fromCharCode(66 + i);           // year i -> column B, C, ...
  const lastCol = col(n - 1);
  const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  const fye = mdl.fye ? months[Number(mdl.fye.slice(5, 7)) - 1] : "";
  const BLUE = { color: { argb: "FF1F4FBF" } };
  const NUM = '#,##0.0;(#,##0.0);"–"', PCT = '0.0%;(0.0%);"–"', MULTF = '0.0"x";(0.0"x");"–"', EPS = '0.00;(0.00);"–"', DAYS = '0;(0);"–"';
  const mil = (v) => (v === undefined || v === null ? null : v / 1e6);
  const g = (y, k) => (y[k] === undefined ? null : y[k]);

  function sheet(name, title) {
    const ws = wb.addWorksheet(name, { views: [{ state: "frozen", xSplit: 1, ySplit: 5, showGridLines: false }] });
    ws.getColumn(1).width = 44;
    for (let i = 0; i < n; i++) ws.getColumn(i + 2).width = 12;
    ws.getCell("A1").value = `${mdl.n} (${mdl.t})`;
    ws.getCell("A1").font = { bold: true, size: 13 };
    ws.getCell("A2").value = title;
    ws.getCell("A2").font = { bold: true };
    ws.getCell("A3").value = `Fiscal year ends ${fye}; ${cur} millions except per-share data`;
    ws.getCell("A3").font = { italic: true, color: { argb: "FF5B6977" } };
    const hr = ws.getRow(5);
    hr.getCell(1).value = "";
    Y.forEach((y, i) => { hr.getCell(i + 2).value = `FY${y.fy}A`; });
    hr.font = { bold: true };
    hr.eachCell((c) => { c.border = { bottom: { style: "thin" } }; c.alignment = { horizontal: "right" }; });
    ws._qr = 6;
    ws._qk = {};
    return ws;
  }
  /* add a row: vals = function(i) -> number | {formula} | null; key = name to reference */
  function add(ws, key, label, vals, opt = {}) {
    const r = ws._qr++;
    const row = ws.getRow(r);
    row.getCell(1).value = label;
    if (opt.indent) row.getCell(1).alignment = { indent: opt.indent };
    if (vals) {
      for (let i = 0; i < n; i++) {
        const v = vals(i);
        if (v === null || v === undefined || (typeof v === "number" && !Number.isFinite(v))) continue;
        const cell = row.getCell(i + 2);
        cell.value = v;
        cell.numFmt = opt.fmt || NUM;
        if (typeof v === "number") cell.font = BLUE;
      }
    }
    if (opt.bold) row.font = { bold: true };
    if (opt.top) for (let i = 1; i <= n + 1; i++) row.getCell(i).border = { top: { style: "thin" } };
    if (opt.italic) row.getCell(1).font = { italic: true, color: { argb: "FF5B6977" } };
    if (key) ws._qk[key] = r;
    return r;
  }
  const gap = (ws) => { ws._qr++; };
  const head = (ws, text) => { const r = ws._qr++; ws.getCell(`A${r}`).value = text; ws.getCell(`A${r}`).font = { bold: true, color: { argb: "FF14212E" } }; };
  const ref = (ws, key, i, sheetName) => (ws._qk[key] ? `${sheetName ? `'${sheetName}'!` : ""}${col(i)}${ws._qk[key]}` : null);
  const F = (expr) => ({ formula: expr });
  const iferr = (expr) => F(`IFERROR(${expr},"")`);
  const has = (k) => Y.some((y) => y[k] !== undefined && y[k] !== null);

  /* ---------------- Cover */
  const cv = wb.addWorksheet("Cover", { views: [{ showGridLines: false }] });
  cv.getColumn(1).width = 26; cv.getColumn(2).width = 80;
  [["Company", `${mdl.n} (${mdl.t})`], ["Industry", mdl.ind || ""], ["Fiscal year end", fye], ["Currency", `${cur} millions (per-share data in ${cur})`],
    ["Years", `FY${Y[0].fy} – FY${Y[n - 1].fy} (annual, as reported)`], ["Source", "SEC XBRL financial statements (10-K / 20-F). Month-end prices, split-adjusted, for the valuation block."],
    ["Colour code", "Blue = reported figure. Black = formula. 'Other' lines balance each statement to its reported total."],
    ["Generated", new Date().toISOString().slice(0, 10)]].forEach(([a, b], i) => {
    cv.getCell(`A${i + 2}`).value = a; cv.getCell(`A${i + 2}`).font = { bold: true };
    cv.getCell(`B${i + 2}`).value = b; cv.getCell(`B${i + 2}`).alignment = { wrapText: true };
  });
  cv.getCell("A1").value = "Financial statements"; cv.getCell("A1").font = { bold: true, size: 14 };

  /* ---------------- Income statement */
  const is = sheet("IS", "Income Statement");
  const IS = "IS";
  add(is, "rev", "Revenue", (i) => mil(g(Y[i], "revenue")), { bold: true });
  add(is, "rev_g", "% yoy", (i) => (i ? iferr(`${col(i)}${is._qk.rev}/${col(i - 1)}${is._qk.rev}-1`) : null), { fmt: PCT, italic: true, indent: 1 });
  const cogsIn = has("cost_of_revenue"), gpIn = has("gross_profit");
  add(is, "cogs", "Cost of revenue", (i) => {
    const y = Y[i];
    if (y.cost_of_revenue != null) return mil(y.cost_of_revenue);
    if (y.gross_profit != null && y.revenue != null) return F(`${col(i)}${is._qk.rev}-${mil(y.gross_profit)}`);
    return null;
  });
  add(is, "gp", "Gross profit", (i) => {
    const y = Y[i];
    if (y.cost_of_revenue != null || y.gross_profit != null) return F(`${col(i)}${is._qk.rev}-${col(i)}${is._qk.cogs}`);
    return null;
  }, { bold: true, top: true });
  add(is, "gm", "Gross margin", (i) => iferr(`${col(i)}${is._qk.gp}/${col(i)}${is._qk.rev}`), { fmt: PCT, italic: true, indent: 1 });
  const split = has("selling_marketing") || has("general_admin");
  const opex = [];
  if (split) {
    opex.push(add(is, "sm", "Sales & marketing", (i) => mil(g(Y[i], "selling_marketing")), { indent: 1 }));
    opex.push(add(is, "ga", "General & administrative", (i) => mil(g(Y[i], "general_admin")), { indent: 1 }));
  } else {
    opex.push(add(is, "sga", "Selling, general & administrative", (i) => mil(g(Y[i], "sga")), { indent: 1 }));
  }
  opex.push(add(is, "rnd", "Research & development", (i) => mil(g(Y[i], "rnd")), { indent: 1 }));
  const otherOpRow = is._qr;
  add(is, "oth_op", "Other operating expense, net", (i) => {
    if (Y[i].x_operating_income == null || (!cogsIn && !gpIn)) return null;
    return F(`${col(i)}${is._qk.gp}-${opex.map((r) => `${col(i)}${r}`).join("-")}-${col(i)}${otherOpRow + 2}`);
  }, { indent: 1 });
  add(is, "opex", "Total operating expenses", (i) => ((cogsIn || gpIn) && Y[i].x_operating_income != null
    ? F(`SUM(${col(i)}${opex[0]}:${col(i)}${otherOpRow})`) : null), { top: true });
  add(is, "ebit", "Operating income (EBIT)", (i) => mil(g(Y[i], "x_operating_income")), { bold: true });
  add(is, "om", "Operating margin", (i) => iferr(`${col(i)}${is._qk.ebit}/${col(i)}${is._qk.rev}`), { fmt: PCT, italic: true, indent: 1 });
  add(is, "da", "Depreciation & amortization", (i) => mil(g(Y[i], "da") != null ? Math.abs(Y[i].da) : null), { indent: 1 });
  add(is, "ebitda", "EBITDA", (i) => (Y[i].da != null && Y[i].x_operating_income != null ? F(`${col(i)}${is._qk.ebit}+${col(i)}${is._qk.da}`) : null), { bold: true });
  add(is, "ebitda_m", "EBITDA margin", (i) => iferr(`${col(i)}${is._qk.ebitda}/${col(i)}${is._qk.rev}`), { fmt: PCT, italic: true, indent: 1 });
  gap(is);
  add(is, "int_exp", "Interest expense", (i) => (Y[i].interest_expense != null ? -Math.abs(mil(Y[i].interest_expense)) : null), { indent: 1 });
  add(is, "int_inc", "Interest income", (i) => mil(g(Y[i], "interest_income")), { indent: 1 });
  add(is, "oth_nonop", "Other non-operating income, net", (i) => (Y[i].pretax_income != null && Y[i].x_operating_income != null
    ? F(`${col(i)}${is._qk.int_exp + 3}-${col(i)}${is._qk.ebit}-${col(i)}${is._qk.int_exp}-${col(i)}${is._qk.int_inc}`) : null), { indent: 1 });
  add(is, "pretax", "Pretax income", (i) => mil(g(Y[i], "pretax_income")), { bold: true, top: true });
  add(is, "tax", "Income tax", (i) => (Y[i].income_tax != null ? -mil(Y[i].income_tax) : null), { indent: 1 });
  add(is, "etr", "Effective tax rate", (i) => iferr(`-${col(i)}${is._qk.tax}/${col(i)}${is._qk.pretax}`), { fmt: PCT, italic: true, indent: 1 });
  add(is, "ni", "Net income", (i) => mil(g(Y[i], "net_income")), { bold: true, top: true });
  add(is, "ni_g", "% yoy", (i) => (i ? iferr(`${col(i)}${is._qk.ni}/${col(i - 1)}${is._qk.ni}-1`) : null), { fmt: PCT, italic: true, indent: 1 });
  add(is, "nm", "Net margin", (i) => iferr(`${col(i)}${is._qk.ni}/${col(i)}${is._qk.rev}`), { fmt: PCT, italic: true, indent: 1 });
  gap(is);
  add(is, "eps", "Diluted EPS (as reported)", (i) => g(Y[i], "eps_diluted"), { fmt: EPS });
  add(is, "sh_rep", "Diluted shares, m (as reported)", (i) => mil(g(Y[i], "diluted_shares")));
  add(is, "sh", "Diluted shares, m (today's share basis)", (i) => mil(g(Y[i], "shares_basis")));
  add(is, "eps_adj", "EPS on today's share basis", (i) => iferr(`${col(i)}${is._qk.ni}/${col(i)}${is._qk.sh}`), { fmt: EPS });
  add(is, "sbc", "Stock-based compensation (memo)", (i) => mil(g(Y[i], "sbc")), { italic: true });

  /* ---------------- Balance sheet */
  const bs = sheet("BS", "Balance Sheet");
  head(bs, "Assets");
  const ca = [];
  ca.push(add(bs, "cash", "Cash & equivalents", (i) => mil(g(Y[i], "cash")), { indent: 1 }));
  ca.push(add(bs, "sti", "Short-term investments", (i) => mil(g(Y[i], "st_investments")), { indent: 1 }));
  ca.push(add(bs, "ar", "Accounts receivable", (i) => mil(g(Y[i], "accounts_receivable")), { indent: 1 }));
  ca.push(add(bs, "inv", "Inventory", (i) => mil(g(Y[i], "inventory")), { indent: 1 }));
  const tcaRow = bs._qr + 1;
  add(bs, "oca", "Other current assets", (i) => (Y[i].assets_current != null ? F(`${col(i)}${tcaRow}-SUM(${col(i)}${ca[0]}:${col(i)}${ca[3]})`) : null), { indent: 1 });
  add(bs, "tca", "Total current assets", (i) => mil(g(Y[i], "assets_current")), { bold: true, top: true });
  const nca = [];
  nca.push(add(bs, "ppe", "PP&E, net", (i) => mil(g(Y[i], "ppe_net")), { indent: 1 }));
  nca.push(add(bs, "gw", "Goodwill", (i) => mil(g(Y[i], "goodwill")), { indent: 1 }));
  nca.push(add(bs, "intang", "Intangible assets", (i) => mil(g(Y[i], "intangibles")), { indent: 1 }));
  nca.push(add(bs, "lti", "Long-term investments", (i) => mil(g(Y[i], "lt_investments")), { indent: 1 }));
  const taRow = bs._qr + 1;
  add(bs, "onca", "Other non-current assets", (i) => (Y[i].assets != null && Y[i].assets_current != null
    ? F(`${col(i)}${taRow}-${col(i)}${bs._qk.tca}-SUM(${col(i)}${nca[0]}:${col(i)}${nca[3]})`) : null), { indent: 1 });
  add(bs, "ta", "Total assets", (i) => mil(g(Y[i], "assets")), { bold: true, top: true });
  gap(bs);
  head(bs, "Liabilities and equity");
  const cl = [];
  cl.push(add(bs, "ap", "Accounts payable", (i) => mil(g(Y[i], "accounts_payable")), { indent: 1 }));
  cl.push(add(bs, "accr", "Accrued liabilities", (i) => mil(g(Y[i], "accrued_liabilities")), { indent: 1 }));
  cl.push(add(bs, "dr_c", "Deferred revenue, current", (i) => mil(g(Y[i], "deferred_revenue_current")), { indent: 1 }));
  const tclRow = bs._qr + 1;
  add(bs, "ocl", "Other current liabilities (incl. short-term debt)", (i) => (Y[i].liabilities_current != null
    ? F(`${col(i)}${tclRow}-SUM(${col(i)}${cl[0]}:${col(i)}${cl[2]})`) : null), { indent: 1 });
  add(bs, "tcl", "Total current liabilities", (i) => mil(g(Y[i], "liabilities_current")), { bold: true, top: true });
  add(bs, "dr_nc", "Deferred revenue, non-current", (i) => mil(g(Y[i], "deferred_revenue_noncurrent")), { indent: 1 });
  const tlRow = bs._qr + 1;
  const tl = (i) => {
    const y = Y[i];
    if (y.liabilities != null) return mil(y.liabilities);
    if (y.assets != null && y.equity != null) {   // not tagged: total assets less equity, minority and preferred
      return F(`${col(i)}${bs._qk.ta}-${mil(y.equity)}-${mil(y.minority_interest || 0)}-${mil(y.preferred_equity || 0)}`);
    }
    return null;
  };
  add(bs, "oncl", "Other non-current liabilities (incl. long-term debt)", (i) => (tl(i) !== null && Y[i].liabilities_current != null
    ? F(`${col(i)}${tlRow}-${col(i)}${bs._qk.tcl}-${col(i)}${bs._qk.dr_nc}`) : null), { indent: 1 });
  add(bs, "tl", "Total liabilities", tl, { bold: true, top: true });
  add(bs, "pref", "Preferred equity", (i) => mil(g(Y[i], "preferred_equity")), { indent: 1 });
  add(bs, "mi", "Non-controlling interest", (i) => mil(g(Y[i], "minority_interest")), { indent: 1 });
  add(bs, "eq", "Shareholders' equity", (i) => mil(g(Y[i], "equity")), { indent: 1 });
  add(bs, "re", "of which retained earnings", (i) => mil(g(Y[i], "retained_earnings")), { indent: 2, italic: true });
  add(bs, "tle", "Total liabilities & equity", (i) => F(`${col(i)}${bs._qk.tl}+${col(i)}${bs._qk.pref}+${col(i)}${bs._qk.mi}+${col(i)}${bs._qk.eq}`), { bold: true, top: true });
  add(bs, "chk", "Check (assets – liabilities & equity)", (i) => (Y[i].assets != null ? F(`ROUND(${col(i)}${bs._qk.ta}-${col(i)}${bs._qk.tle},1)`) : null), { italic: true });
  gap(bs);
  head(bs, "Memo");
  add(bs, "debt", "Total debt", (i) => mil(g(Y[i], "x_total_debt")), { indent: 1 });
  add(bs, "netdebt", "Net debt (debt – cash – short-term investments)", (i) => F(`${col(i)}${bs._qk.debt}-${col(i)}${bs._qk.cash}-${col(i)}${bs._qk.sti}`), { indent: 1 });
  add(bs, "nwc", "Net working capital (current assets ex cash – current liabilities)", (i) => (Y[i].assets_current != null && Y[i].liabilities_current != null
    ? F(`${col(i)}${bs._qk.tca}-${col(i)}${bs._qk.cash}-${col(i)}${bs._qk.sti}-${col(i)}${bs._qk.tcl}`) : null), { indent: 1 });
  add(bs, "ic", "Invested capital (screener definition)", (i) => mil(g(Y[i], "x_invested_capital")), { indent: 1 });

  /* ---------------- Cash flow */
  const cf = sheet("CF", "Cash Flow Statement");
  head(cf, "Operating activities");
  add(cf, "ni", "Net income", (i) => F(`'${IS}'!${col(i)}${is._qk.ni}`), { indent: 1 });
  add(cf, "da", "Depreciation & amortization", (i) => F(`'${IS}'!${col(i)}${is._qk.da}`), { indent: 1 });
  add(cf, "sbc", "Stock-based compensation", (i) => mil(g(Y[i], "sbc")), { indent: 1 });
  const cfoRow = cf._qr + 1;
  add(cf, "wc", "Working capital and other items", (i) => (Y[i].ocf != null ? F(`${col(i)}${cfoRow}-${col(i)}${cf._qk.ni}-${col(i)}${cf._qk.da}-${col(i)}${cf._qk.sbc}`) : null), { indent: 1 });
  add(cf, "cfo", "Cash from operations", (i) => mil(g(Y[i], "ocf")), { bold: true, top: true });
  gap(cf);
  head(cf, "Investing activities");
  const neg = (v) => (v === undefined || v === null ? null : -Math.abs(v / 1e6));
  add(cf, "capex", "Capital expenditure (PP&E)", (i) => neg(Y[i].capex_ppe), { indent: 1 });
  add(cf, "capsw", "Capitalized software", (i) => neg(Y[i].capex_software), { indent: 1 });
  add(cf, "acq", "Acquisitions", (i) => neg(Y[i].acquisitions), { indent: 1 });
  const cfiRow = cf._qr + 1;
  add(cf, "oinv", "Other investing (incl. securities)", (i) => (Y[i].cfi != null ? F(`${col(i)}${cfiRow}-SUM(${col(i)}${cf._qk.capex}:${col(i)}${cf._qk.acq})`) : null), { indent: 1 });
  add(cf, "cfi", "Cash from investing", (i) => mil(g(Y[i], "cfi")), { bold: true, top: true });
  gap(cf);
  head(cf, "Financing activities");
  add(cf, "dbt_i", "Debt issued", (i) => mil(g(Y[i], "debt_issued")), { indent: 1 });
  add(cf, "dbt_r", "Debt repaid", (i) => neg(Y[i].debt_repaid), { indent: 1 });
  add(cf, "bb", "Share buybacks", (i) => neg(Y[i].buybacks), { indent: 1 });
  add(cf, "div", "Dividends paid", (i) => neg(Y[i].dividends), { indent: 1 });
  add(cf, "eqi", "Shares issued", (i) => mil(g(Y[i], "equity_issued")), { indent: 1 });
  const cffRow = cf._qr + 1;
  add(cf, "ofin", "Other financing", (i) => (Y[i].cff != null ? F(`${col(i)}${cffRow}-SUM(${col(i)}${cf._qk.dbt_i}:${col(i)}${cf._qk.eqi})`) : null), { indent: 1 });
  add(cf, "cff", "Cash from financing", (i) => mil(g(Y[i], "cff")), { bold: true, top: true });
  add(cf, "fx", "Exchange-rate effect", (i) => mil(g(Y[i], "fx_effect")), { indent: 1 });
  add(cf, "chg", "Net change in cash", (i) => (Y[i].ocf != null && Y[i].cfi != null && Y[i].cff != null
    ? F(`${col(i)}${cf._qk.cfo}+${col(i)}${cf._qk.cfi}+${col(i)}${cf._qk.cff}+${col(i)}${cf._qk.fx}`) : null), { bold: true, top: true });
  gap(cf);
  head(cf, "Free cash flow");
  add(cf, "fcf", "Free cash flow (CFO – capex – capitalized software)", (i) => (Y[i].ocf != null
    ? F(`${col(i)}${cf._qk.cfo}+${col(i)}${cf._qk.capex}+${col(i)}${cf._qk.capsw}`) : null), { bold: true });
  add(cf, "fcf_m", "FCF margin", (i) => iferr(`${col(i)}${cf._qk.fcf}/'${IS}'!${col(i)}${is._qk.rev}`), { fmt: PCT, italic: true, indent: 1 });
  add(cf, "fcf_ps", "FCF per share (today's share basis)", (i) => iferr(`${col(i)}${cf._qk.fcf}/'${IS}'!${col(i)}${is._qk.sh}`), { fmt: EPS, indent: 1 });
  add(cf, "fcf_ni", "FCF / net income", (i) => iferr(`${col(i)}${cf._qk.fcf}/${col(i)}${cf._qk.ni}`), { fmt: MULTF, indent: 1 });

  /* ---------------- Metrics */
  const mt = sheet("Metrics", "Key metrics");
  const ISr = (k, i) => `'${IS}'!${col(i)}${is._qk[k]}`;
  const BSr = (k, i) => `'BS'!${col(i)}${bs._qk[k]}`;
  const CFr = (k, i) => `'CF'!${col(i)}${cf._qk[k]}`;
  const avg = (fn, i) => (i ? `AVERAGE(${fn(i)},${fn(i - 1)})` : fn(i));
  head(mt, "Growth");
  add(mt, null, "Revenue growth", (i) => (i ? iferr(`${ISr("rev", i)}/${ISr("rev", i - 1)}-1`) : null), { fmt: PCT, indent: 1 });
  add(mt, null, "Revenue CAGR, 3 years", (i) => (i >= 3 ? iferr(`(${ISr("rev", i)}/${ISr("rev", i - 3)})^(1/3)-1`) : null), { fmt: PCT, indent: 1 });
  add(mt, null, "Revenue CAGR, 5 years", (i) => (i >= 5 ? iferr(`(${ISr("rev", i)}/${ISr("rev", i - 5)})^(1/5)-1`) : null), { fmt: PCT, indent: 1 });
  add(mt, null, "EBIT growth", (i) => (i ? iferr(`${ISr("ebit", i)}/${ISr("ebit", i - 1)}-1`) : null), { fmt: PCT, indent: 1 });
  add(mt, null, "EPS growth (today's share basis)", (i) => (i ? iferr(`${ISr("eps_adj", i)}/${ISr("eps_adj", i - 1)}-1`) : null), { fmt: PCT, indent: 1 });
  add(mt, null, "FCF per share growth", (i) => (i ? iferr(`${CFr("fcf_ps", i)}/${CFr("fcf_ps", i - 1)}-1`) : null), { fmt: PCT, indent: 1 });
  add(mt, null, "Diluted share count change", (i) => (i ? iferr(`${ISr("sh", i)}/${ISr("sh", i - 1)}-1`) : null), { fmt: PCT, indent: 1 });
  gap(mt);
  head(mt, "Margins");
  add(mt, null, "Gross margin", (i) => F(ISr("gm", i)), { fmt: PCT, indent: 1 });
  add(mt, null, "Operating (EBIT) margin", (i) => F(ISr("om", i)), { fmt: PCT, indent: 1 });
  add(mt, null, "EBITDA margin", (i) => F(ISr("ebitda_m", i)), { fmt: PCT, indent: 1 });
  add(mt, null, "Net margin", (i) => F(ISr("nm", i)), { fmt: PCT, indent: 1 });
  add(mt, null, "FCF margin", (i) => F(CFr("fcf_m", i)), { fmt: PCT, indent: 1 });
  add(mt, null, "R&D / revenue", (i) => iferr(`${ISr("rnd", i)}/${ISr("rev", i)}`), { fmt: PCT, indent: 1 });
  add(mt, null, "Stock-based comp / revenue", (i) => iferr(`${ISr("sbc", i)}/${ISr("rev", i)}`), { fmt: PCT, indent: 1 });
  gap(mt);
  head(mt, "Returns");
  add(mt, "taxr", "Tax rate used for NOPAT", (i) => g(Y[i], "x_tax_rate_used"), { fmt: PCT, indent: 1 });
  add(mt, "nopat", "NOPAT (EBIT × (1 – tax rate))", (i) => F(`${ISr("ebit", i)}*(1-${col(i)}${mt._qk.taxr})`), { indent: 1 });
  add(mt, null, "ROIC (NOPAT / average invested capital)", (i) => iferr(`${col(i)}${mt._qk.nopat}/${avg((j) => BSr("ic", j), i)}`), { fmt: PCT, indent: 1 });
  add(mt, null, "Cash ROIC (FCF / average invested capital)", (i) => iferr(`${CFr("fcf", i)}/${avg((j) => BSr("ic", j), i)}`), { fmt: PCT, indent: 1 });
  add(mt, null, "Return on equity", (i) => iferr(`${ISr("ni", i)}/${avg((j) => BSr("eq", j), i)}`), { fmt: PCT, indent: 1 });
  add(mt, null, "Return on assets", (i) => iferr(`${ISr("ni", i)}/${avg((j) => BSr("ta", j), i)}`), { fmt: PCT, indent: 1 });
  gap(mt);
  head(mt, "Cash conversion and reinvestment");
  add(mt, null, "FCF / net income", (i) => F(CFr("fcf_ni", i)), { fmt: MULTF, indent: 1 });
  add(mt, null, "Cash from operations / net income", (i) => iferr(`${CFr("cfo", i)}/${ISr("ni", i)}`), { fmt: MULTF, indent: 1 });
  add(mt, null, "Capex / revenue", (i) => iferr(`-(${CFr("capex", i)}+${CFr("capsw", i)})/${ISr("rev", i)}`), { fmt: PCT, indent: 1 });
  add(mt, null, "Capex / D&A", (i) => iferr(`-(${CFr("capex", i)}+${CFr("capsw", i)})/${ISr("da", i)}`), { fmt: MULTF, indent: 1 });
  add(mt, null, "Buybacks + dividends / FCF", (i) => iferr(`-(${CFr("bb", i)}+${CFr("div", i)})/${CFr("fcf", i)}`), { fmt: PCT, indent: 1 });
  add(mt, null, "Acquisitions / cash from operations", (i) => iferr(`-${CFr("acq", i)}/${CFr("cfo", i)}`), { fmt: PCT, indent: 1 });
  gap(mt);
  head(mt, "Balance sheet");
  add(mt, null, "Net debt / EBITDA", (i) => iferr(`${BSr("netdebt", i)}/${ISr("ebitda", i)}`), { fmt: MULTF, indent: 1 });
  add(mt, null, "Net debt / cash from operations", (i) => iferr(`${BSr("netdebt", i)}/${CFr("cfo", i)}`), { fmt: MULTF, indent: 1 });
  add(mt, null, "Interest coverage (EBIT / interest)", (i) => iferr(`${ISr("ebit", i)}/-${ISr("int_exp", i)}`), { fmt: MULTF, indent: 1 });
  add(mt, null, "Debt / equity", (i) => iferr(`${BSr("debt", i)}/${BSr("eq", i)}`), { fmt: MULTF, indent: 1 });
  add(mt, null, "Goodwill & intangibles / total assets", (i) => iferr(`(${BSr("gw", i)}+${BSr("intang", i)})/${BSr("ta", i)}`), { fmt: PCT, indent: 1 });
  gap(mt);
  head(mt, "Working capital");
  add(mt, "dso", "Receivable days (DSO)", (i) => iferr(`${BSr("ar", i)}/${ISr("rev", i)}*365`), { fmt: DAYS, indent: 1 });
  add(mt, "dio", "Inventory days (DIO)", (i) => iferr(`${BSr("inv", i)}/${ISr("cogs", i)}*365`), { fmt: DAYS, indent: 1 });
  add(mt, "dpo", "Payable days (DPO)", (i) => iferr(`${BSr("ap", i)}/${ISr("cogs", i)}*365`), { fmt: DAYS, indent: 1 });
  add(mt, null, "Cash conversion cycle (days)", (i) => iferr(`N(${col(i)}${mt._qk.dso})+N(${col(i)}${mt._qk.dio})-N(${col(i)}${mt._qk.dpo})`), { fmt: DAYS, indent: 1 });
  add(mt, null, "Deferred revenue / revenue", (i) => iferr(`(${BSr("dr_c", i)}+${BSr("dr_nc", i)})/${ISr("rev", i)}`), { fmt: PCT, indent: 1 });
  const px = mdl.px || {};
  if (Object.keys(px).length) {
    gap(mt);
    head(mt, "Valuation at fiscal year end (month-end price, split-adjusted)");
    add(mt, "price", "Share price", (i) => (px[Y[i].fy] != null ? px[Y[i].fy] : null), { fmt: EPS, indent: 1 });
    add(mt, "mcap", "Market cap (price × today's-basis shares)", (i) => (px[Y[i].fy] != null ? F(`${col(i)}${mt._qk.price}*${ISr("sh", i)}`) : null), { indent: 1 });
    add(mt, "ev", "Enterprise value", (i) => (px[Y[i].fy] != null ? F(`${col(i)}${mt._qk.mcap}+${BSr("netdebt", i)}+${BSr("mi", i)}`) : null), { indent: 1 });
    add(mt, null, "P/E", (i) => iferr(`IF(${ISr("ni", i)}>0,${col(i)}${mt._qk.mcap}/${ISr("ni", i)},"")`), { fmt: MULTF, indent: 1 });
    add(mt, null, "EV/EBIT", (i) => iferr(`IF(${ISr("ebit", i)}>0,${col(i)}${mt._qk.ev}/${ISr("ebit", i)},"")`), { fmt: MULTF, indent: 1 });
    add(mt, null, "EV/EBITDA", (i) => iferr(`IF(${ISr("ebitda", i)}>0,${col(i)}${mt._qk.ev}/${ISr("ebitda", i)},"")`), { fmt: MULTF, indent: 1 });
    add(mt, null, "EV/Sales", (i) => iferr(`${col(i)}${mt._qk.ev}/${ISr("rev", i)}`), { fmt: MULTF, indent: 1 });
    add(mt, null, "FCF yield", (i) => iferr(`${CFr("fcf", i)}/${col(i)}${mt._qk.mcap}`), { fmt: PCT, indent: 1 });
    if (cur !== "USD") add(mt, null, `Note: prices are in USD, statements in ${cur} - multiples need an FX adjustment.`, null, { italic: true });
  }
  wb.views = [{ activeTab: 1 }];
  return wb;
}

/* ------------------------------------------------------------------ couldn't screen */
function renderGaps() {
  const g = S.meta.gaps;
  const ex = S.meta.excluded.map(([why, n]) => `<li>${esc(why.replace("not screened: ", ""))}: ${n}</li>`).join("");
  $("#gaps").innerHTML = `<p class="list-note">${g.length} companies. ${S.meta.screened} of ${S.meta.universe} NYSE and Nasdaq companies were screened.</p>
    <div class="tbl-wrap"><table class="gaps-tbl"><thead><tr><th>Ticker</th><th>Company</th><th>Industry</th><th>Why it wasn't screened</th></tr></thead><tbody>
    ${g.map((x) => `<tr><td>${esc(x.t)}</td><td>${esc(x.n)}</td><td>${esc(x.ind)}</td><td>${esc(x.why)}</td></tr>`).join("")}
    </tbody></table></div>
    ${ex ? `<h4>Excluded industries</h4><ul class="notes">${ex}</ul>` : ""}`;
}

window.addEventListener("hashchange", () => { if (S.meta) route(); });
boot();
