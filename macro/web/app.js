/* Macro Compass - static front end. Reads /data/data.bin (gzip'd JSON; public build, or AES-GCM when a password is set),
   built by macro/engine.py + macro/site.py, served by its own Cloudflare Worker "macro-compass".
   Flow: indicators -> three dials -> state -> investors' playbook -> history check -> calls -> track record. */
"use strict";
const $ = s => document.querySelector(s);
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const store = {get(k){ try { return localStorage.getItem(k); } catch(e){ return null; } },
  set(k,v){ try { localStorage.setItem(k, v); } catch(e){} }, del(k){ try { localStorage.removeItem(k); } catch(e){} }};
let D = null, H = store.get("mc-h") || "12", KEY = null, INFO = null, N = 0;
const OPEN = new Set();
const STATES = ["expansion", "late", "overheating", "contraction", "stagflation", "recovery"];
const MON = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
const mlab = m => { const [y, mo] = m.split("-"); return `${MON[+mo - 1]} ${y}`; };
const pct = (v, d = 0) => v == null ? "–" : `${v > 0 ? "+" : v < 0 ? "−" : ""}${Math.abs(v).toFixed(d)}%`;
const lastOf = a => { for (let i = a.length - 1; i >= 0; i--) if (a[i] != null) return [a[i], i]; return [null, -1]; };
const word = s => s == null ? "–" : s >= 65 ? "High" : s <= 35 ? "Low" : "Normal";

/* ------------------------------------------------------------------ crypto (same scheme as the triage site) */
const b64 = s => Uint8Array.from(atob(s), c => c.charCodeAt(0));
const toB64 = buf => btoa(String.fromCharCode(...new Uint8Array(buf)));
async function gunzipJSON(buf){ const s = new Blob([buf]).stream().pipeThrough(new DecompressionStream("gzip")); return JSON.parse(await new Response(s).text()); }
async function deriveKey(pw){ const k = await crypto.subtle.importKey("raw", new TextEncoder().encode(pw), "PBKDF2", false, ["deriveKey"]);
  return crypto.subtle.deriveKey({name:"PBKDF2", salt:b64(INFO.salt), iterations:INFO.iter, hash:"SHA-256"}, k, {name:"AES-GCM", length:256}, true, ["decrypt"]); }
async function openBlob(buf){ if (INFO.plain) return gunzipJSON(buf); const u = new Uint8Array(buf);
  return gunzipJSON(await crypto.subtle.decrypt({name:"AES-GCM", iv:u.slice(0, 12)}, KEY, u.slice(12))); }
async function tryKey(k){ KEY = k; try { const c = await openBlob(b64(INFO.check).buffer); return !!(c && c.ok); } catch(e){ return false; } }

/* ------------------------------------------------------------------ tooltip */
const tip = $("#tip");
function showTip(e, html){ tip.innerHTML = html; tip.style.opacity = 1;
  const x = Math.min(e.clientX + 14, innerWidth - tip.offsetWidth - 8), y = e.clientY - tip.offsetHeight - 12;
  tip.style.left = Math.max(8, x) + "px"; tip.style.top = (y < 8 ? e.clientY + 18 : y) + "px"; }
function hideTip(){ tip.style.opacity = 0; }

/* ------------------------------------------------------------------ small charts */
function spark(vals, w = 160, h = 28){
  const pts = vals.map((v, i) => v == null ? null : [i / (vals.length - 1) * w, h - 2 - (v / 100) * (h - 4)]);
  let d = "", pen = false;
  pts.forEach(p => { if (!p) { pen = false; return; } d += (pen ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1); pen = true; });
  const last = pts.filter(Boolean).pop();
  return `<svg viewBox="0 0 ${w} ${h}" width="100%" height="${h}" preserveAspectRatio="none" aria-hidden="true">
    <line x1="0" x2="${w}" y1="${h / 2}" y2="${h / 2}" stroke="var(--axis)" stroke-dasharray="2 3"/>
    <path d="${d}" fill="none" stroke="var(--ink3)" stroke-width="1.4" vector-effect="non-scaling-stroke"/>
    ${last ? `<circle cx="${last[0]}" cy="${last[1]}" r="2.6" fill="var(--ink)"/>` : ""}</svg>`;
}
function gauge(s){
  if (s == null) return `<div class="gauge"><div class="mid"></div></div>`;
  const a = Math.min(s, 50), b = Math.max(s, 50);
  return `<div class="gauge" title="${Math.round(s)} out of 100"><div class="fill" style="left:${a}%;width:${b - a}%"></div><div class="mid"></div><div class="mk" style="left:${s}%"></div></div>`;
}
const W = el => Math.max(280, el.clientWidth || 600);

function lineChart(el, series, months, opt = {}){
  const w = W(el), h = opt.h || 260, m = {l: 44, r: 64, t: 10, b: 24};
  const i0 = Math.max(opt.i0 || 0, Math.min(...series.map(s => s.v.findIndex(v => v != null)).filter(x => x >= 0)));
  const n = months.length, span = n - 1 - i0;
  const vals = series.flatMap(s => s.v.slice(i0).filter(v => v != null));
  let lo = opt.log ? Math.min(...vals) : Math.min(...vals, opt.base ?? Infinity), hi = Math.max(...vals);
  if (!opt.log && !opt.ticks) { const T0 = niceTicks(lo, hi, 4); lo = T0.lo; hi = T0.hi; }
  const tr = v => opt.log ? Math.log(v) : v;
  const Y = v => m.t + (h - m.t - m.b) * (1 - (tr(v) - tr(lo)) / (tr(hi) - tr(lo) || 1));
  const X = i => m.l + (w - m.l - m.r) * (i - i0) / (span || 1);
  let g = "";
  if (opt.rec) { let any = false; D.recession.forEach((r, i) => { if (r === 1 && i >= i0) { any = true; g += `<rect x="${X(i).toFixed(1)}" y="${m.t}" width="${Math.max(1, X(i + 1) - X(i)).toFixed(2)}" height="${h - m.t - m.b}" fill="var(--rec)"/>`; } }); if (any) g += recKey(w - m.r, 0); }
  if (opt.hband) opt.hband.forEach(b => { const y1 = Y(Math.min(hi, b.hi)), y0 = Y(Math.max(lo, b.lo)); g += `<rect x="${m.l}" y="${y1}" width="${w - m.l - m.r}" height="${Math.max(0, y0 - y1)}" fill="${b.c}" opacity="${b.o ?? 1}"/>` + (b.t && w >= 640 ? `<text class="zl" x="${m.l + 6}" y="${y0 - 5}">${b.t}</text>` : ""); });
  const ticks = opt.ticks || (opt.log ? [] : niceTicks(lo, hi, 4).t);
  ticks.filter(t => t >= lo && t <= hi).forEach(t => { g += `<line x1="${m.l}" x2="${w - m.r}" y1="${Y(t)}" y2="${Y(t)}" stroke="${t === 0 && opt.zero ? "var(--axis)" : "var(--grid)"}"/><text x="${m.l - 6}" y="${Y(t) + 3.5}" text-anchor="end">${opt.fmtTick ? opt.fmtTick(t) : t}</text>`; });
  if (opt.bands) opt.bands.forEach(b => { if (b.i1 >= i0) g += `<rect x="${X(Math.max(b.i0, i0))}" y="${m.t}" width="${Math.max(1.5, X(b.i1 + 1 > n - 1 ? n - 1 : b.i1 + 1) - X(Math.max(b.i0, i0)))}" height="${h - m.t - m.b}" fill="${b.c}"/>`; });
  const yrs = span / 12, step = yrs > 30 ? 10 : yrs > 14 ? 5 : yrs > 6 ? 2 : 1;
  let lastX = -1e9;
  for (let i = i0; i < n; i++) if (months[i].endsWith("-01") && +months[i].slice(0, 4) % step === 0 && X(i) - lastX > 40) { g += `<text x="${X(i)}" y="${h - 6}" text-anchor="middle">${months[i].slice(0, 4)}</text>`; lastX = X(i); }
  const ends = [];
  series.forEach(s => {
    let d = "", pen = false;
    for (let i = i0; i < n; i++) { const v = s.v[i]; if (v == null) { pen = false; continue; } d += (pen ? "L" : "M") + X(i).toFixed(1) + " " + Y(v).toFixed(1); pen = true; }
    g += `<path d="${d}" fill="none" stroke="${s.c}" stroke-width="${s.wd || 2}" stroke-linejoin="round" stroke-linecap="round"/>`;
    const [lv, li] = lastOf(s.v); if (lv != null) ends.push({y: Y(lv), x: X(li), t: s.endLabel ? s.endLabel(lv) : "", c: s.c});
  });
  ends.sort((a, b) => a.y - b.y).forEach((e, k, arr) => { if (k && e.y - arr[k - 1].y < 13) e.y = arr[k - 1].y + 13; });
  ends.forEach(e => { g += `<circle cx="${e.x}" cy="${e.y}" r="3.5" fill="${e.c}" stroke="var(--card)" stroke-width="2"/>${e.t ? `<text class="lab" x="${e.x + 8}" y="${e.y + 4}">${e.t}</text>` : ""}`; });
  g += `<line class="cx" x1="0" x2="0" y1="${m.t}" y2="${h - m.b}" stroke="var(--axis)" visibility="hidden"/><rect class="hit" x="${m.l}" y="0" width="${w - m.l - m.r}" height="${h}" fill="transparent"/>`;
  el.innerHTML = `<svg viewBox="0 0 ${w} ${h}" height="${h}" role="img" aria-label="${esc(opt.aria || "chart")}">${g}</svg>`;
  const hit = el.querySelector(".hit"), cx = el.querySelector(".cx");
  hit.addEventListener("pointermove", e => {
    const r = el.querySelector("svg").getBoundingClientRect(), px = (e.clientX - r.left) * w / r.width;
    const i = Math.max(i0, Math.min(n - 1, Math.round(i0 + (px - m.l) / (w - m.l - m.r) * span)));
    cx.setAttribute("x1", X(i)); cx.setAttribute("x2", X(i)); cx.setAttribute("visibility", "visible");
    showTip(e, `<div class="d">${mlab(months[i])}${opt.tipExtra ? opt.tipExtra(i) : ""}</div>` + series.map(s => `<div><span style="color:${s.c}">●</span> ${esc(s.name)}: <b>${s.v[i] == null ? "–" : (opt.fmt ? opt.fmt(s.v[i]) : s.v[i])}</b></div>`).join(""));
  });
  hit.addEventListener("pointerleave", () => { hideTip(); cx.setAttribute("visibility", "hidden"); });
}



/* ------------------------------------------------------------------ helpers on the data */
const IND = () => Object.fromEntries(D.meta.indicators.map(i => [i.id, i]));
const stName = s => s && D.meta.stages[s] ? D.meta.stages[s][0] : "Not enough data";
const NAME = () => Object.fromEntries(D.industries.map(i => [i.etf, i.name]));
const NOW = () => N - 1;
const recKey = (xr, y) => `<g class="reckey"><rect x="${xr - 86}" y="${y}" width="8" height="8" fill="var(--rec)"/><text x="${xr - 74}" y="${y + 8}">US recession</text></g>`;
const zoneAt = (id, i) => { const s = D.scores[id][i]; return s == null ? "" : s >= 65 ? "warn" : s <= 35 ? "good" : "normal"; };
const ZW = {warn: "Warning", good: "Supportive", normal: "Normal", "": "No data"};
const GROUPS = {
  A: {pillars: ["growth", "internals"], num: 1, step: "1 · The economy"},
  B: {pillars: ["inflation"], num: 2, step: "2 · Inflation"},
  C: {pillars: ["stress"], num: 3, step: "3 · Market stress"},
  D: {pillars: ["liquidity", "froth"], num: 4, step: "4 · Money, rates and valuations"},
};
const groupInds = g => D.meta.indicators.filter(i => GROUPS[g].pillars.includes(i.pillar));
function count(g, i){ const z = groupInds(g).map(x => zoneAt(x.id, i));
  return {warn: z.filter(x => x === "warn").length, normal: z.filter(x => x === "normal").length, good: z.filter(x => x === "good").length, n: z.filter(Boolean).length}; }
function avgWarn(g, end){ let t = 0, k = 0; for (let i = end - 5; i <= end; i++) if (i >= 0) { t += count(g, i).warn; k++; } return k ? t / k : 0; }
const sup = n => `<sup class="fn">(${n})</sup>`;
function fmtV(v, ind, sign){
  if (v == null) return "–";
  const x = v * ind.scale, s = sign && x > 0 ? "+" : x < 0 ? "−" : "", a = Math.abs(x).toFixed(ind.dp);
  return ind.unit === "%" ? `${s}${a}%` : ind.unit === "pts" ? `${s}${a} pts` : ind.unit === "$bn" ? `${s}$${Number(a).toLocaleString("en-US")}bn`
    : ind.unit === "x" ? `${a}x` : ind.unit === "% of GDP" ? `${a}%` : `${s}${a}`;
}
const hasNeg = id => D.values[id].some(v => v != null && v < 0);
function niceTicks(lo, hi, n = 4){
  const span = hi - lo || Math.abs(hi) || 1; let step = 10 ** Math.floor(Math.log10(span / n)); const e = span / n / step;
  step *= e >= 7.5 ? 10 : e >= 3.5 ? 5 : e >= 1.5 ? 2 : 1;
  const a = Math.floor(lo / step) * step, b = Math.ceil(hi / step) * step, t = [];
  for (let x = a; x <= b + step / 2; x += step) t.push(Math.abs(x) < step / 1e6 ? 0 : x);
  return {t, step, lo: a, hi: b, dp: Math.max(0, -Math.floor(Math.log10(step) + 1e-9))};
}
function tickLab(t, ind, dp){
  const a = Math.abs(t).toLocaleString("en-US", {minimumFractionDigits: dp, maximumFractionDigits: dp}), s = t < 0 ? "−" : "";
  return ind.unit === "%" || ind.unit === "% of GDP" ? `${s}${a}%` : ind.unit === "$bn" ? `${s}$${a}bn` : ind.unit === "x" ? `${a}x` : `${s}${a}`;
}

/* ------------------------------------------------------------------ the analysis: the checks behind the recommendation */
function checks(){
  const X = D.derisk, i = NOW(), sh = X.share[i], fed = X.fed_gate[i], gc = X.growth_cut[i], al = X.alloc;
  const S = X.series, gap = D.values.spx_trend[i], un = S.unemp[i], ua = S.unemp_avg[i], corr = D.values.stockbond[i];
  const band = D.settings.derisk.band.map(x => x * 100);
  return [
    {id: "s1", t: "Warning signals", b: sh >= band[0] ? `${Math.round(sh)}% of the weighted warning signals are on` : `Only ${Math.round(sh)}% of the weighted warning signals are on`, bar: true},
    {id: "s2", t: "The Fed", b: fed ? "The Fed is tightening, so warnings cut stocks" : "The Fed is not tightening, so warnings do not cut stocks"},
    {id: "s3", t: "Growth and trend", b: gc ? "The S&P 500 is below its trend and unemployment is rising: stocks are cut"
      : `The S&P 500 is ${gap >= 0 ? "above" : "below"} its trend and unemployment is ${un > ua ? "rising" : "not rising"}`},
    {id: "s4", t: "Bonds as a hedge", b: corr < 0 ? "Stocks and bonds move in opposite directions: a growth cut would go to Treasuries" : "Stocks and bonds move together: a cut would go to cash"},
    {id: "s5", t: "Commodities", b: X.commod_on[i] ? `Commodities are trending up: ${al.commodities[i]}% held` : "Commodities are not trending up: none held"},
    {id: "s6", t: "Sector leadership", b: X.fully_invested[i] ? "Fully invested: overweight the five strongest sectors, underweight the five weakest" : "Stocks are reduced: sector tilts are on hold"},
  ];
}
function renderTop(){
  const i = NOW(), al = D.derisk.alloc, eq = al.equity[i];
  const parts = PARTS.filter(([k]) => k !== "equity" && al[k] && al[k][i] > 0).map(([k, l]) => `${al[k][i]}% ${l.toLowerCase()}`);
  $("#stageDot").style.background = eq >= 90 ? "var(--good)" : eq >= 50 ? "var(--st-late)" : "var(--bad)";
  $("#stageName").textContent = `${eq}% equity${parts.length ? ", " + parts.join(", ") : ""}`;
  $("#stageWhy").textContent = `Six checks set the portfolio each month. Reading as of ${mlab(D.months[i])}.`;
  $("#points").innerHTML = checks().map((c, k) => `<li><a href="#${c.id}"><span class="pn">${k + 1} · ${esc(c.t)}</span><b>${esc(c.b)}</b>${c.bar ? coreBar() : ""}</a></li>`).join("");
}
function coreBar(){
  const ids = D.derisk.core, z = ids.map(id => zoneAt(id, NOW())), c = {warn: z.filter(x => x === "warn").length, normal: z.filter(x => x === "normal").length, good: z.filter(x => x === "good").length};
  const n = Math.max(1, c.warn + c.normal + c.good), w = x => `${(100 * x / n).toFixed(2)}%`;
  return `<div class="zbar">${c.warn ? `<i class="w" style="width:${w(c.warn)}"></i>` : ""}${c.normal ? `<i class="n" style="width:${w(c.normal)}"></i>` : ""}${c.good ? `<i class="g" style="width:${w(c.good)}"></i>` : ""}</div>
    <div class="zlab"><span class="w">${c.warn} warning</span><span class="n">${c.normal} normal</span><span class="g">${c.good} supportive</span></div>`;
}
const runs = flags => { const out = []; let s0 = null; flags.forEach((f, i) => { if (f && s0 == null) s0 = i; if ((!f || i === flags.length - 1) && s0 != null) { out.push({i0: s0, i1: f ? i : i - 1}); s0 = null; } }); return out; };
const from = y => Math.max(0, D.months.findIndex(m => m >= y));
function sectionHTML(id, k, title, sentence, charts){
  return `<div class="step">${k} · ${esc(title)}</div><h2>${esc(sentence)}</h2>` + charts.map(c => `<div class="card"><div class="ctitle">${esc(c)}</div><div class="chart" data-c="${id}"></div></div>`).join("");
}
function renderPoints(){
  const X = D.derisk, S = X.series, C = checks(), i0 = from(D.derisk.backtest.from), M = D.months;
  const band = D.settings.derisk.band.map(x => x * 100);
  const cut = v => v == null ? null : v;
  // 1. warning signals: weighted share + the three groups of indicator boxes
  const s1 = $("#s1");
  s1.innerHTML = sectionHTML("s1", 1, C[0].t, C[0].b, ["Share of the weighted warning signals that are on"]) +
    ["A", "B", "C"].map(g => `<div class="sub" id="s${g}"></div>`).join("");
  lineChart(s1.querySelector(".chart"), [{v: X.share.map(cut), c: "var(--ink)", name: "Warning share", wd: 1.6, endLabel: v => `${Math.round(v)}%`}], M,
    {i0, rec: true, fmt: v => `${v.toFixed(0)}%`, fmtTick: t => `${t}%`, ticks: [0, 10, 20, 30, 40, 50, 60], base: 0,
     hband: [{lo: band[0], hi: band[1], c: "var(--bad-bg)", o: 0.55, t: "Cut zone while the Fed tightens"}, {lo: band[1], hi: 100, c: "var(--bad-bg)", t: "Fully out while the Fed tightens"}], aria: "warning share"});
  const S2 = {A: "The economy", B: "Inflation", C: "Market stress"};
  ["A", "B", "C"].forEach((g, k) => {
    const inds = groupInds(g).filter(x => D.derisk.core.includes(x.id)), sec = $(`#s${g}`);
    sec.innerHTML = `<div class="step">1${"abc"[k]} · ${S2[g]}</div><div class="ilist">${inds.map((x, j) => indCard(x, `1${"abc"[k]}.${j + 1}`)).join("")}</div>`;
    sec.querySelectorAll(".icard").forEach(drawInd);
  });
  // 2. the Fed
  $("#s2").innerHTML = sectionHTML("s2", 2, C[1].t, C[1].b, ["Fed funds rate vs the tightening line (24-month low + 1 point)"]);
  lineChart($("#s2 .chart"), [{v: S.fed_funds, c: "var(--ink)", name: "Fed funds rate", endLabel: v => `${v.toFixed(2)}%`},
    {v: S.fed_trigger, c: "var(--bad)", wd: 1.2, name: "Tightening line", endLabel: v => `${v.toFixed(2)}%`}], M,
    {i0, rec: true, fmt: v => `${v.toFixed(2)}%`, fmtTick: t => `${t}%`, base: 0, bands: runs(X.fed_gate).map(r => ({...r, c: "var(--bad-bg)"})), aria: "Fed funds"});
  // 3. growth and trend
  $("#s3").innerHTML = sectionHTML("s3", 3, C[2].t, C[2].b, ["S&P 500 vs its 10-month average", "Unemployment rate vs its 12-month average"]);
  const [c3a, c3b] = $("#s3").querySelectorAll(".chart"), cuts = runs(X.growth_cut).map(r => ({...r, c: "var(--bad-bg)"}));
  lineChart(c3a, [{v: D.values.spx_trend, c: "var(--ink)", wd: 1.4, name: "S&P 500 vs 10-month average", endLabel: v => pct(v, 1)}], M,
    {i0, rec: true, zero: true, fmt: v => pct(v, 1), fmtTick: t => `${t}%`, bands: cuts, aria: "trend"});
  lineChart(c3b, [{v: S.unemp, c: "var(--ink)", name: "Unemployment rate", endLabel: v => `${v.toFixed(1)}%`}, {v: S.unemp_avg, c: "var(--ink3)", wd: 1.2, name: "12-month average"}], M,
    {i0, rec: true, fmt: v => `${v.toFixed(1)}%`, fmtTick: t => `${t}%`, bands: cuts, aria: "unemployment"});
  // 4. bonds as a hedge
  $("#s4").innerHTML = sectionHTML("s4", 4, C[3].t, C[3].b, ["Stock-bond correlation, last 12 months"]);
  lineChart($("#s4 .chart"), [{v: D.values.stockbond, c: "var(--ink)", wd: 1.4, name: "Correlation", endLabel: v => v.toFixed(2)}], M,
    {i0, rec: true, zero: true, fmt: v => v.toFixed(2), fmtTick: t => t.toFixed(1), hband: [{lo: -1, hi: 0, c: "var(--good-bg)", t: "Treasuries hedge stocks"}], aria: "stock-bond correlation"});
  // 5. commodities
  $("#s5").innerHTML = sectionHTML("s5", 5, C[4].t, C[4].b, ["Commodity index vs its 10-month average (index, today = 100)"]);
  lineChart($("#s5 .chart"), [{v: S.commod, c: "var(--s2)", name: "Commodity index", endLabel: v => v.toFixed(0)}, {v: S.commod_ma, c: "var(--ink3)", wd: 1.2, name: "10-month average"}], M,
    {i0, rec: true, log: true, ticks: [2, 5, 10, 20, 50, 100, 200], fmt: v => v.toFixed(1), bands: runs(X.commod_on).map(r => ({...r, c: "var(--good-bg)"})), aria: "commodities"});
  // 6. sector leadership
  $("#s6").innerHTML = sectionHTML("s6", 6, C[5].t, C[5].b, ["Sector return over the past 12 months, excluding the last month"]);
  sectorBars($("#s6 .chart"));
}
function sectorBars(el){
  const T = D.derisk.tilt, i = NOW(); if (!T) { el.innerHTML = ""; return; }
  const rows = D.industries.map(it => ({n: it.name, e: it.etf, v: T.mom_now[it.etf], a: T.actions[it.etf][i]})).filter(r => r.v != null).sort((a, b) => b.v - a.v);
  const w = W(el), bh = 18, gap = 6, m = {l: 150, r: 56, t: 6, b: 6}, h = m.t + m.b + rows.length * (bh + gap);
  const lo = Math.min(0, ...rows.map(r => r.v)), hi = Math.max(0, ...rows.map(r => r.v)), X = v => m.l + (w - m.l - m.r) * (v - lo) / (hi - lo || 1);
  let g = `<line x1="${X(0)}" x2="${X(0)}" y1="${m.t}" y2="${h - m.b}" stroke="var(--axis)"/>`;
  rows.forEach((r, k) => { const y = m.t + k * (bh + gap), x0 = X(Math.min(0, r.v)), x1 = X(Math.max(0, r.v));
    const col = r.a === "over" ? "var(--good)" : r.a === "under" ? "var(--bad)" : "var(--axis)";
    g += `<text x="${m.l - 8}" y="${y + bh - 5}" text-anchor="end">${esc(r.n)}</text><rect x="${x0}" y="${y}" width="${Math.max(1, x1 - x0)}" height="${bh}" rx="3" fill="${col}"/>
      <text class="lab" x="${w - 4}" y="${y + bh - 5}" text-anchor="end">${pct(r.v, 0)}</text>`; });
  el.innerHTML = `<svg viewBox="0 0 ${w} ${h}" height="${h}" role="img" aria-label="Sector momentum">${g}</svg>`;
}

/* ------------------------------------------------------------------ indicator: summary sentence + two charts */
function summary(ind){
  const vals = D.values[ind.id], [cur, ci] = lastOf(vals), ago = ci >= 12 ? vals[ci - 12] : null, z = zoneAt(ind.id, NOW());
  const seen = vals.filter(v => v != null).sort((a, b) => a - b), rng = (seen[Math.floor(.95 * (seen.length - 1))] - seen[Math.floor(.05 * (seen.length - 1))]) || 1;
  const d = ago == null ? null : (cur - ago) * ind.dir / rng;
  const cmp = d == null ? "" : Math.abs(d) < 0.05 ? " and little changed from a year ago" : d > 0 ? " and deteriorating compared with a year ago" : " and improving compared with a year ago";
  const iv = D.ind_view[ind.id], th = iv && iv.warn != null ? ` (${ind.dir > 0 ? "above" : "below"} ${fmtV(iv.warn, ind, hasNeg(ind.id))})` : "";
  const zp = {warn: `in the warning zone${th}`, normal: "in its normal range", good: "in the supportive zone"}[z] || "without enough history to judge";
  const verb = /(permits|sales|stocks)$/.test(ind.short) ? "are" : "is";
  return `${esc(ind.what)}. At ${fmtV(cur, ind, hasNeg(ind.id))}${esc(ind.vp)}, ${esc(ind.short)} ${verb} ${zp}${cmp}, indicating ${esc(ind.means[z] || "no clear signal")}.`;
}
function panel(el, ind, i0, opt){
  const w = W(el), h = opt.h || 170, m = {l: 50, r: opt.r || 10, t: 16, b: 20};
  const vals = D.values[ind.id].map(x => x == null ? null : x * ind.scale), n = N;
  const seen = vals.slice(i0).filter(x => x != null);
  if (!seen.length) { el.innerHTML = ""; return; }
  const srt = [...seen].sort((a, b) => a - b);
  let lo = opt.clip ? srt[Math.floor(.01 * (srt.length - 1))] : srt[0], hi = opt.clip ? srt[Math.ceil(.99 * (srt.length - 1))] : srt[srt.length - 1];
  const [cv, ci] = lastOf(vals); lo = Math.min(lo, cv); hi = Math.max(hi, cv);
  const iv = D.ind_view[ind.id], wv = iv && iv.warn != null ? iv.warn * ind.scale : null;
  if (wv != null) { lo = Math.min(lo, wv); hi = Math.max(hi, wv); }
  if (opt.ago != null) { lo = Math.min(lo, opt.ago); hi = Math.max(hi, opt.ago); }
  const T = niceTicks(lo, hi, opt.nt || 4); lo = T.lo; hi = T.hi;
  const X = i => m.l + (w - m.l - m.r) * (i - i0) / Math.max(1, n - 1 - i0);
  const Y = y => m.t + (h - m.t - m.b) * (1 - (Math.max(lo, Math.min(hi, y)) - lo) / (hi - lo || 1));
  let g = "";
  if (wv != null) { const y = Y(wv), top = ind.dir > 0 ? m.t : y, bot = ind.dir > 0 ? y : h - m.b;
    g += `<rect x="${m.l}" y="${top}" width="${w - m.l - m.r}" height="${Math.max(0, bot - top)}" fill="var(--bad-bg)" opacity=".55"/>
      <line x1="${m.l}" x2="${w - m.r}" y1="${y}" y2="${y}" stroke="var(--bad)" stroke-dasharray="3 3" opacity=".7"/>`;
    if (opt.zoneLabel) g += `<text class="zl" x="${m.l + 6}" y="${ind.dir > 0 ? m.t + 11 : h - m.b - 5}">Warning zone</text>`; }
  let anyRec = false;
  D.recession.forEach((r, i) => { if (r === 1 && i >= i0) { anyRec = true; g += `<rect x="${X(i).toFixed(1)}" y="${m.t}" width="${Math.max(1, X(i + 1) - X(i)).toFixed(2)}" height="${h - m.t - m.b}" fill="var(--rec)"/>`; } });
  if (anyRec) g += recKey(w - m.r, 4);
  T.t.forEach(t => { g += `<line x1="${m.l}" x2="${w - m.r}" y1="${Y(t)}" y2="${Y(t)}" stroke="${t === 0 ? "var(--axis)" : "var(--grid)"}"/><text x="${m.l - 6}" y="${Y(t) + 3.5}" text-anchor="end">${tickLab(t, ind, T.dp)}</text>`; });
  const span = (n - 1 - i0) / 12, step = span > 30 ? 10 : span > 12 ? 5 : span > 5 ? 2 : 1;
  let lastX = -1e9;
  for (let i = i0; i < n; i++) { const mo = D.months[i];
    const tick = opt.monthly ? (mo.endsWith("-01") || mo.endsWith("-07")) : (mo.endsWith("-01") && +mo.slice(0, 4) % step === 0);
    if (tick && X(i) - lastX > 44) { g += `<text x="${X(i)}" y="${h - 5}" text-anchor="middle">${opt.monthly ? mlab(mo) : mo.slice(0, 4)}</text>`; lastX = X(i); } }
  let d = "", pen = false;
  for (let i = i0; i < n; i++) { const y = vals[i]; if (y == null) { pen = false; continue; } d += (pen ? "L" : "M") + X(i).toFixed(1) + " " + Y(y).toFixed(1); pen = true; }
  g += `<path d="${d}" fill="none" stroke="var(--ink)" stroke-width="${opt.monthly ? 1.8 : 1.2}" stroke-linejoin="round"/>`;
  if (opt.ago != null && opt.agoI >= i0) {
    const xa = X(opt.agoI), ya = Y(opt.ago), xc = X(ci), yc = Y(cv), up = yc < ya;
    g += `<line x1="${xa}" x2="${xc}" y1="${ya}" y2="${ya}" stroke="var(--ink2)" stroke-dasharray="2 3"/>
      <line x1="${xc}" x2="${xc}" y1="${ya}" y2="${yc}" stroke="var(--ink2)" stroke-dasharray="2 3"/>
      <circle cx="${xa}" cy="${ya}" r="4" fill="var(--card)" stroke="var(--ink)" stroke-width="1.6"/>
      <text class="lab" x="${xa}" y="${up ? ya + 15 : ya - 8}" text-anchor="start">${mlab(D.months[opt.agoI])}: ${fmtV(opt.ago / ind.scale, ind, hasNeg(ind.id))}</text>`;
  }
  if (cv != null) g += `<circle cx="${X(ci)}" cy="${Y(cv)}" r="4.2" fill="var(--ink)" stroke="var(--card)" stroke-width="1.5"/>` +
    (opt.monthly ? `<text class="lab" x="${X(ci) - 6}" y="${opt.ago != null && Y(cv) < Y(opt.ago) ? Y(cv) - 8 : Y(cv) + 16}" text-anchor="end">${mlab(D.months[ci])}: ${fmtV(cv / ind.scale, ind, hasNeg(ind.id))}</text>` : "");
  g += `<line class="cx" x1="0" x2="0" y1="${m.t}" y2="${h - m.b}" stroke="var(--axis)" visibility="hidden"/><rect class="hit" x="${m.l}" y="0" width="${w - m.l - m.r}" height="${h}" fill="transparent"/>`;
  el.innerHTML = `<svg viewBox="0 0 ${w} ${h}" height="${h}" role="img" aria-label="${esc(ind.title)}">${g}</svg>`;
  const hit = el.querySelector(".hit"), cx = el.querySelector(".cx");
  hit.addEventListener("pointermove", e => {
    const r = el.querySelector("svg").getBoundingClientRect(), px = (e.clientX - r.left) * w / r.width;
    const i = Math.max(i0, Math.min(n - 1, Math.round(i0 + (px - m.l) / (w - m.l - m.r) * (n - 1 - i0))));
    cx.setAttribute("x1", X(i)); cx.setAttribute("x2", X(i)); cx.setAttribute("visibility", "visible");
    showTip(e, `<div class="d">${mlab(D.months[i])}${D.recession[i] === 1 ? " · recession" : ""}</div><b>${fmtV(D.values[ind.id][i], ind, hasNeg(ind.id))}</b>`);
  });
  hit.addEventListener("pointerleave", () => { hideTip(); cx.setAttribute("visibility", "hidden"); });
}
function drawInd(card){
  const ind = IND()[card.dataset.id], vals = D.values[ind.id];
  const iFirst = Math.max(D.months.findIndex(x => x >= "1970-01"), vals.findIndex(x => x != null));
  const [, ci] = lastOf(vals), agoI = ci - 12, ago = agoI >= 0 && vals[agoI] != null ? vals[agoI] * ind.scale : null;
  panel(card.querySelector(".long"), ind, iFirst, {clip: true, zoneLabel: true});
}
function indCard(ind, num){
  const v = D.ind_view[ind.id], z = zoneAt(ind.id, NOW()), vals = D.values[ind.id];
  const first = D.months[Math.max(D.months.findIndex(x => x >= "1970-01"), vals.findIndex(x => x != null))];
  let after = "";
  const hist = v && v.hist["12"];
  if (hist && hist.length >= 4) {
    const f = r => `<span class="chip ${r[1] >= 0 ? "over" : "under"}" title="beat the 20-sector average in ${r[2]}% of those months">${esc(NAME()[r[0]])} ${pct(r[1], 1)}</span>`;
    after = `<div class="after"><span class="muted">Sectors after past readings like this, over the next 12 months vs the 20-sector average</span><div class="chips"><span class="lab">Best</span>${hist.slice(0, 3).map(f).join("")}<span class="lab sp">Worst</span>${hist.slice(-3).reverse().map(f).join("")}</div></div>`;
  }
  return `<div class="icard z-${z}" id="ic-${ind.id}" data-id="${ind.id}"><div class="ihd"><span class="inum">${num}</span><b>${esc(ind.title)}</b><span class="tag ${z}">${ZW[z]}</span></div>
    <p class="isum">${summary(ind)}</p>
    <div class="chart long"></div></div>`;
}
const ZORDER = {warn: 0, good: 1, normal: 2, "": 3};
function footnotes(extra){ return `<ol class="fns">${extra.map(t => `<li>${t}</li>`).join("")}</ol>`; }

/* ------------------------------------------------------------------ recommendation 1: portfolio, by quarter */
const qOf = mo => `${mo.slice(0, 4)}-Q${Math.ceil(+mo.slice(5, 7) / 3)}`;
const qLab = q => `${q.slice(5)} ${q.slice(0, 4)}`;
const sgn = d => { const r = Math.round(d); return `${r > 0 ? "+" : r < 0 ? "−" : ""}${Math.abs(r)}%`; };
const PARTS = [["equity", "Equity", "var(--s1)"], ["cash", "Cash", "var(--axis)"], ["bond", "Bond", "var(--s3)"], ["commodities", "Commodities", "var(--s2)"]];
function allocAt(i){ const A = D.derisk.alloc, e = A ? A.equity[i] : D.derisk.exposure[i];
  return {equity: e ?? 100, bond: A ? (A.bond[i] ?? 0) : 0, cash: A ? Math.max(0, A.cash[i] ?? 0) : 100 - (e ?? 100), commodities: A && A.commodities ? (A.commodities[i] ?? 0) : 0}; }
const mix = x => PARTS.map(([k, l]) => `${x[k]}% ${l.toLowerCase()}`).join(", ");
function quarters(){
  const B = D.derisk.backtest, i0 = D.months.indexOf(B.from), Q = [];
  for (let i = i0 + 1; i < N; i++) {
    const q = qOf(D.months[i]); let cur = Q[Q.length - 1];
    if (!cur || cur.q !== q) { cur = {q, al: []}; Q.push(cur); }
    cur.al.push(allocAt(i - 1));                                   // held during month i = set at the end of month i-1
    cur.sp = 100 * B.curves.sp500[i]; cur.rec = 100 * B.curves.strategy[i];
  }
  Q.forEach(x => PARTS.forEach(([k]) => { x[k] = Math.round(x.al.reduce((a, b) => a + b[k], 0) / x.al.length); }));
  const last = Q[Q.length - 1];
  Object.assign(last, allocAt(N - 1), {now: true});               // the call for the current quarter: latest reading
  Q.forEach((x, k) => { x.d = k ? ((x.rec / Q[k - 1].rec) / (x.sp / Q[k - 1].sp) - 1) * 100 : 0; });
  return Q;
}
function renderExposure(){
  const Q = quarters(), now = Q[Q.length - 1];
  $("#xHead").innerHTML = `<span class="q">${qLab(now.q)}</span><b>${now.equity}% equity</b><span>${now.cash}% cash · ${now.bond}% bond · ${now.commodities}% commodities</span>`;
  masterChart($("#xChart"), Q);
}
function masterChart(el, Q){
  const w = W(el), narrow = w < 640, m = {l: 52, r: narrow ? 10 : 150, t: 26, b: 22};
  const hA = 90, hB = narrow ? 200 : 260, gap = 40, n = Q.length;
  const yA = m.t, yB = yA + hA + gap, h = yB + hB + m.b;
  const X_ = k => m.l + (w - m.l - m.r) * k / Math.max(1, n - 1), bw = Math.max(1.5, (w - m.l - m.r) / n - 0.6);
  const YA = v => yA + hA * (100 - v) / 100;
  const vals = Q.flatMap(x => [x.sp, x.rec]);
  const lo = Math.log(Math.min(...vals)), hi = Math.log(Math.max(...vals));
  const YB = v => yB + hB * (1 - (Math.log(v) - lo) / (hi - lo));
  let g = "";
  // panel A: the recommended portfolio, stacked
  Q.forEach((x, k) => { let top = 100;
    PARTS.forEach(([key, , col]) => { const v = x[key]; if (v <= 0) return;
      g += `<rect x="${X_(k) - bw / 2}" y="${YA(top)}" width="${bw}" height="${YA(top - v) - YA(top)}" fill="${col}" opacity="${x.now ? 1 : 0.75}"/>`; top -= v; }); });
  [100, 50, 0].forEach(t => { g += `<text x="${m.l - 6}" y="${YA(t) + 3.5}" text-anchor="end">${t}%</text>`; });
  if (!narrow) g += `<text class="lab" x="${m.l}" y="${yA - 10}">Recommended portfolio</text>`;
  let kx = narrow ? m.l : w - 4 - PARTS.reduce((a, [, l]) => a + l.length * 6.6 + 16, 0);
  PARTS.forEach(([, l, col]) => {
    g += `<rect x="${kx}" y="${yA - 19}" width="10" height="10" rx="2" fill="${col}"/><text x="${kx + 14}" y="${yA - 10}">${l}</text>`; kx += l.length * 6.6 + 16; });
  // panel B: growth of $100
  D.recession.forEach((r, i) => { if (r !== 1) return; const k = Q.findIndex(x => x.q === qOf(D.months[i])); if (k < 0) return;
    g += `<rect x="${X_(k) - bw / 2}" y="${yB - 10}" width="${bw + 0.6}" height="6" fill="var(--rec)"/>`; });
  g += recKey(w - 4, yB - 22);
  [100, 1000, 10000, 100000].filter(t => Math.log(t) >= lo && Math.log(t) <= hi).forEach(t => {
    g += `<line x1="${m.l}" x2="${w - m.r}" y1="${YB(t)}" y2="${YB(t)}" stroke="var(--grid)"/><text x="${m.l - 6}" y="${YB(t) + 3.5}" text-anchor="end">$${t.toLocaleString("en-US")}</text>`; });
  const path = key => Q.map((x, k) => `${k ? "L" : "M"}${X_(k).toFixed(1)} ${YB(x[key]).toFixed(1)}`).join("");
  g += `<path d="${path("sp")}" fill="none" stroke="var(--ink)" stroke-width="2"/><path d="${path("rec")}" fill="none" stroke="var(--s1)" stroke-width="2.6"/>`;
  const L = Q[n - 1];
  if (!narrow) {
    const ys = YB(L.sp), yr = YB(L.rec), sep = Math.abs(ys - yr) < 14 ? 7 : 0;
    g += `<text class="endlab" x="${w - m.r + 8}" y="${yr + 4 + (yr <= ys ? -sep : sep)}" style="fill:var(--s1)">Recommended</text>`;
    g += `<text class="endlab" x="${w - m.r + 8}" y="${ys + 4 + (ys < yr ? -sep : sep)}">S&P 500</text>`;
  } else g += `<text class="lab" x="${m.l + 4}" y="${yB + 12}"><tspan style="fill:var(--s1)">━ Recommended</tspan>  ━ S&P 500</text>`;
  g += `<text class="lab" x="${m.l}" y="${yB - 14}">Growth of $100 since ${Q[0].q.slice(0, 4)}</text>`;
  let lastX = -1e9;
  Q.forEach((x, k) => { const y = +x.q.slice(0, 4); if (x.q.endsWith("Q1") && y % 5 === 0 && X_(k) - lastX > 40) { g += `<text x="${X_(k)}" y="${h - 5}" text-anchor="middle">${y}</text>`; lastX = X_(k); } });
  g += `<line class="cx" x1="0" x2="0" y1="${yA}" y2="${yB + hB}" stroke="var(--ink3)" visibility="hidden"/><circle class="d1" r="4" fill="var(--ink)" visibility="hidden"/><circle class="d2" r="4.5" fill="var(--s1)" visibility="hidden"/><rect class="hit" x="${m.l - 4}" y="0" width="${w - m.l - m.r + 8}" height="${h}" fill="transparent"/>`;
  el.innerHTML = `<svg viewBox="0 0 ${w} ${h}" height="${h}" role="img" aria-label="Recommended portfolio by quarter and its growth vs the S&P 500">${g}</svg>`;
  const svg = el.querySelector("svg"), cx = el.querySelector(".cx"), d1 = el.querySelector(".d1"), d2 = el.querySelector(".d2");
  el.querySelector(".hit").addEventListener("pointermove", e => {
    const r = svg.getBoundingClientRect(), px = (e.clientX - r.left) * w / r.width;
    const k = Math.max(0, Math.min(n - 1, Math.round((px - m.l) / (w - m.l - m.r) * (n - 1)))), x = Q[k];
    cx.setAttribute("x1", X_(k)); cx.setAttribute("x2", X_(k)); cx.setAttribute("visibility", "visible");
    d1.setAttribute("cx", X_(k)); d1.setAttribute("cy", YB(x.sp)); d1.setAttribute("visibility", "visible");
    d2.setAttribute("cx", X_(k)); d2.setAttribute("cy", YB(x.rec)); d2.setAttribute("visibility", "visible");
    showTip(e, `<div class="d">${qLab(x.q)}</div><b>${mix(x)}</b>` + (k ? `<div>Performance vs S&P 500: <b>${sgn(x.d)}</b></div>` : ""));
  });
  el.querySelector(".hit").addEventListener("pointerleave", () => { hideTip(); [cx, d1, d2].forEach(l => l.setAttribute("visibility", "hidden")); });
}

/* ------------------------------------------------------------------ call 2: sectors (momentum tilt while fully invested) */
const ACT = {over: ["over", "▲", "Overweight"], under: ["under", "▼", "Underweight"], neutral: ["neutral", "●", "Neutral"]};
const WHYM = {over: "One of the five strongest sectors over the past year; leadership tends to persist while the market is healthy.",
  under: "One of the five weakest sectors over the past year; laggards tend to keep lagging while the trend holds.",
  neutral: "In the middle of the pack over the past year, so it is held at its normal weight."};
function renderIndustries(){
  const T = D.derisk.tilt, i = NOW(), live = D.derisk.fully_invested[i];
  $("#actHead").textContent = live ? "Tilts for this month." : "On hold: tilts apply only while the portfolio is fully in stocks.";
  $("#actWhy").textContent = live ? "Against holding all 20 sectors equally." : "These are the tilts that would apply.";
  const rows = D.industries.map(it => { const a = T ? T.actions[it.etf][i] : "neutral", c = a === "hold" ? null : a;
    const raw = c || (T && T.mom_now[it.etf] != null ? null : "neutral");
    return {it, c: c || "neutral", o: c === "over" ? 0 : c === "under" ? 1 : 2, v: T ? T.mom_now[it.etf] : null}; })
    .sort((a, b) => a.o - b.o || (b.v ?? 0) - (a.v ?? 0));
  $("#indTable").innerHTML = `<thead><tr><th>Sector</th><th>Call</th><th>Why now</th></tr></thead><tbody>` + rows.map(r => {
    const [cls, ic, tx] = ACT[r.c] || ACT.neutral;
    return `<tr><td><b>${esc(r.it.name)}</b> <span class="etf muted">${r.it.etf}</span></td><td><span class="pill ${cls}${!live && r.c !== "neutral" ? " hold" : ""}"><span aria-hidden="true">${ic}</span>${tx}${!live && r.c !== "neutral" ? " · on hold" : ""}</span></td><td class="why">${esc(WHYM[r.c])}</td></tr>`; }).join("") + "</tbody>";
}

/* ------------------------------------------------------------------ pages */
let PAGE = (location.hash === "#calls" ? "calls" : store.get("mc-p")) || "reading";
function setPage(p){ PAGE = p; store.set("mc-p", p);
  $("#pReading").hidden = p !== "reading"; $("#pCalls").hidden = p !== "calls";
  document.querySelectorAll("#tabs button").forEach(b => b.setAttribute("aria-selected", b.dataset.p === p));
  history.replaceState(null, "", p === "calls" ? "#calls" : location.pathname);
  renderAll(); }
function renderAll(){ if (PAGE === "calls") { renderExposure(); renderIndustries(); } else { renderTop(); renderPoints(); } }
async function start(){
  const buf = await (await fetch("/data/data.bin", {cache: "no-cache"})).arrayBuffer();
  D = await openBlob(buf); N = D.months.length;
  $("#lock").hidden = true; $("#shell").hidden = false;
  $("#foot").textContent = `Reading as of ${mlab(D.asof)} · updated ${D.updated} · version ${D.version}. Not investment advice.`;
  document.querySelectorAll("#tabs button").forEach(b => { b.onclick = () => { setPage(b.dataset.p); scrollTo(0, 0); }; });
  setPage(PAGE);
  let t; addEventListener("resize", () => { clearTimeout(t); t = setTimeout(renderAll, 150); });
}
function showLock(msg){ $("#shell").hidden = true; $("#lock").hidden = false; $("#lockMsg").textContent = msg; $("#pw").focus(); }
$("#lockForm").addEventListener("submit", async ev => {
  ev.preventDefault(); const btn = $("#unlockBtn"); btn.disabled = true; btn.textContent = "Opening…"; $("#lockMsg").textContent = "";
  try {
    const k = await deriveKey($("#pw").value.trim());
    if (!(await tryKey(k))) { $("#lockMsg").textContent = "That password didn't open the data. Check it and try again."; return; }
    if ($("#remember").checked) store.set("mc-key", JSON.stringify({salt: INFO.salt, k: toB64(await crypto.subtle.exportKey("raw", k))}));
    $("#pw").value = ""; await start();
  } catch(e){ $("#lockMsg").textContent = "Couldn't open the data: " + e.message; }
  finally { btn.disabled = false; btn.textContent = "Open"; }
});
(async () => {
  try { INFO = await (await fetch("/data/keyinfo.json", {cache: "no-cache"})).json(); }
  catch(e){ showLock("No data yet: the Macro workflow hasn't published the page."); return; }
  if (INFO.plain) { await start(); return; }
  const saved = store.get("mc-key");
  if (saved) { try { const {salt, k} = JSON.parse(saved);
      if (salt === INFO.salt) { const key = await crypto.subtle.importKey("raw", b64(k), {name: "AES-GCM"}, true, ["decrypt"]);
        if (await tryKey(key)) { await start(); return; } } } catch(e){}
    store.del("mc-key"); }
  showLock("");
})();
