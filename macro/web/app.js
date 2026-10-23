/* Macro Compass - static front end. Reads /macro/data/data.bin (gzip'd JSON, AES-GCM, key from the site password
   via PBKDF2-SHA256; same scheme and saved key as the triage site), built by macro/engine.py + macro/site.py. */
"use strict";
const $ = s => document.querySelector(s);
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const store = {get(k){ try { return localStorage.getItem(k); } catch(e){ return null; } },
  set(k,v){ try { localStorage.setItem(k, v); } catch(e){} }, del(k){ try { localStorage.removeItem(k); } catch(e){} }};
let D = null, H = store.get("mc-h") || "12", KEY = null, INFO = null, N = 0;
const OPEN = new Set();
const STAGE_ORDER = ["expansion", "late", "contraction", "recovery"];
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

function stripChart(el){
  const i0 = D.months.findIndex(m => m >= "1970-01"), ms = D.months.slice(i0), st = D.stage.slice(i0), rec = D.recession.slice(i0);
  const w = W(el), h = 54, top = 12, bh = 24, n = ms.length, bw = w / n;
  let g = "";
  rec.forEach((r, i) => { if (r === 1) g += `<rect x="${(i * bw).toFixed(2)}" y="2" width="${(bw + .4).toFixed(2)}" height="6" fill="var(--rec)"/>`; });
  let runStart = 0;
  for (let i = 1; i <= n; i++) if (i === n || st[i] !== st[runStart]) {
    if (st[runStart]) g += `<rect x="${(runStart * bw).toFixed(2)}" y="${top}" width="${((i - runStart) * bw + .4).toFixed(2)}" height="${bh}" fill="var(--st-${st[runStart]})"/>`;
    runStart = i;
  }
  ms.forEach((m, i) => { if (m.endsWith("-01") && +m.slice(0, 4) % 10 === 0) g += `<text x="${(i * bw).toFixed(1)}" y="${h - 2}">${m.slice(0, 4)}</text>`; });
  g += `<rect class="hit" x="0" y="0" width="${w}" height="${h}" fill="transparent"/>`;
  el.innerHTML = `<svg viewBox="0 0 ${w} ${h}" height="${h}" role="img" aria-label="Stage each month since 1970">${g}</svg>`;
  el.querySelector(".hit").addEventListener("pointermove", e => {
    const r = el.getBoundingClientRect(), i = Math.max(0, Math.min(n - 1, Math.floor((e.clientX - r.left) / r.width * n)));
    const s = st[i]; showTip(e, `<div class="d">${mlab(ms[i])}${rec[i] === 1 ? " · recession" : ""}</div><b>${s ? D.meta.stages[s][0] : "Not enough data"}</b>`);
  });
  el.querySelector(".hit").addEventListener("pointerleave", hideTip);
}

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
const PIL = () => Object.fromEntries(D.meta.pillars.map(p => [p[0], p]));
const latest = arr => { const [v, i] = lastOf(arr); return i >= N - 4 ? v : null; };   // stale after 3 months
function driverInfo(k){
  const p = PIL()[k];
  if (p) return {name: p[1], series: D.pillars[k], who: null};
  const i = IND()[k]; return {name: i.name, plain: i.plain, series: D.scores[k], who: i.who};
}
const whoText = w => (w || []).map(x => x[1].startsWith("#") ? `${x[0]}` : `${x[0].replace(" (X)", "")} (X post)`).filter((v, i, a) => a.indexOf(v) === i).join(", ");

/* ------------------------------------------------------------------ 1 stage */
function renderStage(){
  const [s, i] = lastOf(D.stage); const [name, why] = D.meta.stages[s];
  let j = i; while (j > 0 && D.stage[j - 1] === s) j--;
  const g = D.growth3[i], d = D.growth_d6[i];
  $("#stageDot").style.background = `var(--st-${s})`;
  $("#stageName").textContent = name;
  $("#stageWhy").textContent = why;
  $("#stageFacts").textContent = `Since ${mlab(D.months[j])} · growth pressure, 6-month average: ${Math.round(g)} out of 100, ${d >= 0 ? "up" : "down"} ${Math.abs(Math.round(d))} in a year`;
  $("#cycle").innerHTML = STAGE_ORDER.map(k => `<div class="cyc${k === s ? " on" : ""}" style="${k === s ? `border-color:var(--st-${k})` : ""}"><b><i style="background:var(--st-${k})"></i>${D.meta.stages[k][0]}</b><span>${D.meta.stages[k][1]}</span></div>`).join("");
  stripChart($("#strip"));
}

/* ------------------------------------------------------------------ 2 pillars */
function renderPillars(){
  const ind = D.meta.indicators, from = Math.max(0, N - 120);
  $("#pillars").innerHTML = D.meta.pillars.map(([k, name, q]) => {
    const a = D.pillars[k], s = latest(a), prev = a[N - 4];
    const tr = s == null || prev == null ? "" : s - prev >= 5 ? "rising" : s - prev <= -5 ? "easing" : "steady";
    const rows = ind.filter(x => x.pillar === k).map(x => {
      const v = latest(D.scores[x.id]);
      return `<div class="irow${v == null ? " na" : ""}"><div>${esc(x.name)}<div class="who">Suggested by ${esc(whoText(x.who))}</div></div>
        <div class="spark">${spark(D.scores[x.id].slice(from))}</div><div class="sc num">${v == null ? "–" : Math.round(v)}</div><div>${gauge(v)}</div></div>`;
    }).join("");
    const open = OPEN.has("p-" + k);
    return `<div class="prow" tabindex="0" role="button" aria-expanded="${open}" data-k="${k}"><div class="pn"><b>${esc(name)}</b><span>${esc(q)}</span></div>${gauge(s)}
      <div class="pword"><b class="num">${s == null ? "–" : Math.round(s)}</b>${word(s)}${tr ? ` · ${tr}` : ""}</div><span class="chev" aria-hidden="true">›</span></div>
      <div class="pdetail" ${open ? "" : "hidden"}><div class="irow" style="font-size:12px;color:var(--ink3)"><div>Indicator</div><div class="spark">Last 10 years</div><div class="sc">Score</div><div></div></div>${rows}</div>`;
  }).join("");
  document.querySelectorAll(".prow").forEach(r => { const t = () => { const k = "p-" + r.dataset.k; OPEN.has(k) ? OPEN.delete(k) : OPEN.add(k); renderPillars(); };
    r.onclick = t; r.onkeydown = e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); t(); } }; });
}

/* ------------------------------------------------------------------ 3 industries */
const ACT = {over: ["over", "▲", "Overweight"], under: ["under", "▼", "Underweight"], neutral: ["neutral", "●", "Neutral"]};
const pill = a => { const [c, i, t] = ACT[a] || ACT.neutral; return `<span class="pill ${c}"><span aria-hidden="true">${i}</span>${t}</span>`; };
function renderIndustries(){
  const hz = D.horizons[H], band = Math.round(hz.band * 100);
  const rows = D.industries.map(it => ({it, now: hz.now[it.etf]})).map(r => {
    const n = r.now; r.rr = n ? n.p_risk / n.base_risk : 1; r.ro = n ? n.p_opp / n.base_opp : 1; r.a = n ? n.action : "neutral"; return r; });
  const nOver = rows.filter(r => r.a === "over").length, nUnder = rows.filter(r => r.a === "under").length;
  $("#actHead").textContent = nOver + nUnder === 0 ? "No industry stands out right now: hold them evenly"
    : `${nOver ? `${nOver} to overweight` : ""}${nOver && nUnder ? ", " : ""}${nUnder ? `${nUnder} to underweight` : ""}, the rest neutral`;
  $("#actSub").textContent = `For each industry ETF: how often it lagged or beat the S&P 500 by ${band}% or more over the next ${H} months, in past months when its drivers looked like today. We act when the odds are 1.5 times their normal level.`;
  const grp = [["over", "Overweight", (a, b) => b.ro - a.ro], ["under", "Underweight", (a, b) => b.rr - a.rr], ["neutral", "Neutral", (a, b) => a.it.name.localeCompare(b.it.name)]];
  let html = `<thead><tr><th>Industry</th><th>Call</th><th>Lags the market by ${band}%+</th><th>Beats the market by ${band}%+</th><th>Drivers today</th></tr></thead><tbody>`;
  grp.forEach(([a, label, sort]) => {
    const g = rows.filter(r => r.a === a).sort(sort); if (!g.length) return;
    html += `<tr class="grp"><td colspan="5">${label}</td></tr>`;
    g.forEach(r => {
      const n = r.now, ds = latest(r.it.driver), open = OPEN.has("i-" + r.it.etf);
      html += `<tr class="irow2" tabindex="0" data-e="${r.it.etf}" aria-expanded="${open}"><td><b>${esc(r.it.name)}</b> <span class="etf muted">${r.it.etf}</span></td><td>${pill(r.a)}</td>
        <td class="odds${r.rr >= 1.5 ? " hi" : ""}">${n ? `<b class="num">${Math.round(n.p_risk)}%</b> <span>usually ${Math.round(n.base_risk)}%</span>` : "–"}</td>
        <td class="odds${r.ro >= 1.5 ? " hiopp" : ""}">${n ? `<b class="num">${Math.round(n.p_opp)}%</b> <span>usually ${Math.round(n.base_opp)}%</span>` : "–"}</td>
        <td class="why">${ds == null ? "–" : `${Math.round(ds)} · ${ds >= 65 ? "strong headwinds" : ds <= 35 ? "strong tailwinds" : "mixed"}`}</td></tr>`;
      if (open) html += `<tr class="idetail"><td colspan="5">${detailHTML(r.it)}</td></tr>`;
    });
  });
  $("#indTable").innerHTML = html + "</tbody>";
  document.querySelectorAll("tr.irow2").forEach(tr => { const t = () => { const k = "i-" + tr.dataset.e; OPEN.has(k) ? OPEN.delete(k) : OPEN.add(k); renderIndustries(); };
    tr.onclick = t; tr.onkeydown = e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); t(); } }; });
  D.industries.forEach(it => { const el = document.getElementById("rel-" + it.etf); if (el) relChart(el, it); });
}
function detailHTML(it){
  const drv = it.drivers.map(([k, sign]) => {
    const d = driverInfo(k), s = latest(d.series);
    return `<div class="drv"><div>${esc(d.name)}<div class="dir">${sign > 0 ? "High = headwind" : "High = tailwind"}</div></div>${gauge(s)}<b class="num" style="text-align:right">${s == null ? "–" : Math.round(s)}</b></div>`;
  }).join("");
  return `<div class="idet"><div><h4>${esc(it.name)} vs the S&P 500, last 15 years</h4><div class="legend"><span><i style="background:var(--good-bg);height:10px"></i>Overweight call</span><span><i style="background:var(--bad-bg);height:10px"></i>Underweight call</span></div><div class="chart" id="rel-${it.etf}"></div>
    <p class="muted" style="font-size:12.5px;margin:6px 0 0">Line rising = beating the market. ${it.etf_from ? `${it.etf} trades from ${mlab(it.etf_from)}; before that, its industry index.` : ""}</p></div>
    <div><h4>What drives it</h4>${drv}${it.who && it.who.length ? `<p class="muted" style="font-size:12.5px;margin:8px 0 0">Links suggested by ${esc(whoText(it.who))}</p>` : ""}</div></div>`;
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
    tipExtra: i => acts[i] && acts[i] !== "neutral" ? ` · ${ACT[acts[i]][2]}` : "", aria: `${it.name} relative to the S&P 500`});
}

/* ------------------------------------------------------------------ 4 track record */
function renderBacktest(){
  const hz = D.horizons[H], bt = hz.backtest.etf, st = bt.stats, lg = hz.backtest.long.stats, band = Math.round(hz.band * 100);
  const diff = st.compass && st.equal ? st.compass.cagr - st.equal.cagr : 0;
  $("#btHead").textContent = Math.abs(diff) < 0.5 ? "So far the calls have made little difference to returns"
    : diff > 0 ? `The calls added ${diff.toFixed(1)}% a year` : `The calls cost ${Math.abs(diff).toFixed(1)}% a year`;
  $("#btSub").textContent = `Since ${mlab(st.compass.from)}: the 20 ETFs held equally, but tilted each month by that month's ${H}-month calls (overweight 1.5×, underweight 0.5×), using only data available at the time.`;
  const C = {compass: ["With the calls", "var(--s1)"], equal: ["The 20 ETFs, equal weight", "var(--s2)"], market: ["S&P 500", "var(--s3)"]};
  $("#btLegend").innerHTML = Object.entries(C).map(([k, [n, c]]) => `<span><i style="background:${c}"></i>${n}</span>`).join("");
  lineChart($("#btChart"), Object.entries(C).map(([k, [n, c]]) => ({name: n, v: bt.curves[k].map(x => x == null ? null : 100 * x), c,
    wd: k === "compass" ? 2.4 : 1.6, endLabel: v => `$${Math.round(v)}`})), D.months, {log: true, ticks: [100, 200, 300, 400, 600, 800, 1000], fmtTick: t => `$${t}`, fmt: v => `$${Math.round(v)}`, aria: "Growth of $100"});
  const R = [["compass", "With the calls"], ["equal", "Equal weight"], ["momentum", "Last year's winners"], ["trend", "Trend (above 10-month average)"], ["market", "S&P 500"]];
  $("#btStats").innerHTML = `<thead><tr><th>Since ${st.compass.from.slice(0, 4)}</th><th>Per year</th><th>Worst fall</th></tr></thead><tbody>` +
    R.map(([k, n]) => st[k] ? `<tr class="${k === "compass" ? "me" : ""}"><td>${n}</td><td>${pct(st[k].cagr, 1)}</td><td>${pct(st[k].maxdd, 0)}</td></tr>` : "").join("") +
    (lg.compass && lg.equal ? `<tr><td colspan="3" style="font-size:12px;color:var(--ink3);text-align:left;padding-top:10px">Same test on industry indexes since ${lg.compass.from.slice(0, 4)}: ${pct(lg.compass.cagr, 1)} a year with the calls vs ${pct(lg.equal.cagr, 1)} equal weight.</td></tr>` : "") + "</tbody>";
  const hb = (lab, h, ok) => `<div class="hit">${lab}<div><b class="num">${h.hit == null ? "–" : Math.round(h.hit) + "%"}</b> <span class="muted">of ${h.calls} calls ${ok}, vs ${Math.round(h.base)}% for any industry in any month</span></div>
    <div class="hitbar"><i style="width:${Math.round(h.hit || 0)}%;max-width:60%;background:var(--ink2)"></i><i style="width:${Math.round(h.base)}%;max-width:60%;background:var(--axis)"></i></div></div>`;
  $("#btHits").innerHTML = hb("Underweight calls", bt.hit.under, `lagged the market by ${band}%+`) + hb("Overweight calls", bt.hit.over, `beat the market by ${band}%+`);
  const L = D.live, sc = L && L.scored && L.scored[H];
  $("#liveBox").innerHTML = !L || !L.rows ? `<div><h3>Live record</h3><p>Every month's calls are saved permanently once the month ends, starting with October 2026, so the record can't be edited later. First results: 6-month calls in April 2027, 12-month calls in October 2027.</p></div>`
    : `<div><h3>Live record since ${mlab(L.first)}</h3><p>${sc && (sc.over.calls + sc.under.calls) ? `Underweight calls lagged the market by ${band}%+ in ${sc.under.hit ?? "–"}% of ${sc.under.calls} cases; overweight calls beat it in ${sc.over.hit ?? "–"}% of ${sc.over.calls}.` : "No call has reached its end date yet."} ${sc ? `${sc.pending} calls still running.` : ""}</p></div>`;
}

/* ------------------------------------------------------------------ 5 how it works */
function renderHow(){
  const P = PIL(), rep = D.report || {};
  const rows = D.meta.indicators.filter(i => i.pillar).map(i => { const r = rep[i.id];
    return `<tr><td>${esc(i.name)}</td><td>${esc(P[i.pillar][1])}</td><td>${esc(whoText(i.who))}</td>
      <td class="r">${r && r.worst_fifth_fwd != null ? `${pct(r.worst_fifth_fwd, 1)} <span class="muted">vs ${pct(r.normal_fwd, 1)}</span>` : "–"}</td>
      <td class="r">${r && r.pre_recession != null ? `${r.pre_recession} <span class="muted">(${r.recessions})</span>` : "–"}</td></tr>`; }).join("");
  const nInv = new Set(D.meta.indicators.flatMap(i => i.who.map(w => w[0]))).size;
  $("#how").innerHTML = `<ol>
    <li><b>Investors suggest the indicators.</b> ${D.meta.indicators.length} indicators from ${nInv} investors in our transcript library and X posts.</li>
    <li><b>Each reading gets a score from 0 to 100</b>: how it compares with all its own past readings up to that month. Economic data enter only once they were published.</li>
    <li><b>Scores roll up into six areas.</b> The growth area sets the stage: high and rising pressure is Contraction, high and easing is Recovery, low and easing is Expansion, low and rising is Late cycle.</li>
    <li><b>Each industry has its drivers</b>, as investors described them. We look at every past month whose driver score was in the same fifth as today and count how often the industry then lagged or beat the market. We act when those odds are 1.5 times normal.</li>
    <li><b>Nothing is fitted to the whole history.</b> Each month uses only what was known then. The live record keeps scoring the calls as they come due.</li></ol>
    <div><h3 style="font-size:15px;margin:0 0 6px">Indicator report card</h3><p class="sub" style="font-size:13.5px">What followed when each indicator was in its worst fifth. Stocks = S&P 500 over the next 12 months. Before recessions = its average score 6 months before a recession began (number of recessions in brackets).</p></div>
    <div class="tablewrap"><table><thead><tr><th>Indicator</th><th>Area</th><th>Suggested by</th><th class="r">Stocks next 12 months</th><th class="r">Before recessions</th></tr></thead><tbody>${rows}</tbody></table></div>
    <p class="muted" style="font-size:12.5px;margin:0">Data: FRED (St. Louis Fed)${D.fred_key ? ", first-published values" : ""}, Kenneth French data library, Yahoo Finance, multpl.com. Version ${D.version}. Not investment advice.</p>`;
}

/* ------------------------------------------------------------------ boot */
function renderAll(){ renderStage(); renderPillars(); renderIndustries(); renderBacktest(); renderHow(); }
function setH(h){ H = h; store.set("mc-h", h); document.querySelectorAll("#horizon button").forEach(b => b.setAttribute("aria-pressed", b.dataset.h === H));
  renderIndustries(); renderBacktest(); }
async function start(){
  const buf = await (await fetch("/macro/data/data.bin", {cache: "no-cache"})).arrayBuffer();
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
    if ($("#remember").checked) store.set("qt-key", JSON.stringify({salt: INFO.salt, k: toB64(await crypto.subtle.exportKey("raw", k))}));
    $("#pw").value = ""; await start();
  } catch(e){ $("#lockMsg").textContent = "Couldn't open the data: " + e.message; }
  finally { btn.disabled = false; btn.textContent = "Open"; }
});
$("#lockNow").onclick = () => { store.del("qt-key"); location.reload(); };
(async () => {
  try { INFO = await (await fetch("/macro/data/keyinfo.json", {cache: "no-cache"})).json(); }
  catch(e){ showLock("No data yet: the Macro workflow hasn't published the page."); return; }
  if (INFO.plain) { await start(); return; }
  const saved = store.get("qt-key");
  if (saved) { try { const {salt, k} = JSON.parse(saved);
      if (salt === INFO.salt) { const key = await crypto.subtle.importKey("raw", b64(k), {name: "AES-GCM"}, true, ["decrypt"]);
        if (await tryKey(key)) { await start(); return; } } } catch(e){}
    store.del("qt-key"); }
  showLock("");
})();
