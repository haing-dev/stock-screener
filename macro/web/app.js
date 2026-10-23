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
  panel(card.querySelector(".zoom"), ind, Math.max(iFirst, N - 25), {monthly: true, ago, agoI, nt: 3, r: 14});
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
    <div class="ich"><div class="chart long"></div><div class="chart zoom"></div></div>${after}</div>`;
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

/* ------------------------------------------------------------------ call 1: stock exposure (master chart) */
function renderExposure(){
  const X = D.derisk, B = X.backtest, S = D.settings.derisk, i = NOW(), e = X.exposure[i], sh = X.share[i];
  const lo = Math.round(S.band[0] * 100), hi = Math.round(S.band[1] * 100), minS = Math.round(S.min_stocks * 100);
  const ind = IND(), names = X.warnings_now.map(k => ind[k].title);
  $("#xHead").textContent = e >= 100 ? "Hold 100% in stocks" : `Hold ${e}% in stocks and ${100 - e}% in cash`;
  $("#xSub").textContent = `The more of the 28 indicators in sections 1 to 3 sit in their warning zone, the more moves to cash, counting most the indicators that warned best before past falls. `
    + `Nothing moves while fewer than ${lo}% warn; at ${hi}% or more, ${100 - minS}% sits in cash. Now ${Math.round(sh)}% warn${names.length ? ` (${names.slice(0, 6).join(", ")}${names.length > 6 ? " and others" : ""})` : ""}.`;
  const st = B.stats, sp = st.sp500, sr = st.strategy;
  const eps = B.episodes.filter(x => x.diff != null);
  const best = [...eps].sort((a, b) => b.diff - a.diff).slice(0, 2), worst = [...eps].sort((a, b) => a.diff - b.diff).slice(0, 2);
  const yr = x => x.from.slice(0, 4) === x.to.slice(0, 4) ? x.from.slice(0, 4) : `${x.from.slice(0, 4)}–${x.to.slice(2, 4)}`;
  $("#xNote").textContent = `Since ${B.from.slice(0, 4)}: ${pct(sr.cagr, 1)} a year with the rule vs ${pct(sp.cagr, 1)} for the S&P 500, worst fall ${pct(sr.maxdd, 0)} vs ${pct(sp.maxdd, 0)}. `
    + `Biggest bullets dodged: ${best.map(yr).join(" and ")}. Costliest false alarms: ${worst.map(yr).join(" and ")}. `
    + `Cash earns the 3-month US Treasury bill rate. Returns include dividends; no trading costs or taxes.`;
  masterChart($("#xChart"), X, B);
}
function masterChart(el, X, B){
  const w = W(el), narrow = w < 640, m = {l: 42, r: narrow ? 12 : 92, t: 40, b: 22}, h1 = narrow ? 240 : 280, gap = 22, h2 = 74, h = m.t + h1 + gap + h2 + m.b;
  const i0 = D.months.indexOf(B.from), n = N;
  const X_ = i => m.l + (w - m.l - m.r) * (i - i0) / Math.max(1, n - 1 - i0);
  const ddS = B.drawdown.sp500, ddR = B.drawdown.strategy, ex = X.exposure;
  const lo = Math.min(-50, ...ddS.slice(i0).filter(v => v != null)), T = niceTicks(lo, 0, 5);
  const Y1 = v => m.t + h1 * (v - 0) / (T.lo - 0);
  const y2top = m.t + h1 + gap, Y2 = v => y2top + h2 * (100 - v) / 50;
  let g = "";
  // recessions (thin bars above the top lane) + key
  D.recession.forEach((r, i) => { if (r === 1 && i >= i0) g += `<rect x="${X_(i).toFixed(1)}" y="${m.t - 10}" width="${Math.max(1, X_(i + 1) - X_(i)).toFixed(2)}" height="6" fill="var(--rec)"/>`; });
  g += recKey(w - 4, 4) + `<text class="lab" x="${m.l}" y="12">Fall from the previous peak</text>`;
  // big cuts: green = dodged a fall, red = cost money (false alarm or missed rebound)
  const eps = B.episodes.filter(x => x.diff != null && Math.abs(x.diff) >= (narrow ? 8 : 5));
  eps.forEach((x, k) => {
    const a = D.months.indexOf(x.from), b = D.months.indexOf(x.to) + 1, good = x.diff > 0;
    g += `<rect class="ep" data-k="${k}" x="${X_(a)}" y="${m.t}" width="${Math.max(2, X_(b) - X_(a))}" height="${h1}" fill="var(${good ? "--good-bg" : "--bad-bg"})"/>`;
  });
  T.t.forEach(t => { g += `<line x1="${m.l}" x2="${w - m.r}" y1="${Y1(t)}" y2="${Y1(t)}" stroke="var(--grid)"/><text x="${m.l - 6}" y="${Y1(t) + 3.5}" text-anchor="end">${t}%</text>`; });
  let area = `M${X_(i0)} ${Y1(0)}`, line = "";
  for (let i = i0; i < n; i++) { if (ddS[i] != null) area += `L${X_(i).toFixed(1)} ${Y1(ddS[i]).toFixed(1)}`; }
  area += `L${X_(n - 1)} ${Y1(0)}Z`;
  let pen = false;
  for (let i = i0; i < n; i++) { const v = ddR[i]; if (v == null) { pen = false; continue; } line += (pen ? "L" : "M") + X_(i).toFixed(1) + " " + Y1(v).toFixed(1); pen = true; }
  g += `<path d="${area}" fill="var(--axis)" opacity=".55"/><path d="${line}" fill="none" stroke="var(--s1)" stroke-width="1.6"/>`;
  // labels for the big cuts (two rows so they don't collide)
  eps.forEach((x, k) => {
    const a = D.months.indexOf(x.from), b = D.months.indexOf(x.to) + 1, cx = (X_(a) + X_(b)) / 2, good = x.diff > 0;
    const y = Y1(T.lo) - 8 - (k % 3) * 14;
    g += `<text class="eplab ${good ? "pos" : "neg"}" x="${cx}" y="${y}" text-anchor="middle">${narrow ? (good ? "+" : "−") : good ? "Dodged " : "Cost "}${Math.abs(Math.round(x.diff))}%</text>`;
  });
  // end labels
  const [ls, lsi] = lastOf(ddS), [lr, lri] = lastOf(ddR);
  const yS = Y1(ls), yR = Y1(lr), sep = Math.abs(yS - yR) < 13 ? 13 : 0;
  if (!narrow) {
    g += `<text class="lab" x="${w - m.r + 6}" y="${yS + 4 + (yS >= yR ? sep / 2 : -sep / 2)}" style="fill:var(--ink3)">S&P 500</text>`;
    g += `<text class="lab" x="${w - m.r + 6}" y="${yR + 4 + (yR > yS ? sep / 2 : -sep / 2)}" style="fill:var(--s1)">With the rule</text>`;
  } else g += `<text class="lab" x="${w - 4}" y="26" text-anchor="end"><tspan style="fill:var(--s1)">— with the rule</tspan>  <tspan style="fill:var(--ink3)">▮ S&P 500</tspan></text>`;
  // lane 2: share held in stocks
  let ea = `M${X_(i0)} ${Y2(50)}`;
  for (let i = i0; i < n; i++) { const v = ex[i - 1] ?? 100; ea += `L${X_(i).toFixed(1)} ${Y2(v).toFixed(1)}L${X_(i + 1 > n - 1 ? n - 1 : i + 1).toFixed(1)} ${Y2(v).toFixed(1)}`; }
  ea += `L${X_(n - 1)} ${Y2(50)}Z`;
  g += `<path d="${ea}" fill="var(--s1)" opacity=".25"/>`;
  [100, 50].forEach(t => { g += `<line x1="${m.l}" x2="${w - m.r}" y1="${Y2(t)}" y2="${Y2(t)}" stroke="var(--grid)"/><text x="${m.l - 6}" y="${Y2(t) + 3.5}" text-anchor="end">${t}%</text>`; });
  g += `<text class="lab" x="${m.l + 4}" y="${y2top - 4}">Share held in stocks (the rest in cash)</text>`;
  let lastX = -1e9;
  for (let i = i0; i < n; i++) if (D.months[i].endsWith("-01") && +D.months[i].slice(0, 4) % 5 === 0 && X_(i) - lastX > 40) { g += `<text x="${X_(i)}" y="${h - 5}" text-anchor="middle">${D.months[i].slice(0, 4)}</text>`; lastX = X_(i); }
  g += `<line class="cx" x1="0" x2="0" y1="${m.t}" y2="${y2top + h2}" stroke="var(--ink3)" visibility="hidden"/><rect class="hit" x="${m.l}" y="0" width="${w - m.l - m.r}" height="${h}" fill="transparent"/>`;
  el.innerHTML = `<svg viewBox="0 0 ${w} ${h}" height="${h}" role="img" aria-label="S&P 500 falls and the rule's cuts since ${B.from.slice(0, 4)}">${g}</svg>`;
  const hit = el.querySelector(".hit"), cx = el.querySelector(".cx");
  const all = B.episodes;
  hit.addEventListener("pointermove", e => {
    const r = el.querySelector("svg").getBoundingClientRect(), px = (e.clientX - r.left) * w / r.width;
    const i = Math.max(i0, Math.min(n - 1, Math.round(i0 + (px - m.l) / (w - m.l - m.r) * (n - 1 - i0))));
    cx.setAttribute("x1", X_(i)); cx.setAttribute("x2", X_(i)); cx.setAttribute("visibility", "visible");
    const mo = D.months[i], epi = all.find(x => mo >= x.from && mo <= x.to);
    showTip(e, `<div class="d">${mlab(mo)}${D.recession[i] === 1 ? " · US recession" : ""}</div>Fall from peak: S&P 500 <b>${pct(ddS[i], 0)}</b>, with the rule <b>${pct(ddR[i], 0)}</b><br>Held in stocks: <b>${ex[i - 1] ?? 100}%</b>`
      + (epi ? `<div style="margin-top:4px">Cut ${mlab(epi.from)}${epi.to !== epi.from ? ` to ${mlab(epi.to)}` : ""}: S&P 500 ${pct(epi.sp500, 0)}, with the rule ${pct(epi.strategy, 0)} → <b>${epi.diff > 0 ? `dodged ${Math.abs(epi.diff).toFixed(0)}%` : `cost ${Math.abs(epi.diff).toFixed(0)}%`}</b></div>` : ""));
  });
  hit.addEventListener("pointerleave", () => { hideTip(); cx.setAttribute("visibility", "hidden"); });
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
  $("#actHead").textContent = live ? `${stName(s)}${high ? ", markets in risk-off mode" : ""}: what to tilt` : "On hold: no reading is extreme";
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
