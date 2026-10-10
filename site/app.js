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
/* SEC names arrive as 'COSTCO WHOLESALE CORP /NEW': drop the state suffix and soften all-caps names */
function niceName(n) {
  let s = String(n || "").replace(/\s*\/[A-Z]{2,4}\/?\s*$/, "").trim();
  if (s && s === s.toUpperCase() && /[A-Z]{3}/.test(s)) {
    const keep = new Set(["LLC", "LP", "PLC", "NV", "SA", "AG", "SE", "USA", "US", "II", "III", "REIT", "ETF"]);
    s = s.toLowerCase().replace(/\b([a-z])([a-z'&.]*)/g, (w, a, b) => (keep.has(w.toUpperCase()) ? w.toUpperCase() : a.toUpperCase() + b));
  }
  return s;
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

/* Near-miss reasons, one per rule, in one format: "Miss due to <what> being <value> (needs <rule>)" or "Miss due to
   insufficient information on <what>". */
function gateReason(g, code, row, i) {
  if (code === "D") return `Miss due to insufficient information on ${g.what || g.name.toLowerCase()}`;
  if (code !== "F") return "";
  if (g.ftxt) return `Miss due to ${g.ftxt}`;
  const v = row.v[i];
  if (v) return `Miss due to ${g.what || g.name.toLowerCase()} being ${v}${g.need ? ` (needs ${g.need})` : ""}`;
  return `Miss due to ${row.nt[g.id] || (g.what || g.name.toLowerCase()) + " failing the rule"}`;
}
const holdReason = (h) => `Miss due to insufficient information: ${h}`;
/* all the reasons a company isn't a clean pass (company page) */
function reasonOf(st, row, scr) {
  if (st.s === "PASS") return "";
  const out = [];
  scr.gates.forEach((g, i) => { if (!g.hidden && (row.g[i] === "F" || row.g[i] === "D")) out.push(gateReason(g, row.g[i], row, i)); });
  return out.concat(row.h.map(holdReason)).join("; ");
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
  $("#purpose").textContent = scr.thesis ? "" : scr.purpose;
  $("#purpose").hidden = !!scr.thesis;
  $("#thesis").innerHTML = thesisHTML(scr);
  $("#thesis").hidden = !scr.thesis;
  $("#thesis").classList.toggle("avoid", !!scr.avoid);
  document.title = scr.title + " – Stock Screener";
  renderRules(scr, off);
  renderViews(scr, off);
  renderTable(scr, off);
}

function thesisHTML(scr) {
  const t = scr.thesis;
  if (!t) return "";
  const ex = t.ex || {};
  const src = (ex.src || []).map(([l, u]) => `<a href="${esc(u)}" target="_blank" rel="noopener">${esc(l)}</a>`).join("");
  return `<div class="th-main">
      <p class="th-def">${esc(t.def)}</p>
      <h3 class="th-h">${scr.avoid ? "What marks one" : "What defines one"}</h3>
      <ul class="th-traits">${t.traits.map((x) => `<li>${esc(x)}</li>`).join("")}</ul>
      <p class="th-cause">${esc(t.cause)}</p>
    </div>
    <aside class="th-ex" aria-label="Example">
      <p class="th-k">${scr.avoid ? "A case to remember" : "A typical example"}</p>
      <p class="th-co">${esc(ex.co || "")}</p>
      <p class="th-stat">${esc(ex.stat || "")}<span>${esc(ex.stat_label || "")}</span></p>
      <p class="th-text">${esc(ex.text || "")}</p>
      ${src ? `<p class="th-src">${src}</p>` : ""}
    </aside>`;
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
function rowsFor(scr, off) {
  const vis = visibleSet();
  let rows = scr.rows.map((r) => ({ r, st: statusOf(r, scr, off), c: S.comp.companies[r.c] })).filter((x) => x.c);
  rows = S.q ? rows.filter((x) => (x.c.t + " " + x.c.n + " " + (x.c.other || "")).toLowerCase().includes(S.q))
             : rows.filter((x) => vis.has(x.st.s));
  return rows;
}
function sortRows(rows, val, fallback) {
  if (S.sort) {
    const { k, dir } = S.sort;
    rows.sort((a, b) => {
      const va = val(a, k), vb = val(b, k);
      if (va === undefined || va === null) return 1;
      if (vb === undefined || vb === null) return -1;
      return (va > vb ? 1 : va < vb ? -1 : 0) * dir;
    });
  } else rows.sort(fallback);
}
function th(k, label, cls = "", title = "") {
  const sorted = S.sort && S.sort.k === k;
  const arrow = sorted ? (S.sort.dir > 0 ? " ↑" : " ↓") : "";
  return `<th class="${cls}" aria-sort="${sorted ? (S.sort.dir > 0 ? "ascending" : "descending") : "none"}"${title ? ` title="${esc(title)}"` : ""}><button type="button" data-k="${esc(k)}" class="${sorted ? "sorted" : ""}">${esc(label)}${arrow}</button></th>`;
}
function bindTable(scr, off, better) {
  $("#table").querySelectorAll("thead button").forEach((b) => b.addEventListener("click", () => {
    const k = b.dataset.k;
    S.sort = S.sort && S.sort.k === k ? { k, dir: -S.sort.dir } : { k, dir: better(k) === "high" ? -1 : 1 };
    renderTable(scr, off);
  }));
  $("#table").querySelectorAll("tbody tr").forEach((el) => {
    el.addEventListener("click", (e) => { if (!e.target.closest("a, [data-tip]")) location.hash = `${S.cur}/${el.dataset.t}`; });
    el.addEventListener("keydown", (e) => { if (e.key === "Enter" && e.target === el) location.hash = `${S.cur}/${el.dataset.t}`; });
  });
}
const STATUS_LABEL = { PASS: "Pass", CHECK: "Near miss", ONE: "Near miss", FAIL: "Fails" };
function holdersNote() {
  const p = S.meta.holders_period;
  return p ? ` Top holders from 13F filings for ${niceDate(p)}; index funds and broker platforms left out.` : "";
}
function renderTable(scr, off) {
  if (S.view === "near" && !S.q) { renderNear(scr, off); return; }
  const M = S.comp.metrics;
  const rows = rowsFor(scr, off);
  const val = (x, k) => (k === "_t" ? x.c.t : k === "_px" ? (x.c.px && x.c.px.o ? x.c.px.c / x.c.px.o - 1 : null)
    : k === "_rg" ? rangePos(x.c.px) : k === "_ind" ? (x.c.ind || "") : x.c.m[k]);
  sortRows(rows, val, (a, b) => ORDER[a.st.s] - ORDER[b.st.s] || (b.c.m.market_cap_usd || 0) - (a.c.m.market_cap_usd || 0));
  const mk = scr.metrics;
  const head = `<thead><tr>${th("_t", "Company", "c-co")}${th("_px", "Price (vs open)", "c-px num")}${th("_rg", "52-week range", "c-rg")}${th("_ind", "Industry", "c-ind")}` +
    mk.map((k) => th(k, M[k][0], "num")).join("") + `<th class="c-ho">Top holders</th></tr></thead>`;
  const shown = rows.slice(0, 400);
  const body = shown.map((x) => rowHTML(x, scr, mk)).join("");
  const empty = S.q ? "No company matches that search in this screen." : scr.avoid ? "No company is flagged with these rules."
    : "No company passes with these rules. See Near misses, or switch a rule off.";
  $("#table").innerHTML = `<table class="list-tbl">${head}<tbody>${body}</tbody></table>` + (shown.length ? "" : `<div class="empty">${empty}</div>`);
  $("#listNote").textContent = `${rows.length} of ${scr.rows.length} companies` +
    (rows.length > shown.length ? ` (first ${shown.length}; search to find others)` : "") + ". Select a company for its page." + holdersNote();
  bindTable(scr, off, (k) => (k.startsWith("_") ? null : M[k][2]));
}

/* Near misses: one column per rule, a green dot where it passes and an amber dot (with the reason) where it misses.
   Most rules met first. */
function renderNear(scr, off) {
  const gates = scr.gates.map((g, i) => ({ g, i })).filter(({ g }) => !g.hidden && !off.has(g.id));
  const rows = rowsFor(scr, off);
  const anyHold = rows.some((x) => x.r.h.length);
  rows.forEach((x) => {
    let p = 0, m = 0;
    gates.forEach(({ i }) => { const c = x.r.g[i]; if (c === "P") p++; else if (c === "F" || c === "D") m++; });
    if (anyHold) { if (x.r.h.length) m++; else p++; }
    x.pass = p; x.miss = m;
  });
  const val = (x, k) => (k === "_t" ? x.c.t : k === "_px" ? (x.c.px && x.c.px.o ? x.c.px.c / x.c.px.o - 1 : null)
    : k === "_rg" ? rangePos(x.c.px) : null);
  sortRows(rows, val, (a, b) => b.pass - a.pass || a.miss - b.miss || (b.c.m.market_cap_usd || 0) - (a.c.m.market_cap_usd || 0));
  const dot = (cls, label, tip) => `<span class="dot ${cls}"${tip ? ` tabindex="0" data-tip="${esc(tip)}"` : ""} role="img" aria-label="${esc(label)}"></span>`;
  const head = `<thead><tr>${th("_t", "Company", "c-co")}${th("_px", "Price (vs open)", "c-px num")}${th("_rg", "52-week range", "c-rg")}` +
    gates.map(({ g }) => `<th class="c-dot" title="${esc(g.name + ": " + g.rule)}"><span>${esc(g.name)}</span></th>`).join("") +
    (anyHold ? `<th class="c-dot" title="Data the screen couldn't confirm"><span>Data check</span></th>` : "") +
    `<th class="c-ho">Top holders</th></tr></thead>`;
  const shown = rows.slice(0, 400);
  const body = shown.map((x) => {
    const dots = gates.map(({ g, i }) => {
      const c = x.r.g[i];
      let d;
      if (c === "P") d = dot("ok", `${g.name}: meets the rule`);
      else if (c === "F" || c === "D") { const why = gateReason(g, c, x.r, i); d = dot("miss", `${g.name}: ${why}`, why); }
      else d = dot("na", `${g.name}: doesn't apply`);
      return `<td class="c-dot" data-label="${esc(g.name)}">${d}</td>`;
    }).join("");
    const hold = !anyHold ? "" : `<td class="c-dot" data-label="Data check">${x.r.h.length
      ? dot("miss", "Data check", x.r.h.map(holdReason).join("; ")) : dot("ok", "Data check: confirmed")}</td>`;
    return `<tr tabindex="0" data-t="${esc(x.c.t)}">
      <td class="c-co"><span class="tk">${esc(x.c.t)}</span> <span class="nm" title="${esc(niceName(x.c.n))}">${esc(niceName(x.c.n))}</span><span class="tally">${x.pass} of ${x.pass + x.miss} rules met</span></td>
      <td class="c-px num" data-label="Price (vs open)">${pxHTML(x.c.px)}</td>
      <td class="c-rg" data-label="52-week range">${rangeHTML(x.c.px)}</td>
      ${dots}${hold}
      <td class="c-ho" data-label="Top holders">${holdersCell(x.c.ho)}</td>
    </tr>`;
  }).join("");
  $("#table").innerHTML = `<table class="list-tbl near-tbl">${head}<tbody>${body}</tbody></table>` +
    (shown.length ? "" : `<div class="empty">No near misses with these rules.</div>`);
  $("#listNote").innerHTML = `${rows.length} ${scr.avoid ? "nearly flagged" : rows.length === 1 ? "near miss" : "near misses"}, most rules met first. <span class="legend"><span class="dot ok"></span> meets the rule ` +
    `<span class="dot miss"></span> misses it (point at it for the reason) <span class="dot na"></span> doesn't apply</span>` + esc(holdersNote());
  bindTable(scr, off, () => null);
}

/* one floating tooltip for the amber dots (works inside the scrolling table, with mouse and keyboard) */
(function tooltips() {
  const tip = document.createElement("div");
  tip.id = "tip"; tip.setAttribute("role", "tooltip"); tip.hidden = true;
  document.body.appendChild(tip);
  const show = (el) => {
    tip.textContent = el.dataset.tip; tip.hidden = false;
    const r = el.getBoundingClientRect(), w = Math.min(320, window.innerWidth - 24);
    tip.style.maxWidth = w + "px";
    const tw = tip.offsetWidth, thh = tip.offsetHeight;
    let left = Math.max(12, Math.min(window.innerWidth - tw - 12, r.left + r.width / 2 - tw / 2));
    let top = r.top - thh - 8;
    if (top < 8) top = r.bottom + 8;
    tip.style.left = left + "px"; tip.style.top = top + "px";
  };
  const hide = () => { tip.hidden = true; };
  document.addEventListener("mouseover", (e) => { const el = e.target.closest("[data-tip]"); if (el) show(el); else hide(); });
  document.addEventListener("focusin", (e) => { const el = e.target.closest("[data-tip]"); if (el) show(el); else hide(); });
  document.addEventListener("scroll", hide, true);
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") hide(); });
})();

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
function holdersCell(ho) {
  if (!ho || !ho.top || !ho.top.length) return '<span class="muted">–</span>';
  const full = ho.top.map(([n, p, sp]) => `${n}${p != null ? ` (${(p * 100).toFixed(1)}%)` : ""}${sp ? " – healthcare specialist" : ""}`).join("\n");
  return `<span class="ho" title="${esc(full)}">${ho.top.map(([n, , sp]) => `<span>${esc(n)}${sp ? '<b class="spec" aria-label="healthcare specialist">★</b>' : ""}</span>`).join("")}</span>`;
}
function rowHTML(x, scr, mk) {
  const c = x.c;
  const reason = S.q && x.st.s !== "PASS" ? STATUS_LABEL[x.st.s] : "";
  const cells = mk.map((k) => {
    const u = c.mu.includes(k);
    const nmk = (c.nm || {})[k];
    if (nmk) return `<td class="num" data-label="${esc(S.comp.metrics[k][0])}"><span class="u" title="${esc(nmk)}">n/m</span></td>`;
    return `<td class="num" data-label="${esc(S.comp.metrics[k][0])}"><span class="${u ? "u" : ""}" ${u ? `title="Unverified: ${esc(c.vi)}"` : ""}>${u ? "≈" : ""}${fmt(c.m[k], S.comp.metrics[k][1])}</span></td>`;
  }).join("");
  const pill = x.st.s === "FAIL" ? "fail" : "miss";
  return `<tr tabindex="0" data-t="${esc(c.t)}">
    <td class="c-co"><span class="tk">${esc(c.t)}</span> <span class="nm" title="${esc(niceName(c.n))}">${esc(niceName(c.n))}</span>${reason ? ` <span class="badge ${pill}">${esc(reason)}</span>` : ""}</td>
    <td class="c-px num" data-label="Price (vs open)">${pxHTML(c.px)}</td>
    <td class="c-rg" data-label="52-week range">${rangeHTML(c.px)}</td>
    <td class="c-ind" data-label="Industry"><span title="${esc(c.ind)}">${esc(c.ind || "–")}</span></td>
    ${cells}
    <td class="c-ho" data-label="Top holders">${holdersCell(c.ho)}</td>
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
  const nm = c.nm || {};
  const facts = keys.filter((k) => c.m[k] !== undefined || nm[k]).map((k) =>
    `<div class="fact"${nm[k] ? ` title="${esc(nm[k])}"` : ""}><span>${esc(M[k][0])}</span><b>${nm[k] ? "n/m" : (c.mu.includes(k) ? "≈" : "") + fmt(c.m[k], M[k][1])}</b></div>`).join("");
  $("#companyView").hidden = false;
  $("#companyView").innerHTML = `
    <a class="back" href="#${esc(S.cur)}">← ${esc(scr.title)}</a>
    <header class="co-head">
      <div>
        <h2>${esc(c.t)} <span class="co-name">${esc(niceName(c.n))}</span></h2>
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
    ${holdersCard(c)}
    <section class="card">
      <h3>Financial statements</h3>
      ${c.mdl ? `<p class="muted">Income statement, balance sheet, cash flow and a metrics page for up to 10 years, from SEC filings, as an Excel file. Lines and ratios follow the company's industry, and the cover sheet confirms the three statements tie.</p>
        <button type="button" id="genXlsx" class="btn">Generate financial statements</button> <span id="genMsg" class="muted"></span>`
      : '<p class="muted">No statement data stored for this company.</p>'}
    </section>`;
  window.scrollTo(0, 0);
  bindPv(c);
  const gb = $("#genXlsx");
  if (gb) gb.addEventListener("click", () => generateModel(cid, gb));
}

const OPS = [["revenue_cagr_3y", "Revenue growth (3y)", "pct"], ["gross_margin_latest", "Gross margin", "pct"],
  ["ttm_operating_margin", "Operating margin", "pct"], ["roic_median", "ROIC (10y median)", "pct"],
  ["fcf_conversion", "Cash conversion", "x"], ["net_debt_to_ebitda", "Net debt / EBITDA", "x"]];
const mean = (a) => (a.length ? a.reduce((s, v) => s + v, 0) / a.length : null);
const median = (a) => {
  if (!a.length) return null;
  const b = [...a].sort((x, y) => x - y), k = Math.floor(b.length / 2);
  return b.length % 2 ? b[k] : (b[k - 1] + b[k]) / 2;
};
function pvHTML(c) {
  const pv = c.pv;
  if (!pv) return `<h3>Valuation against peers</h3><p class="muted">Prepared for companies on a Pass or Near-miss list.</p>`;
  const tabsList = [...pv.mult, "ops"];
  const k = tabsList.includes(S.pvMult) ? S.pvMult : pv.mult[0];
  const tabs = `<div class="seg small" role="tablist">${tabsList.map((m) =>
    `<button type="button" role="tab" aria-selected="${m === k}" data-m="${m}">${m === "ops" ? "Operating metrics" : MULT[m][0]}</button>`).join("")}</div>`;
  const peers = pv.rows.filter((r) => !r.me);
  const nums = (fn) => peers.map(fn).filter((v) => typeof v === "number" && Number.isFinite(v));
  let head, body, foot;
  if (k === "ops") {
    const ops = OPS.filter(([key]) => pv.rows.some((r) => r.op && r.op[key] != null));
    head = `<th>Company</th><th>Revenue</th>${ops.map(([, l]) => `<th>${esc(l)}</th>`).join("")}`;
    body = pv.rows.map((r) => `<tr class="${r.me ? "me" : ""}"><td>${esc(r.t)}<span class="pn">${esc(niceName(r.n))}</span></td><td>${fmt(r.rev, "usd")}</td>` +
      ops.map(([key, , f]) => `<td>${fmt((r.op || {})[key], f)}</td>`).join("") + "</tr>").join("");
    const stat = (fn, lab) => `<tr class="agg"><td>${lab}</td><td>${fmt(fn(nums((r) => r.rev)), "usd")}</td>` +
      ops.map(([key, , f]) => `<td>${fmt(fn(nums((r) => (r.op || {})[key])), f)}</td>`).join("") + "</tr>";
    foot = stat(mean, "Peer mean") + stat(median, "Peer median");
  } else {
    const f = MULT[k][1];
    head = `<th>Company</th><th>Revenue</th><th>Now</th><th>3-yr avg</th><th>10-yr avg</th>`;
    body = pv.rows.map((r) => {
      const v = r.v[k] || [];
      const avg10 = v[2] != null ? fmt(v[2], f) + (v[3] && v[3] < 10 ? `<sup>${v[3]}y</sup>` : "") : "–";
      return `<tr class="${r.me ? "me" : ""}"><td>${esc(r.t)}<span class="pn">${esc(niceName(r.n))}</span></td><td>${fmt(r.rev, "usd")}</td>` +
        `<td>${fmt(v[0], f)}</td><td>${fmt(v[1], f)}</td><td>${avg10}</td></tr>`;
    }).join("");
    const stat = (fn, lab) => `<tr class="agg"><td>${lab}</td><td>${fmt(fn(nums((r) => r.rev)), "usd")}</td>` +
      [0, 1, 2].map((j) => `<td>${fmt(fn(nums((r) => (r.v[k] || [])[j])), f)}</td>`).join("") + "</tr>";
    foot = stat(mean, "Peer mean") + stat(median, "Peer median");
  }
  const vd = k !== "ops" ? (pv.verdict[k] || {}).v : null;
  return `<div class="pv-top"><h3>Valuation against peers</h3>${pv.overall ? `<span class="chip v-${pv.overall.replace(" ", "-")}">${VERDICT[pv.overall]} overall</span>` : ""}
      ${vd ? `<span class="chip v-${vd.replace(" ", "-")}">${esc(MULT[k][0])}: ${VERDICT[vd]}</span>` : ""}</div>
    ${tabs}
    <div class="tbl-wrap"><table class="pv-tbl"><thead><tr>${head}</tr></thead><tbody>${body}</tbody>${peers.length ? `<tfoot>${foot}</tfoot>` : ""}</table></div>`;
}
function holdersCard(c) {
  const ho = c.ho;
  if (!ho || !ho.top || !ho.top.length) return "";
  const p = S.meta.holders_period;
  const rows = ho.top.map(([n, pc, sp]) => `<tr><td>${esc(n)}${sp ? ' <span class="chip spec-chip">Healthcare specialist</span>' : ""}</td><td>${pc != null ? (pc * 100).toFixed(1) + "%" : "–"}</td></tr>`).join("");
  const spec = ho.sp && ho.sp.length && !ho.top.some((x) => x[2])
    ? `<p class="muted small">Healthcare specialists also holding: ${ho.sp.map(esc).join(", ")}.</p>` : "";
  return `<section class="card"><div class="pv-top"><h3>Top institutional holders</h3>${p ? `<span class="chip">13F, ${esc(niceDate(p))}</span>` : ""}</div>
    <div class="tbl-wrap"><table class="pv-tbl ho-tbl"><thead><tr><th>Holder</th><th>Share of the company</th></tr></thead><tbody>${rows}</tbody></table></div>
    <p class="muted small">${ho.n} institutions report holding it. Index funds and broker platforms are left out.</p>${spec}</section>`;
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
