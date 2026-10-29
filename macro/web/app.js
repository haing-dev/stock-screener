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

/* ------------------------------------------------------------------ the analysis: action first, then the story */
const GTXT = {
  A: {name: "The economy", desc: "how fast the US economy is growing, from jobs and housing to what the stock market's own sectors signal",
      lv: [["The economy looks healthy", "growth is holding up"], ["The economy is sending mixed signals", "growth is uneven, with some parts slowing while others hold up"], ["Most economic signals are flashing warnings", "the economy is losing momentum"]]},
  B: {name: "Inflation", desc: "how fast prices are rising, from consumer and producer prices to inflation expectations and commodities",
      lv: [["Inflation is under control", "price pressures are contained"], ["Inflation pressure is building in places", "some price measures are running hot"], ["Inflation pressure is high", "prices are rising fast enough to keep the Fed on guard"]]},
  C: {name: "Market stress", desc: "how nervous financial markets are, from volatility and credit to the dollar and bank stocks",
      lv: [["Markets are calm", "investors are comfortable taking risk"], ["Markets show pockets of stress", "parts of the market are nervous"], ["Markets are under stress", "investors are pulling back from risk"]]},
};
const coreOf = g => groupInds(g).filter(x => D.derisk.core.includes(x.id));
function zc(ids, i){ const z = ids.map(id => zoneAt(id, i)); return {warn: z.filter(x => x === "warn").length, n: z.filter(Boolean).length}; }
function gstat(g){ const ids = coreOf(g).map(x => x.id), now = zc(ids, NOW()), ago = zc(ids, NOW() - 12), f = now.warn / Math.max(1, now.n);
  const [t, m] = GTXT[g].lv[f >= 0.5 ? 2 : f >= 0.25 ? 1 : 0]; return {t, m, now, ago}; }
const p1 = v => v == null ? "–" : `${v.toFixed(1)}%`, p2 = v => v == null ? "–" : `${v.toFixed(2)}%`;
const names = list => list.length <= 1 ? list.join("") : list.slice(0, -1).join(", ") + " and " + list[list.length - 1];
const lc = s => s.charAt(0).toLowerCase() + s.slice(1);
function facts(){
  const X = D.derisk, S = X.series, i = NOW(), al = X.alloc, T = X.tilt;
  const lead = T ? D.industries.map(it => ({n: it.name, a: T.actions[it.etf][i], v: T.mom_now[it.etf]})).filter(r => r.v != null).sort((a, b) => b.v - a.v) : [];
  return {i, e: X.exposure[i], eq: al.equity[i], com: al.commodities[i], bond: al.bond[i], cash: Math.max(0, al.cash[i]),
    share: X.share[i], fed: X.fed_gate[i], ff: S.fed_funds[i], trig: S.fed_trigger[i], ff12: S.fed_funds[i - 12],
    gc: X.growth_cut[i], gap: D.values.spx_trend[i], gap12: D.values.spx_trend[i - 12], un: S.unemp[i], ua: S.unemp_avg[i], un12: S.unemp[i - 12],
    corr: D.values.stockbond[i], corr12: D.values.stockbond[i - 12], con: X.commod_on[i], c12: S.commod_12m[i],
    cgap: S.commod[i] / S.commod_ma[i] * 100 - 100, full: X.fully_invested[i],
    top: lead.filter(r => r.a === "over").map(r => r.n), bot: lead.filter(r => r.a === "under").map(r => r.n), lead,
    core: X.core.length, warn: zc(X.core, i).warn, warn12: zc(X.core, i - 12).warn};
}
function renderTop(){
  const F = facts(), G = {A: gstat("A"), B: gstat("B"), C: gstat("C")};
  const extra = F.com > 0 ? ` and ${F.com}% in commodities` : "";
  $("#actTitle").textContent = F.e >= 100 ? `Stay invested: hold ${F.eq}% in stocks${extra}`
    : F.gc ? `Cut stocks to ${F.eq}%: the market and the job market are turning down together`
    : `Reduce stocks to ${F.eq}%: warnings are high while the Fed is tightening`;
  $("#actSub").textContent = `Reading as of ${mlab(D.months[F.i])}. The portfolio is set once a month from the eight areas of evidence below.`;
  $("#mixStats").innerHTML = [["key", F.eq, "in US stocks"], ["", F.com, "in commodities"], ["", F.bond, "in long Treasuries"], ["", F.cash, "in cash"]]
    .map(([k, v, l]) => `<div class="stat ${k}"><b>${v}%</b><span>${l}</span></div>`).join("");
  const lvl = F.warn / F.core >= 0.5 ? "bright" : F.warn / F.core >= 0.25 ? "mixed" : "mostly off";
  const items = [
    {b: `Warning lights are ${lvl}: ${F.warn} of ${F.core} signals are in their danger zone`,
     p: `${G.A.m.charAt(0).toUpperCase() + G.A.m.slice(1)}; ${G.B.m}; and ${G.C.m}. A year ago ${F.warn12} signals were warning.`, see: ["#s1", "Sections 1–3"]},
    {b: F.fed ? "And the Fed is tightening, so these warnings count" : "But warnings only count when the Fed is tightening, and it is not",
     p: F.fed ? `The Fed funds rate is ${p2(F.ff)}, above its tightening line of ${p2(F.trig)}. When the Fed squeezes the economy, warnings like these have often come before big falls, so the rule acts on them.`
       : `The Fed funds rate is ${p2(F.ff)}, below its tightening line of ${p2(F.trig)}. Without the Fed squeezing the economy, warnings like these have more often been false alarms than the start of a bear market.`, see: ["#s4", "Section 4"]},
    {b: F.gc ? "And both signs of a real downturn are on" : "There is no sign of an actual downturn",
     p: `The S&P 500 is ${pct(F.gap, 1)} ${F.gap >= 0 ? "above" : "below"} its 10-month trend, and unemployment (${p1(F.un)}) is ${F.un > F.ua ? "above" : "below"} its 12-month average (${p2(F.ua)}). ${F.gc ? "Together these have marked the start of most recession bear markets, so stocks are cut." : "A cut needs both to turn at the same time."}`, see: ["#s5", "Section 5"]},
    {b: F.e >= 100 ? "So stocks stay at full weight, with two adjustments" : `So stocks are cut to ${F.eq}%`,
     p: (F.con ? `Commodities are trending up (${pct(F.c12, 0)} over 12 months), which earns them ${F.com}% of the portfolio. ` : "Commodities are not trending up, so none are held. ")
       + (F.full ? `Within stocks, the rule leans toward the five strongest sectors of the past year: ${names(F.top.map(lc))}.` : "Sector tilts are paused while stocks are reduced."), see: ["#s7", "Sections 7–8"]},
    {b: F.corr < 0 ? "If the picture turns, long Treasuries are the cushion" : "If the picture turns, cash is the cushion",
     p: F.corr < 0 ? `Stocks and bonds currently move in opposite directions (correlation ${F.corr.toFixed(2)}), so a downturn-driven cut would go into long Treasuries, which tend to rise when stocks fall.`
       : `Stocks and bonds currently move together (correlation ${F.corr.toFixed(2)}), so bonds would not protect a fall; any cut would go to cash.`, see: ["#s6", "Section 6"]},
  ];
  $("#story").innerHTML = items.map(x => `<li><div><b>${esc(x.b)}</b><p>${esc(x.p)}</p><a class="see" href="${x.see[0]}">${x.see[1]} →</a></div></li>`).join("");
}
const runs = flags => { const out = []; let s0 = null; flags.forEach((f, i) => { if (f && s0 == null) s0 = i; if ((!f || i === flags.length - 1) && s0 != null) { out.push({i0: s0, i1: f ? i : i - 1}); s0 = null; } }); return out; };
const from = y => Math.max(0, D.months.findIndex(m => m >= y));
function head(k, title, lead){ return `<div class="snum">${k}</div><h2>${esc(title)}</h2><hr class="keyline"><p class="lead">${esc(lead)}</p>`; }
function cblock(num, title, metric, sentence, status){
  return `<div class="icard"><div class="ihd"><span class="inum">${num}</span><b>${esc(title)}</b>${status ? `<span class="tag ${status[0]}">${status[1]}</span>` : ""}</div>
    <p class="isum">${esc(sentence)}</p><div class="metric">${esc(metric)}</div><div class="chart"></div></div>`;
}
function renderPoints(){
  const X = D.derisk, S = X.series, F = facts(), i0 = from(X.backtest.from), M = D.months, i = F.i;
  // 1-3: the three groups of warning signals
  ["A", "B", "C"].forEach((g, k) => {
    const st = gstat(g), inds = coreOf(g), sec = $(`#s${k + 1}`);
    sec.innerHTML = head(k + 1, `${st.t}: ${st.now.warn} of ${st.now.n} signals warn`,
      `This section tracks ${GTXT[g].desc}. ${st.now.warn} of its ${st.now.n} signals are in their warning zone, versus ${st.ago.warn} a year ago, meaning ${st.m}. These warnings move the portfolio only while the Fed is tightening (section 4).`)
      + `<div class="ilist">${inds.map((x, j) => indCard(x, `${k + 1}.${j + 1}`)).join("")}</div>`;
    sec.querySelectorAll(".icard").forEach(drawInd);
  });
  // 4: the Fed
  $("#s4").innerHTML = head(4, F.fed ? "The Fed is tightening, so the warnings above cut stocks" : "The Fed is not tightening, so the warnings above do not cut stocks",
    `Warning signals have come before big stock falls mainly when the Fed was raising rates to slow the economy, so the rule acts on them only while the Fed funds rate is at least 1 point above its lowest level of the past two years. Today the rate is ${p2(F.ff)} against a tightening line of ${p2(F.trig)}, meaning ${F.fed ? "the Fed is squeezing the economy and the warnings count" : "the Fed is not squeezing the economy, so the warnings are noted but not acted on"}.`)
    + `<div class="ilist one">${cblock("4.1", "Fed funds rate vs the tightening line", "%, monthly; line = lowest rate of the past 24 months + 1 point; shaded = tightening",
      `This chart measures the Fed's policy rate against its tightening line. It is currently ${p2(F.ff)}, versus ${p2(F.ff12)} a year ago and a line at ${p2(F.trig)}, meaning ${F.fed ? "rates are high enough above their recent low to count as tightening" : "rates are not far enough above their recent low to count as tightening"}.`,
      F.fed ? ["warn", "Tightening"] : ["good", "Not tightening"])}</div>`;
  lineChart($("#s4 .chart"), [{v: S.fed_funds, c: "var(--s1)", name: "Fed funds rate", endLabel: v => p2(v)},
    {v: S.fed_trigger, c: "var(--g-mid)", wd: 1.2, name: "Tightening line", endLabel: v => p2(v)}], M,
    {i0, rec: true, fmt: p2, fmtTick: t => `${t}%`, base: 0, bands: runs(X.fed_gate).map(r => ({...r, c: "var(--bad-bg)"})), aria: "Fed funds"});
  // 5: growth and trend
  const two = (F.gap < 0) + (F.un > F.ua);
  $("#s5").innerHTML = head(5, F.gc ? "A downturn is under way: stocks are below trend and unemployment is rising" : two === 1 ? "One of the two downturn signs is on; a cut needs both" : "There is no sign of a downturn: stocks are above trend and unemployment is not rising",
    `Regardless of the Fed, the rule moves out of stocks when two things happen together: the S&P 500 falls below its 10-month average and unemployment rises above its 12-month average. Together they marked the start of the 2001 and 2008 bear markets. Today ${two === 0 ? "neither is on" : two === 1 ? "only one is on" : "both are on"}, meaning ${F.gc ? "stocks are cut" : "there is no reason to cut stocks for growth"}.`)
    + `<div class="ilist">${cblock("5.1", "S&P 500 vs its 10-month average", "%, monthly; shaded = both downturn signs on",
      `This chart measures how far the S&P 500 is above or below its average of the last 10 months. It is currently ${pct(F.gap, 1)}, versus ${pct(F.gap12, 1)} a year ago, meaning the market's trend is ${F.gap >= 0 ? "up" : "down"}.`, F.gap >= 0 ? ["good", "Above trend"] : ["warn", "Below trend"])}
      ${cblock("5.2", "Unemployment rate vs its 12-month average", "%, monthly; shaded = both downturn signs on",
      `This chart measures the share of the workforce without a job against its own average of the past year. It is currently ${p1(F.un)}, versus ${p2(F.ua)} for the average and ${p1(F.un12)} a year ago, meaning the job market is ${F.un > F.ua ? "weakening" : "holding steady"}.`, F.un > F.ua ? ["warn", "Rising"] : ["good", "Not rising"])}</div>`;
  const [c5a, c5b] = $("#s5").querySelectorAll(".chart"), cuts = runs(X.growth_cut).map(r => ({...r, c: "var(--bad-bg)"}));
  lineChart(c5a, [{v: D.values.spx_trend, c: "var(--s1)", wd: 1.4, name: "S&P 500 vs 10-month average", endLabel: v => pct(v, 1)}], M,
    {i0, rec: true, zero: true, fmt: v => pct(v, 1), fmtTick: t => `${t}%`, bands: cuts, aria: "trend"});
  lineChart(c5b, [{v: S.unemp, c: "var(--s1)", name: "Unemployment rate", endLabel: v => p1(v)}, {v: S.unemp_avg, c: "var(--g-mid)", wd: 1.2, name: "12-month average"}], M,
    {i0, rec: true, fmt: p1, fmtTick: t => `${t}%`, bands: cuts, aria: "unemployment"});
  // 6: bonds as a hedge
  $("#s6").innerHTML = head(6, F.corr < 0 ? "If stocks were cut for growth, long Treasuries would cushion the fall" : "If stocks were cut, cash would be safer than Treasuries",
    `When stocks and bonds move in opposite directions, long Treasuries tend to rise as stocks fall, so a growth-driven cut goes into them. When they move together, as in the 2022 inflation shock, bonds fall too and the cut goes to cash. Today the 12-month correlation is ${F.corr.toFixed(2)}, versus ${F.corr12.toFixed(2)} a year ago, meaning ${F.corr < 0 ? "Treasuries currently hedge stocks" : "Treasuries currently do not hedge stocks"}. Nothing is cut today, so this only sets the plan.`)
    + `<div class="ilist one">${cblock("6.1", "Stock-bond correlation, last 12 months", "Correlation of monthly returns, −1 to +1; shaded = Treasuries hedge stocks",
      `This chart measures how closely stock and long-bond returns moved together over the past year. It is currently ${F.corr.toFixed(2)}, versus ${F.corr12.toFixed(2)} a year ago, meaning bonds ${F.corr < 0 ? "have been moving against stocks, as a hedge should" : "have been moving with stocks, so they would not protect a fall"}.`, F.corr < 0 ? ["good", "Hedging"] : ["warn", "Not hedging"])}</div>`;
  lineChart($("#s6 .chart"), [{v: D.values.stockbond, c: "var(--s1)", wd: 1.4, name: "Correlation", endLabel: v => v.toFixed(2)}], M,
    {i0, rec: true, zero: true, fmt: v => v.toFixed(2), fmtTick: t => t.toFixed(1), hband: [{lo: -1, hi: 0, c: "var(--good-bg)"}], aria: "stock-bond correlation"});
  // 7: commodities
  $("#s7").innerHTML = head(7, F.con ? "Commodities are in an uptrend, so 10% of the portfolio goes to them" : "Commodities are not in an uptrend, so none are held",
    `A broad commodity index has been worth holding while its price trend is up: it moves differently from stocks and protects against rising prices. The rule holds 10% while the index is up over 12 months and above its 10-month average. Today it is ${pct(F.c12, 0)} over 12 months and ${pct(F.cgap, 0)} versus its average, meaning ${F.con ? "both conditions are met" : "the trend is not strong enough"}.`)
    + `<div class="ilist one">${cblock("7.1", "Commodity index vs its 10-month average", "Index, today = 100, log scale; shaded = commodities held",
      `This chart measures the price of a broad basket of commodity futures (energy, metals and farm goods) against its own 10-month average. It is currently ${pct(F.cgap, 0)} versus that average and ${pct(F.c12, 0)} over the past year, meaning ${F.con ? "the uptrend that earns a 10% holding is in place" : "there is no uptrend to follow"}.`, F.con ? ["good", "Held"] : ["", "Not held"])}</div>`;
  lineChart($("#s7 .chart"), [{v: S.commod, c: "var(--s1)", name: "Commodity index", endLabel: v => v.toFixed(0)}, {v: S.commod_ma, c: "var(--g-mid)", wd: 1.2, name: "10-month average"}], M,
    {i0, rec: true, log: true, ticks: [2, 5, 10, 20, 50, 100, 200], fmt: v => v.toFixed(1), bands: runs(X.commod_on).map(r => ({...r, c: "var(--good-bg)"})), aria: "commodities"});
  // 8: sector leadership
  const tb = F.lead.filter(r => r.a === "over"), bb = F.lead.filter(r => r.a === "under");
  $("#s8").innerHTML = head(8, F.full ? `Within stocks, lean toward ${names(F.top.map(lc))}` : "Sector tilts are on hold while stocks are reduced",
    `Sectors that led over the past year have tended to keep leading for a while. While fully invested, the rule holds the five strongest of the 20 sectors at 1.5 times their normal weight and the five weakest at half. Today the leaders are ${names(F.top.map(lc))} and the laggards are ${names(F.bot.map(lc))}, meaning the market is being driven by ${names(F.top.slice(0, 2).map(lc))} rather than ${names(F.bot.slice(-2).map(lc))}.`)
    + `<div class="ilist one">${cblock("8.1", "Sector returns over the past 12 months", "%, excluding the most recent month; blue = overweight, red = underweight",
      tb.length ? `This chart measures each sector's return over the past year, skipping the latest month. The five leaders returned ${pct(tb[tb.length - 1].v, 0)} to ${pct(tb[0].v, 0)} and the five laggards ${pct(bb[bb.length - 1].v, 0)} to ${pct(bb[0].v, 0)}, meaning leadership is ${tb[0].v - bb[bb.length - 1].v > 50 ? "very concentrated" : "moderately spread"}.` : "No sector data.", null)}</div>`;
  sectorBars($("#s8 .chart"));
}
function sectorBars(el){
  const T = D.derisk.tilt, i = NOW(); if (!T) { el.innerHTML = ""; return; }
  const rows = D.industries.map(it => ({n: it.name, e: it.etf, v: T.mom_now[it.etf], a: T.actions[it.etf][i]})).filter(r => r.v != null).sort((a, b) => b.v - a.v);
  const w = W(el), bh = 18, gap = 6, m = {l: 150, r: 50, t: 4, b: 4}, h = m.t + m.b + rows.length * (bh + gap);
  const lo = Math.min(0, ...rows.map(r => r.v)), hi = Math.max(0, ...rows.map(r => r.v)), X = v => m.l + (w - m.l - m.r) * (v - lo) / (hi - lo || 1);
  let g = `<line x1="${X(0)}" x2="${X(0)}" y1="${m.t}" y2="${h - m.b}" stroke="var(--black)" stroke-width=".75"/>`;
  rows.forEach((r, k) => { const y = m.t + k * (bh + gap), x0 = X(Math.min(0, r.v)), x1 = X(Math.max(0, r.v));
    const col = r.a === "over" ? "var(--eblue)" : r.a === "under" ? "var(--red)" : "var(--g-sl)";
    g += `<text x="${m.l - 8}" y="${y + bh - 5}" text-anchor="end">${esc(r.n)}</text><rect x="${x0}" y="${y}" width="${Math.max(1, x1 - x0)}" height="${bh}" fill="${col}"/>
      <text class="lab" x="${w - 2}" y="${y + bh - 5}" text-anchor="end">${pct(r.v, 0)}</text>`; });
  el.innerHTML = `<svg viewBox="0 0 ${w} ${h}" height="${h}" role="img" aria-label="Sector momentum">${g}</svg>`;
}

/* ------------------------------------------------------------------ indicator: summary sentence + two charts */
const UNITS = {"%": "%", "pts": "Percentage points", "x": "Times", "$bn": "USD billions", "% of GDP": "% of GDP", "": "Index"};
function summary(ind){
  const vals = D.values[ind.id], [cur, ci] = lastOf(vals), ago = ci >= 12 ? vals[ci - 12] : null, z = zoneAt(ind.id, NOW()), sg = hasNeg(ind.id);
  const iv = D.ind_view[ind.id], th = iv && iv.warn != null ? ` (${ind.dir > 0 ? "above" : "below"} ${fmtV(iv.warn, ind, sg)})` : "";
  const zp = {warn: `inside its warning zone${th}`, normal: "within its normal range", good: "in its supportive zone"}[z] || "without enough history to judge";
  const what = ind.what.replace(/^.*?\bmeasures?\s+/, "");
  return `This chart measures ${what}. It is currently ${fmtV(cur, ind, sg)}${ind.vp}${ago != null ? `, versus ${fmtV(ago, ind, sg)} a year ago` : ""}, ${zp}, meaning ${ind.means[z] || "no clear signal"}.`;
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
      <line x1="${m.l}" x2="${w - m.r}" y1="${y}" y2="${y}" stroke="var(--g-mid)" stroke-width=".75" stroke-dasharray="3 3"/>`;
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
  g += `<path d="${d}" fill="none" stroke="var(--s1)" stroke-width="${opt.monthly ? 2 : 1.3}" stroke-linejoin="round"/>`;
  if (opt.ago != null && opt.agoI >= i0) {
    const xa = X(opt.agoI), ya = Y(opt.ago), xc = X(ci), yc = Y(cv), up = yc < ya;
    g += `<line x1="${xa}" x2="${xc}" y1="${ya}" y2="${ya}" stroke="var(--ink2)" stroke-dasharray="2 3"/>
      <line x1="${xc}" x2="${xc}" y1="${ya}" y2="${yc}" stroke="var(--ink2)" stroke-dasharray="2 3"/>
      <circle cx="${xa}" cy="${ya}" r="4" fill="var(--card)" stroke="var(--ink)" stroke-width="1.6"/>
      <text class="lab" x="${xa}" y="${up ? ya + 15 : ya - 8}" text-anchor="start">${mlab(D.months[opt.agoI])}: ${fmtV(opt.ago / ind.scale, ind, hasNeg(ind.id))}</text>`;
  }
  if (cv != null) g += `<circle cx="${X(ci)}" cy="${Y(cv)}" r="4.2" fill="var(--cyan)" stroke="var(--white)" stroke-width="1.5"/>` +
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
  panel(card.querySelector(".chart"), ind, iFirst, {clip: true});
}
function indCard(ind, num){
  const z = zoneAt(ind.id, NOW());
  return `<div class="icard" id="ic-${ind.id}" data-id="${ind.id}"><div class="ihd"><span class="inum">${num}</span><b>${esc(ind.title)}</b><span class="tag ${z}">${ZW[z]}</span></div>
    <p class="isum">${esc(summary(ind))}</p><div class="metric">${UNITS[ind.unit] ?? ""}${ind.vp ? "," + ind.vp : ""}; red band = warning zone</div><div class="chart long"></div></div>`;
}
const ZORDER = {warn: 0, good: 1, normal: 2, "": 3};
function footnotes(extra){ return `<ol class="fns">${extra.map(t => `<li>${t}</li>`).join("")}</ol>`; }

/* ------------------------------------------------------------------ recommendation 1: portfolio, by quarter */
const qOf = mo => `${mo.slice(0, 4)}-Q${Math.ceil(+mo.slice(5, 7) / 3)}`;
const qLab = q => `${q.slice(5)} ${q.slice(0, 4)}`;
const sgn = d => { const r = Math.round(d); return `${r > 0 ? "+" : r < 0 ? "−" : ""}${Math.abs(r)}%`; };
const PARTS = [["equity", "Equity", "var(--deep)"], ["cash", "Cash", "var(--g-sl)"], ["bond", "Bond", "var(--eblue)"], ["commodities", "Commodities", "var(--cyan)"]];
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
  $("#xTitle").textContent = `Hold ${now.equity}% in stocks${now.commodities ? `, ${now.commodities}% in commodities` : ""}${now.bond ? `, ${now.bond}% in long Treasuries` : ""}${now.cash ? `, ${now.cash}% in cash` : ""} this quarter`;
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
  let kx = narrow ? m.l : w - 4 - PARTS.reduce((a, [, l]) => a + l.length * 7.2 + 18, 0);
  PARTS.forEach(([, l, col]) => {
    g += `<rect x="${kx}" y="${yA - 19}" width="10" height="10" rx="2" fill="${col}"/><text x="${kx + 14}" y="${yA - 10}">${l}</text>`; kx += l.length * 7.2 + 18; });
  // panel B: growth of $100
  D.recession.forEach((r, i) => { if (r !== 1) return; const k = Q.findIndex(x => x.q === qOf(D.months[i])); if (k < 0) return;
    g += `<rect x="${X_(k) - bw / 2}" y="${yB - 10}" width="${bw + 0.6}" height="6" fill="var(--rec)"/>`; });
  g += recKey(w - 4, yB - 22);
  [100, 1000, 10000, 100000].filter(t => Math.log(t) >= lo && Math.log(t) <= hi).forEach(t => {
    g += `<line x1="${m.l}" x2="${w - m.r}" y1="${YB(t)}" y2="${YB(t)}" stroke="var(--grid)"/><text x="${m.l - 6}" y="${YB(t) + 3.5}" text-anchor="end">$${t.toLocaleString("en-US")}</text>`; });
  const path = key => Q.map((x, k) => `${k ? "L" : "M"}${X_(k).toFixed(1)} ${YB(x[key]).toFixed(1)}`).join("");
  g += `<path d="${path("sp")}" fill="none" stroke="var(--g-light)" stroke-width="2"/><path d="${path("rec")}" fill="none" stroke="var(--deep)" stroke-width="2.4"/>`;
  const L = Q[n - 1];
  if (!narrow) {
    const ys = YB(L.sp), yr = YB(L.rec), sep = Math.abs(ys - yr) < 14 ? 7 : 0;
    g += `<text class="endlab" x="${w - m.r + 8}" y="${yr + 4 + (yr <= ys ? -sep : sep)}" style="fill:var(--deep)">Recommended</text>`;
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
  const tops = facts().top.map(lc);
  $("#sTitle").textContent = live ? `Within stocks, overweight ${names(tops)}` : "Sector tilts are on hold while stocks are reduced";
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
