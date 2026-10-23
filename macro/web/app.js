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
const supL = t => esc(t).replace(/\b(L12M|L6M|L3M)\b/g, m => m + sup(2));
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
function stripChart(el){
  const i0 = D.months.findIndex(m => m >= "1970-01"), ms = D.months.slice(i0), st = D.regime.slice(i0), rec = D.recession.slice(i0), sh = D.stress_high.slice(i0);
  const w = W(el), h = 62, top = 10, bh = 26, n = ms.length, bw = w / n;
  let g = "";
  rec.forEach((r, i) => { if (r === 1) g += `<rect x="${(i * bw).toFixed(2)}" y="1" width="${(bw + .4).toFixed(2)}" height="6" fill="var(--rec)"/>`; });
  let run = 0;
  for (let i = 1; i <= n; i++) if (i === n || st[i] !== st[run]) {
    if (st[run]) g += `<rect x="${(run * bw).toFixed(2)}" y="${top}" width="${((i - run) * bw + .4).toFixed(2)}" height="${bh}" fill="var(--st-${st[run]})"/>`;
    run = i;
  }
  sh.forEach((x, i) => { if (x) g += `<rect x="${(i * bw).toFixed(2)}" y="${top + bh + 2}" width="${(bw + .4).toFixed(2)}" height="4" fill="var(--stress)"/>`; });
  ms.forEach((m, i) => { if (m.endsWith("-01") && +m.slice(0, 4) % 10 === 0) g += `<text x="${(i * bw).toFixed(1)}" y="${h - 1}">${m.slice(0, 4)}</text>`; });
  g += `<rect class="hit" x="0" y="0" width="${w}" height="${h}" fill="transparent"/>`;
  el.innerHTML = `<svg viewBox="0 0 ${w} ${h}" height="${h}" role="img" aria-label="Economic state each month since 1970">${g}</svg>`;
  el.querySelector(".hit").addEventListener("pointermove", e => {
    const r = el.getBoundingClientRect(), i = Math.max(0, Math.min(n - 1, Math.floor((e.clientX - r.left) / r.width * n)));
    showTip(e, `<div class="d">${mlab(ms[i])}${rec[i] === 1 ? " · recession" : ""}</div><b>${stName(st[i])}</b>${sh[i] ? "<div>Markets in risk-off mode</div>" : ""}`);
  });
  el.querySelector(".hit").addEventListener("pointerleave", hideTip);
}
function renderTop(){
  const i = NOW(), s = D.regime[i], S = sentences(), hz = D.horizons[H];
  let j = i; while (j > 0 && D.regime[j - 1] === s) j--;
  $("#stageDot").style.background = `var(--st-${s})`;
  $("#stageName").textContent = stName(s);
  $("#stageWhy").textContent = `${S.A}. ${S.B}. ${S.C}. Reading since ${mlab(D.months[j])}.`;
  $("#points").innerHTML = ["A", "B", "C"].map(g => `<li><a href="#s${g}"><span class="pn">${GROUPS[g].num}</span><b>${S[g]}</b>${zoneBar(g)}
    ${jumped(g) ? `<span class="jump">Warning signals jumped this month: ${jumped(g).now}, from about ${jumped(g).a6}</span>` : ""}</a></li>`).join("");
  const o = D.industries.filter(it => hz.now[it.etf]?.action === "over"), u = D.industries.filter(it => hz.now[it.etf]?.action === "under");
  const ch = (l, c) => l.map(it => `<span class="chip ${c}">${esc(it.name)}</span>`).join("");
  $("#callSum").innerHTML = `<div class="chips"><span class="lab">Overweight</span>${o.length ? ch(o, "over") : "<span class='muted'>none</span>"}</div>
    <div class="chips"><span class="lab">Underweight</span>${u.length ? ch(u, "under") : "<span class='muted'>none</span>"}</div>
    <a class="more" href="#s4">Next ${H} months · the calls and how they would have traded</a>`;
  $("#stripKey").innerHTML = STATES.map(k => `<span><i style="background:var(--st-${k})"></i>${D.meta.stages[k][0]}</span>`).join("") +
    `<span><i class="str"></i>Risk-off</span><span><i class="rec"></i>US recession</span>`;
  stripChart($("#strip"));
}

/* ------------------------------------------------------------------ indicator: summary sentence + two charts */
function summary(ind){
  const vals = D.values[ind.id], [cur, ci] = lastOf(vals), ago = ci >= 12 ? vals[ci - 12] : null, z = zoneAt(ind.id, NOW());
  const seen = vals.filter(v => v != null).sort((a, b) => a - b), rng = (seen[Math.floor(.95 * (seen.length - 1))] - seen[Math.floor(.05 * (seen.length - 1))]) || 1;
  const d = ago == null ? null : (cur - ago) * ind.dir / rng;
  const cmp = d == null ? "" : Math.abs(d) < 0.05 ? " and little changed from a year ago" : d > 0 ? " and deteriorating compared with a year ago" : " and improving compared with a year ago";
  const zp = {warn: "in the warning zone", normal: "in its normal range", good: "in the supportive zone"}[z] || "without enough history to judge";
  const verb = /(permits|sales|stocks)$/.test(ind.short) ? "are" : "is";
  return `${esc(ind.what)}. At ${fmtV(cur, ind, hasNeg(ind.id))}${esc(ind.vp)}, ${esc(ind.short)} ${verb} ${zp}${sup(1)}${cmp}, indicating ${esc(ind.means[z] || "no clear signal")}.`;
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
    if (opt.zoneLabel) g += `<text class="zl" x="${m.l + 6}" y="${ind.dir > 0 ? Math.max(m.t + 11, y - 5) : Math.min(h - m.b - 4, y + 13)}">Warning zone: ${ind.dir > 0 ? "above" : "below"} ${tickLab(wv, ind, ind.dp)}</text>`; }
  D.recession.forEach((r, i) => { if (r === 1 && i >= i0) g += `<rect x="${X(i).toFixed(1)}" y="${m.t}" width="${Math.max(1, X(i + 1) - X(i)).toFixed(2)}" height="${h - m.t - m.b}" fill="var(--rec)"/>`; });
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
  panel(card.querySelector(".long"), ind, iFirst, {clip: true});
  panel(card.querySelector(".zoom"), ind, Math.max(iFirst, N - 25), {monthly: true, ago, agoI, nt: 3, r: 14});
}
function indCard(ind, num){
  const v = D.ind_view[ind.id], z = zoneAt(ind.id, NOW()), vals = D.values[ind.id];
  const first = D.months[Math.max(D.months.findIndex(x => x >= "1970-01"), vals.findIndex(x => x != null))];
  let after = "";
  const hist = v && v.hist[H];
  if (hist && hist.length >= 4) {
    const f = r => `<span class="chip ${r[1] >= 0 ? "over" : "under"}" title="beat the S&P 500 in ${r[2]}% of those months">${esc(NAME()[r[0]])} ${pct(r[1], 1)}</span>`;
    after = `<div class="after"><span class="muted">Sectors after past readings in this zone, next ${H} months vs S&P 500${sup(4)}</span>
      <div class="chips"><span class="lab">Best</span>${hist.slice(0, 3).map(f).join("")}<span class="lab sp">Worst</span>${hist.slice(-3).reverse().map(f).join("")}</div></div>`;
  }
  return `<div class="icard z-${z}" data-id="${ind.id}"><div class="ihd"><span class="inum">${num}</span><b>${supL(ind.title)}</b><span class="tag ${z}">${ZW[z]}</span></div>
    <p class="isum">${summary(ind)}</p>
    <div class="ich"><div><div class="cap">Since ${first.slice(0, 4)}${sup(3)}${v && v.warn != null ? ` · <span class="wz">red band = warning zone, ${ind.dir > 0 ? "above" : "below"} ${fmtV(v.warn, ind, hasNeg(ind.id))}</span>` : ""}</div><div class="chart long"></div></div><div><div class="cap">Last 2 years</div><div class="chart zoom"></div></div></div>${after}</div>`;
}
const ZORDER = {warn: 0, good: 1, normal: 2, "": 3};
function footnotes(extra){
  const L = [
    "Warning zone (red band): the worst third of the indicator's own readings since its data begin; supportive zone: the best third; normal: the middle third.",
    "L12M, L6M, L3M: last 12, 6 or 3 months. \"vs L12M\" is the change from the same month a year earlier; \"L6M return\" is the return over the last 6 months.",
    "Grey bands: US recessions (National Bureau of Economic Research).",
    "Average return vs the S&P 500 in all past months when this indicator was in the same zone as now; sector indexes stand in before each ETF existed.",
  ].concat(extra || []);
  return `<ol class="fns">${L.map(t => `<li>${t}</li>`).join("")}</ol>`;
}
function renderPoint(g, sec, title){
  const inds = groupInds(g).map((x, k) => [x, `${GROUPS[g].num}.${k + 1}`]), show = inds;
  const j = g === "A" ? jumped(g) : null;
  const extra = g === "A" ? [`The economy reading uses 6-month averages of these signals and changes only after 3 months in a row.${j ? ` This month ${j.now} signals are in the warning zone, up from about ${j.a6} on average over the previous 6 months; if that persists, the reading will turn.` : ""}`]
    : g === "B" ? ["Inflation counts as running hot when these signals, averaged over 6 months, sit clearly toward the high end of their history."]
    : g === "C" ? ["Risk-off mode starts when these signals on average are deep in their worst third of history, and ends once they ease back."]
    : ["Shown for context only. Adding these signals to the reading made past calls worse, so they do not affect the calls."];
  sec.innerHTML = `${title ? `<div class="step">${GROUPS[g].step}</div><h2>${esc(title)}${sup(5)}</h2>` : ""}${zoneBar(g, 1)}
    <div class="ilist">${show.map(([x, k]) => indCard(x, k)).join("")}</div>
    ${footnotes(extra)}`;
  sec.querySelectorAll(".icard").forEach(drawInd);
}
function renderPoints(){
  const S = sentences();
  renderPoint("A", $("#sA"), S.A); renderPoint("B", $("#sB"), S.B); renderPoint("C", $("#sC"), S.C);
  renderPoint("D", $("#bgBody"), "");
}

/* ------------------------------------------------------------------ what to do */
const ACT = {over: ["over", "▲", "Overweight"], under: ["under", "▼", "Underweight"], neutral: ["neutral", "●", "Neutral"]};
const pill = a => { const [c, i, t] = ACT[a] || ACT.neutral; return `<span class="pill ${c}"><span aria-hidden="true">${i}</span>${t}</span>`; };
function renderIndustries(){
  const i = NOW(), s = D.regime[i], high = D.stress_high[i], hz = D.horizons[H];
  const r = D.meta.rules[s];
  $("#actHead").textContent = `${stName(s)}${high ? " in risk-off mode" : ""}: what this has meant for sectors`;
  $("#actWhy").innerHTML = `<b>The logic:</b> ${esc(r.why)}${high ? ` <b>Risk-off:</b> ${esc(D.meta.stress_rule.why)}` : ""} <b>The check:</b> a sector is only overweighted or underweighted if it actually beat or lagged the S&P 500 on average over the next ${H} months in past months like now. Otherwise it stays neutral.`;
  const rows = D.industries.map(it => { const n = hz.now[it.etf] || {}; const t = n.tilt || 0;
    const g = n.action === "over" ? 0 : n.action === "under" ? 1 : t !== 0 ? 2 : 3; return {it, n, t, g}; });
  const G = ["Overweight", "Underweight", "The logic says yes, history says no: neutral", "Neutral"];
  let html = `<thead><tr><th>Sector</th><th>Call</th><th>The logic</th><th class="r">Past months like now (${esc(stName(s))}, ${high ? "risk-off" : "no risk-off"}):<br>avg vs S&P 500, next ${H} months</th><th class="r">Beat the S&P 500<br>in</th></tr></thead><tbody>`;
  [0, 1, 2, 3].forEach(gi => {
    const sg = gi === 1 ? -1 : 1;
    const g = rows.filter(x => x.g === gi).sort((a, b) => sg * ((b.n.mean_rel ?? -99) - (a.n.mean_rel ?? -99))); if (!g.length) return;
    html += `<tr class="grp"><td colspan="5">${G[gi]}</td></tr>`;
    g.forEach(x => {
      const n = x.n, open = OPEN.has("i-" + x.it.etf);
      const say = x.t > 0 ? `<span class="chip over">Favoured</span>` : x.t < 0 ? `<span class="chip under">Avoided</span>` : `<span class="muted">No view</span>`;
      html += `<tr class="irow2" tabindex="0" data-e="${x.it.etf}" aria-expanded="${open}"><td><b>${esc(x.it.name)}</b> <span class="etf muted">${x.it.etf}</span></td><td>${pill(n.action)}</td><td>${say}</td>
        <td class="r num"><b class="${n.mean_rel > 0 ? "pos" : n.mean_rel < 0 ? "neg" : ""}">${n.mean_rel == null ? "–" : pct(n.mean_rel, 1)}</b>${n.n ? ` <span class="muted">(${n.n} months)</span>` : ""}</td>
        <td class="r num">${n.pos == null ? "–" : n.pos + "%"}</td></tr>`;
      if (open) html += `<tr class="idetail"><td colspan="5">${detailHTML(x.it)}</td></tr>`;
    });
  });
  $("#indTable").innerHTML = html + "</tbody>";
  document.querySelectorAll("tr.irow2").forEach(tr => { const t = () => { const k = "i-" + tr.dataset.e; OPEN.has(k) ? OPEN.delete(k) : OPEN.add(k); renderIndustries(); };
    tr.onclick = t; tr.onkeydown = e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); t(); } }; });
  D.industries.forEach(it => { const el = document.getElementById("rel-" + it.etf); if (el) relChart(el, it); });
  renderTrade();
  renderHeat();
}
function detailHTML(it){
  return `<h4>${esc(it.name)} (${it.etf}) vs the S&P 500, last 15 years</h4><div class="legend"><span><i style="background:var(--good-bg);height:10px"></i>Overweight call</span><span><i style="background:var(--bad-bg);height:10px"></i>Underweight call</span></div><div class="chart" id="rel-${it.etf}"></div>
    <p class="muted" style="font-size:12.5px;margin:6px 0 0">Line rising = beating the market. ${it.etf_from ? `${it.etf} trades from ${mlab(it.etf_from)}; before that, its industry index.` : ""}</p>`;
}
function relChart(el, it){
  const i0 = Math.max(0, N - 180), base = it.rel_level[i0] || lastOf(it.rel_level.slice(0, i0 + 1))[0];
  const v = it.rel_level.map((x, i) => i < i0 || x == null || !base ? null : 100 * x / base);
  const acts = D.horizons[H].actions[it.etf], bands = [];
  let s = null;
  for (let i = i0; i <= N; i++) { const a = i < N ? acts[i] : null;
    if (s && (a !== s.a)) { bands.push({i0: s.i, i1: i - 1, c: s.a === "over" ? "var(--good-bg)" : "var(--bad-bg)"}); s = null; }
    if (!s && (a === "over" || a === "under")) s = {a, i}; }
  lineChart(el, [{name: `${it.etf} vs S&P 500`, v, c: "var(--ink2)", wd: 1.6}], D.months, {h: 190, bands, ticks: [50, 75, 100, 125, 150, 200, 300], fmt: x => x.toFixed(0),
    tipExtra: i => ` · ${stName(D.regime[i])}${acts[i] && acts[i] !== "neutral" ? ` · ${ACT[acts[i]][2]}` : ""}`, aria: `${it.name} relative to the S&P 500`});
}
function renderHeat(){
  const T = D.state_table[H], now = D.regime[NOW()], high = D.stress_high[NOW()];
  const cols = [...STATES, "stress"], lab = k => k === "stress" ? "Risk-off" : D.meta.stages[k][0];
  $("#heatHead").textContent = "Every state, every sector";
  $("#heatSub").textContent = `Average return vs the S&P 500 over the next ${H} months, in all past months of each state since 1960 (number of months in brackets). Green = beat the market, red = lagged. Industry indexes stand in before each ETF existed.`;
  const cell = c => { if (!c) return `<td class="r muted">–</td>`; const a = Math.min(1, Math.abs(c[0]) / 10);
    return `<td class="r num" style="background:color-mix(in srgb, var(${c[0] >= 0 ? "--good" : "--bad"}) ${Math.round(a * 32)}%, transparent)" title="beat the S&P 500 in ${c[1]}% of ${c[2]} months">${pct(c[0], 1)}</td>`; };
  $("#heat").innerHTML = `<thead><tr><th>Sector</th>${cols.map(k => `<th class="r${k === now || (k === "stress" && high) ? " nowc" : ""}">${lab(k)}${k === now || (k === "stress" && high) ? "<br>(now)" : ""}<br><span class="muted">(${T[k].n})</span></th>`).join("")}</tr></thead><tbody>` +
    D.industries.map(it => `<tr><td><b>${esc(it.name)}</b> <span class="etf muted">${it.etf}</span></td>${cols.map(k => cell(T[k].etf[it.etf])).join("")}</tr>`).join("") + "</tbody>";
}


/* ------------------------------------------------------------------ trade test: every past entry into today's situation */
const k$ = v => v == null ? "–" : `$${Math.round(v / 1000)}k`;
let TRADE = null;
function renderTrade(){
  const i = NOW(), s = D.regime[i], high = D.stress_high[i], E = D.horizons[H].entries || [];
  const sit = `${stName(s)}${high ? " with markets in risk-off mode" : ", markets not in risk-off mode"}`;
  const names = l => l.map(e => esc(NAME()[e])).join(", ") || "none";
  const past = E.slice(0, -1), cur = E[E.length - 1], traded = past.filter(e => e.result && e.result["12"]);
  const beat = (hh, k) => traded.filter(e => e.result[hh]).filter(e => e.result[hh][k] != null && e.result[hh][k] > e.result[hh].sp500).length;
  const nh = hh => traded.filter(e => e.result[hh]).length;
  $("#tradeHead").textContent = `How the calls would have traded: every past entry into ${sit}`;
  $("#tradeSub").innerHTML = `Entry: the end of the month the economy entered this situation. $100,000 goes into that month's calls: <b>long/short</b> = equal amounts bought in each overweight and sold short in each underweight, no leverage (total exposure $100,000); <b>long only</b> = $100,000 split equally across the overweights. Compared with $100,000 in the S&P 500 on the same day; all held without changes${sup(1)}.`;
  const curLine = cur && cur.path ? (() => { const p = cur.path, k = p.long_short.length - 1;
    return `<div><h3>Current entry: ${mlab(cur.month)}</h3><p>Long ${names(cur.over)}. Short ${names(cur.under)}.</p>
      <p>After ${k} month${k === 1 ? "" : "s"}: long/short <b>${k$(p.long_short[k])}</b>, long only <b>${k$(p.long_only[k])}</b>, S&P 500 <b>${k$(p.sp500[k])}</b>.</p></div>`; })()
    : `<div><h3>Current entry: ${cur ? mlab(cur.month) : "–"}</h3><p>No calls in this situation.</p></div>`;
  $("#tradeNow").innerHTML = curLine + (traded.length ? `<div class="tsum">${["12", "24", "36"].filter(nh).map(hh =>
    `<div><b>After ${+hh / 12} year${hh === "12" ? "" : "s"}</b><span>Long/short beat the S&P 500 in ${beat(hh, "long_short")} of ${nh(hh)} entries; long only in ${beat(hh, "long_only")} of ${nh(hh)}</span></div>`).join("")}</div>` : "");
  const cell = (r, k) => r ? `<td class="r num ${r[k] != null && r[k] > r.sp500 ? "pos" : r[k] != null && r[k] < r.sp500 ? "neg" : ""}">${k$(r[k])}</td>` : `<td class="r muted">–</td>`;
  const yrs = ["12", "24", "36"];
  $("#tradeTable").innerHTML = `<thead><tr><th rowspan="2">Entry</th><th rowspan="2">Calls made then</th>${yrs.map(hh => `<th colspan="3" class="c">After ${+hh / 12} year${hh === "12" ? "" : "s"}</th>`).join("")}</tr>
    <tr>${yrs.map(() => `<th class="r">Long/short</th><th class="r">Long only</th><th class="r">S&P 500</th>`).join("")}</tr></thead><tbody>` +
    E.map((e, k) => `<tr class="${e.path ? "trow" : ""}${TRADE === k ? " sel" : ""}" data-k="${k}" ${e.path ? 'tabindex="0"' : ""}><td><b>${mlab(e.month)}</b>${k === E.length - 1 ? " <span class='muted'>(now)</span>" : ""}${e.index_data ? sup(2) : ""}</td>
      <td class="calls">${e.over.length || e.under.length ? `<span class="pos">Long</span> ${names(e.over)}<br><span class="neg">Short</span> ${names(e.under)}` : `<span class="muted">No calls: too little history at the time</span>`}</td>
      ${yrs.map(hh => { const r = e.result && e.result[hh]; return r ? cell(r, "long_short") + cell(r, "long_only") + `<td class="r num">${k$(r.sp500)}</td>` : `<td class="r muted" colspan="3">${e.path ? "not yet" : ""}</td>`; }).join("")}</tr>`).join("") + "</tbody>";
  const rows = [...document.querySelectorAll("#tradeTable tr.trow")];
  rows.forEach(tr => { const t = () => { TRADE = +tr.dataset.k; renderTrade(); };
    tr.onclick = t; tr.onkeydown = e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); t(); } }; });
  if (TRADE == null || !E[TRADE] || !E[TRADE].path) { const withPath = E.map((e, k) => [e, k]).filter(([e]) => e.path && e.result && e.result["12"]); TRADE = withPath.length ? withPath[withPath.length - 1][1] : null; }
  const e = TRADE != null ? E[TRADE] : null;
  if (!e) { $("#tradeChartBox").hidden = true; return; }
  $("#tradeChartBox").hidden = false;
  document.querySelectorAll("#tradeTable tr.trow").forEach(tr => tr.classList.toggle("sel", +tr.dataset.k === TRADE));
  const i0 = D.months.indexOf(e.month), months = D.months.slice(i0, i0 + e.path.sp500.length);
  const C = [["long_short", "Long/short", "var(--s1)"], ["long_only", "Long only", "var(--st-stagflation)"], ["sp500", "S&P 500", "var(--s3)"]];
  $("#tradeLegend").innerHTML = `<b>$100,000 from ${mlab(e.month)}</b>` + C.map(([k, n, c]) => `<span><i style="background:${c}"></i>${n}</span>`).join("") + `<span class="muted">Tap a row to switch</span>`;
  const ser = C.filter(([k]) => e.path[k].some(x => x != null)).map(([k, n, c]) => ({name: n, v: e.path[k], c, wd: k === "long_short" ? 2.4 : 1.6, endLabel: v => k$(v)}));
  const nt = niceTicks(Math.min(...ser.flatMap(s => s.v.filter(x => x != null))), Math.max(...ser.flatMap(s => s.v.filter(x => x != null))), 4);
  lineChart($("#tradeChart"), ser, months, {h: 230, base: 100000, ticks: nt.t, fmtTick: t => k$(t), fmt: v => `$${Math.round(v).toLocaleString("en-US")}`, aria: "Value of $100,000 after entry"});
}

/* ------------------------------------------------------------------ track record */
function renderBacktest(){
  const hz = D.horizons[H], bt = hz.backtest.etf, st = bt.stats, lg = hz.backtest.long.stats;
  const diff = st.compass && st.equal ? st.compass.cagr - st.equal.cagr : 0;
  $("#btHead").textContent = Math.abs(diff) < 0.5 ? "So far the calls have made little difference to returns"
    : diff > 0 ? `The calls added ${diff.toFixed(1)}% a year vs holding all 20 sectors equally` : `The calls cost ${Math.abs(diff).toFixed(1)}% a year vs holding all 20 sectors equally`;
  $("#btSub").textContent = `$100 invested in ${mlab(st.compass.from)} in the 20 sector ETFs, rebalanced monthly: equal amounts, or 1.5× in overweights and 0.5× in underweights using that month's ${H}-month calls and only data available at the time.`;
  const C = {compass: ["With the calls", "var(--s1)"], equal: ["All 20 sectors, equal amounts", "var(--s2)"], market: ["S&P 500", "var(--s3)"]};
  $("#btLegend").innerHTML = Object.entries(C).map(([k, [n, c]]) => `<span><i style="background:${c}"></i>${n}</span>`).join("");
  lineChart($("#btChart"), Object.entries(C).filter(([k]) => bt.curves[k]).map(([k, [n, c]]) => ({name: n, v: bt.curves[k].map(x => x == null ? null : 100 * x), c,
    wd: k === "compass" ? 2.4 : 1.6, endLabel: v => `$${Math.round(v)}`})), D.months, {log: true, ticks: [100, 200, 300, 400, 600, 800, 1000], fmtTick: t => `$${t}`, fmt: v => `$${Math.round(v)}`, aria: "Growth of $100"});
  const Rw = [["compass", "With the calls"], ["investor", "The logic alone (no history check)"], ["equal", "Equal amounts"], ["momentum", "Last year's best sectors"], ["trend", "Sectors above their 10-month average"], ["market", "S&P 500"]];
  $("#btStats").innerHTML = `<thead><tr><th>Since ${st.compass.from.slice(0, 4)}</th><th>Per year</th><th>Worst fall</th></tr></thead><tbody>` +
    Rw.map(([k, n]) => st[k] ? `<tr class="${k === "compass" ? "me" : ""}"><td>${n}</td><td>${pct(st[k].cagr, 1)}</td><td>${pct(st[k].maxdd, 0)}</td></tr>` : "").join("") +
    (lg.compass && lg.equal ? `<tr><td colspan="3" style="font-size:12px;color:var(--ink3);text-align:left;padding-top:10px">Same test on industry indexes since ${lg.compass.from.slice(0, 4)}: ${pct(lg.compass.cagr, 1)} a year with the calls vs ${pct(lg.equal.cagr, 1)} equal amounts.</td></tr>` : "") + "</tbody>";
  const L = D.live, sc = L && L.scored && L.scored[H];
  $("#liveBox").innerHTML = !L || !L.rows ? `<div><h3>Live record</h3><p>Each month's reading and calls are saved permanently once the month ends, starting October 2026, so they can't be changed later. First results: 6-month calls in April 2027, 12-month calls in October 2027.</p></div>`
    : `<div><h3>Live record since ${mlab(L.first)}</h3><p>${sc && (sc.over.calls + sc.under.calls) ? `Underweights lagged the market in ${sc.under.hit ?? "–"}% of ${sc.under.calls} cases; overweights beat it in ${sc.over.hit ?? "–"}% of ${sc.over.calls}.` : "No call has reached its end date yet."} ${sc ? `${sc.pending} calls still running.` : ""}</p></div>`;
}

/* ------------------------------------------------------------------ how it works */
function renderHow(){
  const S = D.settings;
  const rr = STATES.map(k => { const r = D.meta.rules[k]; const n = e => esc(NAME()[e]);
    return `<tr><td><b>${D.meta.stages[k][0]}</b><div class="muted">${esc(D.meta.stages[k][1])}</div></td><td>${r.over.map(n).join(", ")}</td><td>${r.under.map(n).join(", ")}</td><td>${esc(r.why)}</td></tr>`; }).join("") +
    `<tr><td><b>Risk-off</b><div class="muted">Added on top of any state.</div></td><td>${D.meta.stress_rule.over.map(e => esc(NAME()[e])).join(", ")}</td><td>${D.meta.stress_rule.under.map(e => esc(NAME()[e])).join(", ")}</td><td>${esc(D.meta.stress_rule.why)}</td></tr>`;
  $("#how").innerHTML = `<ol>
    <li><b>${D.meta.indicators.length} signals</b> that experienced macro investors watch, from public data (Federal Reserve, Labor Department, market prices). Economic data enter only once they were published.</li>
    <li><b>Each signal is compared with its own history</b>: its worst third of readings is the warning zone, its best third supportive.</li>
    <li><b>The economy:</b> growth data plus market signals, averaged over 6 months. Weak and worsening = Contraction, weak and improving = Recovery, strong and improving = Expansion, strong and worsening = Late cycle. A change needs 3 months in a row.</li>
    <li><b>Inflation running hot</b> turns Expansion and Late cycle into Overheating, and Contraction into Stagflation. <b>Market stress</b> adds a risk-off layer.</li>
    <li><b>Each state has a sector playbook</b> (below), taken from how experienced investors position through the cycle. A sector is only called if past months like now agree. Each month uses only data known then.</li></ol>
    <div class="tablewrap"><table><thead><tr><th>State</th><th>Favoured</th><th>Avoided</th><th>Why</th></tr></thead><tbody>${rr}</tbody></table></div>
    <p class="muted" style="font-size:12.5px;margin:0">Data: FRED (St. Louis Fed)${D.fred_key ? ", as first published" : ""}, Kenneth French data library, Yahoo Finance, multpl.com. Version ${D.version}. Not investment advice.</p>`;
}

function renderAll(){ renderTop(); renderPoints(); renderIndustries(); renderBacktest(); renderHow(); }
function setH(h){ H = h; store.set("mc-h", h); document.querySelectorAll("#horizon button").forEach(b => b.setAttribute("aria-pressed", b.dataset.h === H));
  renderTop(); renderPoints(); renderIndustries(); renderBacktest(); }
async function start(){
  const buf = await (await fetch("/data/data.bin", {cache: "no-cache"})).arrayBuffer();
  D = await openBlob(buf); N = D.months.length;
  $("#lock").hidden = true; $("#shell").hidden = false;
  if (!D.horizons[H]) H = "12";
  document.querySelectorAll("#horizon button").forEach(b => { b.setAttribute("aria-pressed", b.dataset.h === H); b.onclick = () => setH(b.dataset.h); });
  $("#foot").textContent = `Reading as of ${mlab(D.asof)} · updated ${D.updated} · version ${D.version}. Not investment advice.`;
  renderAll();
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
