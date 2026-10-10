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
  if (ticker) { $("#main").hidden = true; renderCompany(ticker); return; }   // a direct link: hide the 'Loading…' list
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
const usdShort = (v) => {
  if (v === null || v === undefined) return "–";
  const a = Math.abs(v), sg = v < 0 ? "−" : "";
  return sg + "$" + (a >= 1e9 ? (a / 1e9).toFixed(1) + "B" : a >= 1e6 ? (a / 1e6).toFixed(0) + "M" : (a / 1e3).toFixed(0) + "K");
};
const pctTxt = (v, d = 1) => (v === null || v === undefined ? "–" : (v * 100).toFixed(d) + "%");
const qLabel = (q) => (/^\d{4}q[1-4]$/i.test(q || "") ? `Q${q.slice(5)} ${q.slice(0, 4)}` : q || "");
const KIND = { new: "New position", add: "Added", cut: "Trimmed", exit: "Sold out" };
/* Ownership: top holders with conviction (share of each holder's own portfolio), buyers and sellers since the previous
   13F quarter, and insider open-market trades over the last 3 quarters. Information only, not a rule. */
function holdersCard(c) {
  const ho = c.ho, ins = c.ins;
  const hasHo = ho && ho.top && ho.top.length, hasIns = ins && (ins.buy || ins.sell || ins.plan_sell);
  if (!hasHo && !hasIns && !(ho && (ho.buy || ho.sell))) return "";
  const p = S.meta.holders_period, pp = S.meta.holders_prev_period;
  let html = `<section class="card own-card"><div class="pv-top"><h3>Ownership</h3>${p ? `<span class="chip">13F, ${esc(niceDate(p))}</span>` : ""}</div>`;
  if (hasHo) {
    const rows = ho.top.map(([n, pc, sp, port, val]) => `<tr><td>${esc(n)}${sp ? ' <span class="chip spec-chip">Healthcare specialist</span>' : ""}</td>
      <td>${pctTxt(pc)}</td><td>${port != null ? pctTxt(port) : "–"}</td><td>${usdShort(val)}</td></tr>`).join("");
    html += `<h4>Top holders</h4><div class="tbl-wrap"><table class="pv-tbl ho-tbl"><thead><tr><th>Holder</th><th>Share of the company</th>
      <th title="Position value / the holder's whole 13F portfolio: a high share means high conviction">Share of its portfolio</th><th>Value</th></tr></thead><tbody>${rows}</tbody></table></div>`;
    const spec = ho.sp && ho.sp.length && !ho.top.some((x) => x[2])
      ? ` Healthcare specialists also holding: ${ho.sp.map(esc).join(", ")}.` : "";
    html += `<p class="muted small">${ho.n} institutions report holding it. Index funds and broker platforms are left out.${spec}</p>`;
  }
  const moveTbl = (rows, title) => rows && rows.length ? `<div><h4>${title}</h4><div class="tbl-wrap"><table class="pv-tbl ho-tbl"><thead><tr><th>Holder</th><th title="Change in shares held">Change</th><th>Value</th><th title="Position value / the holder's whole 13F portfolio">Portfolio</th></tr></thead><tbody>${
    rows.map(([n, dv, k, port, dsh]) => `<tr><td>${esc(n)}</td><td>${esc(KIND[k] || k)}${dsh != null && k !== "new" && k !== "exit" ? ` (${dsh > 0 ? "+" : "−"}${Math.abs(dsh * 100).toFixed(0)}%)` : ""}</td><td>${usdShort(dv)}</td><td>${port != null ? pctTxt(port) : "–"}</td></tr>`).join("")
  }</tbody></table></div></div>` : "";
  if (ho && (ho.buy || ho.sell)) {
    html += `<div class="own-moves">${moveTbl(ho.buy, "Biggest buyers" + (pp ? ` since ${esc(niceDate(pp))}` : ""))}${moveTbl(ho.sell, "Biggest sellers" + (pp ? ` since ${esc(niceDate(pp))}` : ""))}</div>`;
  }
  const qs = S.meta.insider_quarters || [];
  if (hasIns) {
    const side = (k, label) => {
      const e = ins[k];
      if (!e) return `<tr><td>${label}</td><td>0</td><td>–</td><td>–</td><td class="small">none</td></tr>`;
      const top = e.top.map(([n, r, v, d]) => `${esc(n)}${r ? ` (${esc(r)})` : ""} ${usdShort(v)}${d ? `, last ${esc(niceDate(d))}` : ""}`).join("; ");
      return `<tr><td>${label}</td><td>${e.n}</td><td>${e.people}</td><td>${usdShort(e.value)}</td><td class="small">${top}</td></tr>`;
    };
    html += `<h4>Insider trades${qs.length ? `, ${esc(qLabel(qs[qs.length - 1]))} to ${esc(qLabel(qs[0]))}` : ""}</h4>
      <div class="tbl-wrap"><table class="pv-tbl ins-tbl"><thead><tr><th>Open-market trades</th><th>Trades</th><th>People</th><th>Value</th><th class="l">Largest</th></tr></thead><tbody>
      ${side("buy", "Buys")}${side("sell", "Sales")}${side("plan_sell", "Sales under a preset plan (10b5-1)")}</tbody></table></div>
      <p class="muted small">Officers, directors and 10% owners (SEC Forms 4/5). Option exercises, grants and gifts are left out; sales under a preset plan say little about conviction.</p>`;
  } else if (qs.length) {
    html += `<h4>Insider trades</h4><p class="muted small">No open-market insider buys or sales reported from ${esc(qLabel(qs[qs.length - 1]))} to ${esc(qLabel(qs[0]))}.</p>`;
  }
  return html + "</section>";
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
function loadScript(src) {
  return new Promise((res, rej) => {
    const s = document.createElement("script");
    s.src = src;
    s.onload = res;
    s.onerror = () => rej(new Error("couldn't load " + src));
    document.head.appendChild(s);
  });
}
function loadExcel() {
  if (excelLib) return excelLib;
  excelLib = Promise.all([loadScript("vendor/exceljs.min.js"), loadScript("model.js")])
    .then(() => window.ExcelJS)
    .catch((e) => { excelLib = null; throw e; });
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
