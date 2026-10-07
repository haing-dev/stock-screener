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

const S = { key: null, info: null, meta: null, comp: null, screens: {}, cur: null, view: "check", q: "", sort: null, open: new Set(), off: {} };

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
const LABEL = { PASS: "Passes", CHECK: "Check manually", ONE: "Missed 1 rule", FAIL: "Fails" };
/* the Red Flags screen is an avoid list: 'passing' every rule means 'flagged' */
const LABEL_AVOID = { PASS: "Flagged", CHECK: "Check manually", ONE: "Nearly flagged", FAIL: "Not flagged" };
const labelFor = (scr, s) => (scr && scr.avoid ? LABEL_AVOID : LABEL)[s];
/* Same classification as the screener: PASS, CHECK (nothing fails but data is missing or needs a look),
   ONE = a near miss on one rule, only valuation rules fail ('price too high'), or one non-defining rule fails with
   everything else verified; FAIL otherwise. With every rule on this reproduces the screener's own lists. */
function statusOf(row, scr, off) {
  const fails = [];
  let nd = 0, ndBiz = 0, ndHard = 0;
  scr.gates.forEach((g, i) => {
    if (off.has(g.id)) return;
    const c = row.g[i];
    if (c === "F") fails.push(g);
    else if (c === "D") { nd++; if (!g.price) ndBiz++; if (g.hard) ndHard++; }
  });
  const warns = row.w.filter((w) => !off.has(w)).length;
  if (!fails.length) return { s: nd || warns || row.h.length ? "CHECK" : "PASS", fails };
  if (scr.strict && ndHard) return { s: "FAIL", fails };
  if (fails.every((g) => g.valuation)) return { s: "ONE", fails, kind: "price" };
  if (fails.length === 1) {
    const g = fails[0];
    if (row.nr && row.nr === g.id) return { s: "ONE", fails, kind: "near" };
    if (!g.hard && ndBiz <= 1) return { s: "ONE", fails, kind: "one" };
  }
  return { s: "FAIL", fails };
}
const VIEWS = [
  { id: "pass", label: "Passing", avoid: "Flagged", set: ["PASS"] },
  { id: "check", label: "+ check manually", set: ["PASS", "CHECK"] },
  { id: "one", label: "+ near misses", set: ["PASS", "CHECK", "ONE"] },
];
const visibleSet = () => new Set(VIEWS.find((v) => v.id === S.view).set);

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
    const key = await deriveKey($("#pw").value, S.info);
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
  if (window.matchMedia("(max-width: 820px)").matches) $("#rulesBox").open = false;
  $("#lock").hidden = true;
  $("#app").hidden = false;
  $("#table").innerHTML = '<div class="empty">Loading…</div>';
  [S.meta, S.comp] = await Promise.all([fetchBin("meta"), fetchBin("companies")]);
  renderNav();
  renderFreshness();
  const want = (location.hash || "").slice(1) || store.get("qs-screen") || S.meta.screens[0].id;
  await go(S.meta.screens.some((s) => s.id === want) || want === "gaps" ? want : S.meta.screens[0].id);
}

/* ------------------------------------------------------------------ navigation */
function renderNav() {
  const nav = $("#screenNav");
  nav.innerHTML = S.meta.screens.map((s) =>
    (s.group ? `<div class="sep"></div><div class="nav-h">${esc(s.group)}</div>` : "") +
    `<button type="button" data-sid="${s.id}"><span>${esc(s.title)}</span><span class="n" data-count="${s.id}">${s.counts.PASS ?? 0}</span></button>`
  ).join("") + `<div class="sep"></div><button type="button" data-sid="gaps"><span>Couldn't screen</span><span class="n">${S.meta.gaps.length}</span></button>`;
  nav.querySelectorAll("button").forEach((b) => b.addEventListener("click", () => { go(b.dataset.sid); }));
}
function renderFreshness() {
  const m = S.meta;
  $("#freshness").innerHTML =
    `<span>Screened ${esc(niceDate(m.screened_on))}</span><span>Prices: close of ${esc(niceDate(m.price_day))}</span>` +
    `<span>${m.summaries} of ${m.companies} descriptions written</span>`;
}
async function go(sid) {
  S.cur = sid;
  store.set("qs-screen", sid);
  history.replaceState(null, "", "#" + sid);
  document.querySelectorAll("#screenNav button").forEach((b) =>
    b.setAttribute("aria-current", b.dataset.sid === sid ? "page" : "false"));
  if (sid === "gaps") { $("#main").hidden = true; $("#gapsView").hidden = false; renderGaps(); return; }
  $("#main").hidden = false; $("#gapsView").hidden = true;
  if (!S.screens[sid]) {
    $("#table").innerHTML = '<div class="empty">Loading…</div>';
    try {
      S.screens[sid] = await fetchBin("screen_" + sid);
    } catch (e) {
      $("#table").innerHTML = `<div class="empty">Couldn't load this screen's data (${esc(e.message)}). Reload the page to try again.</div>`;
      return;
    }
  }
  S.sort = null;
  S.open.clear();
  render();
}

/* ------------------------------------------------------------------ main view */
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
  const rules = [...scr.gates.map((g) => ({ id: g.id, name: g.name, rule: g.rule, why: g.why, hard: g.hard, price: g.price })),
    ...scr.warnings.map((w) => ({ id: w.id, name: w.name, rule: "warning: sends a pass to 'check manually'", why: "" }))];
  $("#rules").innerHTML = rules.map((r) => {
    const on = !off.has(r.id);
    let gain = 0;
    if (on) {
      const trial = new Set(off); trial.add(r.id);
      scr.rows.forEach((row, i) => { if (!vis.has(base[i]) && vis.has(statusOf(row, scr, trial).s)) gain++; });
    }
    const tip = [r.why, r.hard ? "A defining rule of this screen: failing it never counts as 'missed 1 rule'." : ""].filter(Boolean).join(" ");
    return `<button type="button" class="rule" aria-pressed="${on}" data-id="${esc(r.id)}" title="${esc(tip)}">
      <span class="sw" aria-hidden="true"></span>
      <span class="nm">${esc(r.name)}${r.price ? '<span class="tag">price</span>' : ""}</span>
      <span class="rl">${esc(r.rule)}</span>
      <span class="gain${gain ? " has" : ""}" aria-label="${on ? gain + " companies would join without this rule" : "rule is off"}">${on ? "+" + gain : "off"}</span>
    </button>`;
  }).join("");
  $("#rules").querySelectorAll(".rule").forEach((b) => b.addEventListener("click", () => {
    const id = b.dataset.id;
    if (off.has(id)) off.delete(id); else off.add(id);
    saveOff(S.cur);
    render();
  }));
  $("#resetRules").hidden = off.size === 0;
  $("#rulesOn").textContent = `(${rules.length - rules.filter((r) => off.has(r.id)).length} of ${rules.length} on)`;
}
$("#resetRules").addEventListener("click", () => { offFor(S.cur).clear(); saveOff(S.cur); render(); });

function renderViews(scr, off) {
  const n = { PASS: 0, CHECK: 0, ONE: 0 };
  scr.rows.forEach((r) => { const s = statusOf(r, scr, off).s; if (s in n) n[s]++; });
  const counts = { pass: n.PASS, check: n.PASS + n.CHECK, one: n.PASS + n.CHECK + n.ONE };
  $("#viewSwitch").innerHTML = VIEWS.map((v) =>
    `<button type="button" role="radio" aria-checked="${v.id === S.view}" data-v="${v.id}">${scr.avoid && v.avoid ? v.avoid : v.label} <span>(${counts[v.id]})</span></button>`).join("");
  $("#viewSwitch").querySelectorAll("button").forEach((b) => b.addEventListener("click", () => { S.view = b.dataset.v; render(); }));
  const navCount = document.querySelector(`[data-count="${S.cur}"]`);
  if (navCount) navCount.textContent = n.PASS;
}
$("#search").addEventListener("input", (e) => { S.q = e.target.value.trim().toLowerCase(); renderTable(S.screens[S.cur], offFor(S.cur)); });

const ORDER = { PASS: 0, CHECK: 1, ONE: 2, FAIL: 3 };
function renderTable(scr, off) {
  const vis = visibleSet();
  const M = S.comp.metrics;
  let rows = scr.rows.map((r) => ({ r, st: statusOf(r, scr, off), c: S.comp.companies[r.c] })).filter((x) => x.c);
  rows = S.q ? rows.filter((x) => (x.c.t + " " + x.c.n + " " + (x.c.other || "")).toLowerCase().includes(S.q))
             : rows.filter((x) => vis.has(x.st.s));
  if (S.sort) {
    const { k, dir } = S.sort;
    const val = (x) => (k === "_t" ? x.c.t : k === "_px" ? (x.c.px ? x.c.px.c : null) : x.c.m[k]);
    rows.sort((a, b) => {
      const va = val(a), vb = val(b);
      if (va === undefined || va === null) return 1;
      if (vb === undefined || vb === null) return -1;
      return (va > vb ? 1 : va < vb ? -1 : 0) * dir;
    });
  } else {
    rows.sort((a, b) => ORDER[a.st.s] - ORDER[b.st.s] || (b.c.m.market_cap_usd || 0) - (a.c.m.market_cap_usd || 0));
  }
  const mk = scr.metrics;
  $("#table").style.setProperty("--mcols", mk.length);
  const head = (k, label, cls = "") => {
    const sorted = S.sort && S.sort.k === k;
    const arrow = sorted ? (S.sort.dir > 0 ? " ↑" : " ↓") : "";
    return `<div class="${cls}" role="columnheader" aria-sort="${sorted ? (S.sort.dir > 0 ? "ascending" : "descending") : "none"}"><button type="button" data-k="${k}" class="${sorted ? "sorted" : ""}">${esc(label)}${arrow}</button></div>`;
  };
  let html = `<div class="tr th" role="row">${head("_t", "Company")}${head("_px", "Price")}<div role="columnheader">What it does</div>` +
    mk.map((k) => head(k, M[k][0], "mt")).join("") + "</div>";
  const shown = rows.slice(0, 400);
  html += shown.map((x) => rowHTML(x, scr, mk, off)).join("");
  $("#table").innerHTML = shown.length ? html : html + `<div class="empty">${S.q ? "No company matches that search in this screen." : scr.avoid ? "No company is flagged with these rules." : "No company qualifies with these rules. Switch a rule off, or widen the list above."}</div>`;
  $("#listNote").textContent = `${rows.length} shown of ${scr.rows.length} companies in this screen's industries` +
    (rows.length > shown.length ? ` (first ${shown.length}; search to find others)` : "") +
    ". Under each figure: the median of its industry peers – green where the company looks better, red where it looks worse.";
  $("#table").querySelectorAll(".th button").forEach((b) => b.addEventListener("click", () => {
    const k = b.dataset.k;
    const better = k.startsWith("_") ? null : M[k][2];
    S.sort = S.sort && S.sort.k === k ? { k, dir: -S.sort.dir } : { k, dir: better === "high" || k === "_px" ? -1 : 1 };
    renderTable(scr, off);
  }));
  $("#table").querySelectorAll(".row").forEach((el) => {
    const toggle = () => { const c = el.dataset.c; if (S.open.has(c)) S.open.delete(c); else S.open.add(c); renderTable(scr, off); };
    el.addEventListener("click", (e) => { if (!e.target.closest("a") && !e.target.closest(".detail")) toggle(); });
    el.addEventListener("keydown", (e) => { if (e.target === el && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); toggle(); } });
  });
}

function cmpPeer(k, v, med) {
  const dir = S.comp.metrics[k][2];
  if (!dir || med === undefined || v === undefined || v === null) return "";
  if (S.comp.metrics[k][3] && v <= 0) return "";
  const d = (v - med) / Math.abs(med || 1);
  if (Math.abs(d) < 0.1) return "";
  return (dir === "low" ? d < 0 : d > 0) ? "better" : "worse";
}

function rowHTML(x, scr, mk, off) {
  const c = x.c, r = x.r;
  const peers = c.pg ? S.comp.peers[c.pg] : null;
  const pill = x.st.s !== "ONE" ? labelFor(scr, x.st.s)
    : x.st.kind === "price" ? "Price too high" : x.st.kind === "near" ? `Just misses: ${x.st.fails[0].name}` : `Missed: ${x.st.fails[0].name}`;
  let px = '<div class="px">–</div>';
  if (c.px) {
    const ch = c.px.o ? (c.px.c / c.px.o - 1) * 100 : null;
    px = `<div class="px"><div class="cl">${money(c.px.c)}</div><div class="op">open ${money(c.px.o)}${ch !== null ? ` <span class="chg ${ch >= 0 ? "up" : "dn"}">${ch >= 0 ? "+" : ""}${ch.toFixed(1)}%</span>` : ""}</div></div>`;
  }
  const about = c.sum ? `<div class="about">${esc(c.sum)}</div>` : `<div class="about pending">${esc(c.ind || "")}. Description not written yet.</div>`;
  const cells = mk.map((k) => {
    const v = c.m[k];
    const u = c.mu.includes(k);
    const med = peers ? peers.med[k] : undefined;
    const cls = u ? "" : cmpPeer(k, v, med);
    const f = S.comp.metrics[k][1];
    return `<div class="mt" data-label="${esc(S.comp.metrics[k][0])}" role="cell"><div class="v${u ? " u" : ""}" ${u ? `title="Unverified: ${esc(c.vi)}"` : ""}>${u ? "≈" : ""}${fmt(v, f)}</div>` +
      (med !== undefined ? `<div class="pr ${cls}">peers ${fmt(med, f)}</div>` : "") + "</div>";
  }).join("");
  const open = S.open.has(r.c);
  return `<div class="tr row" role="row" tabindex="0" aria-expanded="${open}" data-c="${r.c}">
    <div class="co" role="cell"><div class="tk">${esc(c.t)}</div><div class="nm" title="${esc(c.n)}">${esc(c.n)}</div><span class="pill ${x.st.s === "ONE" && x.st.kind !== "one" ? "CHECK" : x.st.s}">${esc(pill)}</span></div>
    ${px.replace('<div class="px">', '<div class="px" role="cell">')}
    ${about.replace('<div class="about', '<div role="cell" class="about')}
    ${cells}
    ${open ? detailHTML(x, scr, off, peers) : ""}
  </div>`;
}

function detailHTML(x, scr, off, peers) {
  const c = x.c, r = x.r;
  const gl = scr.gates.map((g, i) => {
    const code = r.g[i];
    const isOff = off.has(g.id);
    const ic = { P: "✓", F: "✗", D: "?", N: "–" }[code] || "?";
    const val = r.v[i] ? `<span class="val">${esc(r.v[i])}</span>` : "<span></span>";
    const note = r.nt[g.id] ? `<span class="note">${esc(r.nt[g.id])}</span>` : "";
    return `<li class="${code}${isOff ? " off" : ""}"><span class="ic" aria-label="${{ P: "pass", F: "fail", D: "no data", N: "not applicable" }[code]}">${ic}</span>` +
      `<span>${esc(g.name)} <span class="src">(${esc(g.rule)})${isOff ? " – switched off" : ""}</span></span>${val}${note}</li>`;
  }).join("");
  const warn = Object.entries(r.wt || {}).map(([id, t]) => `<li>${off.has(id) ? "(switched off) " : ""}${esc(t)}</li>`).join("");
  const holds = r.h.map((h) => `<li>${esc(h)}</li>`).join("");
  const flags = (c.flags || []).map((f) => `<li>${esc(f)}</li>`).join("");
  let peerBlock = "<p class=\"src\">Not enough companies in this industry for a peer comparison.</p>";
  if (peers) {
    const rowsP = scr.metrics.filter((k) => c.m[k] !== undefined || peers.med[k] !== undefined).map((k) => {
      const f = S.comp.metrics[k][1];
      const v = c.m[k], med = peers.med[k];
      const cls = c.mu.includes(k) ? "" : cmpPeer(k, v, med);
      return `<tr><td>${esc(S.comp.metrics[k][0])}</td><td class="${cls}">${c.mu.includes(k) ? "≈" : ""}${fmt(v, f)}</td><td>${med !== undefined ? fmt(med, f) : "–"}</td></tr>`;
    }).join("");
    peerBlock = `<p class="src">${esc(peers.label)}: median of ${peers.n} companies. Largest: ${peers.top.map((p) => esc(p[0])).join(", ")}.</p>
      <table class="peer-tbl"><thead><tr><th>Metric</th><th>${esc(c.t)}</th><th>Peer median</th></tr></thead><tbody>${rowsP}</tbody></table>`;
  }
  const links = [c.url ? `<a href="${esc(c.url)}" target="_blank" rel="noopener">Latest annual report (SEC)</a>` : "",
    c.ev && c.ev.url ? `<a href="${esc(c.ev.url)}" target="_blank" rel="noopener">${esc(c.ev.types)} filing (${esc(c.ev.date)})</a>` : ""].filter(Boolean).join(" &nbsp; ");
  return `<div class="detail" role="cell"><div class="detail-grid">
    <div>
      <h4>About ${esc(c.n)}</h4>
      <p>${c.sum ? esc(c.sum) : "Description not written yet – it is added automatically over the next runs."}</p>
      <p class="src">${c.sum ? "Written by Claude from the " + esc(c.sumsrc || "annual report") + ". " : ""}${esc(c.ind || "")}${c.ex ? ", " + esc(c.ex) : ""}${c.other ? ". Other tickers: " + esc(c.other) : ""}</p>
      ${c.px ? `<p class="src">Price ${money(c.px.c)} at the close of ${esc(niceDate(c.px.d))} (${esc(c.px.src || "")}).${c.vi ? " Market cap: " + esc(c.vi) : ""}</p>` : ""}
      <p>${links}</p>
      <h4>Against peers</h4>${peerBlock}
    </div>
    <div>
      <h4>Rules</h4><ul class="gl">${gl}</ul>
      ${warn ? `<h4>Quality warnings</h4><ul class="notes">${warn}</ul>` : ""}
      ${holds ? `<h4>Check by hand</h4><ul class="notes">${holds}</ul>` : ""}
      ${flags ? `<h4>Things to look at</h4><ul class="notes">${flags}</ul>` : ""}
      ${scr.review ? `<h4>What the numbers can't tell you</h4><p class="src">${esc(scr.review)}</p>` : ""}
    </div>
  </div></div>`;
}

/* ------------------------------------------------------------------ couldn't screen */
function renderGaps() {
  const g = S.meta.gaps;
  const ex = S.meta.excluded.map(([why, n]) => `<li>${esc(why.replace("not screened: ", ""))}: ${n}</li>`).join("");
  $("#gaps").innerHTML = `<p class="list-note">${g.length} companies. ${S.meta.screened} companies were screened out of ${S.meta.universe} listed on NYSE and Nasdaq.</p>
    <table class="gaps-tbl"><thead><tr><th>Ticker</th><th>Company</th><th>Industry</th><th>Why it wasn't screened</th></tr></thead><tbody>
    ${g.map((x) => `<tr><td>${esc(x.t)}</td><td>${esc(x.n)}</td><td>${esc(x.ind)}</td><td>${esc(x.why)}</td></tr>`).join("")}
    </tbody></table>
    ${ex ? `<h4>Left out on purpose (excluded industries)</h4><ul class="notes">${ex}</ul>` : ""}`;
}

window.addEventListener("hashchange", () => {
  const h = location.hash.slice(1);
  if (S.meta && h && h !== S.cur && (h === "gaps" || S.meta.screens.some((s) => s.id === h))) go(h);
});
boot();
