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
  const i0 = Math.min(...series.map(s => s.v.findIndex(v => v != null)).filter(x => x >= 0));
  const n = months.length, span = n - 1 - i0;
  const vals = series.flatMap(s => s.v.slice(i0).filter(v => v != null));
  const lo = opt.log ? Math.min(...vals) : Math.min(...vals, opt.base ?? Infinity), hi = Math.max(...vals);
  const tr = v => opt.log ? Math.log(v) : v;
  const Y = v => m.t + (h - m.t - m.b) * (1 - (tr(v) - tr(lo)) / (tr(hi) - tr(lo) || 1));
  const X = i => m.l + (w - m.l - m.r) * (i - i0) / (span || 1);
  let g = "";
  const ticks = opt.ticks || [];
  ticks.filter(t => t >= lo && t <= hi).forEach(t => { g += `<line x1="${m.l}" x2="${w - m.r}" y1="${Y(t)}" y2="${Y(t)}" stroke="var(--grid)"/><text x="${m.l - 6}" y="${Y(t) + 3.5}" text-anchor="end">${opt.fmtTick ? opt.fmtTick(t) : t}</text>`; });
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

/* ------------------------------------------------------------------ the reading */
function sentences(){
  const i = NOW(), stage = D.stage[i], hot = D.hot[i], high = D.stress_high[i], str = D.pillars.stress[i];
  return {
    A: {expansion: "The economy is strong and getting stronger", late: "The economy is still strong, but signs of slowing are spreading",
        contraction: "The economy is weak and getting weaker", recovery: "The economy is weak but improving"}[stage] || "Not enough data",
    B: hot ? "Inflation is running hot" : "Inflation is under control",
    C: high ? "Markets are in risk-off mode" : str >= D.settings.stress_high[1] ? "Markets are nervous, but not in risk-off mode" : "Markets are calm",
  };
}
function zoneBar(g, fnWarn){
  const c = count(g, NOW()), w = x => `${(100 * x / Math.max(1, c.n)).toFixed(2)}%`;
  return `<div class="zbar" role="img" aria-label="${c.warn} warning, ${c.normal} normal, ${c.good} supportive">
    ${c.warn ? `<i class="w" style="width:${w(c.warn)}"></i>` : ""}${c.normal ? `<i class="n" style="width:${w(c.normal)}"></i>` : ""}${c.good ? `<i class="g" style="width:${w(c.good)}"></i>` : ""}</div>
    <div class="zlab"><span class="w">${c.warn} warning${fnWarn ? sup(fnWarn) : ""}</span><span class="n">${c.normal} normal</span><span class="g">${c.good} supportive</span></div>`;
}
function jumped(g){ const now = count(g, NOW()).warn, a6 = avgWarn(g, NOW() - 1); return now - a6 >= 2.5 ? {now, a6: Math.round(a6)} : null; }
function renderTop(){
  const i = NOW(), s = D.regime[i], S = sentences();
  let j = i; while (j > 0 && D.regime[j - 1] === s) j--;
  $("#stageDot").style.background = `var(--st-${s})`;
  $("#stageName").textContent = stName(s);
  $("#stageWhy").textContent = `${S.A}. ${S.B}. ${S.C}. Reading since ${mlab(D.months[j])}.`;
  $("#points").innerHTML = ["A", "B", "C"].map(g => `<li><a href="#s${g}"><span class="pn">${GROUPS[g].num}</span><b>${S[g]}</b>${zoneBar(g)}
    ${jumped(g) ? `<span class="jump">Warning signals jumped this month: ${jumped(g).now}, from about ${jumped(g).a6}</span>` : ""}</a></li>`).join("");
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
function renderPoint(g, sec, title){
  const inds = groupInds(g).map((x, k) => [x, `${GROUPS[g].num}.${k + 1}`]), show = inds;
  const j = g === "A" ? jumped(g) : null;
  const extra = g === "A" ? [`The economy reading uses 6-month averages of these signals and changes only after 3 months in a row.${j ? ` This month ${j.now} signals are in the warning zone, up from about ${j.a6} on average over the previous 6 months; if that persists, the reading will turn.` : ""}`]
    : g === "B" ? ["Inflation counts as running hot when these signals, averaged over 6 months, sit clearly toward the high end of their history."]
    : g === "C" ? ["Risk-off mode starts when these signals on average are deep in their worst third of history, and ends once they ease back."]
    : ["Shown for context only. Adding these signals to the reading made past calls worse, so they do not affect the calls."];
  sec.innerHTML = `${title ? `<div class="step">${GROUPS[g].step}</div><h2>${esc(title)}${sup(1)}</h2>` : ""}${zoneBar(g)}
    <div class="ilist">${show.map(([x, k]) => indCard(x, k)).join("")}</div>
    ${footnotes(extra)}`;
  sec.querySelectorAll(".icard").forEach(drawInd);
}
function renderPoints(){
  const S = sentences();
  renderPoint("A", $("#sA"), S.A); renderPoint("B", $("#sB"), S.B); renderPoint("C", $("#sC"), S.C);
}

/* ------------------------------------------------------------------ recommendation 1: equity exposure, by quarter */
const qOf = mo => `${mo.slice(0, 4)}-Q${Math.ceil(+mo.slice(5, 7) / 3)}`;
const qLab = q => `${q.slice(5)} ${q.slice(0, 4)}`;
const dlab = d => { const r = Math.round(d); return `(${r > 0 ? "+" : r < 0 ? "−" : ""}${Math.abs(r)}%)`; };
const defName = x => x.def === "bonds" && x.equity < 100 ? "Treasuries" : "cash";
function quarters(){
  const X = D.derisk, B = X.backtest, i0 = D.months.indexOf(B.from), Q = [];
  for (let i = i0 + 1; i < N; i++) {
    const q = qOf(D.months[i]); let cur = Q[Q.length - 1];
    if (!cur || cur.q !== q) { cur = {q, i0: i, eq: []}; Q.push(cur); }
    cur.i1 = i; cur.eq.push(X.exposure[i - 1] ?? 100); cur.def = X.defensive?.[i - 1];           // the share held during month i was set at the end of month i-1
    cur.sp = 100 * B.curves.sp500[i]; cur.rec = 100 * B.curves.strategy[i];       // growth of $100
  }
  const last = Q[Q.length - 1];
  Q.forEach(x => { x.equity = Math.round(x.eq.reduce((a, b) => a + b, 0) / x.eq.length); });
  last.equity = X.exposure[N - 1]; last.def = X.defensive?.[N - 1]; last.now = true;                // the call for the current quarter: latest reading
  return Q;
}
function clusters(Q){
  // each cut (months with part of the money in cash), placed on the quarter axis; d = return vs the S&P 500 over it
  const qk = {}; Q.forEach((x, k) => { qk[x.q] = k; });
  const mi = mo => D.months.indexOf(mo);
  return D.derisk.backtest.episodes.filter(e => e.diff != null).map(e => {
    const s0 = D.months[mi(e.from) + 1] || e.from, s1 = D.months[mi(e.to) + 1] || e.to;   // months actually held
    return {a: qk[qOf(s0)] ?? Q.length - 1, b: qk[qOf(s1)] ?? Q.length - 1, d: e.diff, from: e.from, to: e.to};
  });
}
function renderExposure(){
  const Q = quarters(), now = Q[Q.length - 1], C = clusters(Q);
  Q.forEach((x, k) => { x.d = k ? ((x.rec / Q[k - 1].rec) / (x.sp / Q[k - 1].sp) - 1) * 100 : 0; });
  const won = C.filter(c => c.d >= 1), lost = C.filter(c => c.d <= -1);
  const sum = l => l.reduce((a, c) => a + c.d, 0);
  $("#xHead").innerHTML = `<span class="q">${qLab(now.q)}</span><b>${now.equity}% equity</b><span>${100 - now.equity}% ${defName(now)}</span>`;
  $("#xScore").innerHTML = `<div class="sc good"><b>+${Math.round(sum(won))} pts</b><span>protected in ${won.length} cuts that paid off (percentage points vs the S&P 500, added up)</span></div>
    <div class="sc bad"><b>−${Math.abs(Math.round(sum(lost)))} pts</b><span>lost in ${lost.length} false alarms and missed rebounds (added up the same way)</span></div>
    <div class="sc"><b>${pct(D.derisk.backtest.stats.strategy.maxdd, 0)}</b><span>worst fall with the recommendation, vs ${pct(D.derisk.backtest.stats.sp500.maxdd, 0)} for the S&P 500 (${pct(D.derisk.backtest.stats.strategy.cagr, 1)} vs ${pct(D.derisk.backtest.stats.sp500.cagr, 1)} a year)</span></div>`;
  $("#xNote").textContent = `Each bar is one quarter: green when holding less equity beat staying fully in the S&P 500, red when it cost. Updated as new data come in. The rest is held in 7–10-year Treasuries while stocks and bonds move in opposite directions, otherwise in 3-month Treasury bills. Returns include dividends; no trading costs or taxes.`;
  masterChart($("#xChart"), Q, C);
}
function masterChart(el, Q, C){
  const w = W(el), narrow = w < 640, m = {l: 52, r: narrow ? 10 : 150, t: 26, b: 22};
  const hA = narrow ? 170 : 210, hB = narrow ? 150 : 170, hC = 64, gap = 30, n = Q.length;
  const yA = m.t, yB = yA + hA + gap, yC = yB + hB + gap, h = yC + hC + m.b;
  const X_ = k => m.l + (w - m.l - m.r) * k / Math.max(1, n - 1), bw = Math.max(1.5, (w - m.l - m.r) / n - 0.6);
  const vals = Q.flatMap(x => [x.sp, x.rec]);
  const lo = Math.log(Math.min(...vals)), hi = Math.log(Math.max(...vals));
  const YA = v => yA + hA * (1 - (Math.log(v) - lo) / (hi - lo));
  const dmax = Math.max(10, ...Q.map(x => Math.abs(x.d))), T = niceTicks(-dmax, dmax, 4);
  const YB = v => yB + hB * (T.hi - v) / (T.hi - T.lo);
  const YC = v => yC + hC * (100 - v) / 100;
  let g = "";
  // recessions, as thin bars over the top panel + key
  D.recession.forEach((r, i) => { if (r !== 1) return; const k = Q.findIndex(x => x.q === qOf(D.months[i])); if (k < 0) return;
    g += `<rect x="${X_(k) - bw / 2}" y="${yA - 10}" width="${bw + 0.6}" height="6" fill="var(--rec)"/>`; });
  g += recKey(w - 4, 2);
  // shade every cut period across all panels: green = protected, red = cost
  C.filter(c => Math.abs(c.d) >= 1).forEach(c => {
    g += `<rect x="${X_(c.a) - bw / 2}" y="${yA}" width="${X_(c.b) - X_(c.a) + bw}" height="${yC + hC - yA}" fill="var(${c.d > 0 ? "--good-bg" : "--bad-bg"})" opacity=".7"/>`; });
  // panel A: growth of $100
  [100, 1000, 10000].filter(t => Math.log(t) >= lo && Math.log(t) <= hi).forEach(t => {
    g += `<line x1="${m.l}" x2="${w - m.r}" y1="${YA(t)}" y2="${YA(t)}" stroke="var(--grid)"/><text x="${m.l - 6}" y="${YA(t) + 3.5}" text-anchor="end">$${t.toLocaleString("en-US")}</text>`; });
  const path = key => Q.map((x, k) => `${k ? "L" : "M"}${X_(k).toFixed(1)} ${YA(x[key]).toFixed(1)}`).join("");
  g += `<path d="${path("sp")}" fill="none" stroke="var(--ink)" stroke-width="2"/><path d="${path("rec")}" fill="none" stroke="var(--s1)" stroke-width="2.6"/>`;
  const L = Q[n - 1];
  if (!narrow) {
    const ys = YA(L.sp), yr = YA(L.rec), sep = Math.abs(ys - yr) < 14 ? 7 : 0;
    g += `<text class="endlab" x="${w - m.r + 8}" y="${yr + 4 + (yr <= ys ? -sep : sep)}" style="fill:var(--s1)">Recommended $${Math.round(L.rec).toLocaleString("en-US")}</text>`;
    g += `<text class="endlab" x="${w - m.r + 8}" y="${ys + 4 + (ys < yr ? -sep : sep)}">S&P 500 $${Math.round(L.sp).toLocaleString("en-US")}</text>`;
  }
  g += `<text class="lab" x="${m.l}" y="${yA - 14}">Growth of $100 since ${Q[0].q.slice(0, 4)}${narrow ? "" : ""}</text>`;
  if (narrow) g += `<text class="lab" x="${m.l + 4}" y="${yA + 12}"><tspan style="fill:var(--s1)">━ Recommended</tspan>  ━ S&P 500</text>`;
  // panel B: gain or loss vs the S&P 500 each quarter
  T.t.forEach(t => { g += `<line x1="${m.l}" x2="${w - m.r}" y1="${YB(t)}" y2="${YB(t)}" stroke="${t === 0 ? "var(--axis)" : "var(--grid)"}"/><text x="${m.l - 6}" y="${YB(t) + 3.5}" text-anchor="end">${t > 0 ? "+" : t < 0 ? "−" : ""}${Math.abs(t)}%</text>`; });
  Q.forEach((x, k) => { if (Math.abs(x.d) < 0.05) return; const y0 = YB(0), y1 = YB(x.d);
    g += `<rect x="${X_(k) - bw / 2}" y="${Math.min(y0, y1)}" width="${bw}" height="${Math.max(1, Math.abs(y1 - y0))}" fill="var(${x.d > 0 ? "--good" : "--bad"})"/>`; });
  g += `<text class="lab" x="${m.l}" y="${yB - 10}">Protected (green) or lost (red) vs staying fully in the S&P 500</text>`;
  const big = C.filter(c => Math.abs(c.d) >= (narrow ? 8 : 5));
  big.forEach((c, k) => { const cx = (X_(c.a) + X_(c.b)) / 2, up = c.d > 0;
    const y = up ? YB(T.hi) + 10 + (k % 2) * 12 : YB(T.lo) - 4 - (k % 2) * 12;
    g += `<text class="eplab ${up ? "pos" : "neg"}" x="${cx}" y="${y}" text-anchor="middle">${dlab(c.d)}</text>`; });
  // panel C: portfolio exposure
  Q.forEach((x, k) => { g += `<rect x="${X_(k) - bw / 2}" y="${YC(x.equity)}" width="${bw}" height="${yC + hC - YC(x.equity)}" fill="var(--s1)" opacity="${x.now ? 0.95 : 0.4}"/>`; });
  [100, 50, 0].forEach(t => { g += `<line x1="${m.l}" x2="${w - m.r}" y1="${YC(t)}" y2="${YC(t)}" stroke="var(--grid)"/><text x="${m.l - 6}" y="${YC(t) + 3.5}" text-anchor="end">${t}%</text>`; });
  g += `<text class="lab" x="${m.l}" y="${yC - 8}">Portfolio exposure (equity share)</text>`;
  let lastX = -1e9;
  Q.forEach((x, k) => { const y = +x.q.slice(0, 4); if (x.q.endsWith("Q1") && y % 5 === 0 && X_(k) - lastX > 40) { g += `<text x="${X_(k)}" y="${h - 5}" text-anchor="middle">${y}</text>`; lastX = X_(k); } });
  g += `<line class="cx" x1="0" x2="0" y1="${yA}" y2="${yC + hC}" stroke="var(--ink3)" visibility="hidden"/><circle class="d1" r="4" fill="var(--ink)" visibility="hidden"/><circle class="d2" r="4.5" fill="var(--s1)" visibility="hidden"/><rect class="hit" x="${m.l - 4}" y="0" width="${w - m.l - m.r + 8}" height="${h}" fill="transparent"/>`;
  el.innerHTML = `<svg viewBox="0 0 ${w} ${h}" height="${h}" role="img" aria-label="Where holding less equity protected capital and where it cost, by quarter">${g}</svg>`;
  const svg = el.querySelector("svg"), cx = el.querySelector(".cx"), d1 = el.querySelector(".d1"), d2 = el.querySelector(".d2");
  el.querySelector(".hit").addEventListener("pointermove", e => {
    const r = svg.getBoundingClientRect(), px = (e.clientX - r.left) * w / r.width;
    const k = Math.max(0, Math.min(n - 1, Math.round((px - m.l) / (w - m.l - m.r) * (n - 1)))), x = Q[k];
    cx.setAttribute("x1", X_(k)); cx.setAttribute("x2", X_(k)); cx.setAttribute("visibility", "visible");
    d1.setAttribute("cx", X_(k)); d1.setAttribute("cy", YA(x.sp)); d1.setAttribute("visibility", "visible");
    d2.setAttribute("cx", X_(k)); d2.setAttribute("cy", YA(x.rec)); d2.setAttribute("visibility", "visible");
    const c = C.filter(c => Math.abs(c.d) >= 1).find(c => k >= c.a && k <= c.b);
    showTip(e, `<div class="d">${qLab(x.q)}${x.now ? " · current call" : ""}</div><b>${x.equity}% equity · ${100 - x.equity}% ${defName(x)}</b>`
      + (k && !x.now ? `<div>This quarter vs the S&P 500: <b>${dlab(x.d)}</b></div>` : "")
      + (c && Math.abs(c.d) >= 1 ? `<div>Cut ${mlab(c.from)}${c.to !== c.from ? ` to ${mlab(c.to)}` : ""}: ${c.d > 0 ? "protected" : "cost"} <b>${dlab(c.d)}</b> vs the S&P 500</div>` : "")
      + `<div class="d">$100 became: recommended $${Math.round(x.rec).toLocaleString("en-US")}, S&P 500 $${Math.round(x.sp).toLocaleString("en-US")}</div>`);
  });
  el.querySelector(".hit").addEventListener("pointerleave", () => { hideTip(); [cx, d1, d2].forEach(l => l.setAttribute("visibility", "hidden")); });
}

/* ------------------------------------------------------------------ call 2: sectors */
const ACT = {over: ["over", "▲", "Overweight"], under: ["under", "▼", "Underweight"], neutral: ["neutral", "●", "Neutral"]};
function sectorWhy(etf, n, s, high){
  const R = D.meta.rules[s], SR = D.meta.stress_rule, WHY = D.meta.why, t = n.tilt || 0, st = stName(s);
  const inS = R.over.includes(etf) ? 1 : R.under.includes(etf) ? -1 : 0, inX = high ? (SR.over.includes(etf) ? 1 : SR.under.includes(etf) ? -1 : 0) : 0;
  const c = n.if_extreme || n.action;
  if (c === "over" || c === "under") {
    const parts = [];
    if (inS === t) parts.push(WHY[s][etf]);
    if (inX === t && WHY.stress[etf]) parts.push(WHY.stress[etf]);
    return parts.join(" ");
  }
  if (t !== 0) return `The ${st.toLowerCase()} playbook would ${t > 0 ? "favour" : "avoid"} it, but in past ${st.toLowerCase()} periods it did not actually ${t > 0 ? "beat" : "lag"} the other sectors, so no bet.`;
  if (inS !== 0 && inX !== 0 && inS !== inX) return `The ${st.toLowerCase()} playbook and the risk-off playbook point in opposite directions.`;
  return high ? `Neither the ${st.toLowerCase()} playbook nor the risk-off playbook gives it a clear edge right now.` : `The ${st.toLowerCase()} playbook gives it no clear edge right now.`;
}
function renderIndustries(){
  const i = NOW(), s = D.regime[i], high = D.stress_high[i], hz = D.horizons[H], live = D.extreme[i];
  document.querySelectorAll("#horizon button").forEach(b => b.setAttribute("aria-pressed", b.dataset.h === H));
  $("#actHead").textContent = live ? `${stName(s)}${high ? ", markets in risk-off mode" : ""}.` : "On hold: no reading is extreme.";
  $("#actWhy").textContent = live ? `Calls for the next ${H} months, against holding all 20 sectors equally.`
    : `Sector calls only apply when a reading is extreme. Until then all 20 sectors are held equally; these are the calls that would apply.`;
  const rows = D.industries.map(it => { const n = hz.now[it.etf] || {}; const c = live ? n.action : n.if_extreme;
    return {it, n, c, o: c === "over" ? 0 : c === "under" ? 1 : 2}; }).sort((a, b) => a.o - b.o || a.it.name.localeCompare(b.it.name));
  $("#indTable").innerHTML = `<thead><tr><th>Sector</th><th>Call</th><th>Why now</th></tr></thead><tbody>` + rows.map(r => {
    const [cls, ic, tx] = ACT[r.c] || ACT.neutral;
    const pillH = `<span class="pill ${cls}${!live && r.c !== "neutral" ? " hold" : ""}"><span aria-hidden="true">${ic}</span>${tx}${!live && r.c !== "neutral" ? " · on hold" : ""}</span>`;
    return `<tr><td><b>${esc(r.it.name)}</b> <span class="etf muted">${r.it.etf}</span></td><td>${pillH}</td><td class="why">${esc(sectorWhy(r.it.etf, r.n, s, high))}</td></tr>`; }).join("") + "</tbody>";
}

/* ------------------------------------------------------------------ pages */
let PAGE = (location.hash === "#calls" ? "calls" : store.get("mc-p")) || "reading";
function setPage(p){ PAGE = p; store.set("mc-p", p);
  $("#pReading").hidden = p !== "reading"; $("#pCalls").hidden = p !== "calls";
  document.querySelectorAll("#tabs button").forEach(b => b.setAttribute("aria-selected", b.dataset.p === p));
  history.replaceState(null, "", p === "calls" ? "#calls" : location.pathname);
  renderAll(); }
function renderAll(){ if (PAGE === "calls") { renderExposure(); renderIndustries(); } else { renderTop(); renderPoints(); } }
function setH(h){ H = h; store.set("mc-h", h); renderIndustries(); }
async function start(){
  const buf = await (await fetch("/data/data.bin", {cache: "no-cache"})).arrayBuffer();
  D = await openBlob(buf); N = D.months.length;
  $("#lock").hidden = true; $("#shell").hidden = false;
  if (!D.horizons[H]) H = "12";
  document.querySelectorAll("#horizon button").forEach(b => { b.setAttribute("aria-pressed", b.dataset.h === H); b.onclick = () => setH(b.dataset.h); });
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
