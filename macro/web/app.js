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
const PIL = () => Object.fromEntries(D.meta.pillars.map(p => [p[0], p]));
const latest = arr => { const [v, i] = lastOf(arr); return i >= N - 4 ? v : null; };   // stale after 3 months
const whoText = w => (w || []).map(x => x[1].startsWith("#") ? `${x[0]}` : `${x[0].replace(" (X)", "")} (X post)`).filter((v, i, a) => a.indexOf(v) === i).join(", ");
const stName = s => s && D.meta.stages[s] ? D.meta.stages[s][0] : "Not enough data";
const NAME = () => Object.fromEntries(D.industries.map(i => [i.etf, i.name]));
const FEEDS = {growth: "Economy dial", internals: "Economy dial", inflation: "Inflation dial", stress: "Stress dial", liquidity: "Background", froth: "Background"};
function gaugeT(s, th){
  return gauge(s).replace(/<\/div>$/, `${th == null ? "" : `<div class="th" style="left:${th}%" title="Switches on at ${th}"></div>`}</div>`);
}
const NOW = () => N - 1;

/* ------------------------------------------------------------------ 1 state */
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
    showTip(e, `<div class="d">${mlab(ms[i])}${rec[i] === 1 ? " · recession" : ""}</div><b>${stName(st[i])}</b>${sh[i] ? "<div>Market stress high</div>" : ""}`);
  });
  el.querySelector(".hit").addEventListener("pointerleave", hideTip);
}
function renderStage(){
  const i = NOW(), s = D.regime[i], stage = D.stage[i], hot = D.hot[i], high = D.stress_high[i];
  let j = i; while (j > 0 && D.regime[j - 1] === s) j--;
  const S = D.settings, e = D.econ6[i], d = D.econ_d12[i], inf = D.infl6[i], str = latest(D.pillars.stress);
  $("#stageDot").style.background = `var(--st-${s})`;
  $("#stageName").textContent = stName(s) + (high ? ", markets in risk-off mode" : "");
  $("#stageWhy").textContent = D.meta.stages[s][1] + (high ? " On top of that, markets are under stress." : "");
  $("#stageFacts").textContent = `Since ${mlab(D.months[j])}. The state combines three dials: where growth is heading, whether inflation runs hot, and whether markets are in risk-off mode.`;
  const dial = (title, q, val, on, score, th, foot) => `<div class="dial"><div class="hd"><b>${title}</b><span class="v${on ? " on" : ""}">${val}</span></div>
    <div class="q">${q}</div>${gaugeT(score, th)}<div class="ft">${foot}</div></div>`;
  const stageWord = {expansion: "Strong, improving", late: "Strong, weakening", contraction: "Weak, weakening", recovery: "Weak, improving"}[stage] || "–";
  $("#dials").innerHTML =
    dial("Economy", "Growth data and market health, 6-month average", esc(stageWord), stage === "contraction" || stage === "late", e, null,
      `Pressure ${Math.round(e)} of 100, ${d >= 0 ? "up" : "down"} ${Math.abs(Math.round(d))} in a year. Higher = weaker economy.`) +
    dial("Inflation", "Prices, costs and inflation expectations, 6-month average", hot ? "Running hot" : "Under control", hot, inf, S.inflation_hot[0],
      `${Math.round(inf)} of 100. Hot from ${S.inflation_hot[0]}, cools below ${S.inflation_hot[1]}.${hot && stage === "recovery" ? " In a recovery it doesn't change the playbook." : ""}`) +
    dial("Market stress", "Fear gauge, junk bonds, banks, dollar, chips", high ? "Risk-off" : str >= S.stress_high[1] ? "Rising" : "Calm", high, str, S.stress_high[0],
      `${str == null ? "–" : Math.round(str)} of 100. Risk-off from ${S.stress_high[0]}, ends below ${S.stress_high[1]}.`);
  $("#stripKey").innerHTML = STATES.map(k => `<span><i style="background:var(--st-${k})"></i>${D.meta.stages[k][0]}</span>`).join("") +
    `<span><i class="str"></i>Market stress high</span><span><i class="rec"></i>US recession</span>`;
  stripChart($("#strip"));
}

/* ------------------------------------------------------------------ 2 pillars */
function renderPillars(){
  const ind = D.meta.indicators, from = Math.max(0, N - 120);
  $("#pilSub").textContent = "Each indicator is scored against all its own past readings: 50 is normal, higher means more pressure. Growth and market health set the economy dial; inflation and market stress set their own dials. Money and rates and froth are shown as background: adding them to the dials made past calls worse, so they don't move the calls. Tap an area to see its indicators.";
  $("#pillars").innerHTML = D.meta.pillars.map(([k, name, q]) => {
    const a = D.pillars[k], s = latest(a), prev = a[N - 4];
    const tr = s == null || prev == null ? "" : s - prev >= 5 ? "rising" : s - prev <= -5 ? "easing" : "steady";
    const rows = ind.filter(x => x.pillar === k).map(x => {
      const v = latest(D.scores[x.id]);
      return `<div class="irow${v == null ? " na" : ""}"><div>${esc(x.name)}<div class="who">Suggested by ${esc(whoText(x.who))}</div></div>
        <div class="spark">${spark(D.scores[x.id].slice(from))}</div><div class="sc num">${v == null ? "–" : Math.round(v)}</div><div>${gauge(v)}</div></div>`;
    }).join("");
    const open = OPEN.has("p-" + k);
    return `<div class="prow" tabindex="0" role="button" aria-expanded="${open}" data-k="${k}"><div class="pn"><b>${esc(name)}</b><span>${esc(q)} · ${FEEDS[k]}</span></div>${gauge(s)}
      <div class="pword"><b class="num">${s == null ? "–" : Math.round(s)}</b>${word(s)}${tr ? ` · ${tr}` : ""}</div><span class="chev" aria-hidden="true">›</span></div>
      <div class="pdetail" ${open ? "" : "hidden"}><div class="irow" style="font-size:12px;color:var(--ink3)"><div>Indicator</div><div class="spark">Last 10 years</div><div class="sc">Score</div><div></div></div>${rows}</div>`;
  }).join("");
  document.querySelectorAll(".prow").forEach(r => { const t = () => { const k = "p-" + r.dataset.k; OPEN.has(k) ? OPEN.delete(k) : OPEN.add(k); renderPillars(); };
    r.onclick = t; r.onkeydown = e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); t(); } }; });
}

/* ------------------------------------------------------------------ 3 investor calls + history check */
const ACT = {over: ["over", "▲", "Overweight"], under: ["under", "▼", "Underweight"], neutral: ["neutral", "●", "Neutral"]};
const pill = a => { const [c, i, t] = ACT[a] || ACT.neutral; return `<span class="pill ${c}"><span aria-hidden="true">${i}</span>${t}</span>`; };
const chips = (lab, etfs, cls) => etfs.length ? `<div class="chips"><span class="lab">${lab}</span>${etfs.map(e => `<span class="chip ${cls}" title="${esc(NAME()[e])}">${e}</span>`).join("")}</div>` : "";
function ruleCard(title, r){
  return `<div class="rule"><h3>${esc(title)}</h3>${chips("Buy", r.over, "over")}${chips("Avoid", r.under, "under")}<p>${esc(r.why)}</p>
    <div class="cite">From ${esc(whoText(r.who))}</div></div>`;
}
function renderIndustries(){
  const i = NOW(), s = D.regime[i], high = D.stress_high[i], hz = D.horizons[H], band = Math.round(hz.band * 100);
  $("#actHead").textContent = `In ${stName(s)}${high ? " with markets under stress" : ""}, this is what our investors do`;
  $("#ruleCards").innerHTML = ruleCard(`${stName(s)}: the investors' playbook`, D.meta.rules[s]) +
    (high ? ruleCard("Market stress: added on top", D.meta.stress_rule) : "");
  $("#actSub").textContent = `History check: a call stands only if, in past months of the same situation, the industry ETF did on average move the same way against the S&P 500 over the next ${H} months. Otherwise we stay neutral. Only data known at the time is used.`;
  const rows = D.industries.map(it => { const n = hz.now[it.etf] || {}; const t = n.tilt || 0;
    const g = n.action === "over" ? 0 : n.action === "under" ? 1 : t !== 0 ? 2 : 3; return {it, n, t, g}; });
  const G = ["Overweight", "Underweight", "Investors say yes, history says no: stay neutral", "No view: neutral"];
  let html = `<thead><tr><th>Industry</th><th>Call</th><th>Investors say</th><th>History in this situation (next ${H} months vs S&P 500)</th><th>Lagged by ${band}%+</th><th>Beat by ${band}%+</th></tr></thead><tbody>`;
  [0, 1, 2, 3].forEach(gi => {
    const g = rows.filter(r => r.g === gi).sort((a, b) => (b.n.mean_rel ?? 0) * (gi === 1 ? -1 : 1) - (a.n.mean_rel ?? 0) * (gi === 1 ? -1 : 1)); if (!g.length) return;
    html += `<tr class="grp"><td colspan="6">${G[gi]}</td></tr>`;
    g.forEach(r => {
      const n = r.n, open = OPEN.has("i-" + r.it.etf), mr = n.mean_rel;
      const say = r.t > 0 ? `<span class="chip over">Buy</span>` : r.t < 0 ? `<span class="chip under">Avoid</span>` : `<span class="muted">–</span>`;
      const pool = n.pool === "state+stress" ? `same state${high ? " and stress" : ", no stress"}` : "same state";
      const hist = mr == null ? `<span class="muted">Too few past months</span>`
        : `<b class="num">${pct(mr, 1)}</b> on average in ${n.n} months (${pool})${r.t ? ` · <span class="${n.agrees ? "yes" : "no"}">${n.agrees ? "agrees" : "disagrees"}</span>` : ""}`;
      html += `<tr class="irow2" tabindex="0" data-e="${r.it.etf}" aria-expanded="${open}"><td><b>${esc(r.it.name)}</b> <span class="etf muted">${r.it.etf}</span></td><td>${pill(n.action)}</td><td>${say}</td>
        <td class="hist">${hist}</td>
        <td class="odds${n.p_risk != null && n.p_risk >= 1.25 * n.base_risk ? " hi" : ""}">${n.p_risk != null ? `<b class="num">${Math.round(n.p_risk)}%</b> <span>usually ${Math.round(n.base_risk)}%</span>` : "–"}</td>
        <td class="odds${n.p_opp != null && n.p_opp >= 1.25 * n.base_opp ? " hiopp" : ""}">${n.p_opp != null ? `<b class="num">${Math.round(n.p_opp)}%</b> <span>usually ${Math.round(n.base_opp)}%</span>` : "–"}</td></tr>`;
      if (open) html += `<tr class="idetail"><td colspan="6">${detailHTML(r.it)}</td></tr>`;
    });
  });
  $("#indTable").innerHTML = html + "</tbody>";
  document.querySelectorAll("tr.irow2").forEach(tr => { const t = () => { const k = "i-" + tr.dataset.e; OPEN.has(k) ? OPEN.delete(k) : OPEN.add(k); renderIndustries(); };
    tr.onclick = t; tr.onkeydown = e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); t(); } }; });
  D.industries.forEach(it => { const el = document.getElementById("rel-" + it.etf); if (el) relChart(el, it); });
}
function detailHTML(it){
  const now = D.regime[NOW()], R = D.meta.rules;
  const v = r => r.over.includes(it.etf) ? `<span class="chip over">Buy</span>` : r.under.includes(it.etf) ? `<span class="chip under">Avoid</span>` : `<span class="muted">–</span>`;
  const views = STATES.map(k => `<div class="${k === now ? "now" : ""}"><span>${D.meta.stages[k][0]}${k === now ? " (now)" : ""}</span>${v(R[k])}</div>`).join("") +
    `<div class="${D.stress_high[NOW()] ? "now" : ""}"><span>Market stress, added on top</span>${v(D.meta.stress_rule)}</div>`;
  return `<div class="idet"><div><h4>${esc(it.name)} vs the S&P 500, last 15 years</h4><div class="legend"><span><i style="background:var(--good-bg);height:10px"></i>Overweight call</span><span><i style="background:var(--bad-bg);height:10px"></i>Underweight call</span></div><div class="chart" id="rel-${it.etf}"></div>
    <p class="muted" style="font-size:12.5px;margin:6px 0 0">Line rising = beating the market. ${it.etf_from ? `${it.etf} trades from ${mlab(it.etf_from)}; before that, its industry index.` : ""}</p></div>
    <div><h4>What investors do with it in each state</h4><div class="views">${views}</div></div></div>`;
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

/* ------------------------------------------------------------------ 4 track record */
function renderBacktest(){
  const hz = D.horizons[H], bt = hz.backtest.etf, st = bt.stats, lg = hz.backtest.long.stats, band = Math.round(hz.band * 100);
  const diff = st.compass && st.equal ? st.compass.cagr - st.equal.cagr : 0;
  $("#btHead").textContent = Math.abs(diff) < 0.5 ? "So far the calls have made little difference to returns"
    : diff > 0 ? `The calls added ${diff.toFixed(1)}% a year` : `The calls cost ${Math.abs(diff).toFixed(1)}% a year`;
  $("#btSub").textContent = `Since ${mlab(st.compass.from)}: the 20 ETFs held equally, tilted each month by that month's ${H}-month calls (overweight 1.5×, underweight 0.5×), using only data available at the time. "Investors' playbook only" skips the history check.`;
  const C = {compass: ["With the calls", "var(--s1)"], investor: ["Investors' playbook only", "var(--st-stagflation)"], equal: ["The 20 ETFs, equal weight", "var(--s2)"], market: ["S&P 500", "var(--s3)"]};
  $("#btLegend").innerHTML = Object.entries(C).map(([k, [n, c]]) => `<span><i style="background:${c}"></i>${n}</span>`).join("");
  lineChart($("#btChart"), Object.entries(C).filter(([k]) => bt.curves[k]).map(([k, [n, c]]) => ({name: n, v: bt.curves[k].map(x => x == null ? null : 100 * x), c,
    wd: k === "compass" ? 2.4 : 1.6, endLabel: v => `$${Math.round(v)}`})), D.months, {log: true, ticks: [100, 200, 300, 400, 600, 800, 1000], fmtTick: t => `$${t}`, fmt: v => `$${Math.round(v)}`, aria: "Growth of $100"});
  const Rw = [["compass", "With the calls"], ["investor", "Investors' playbook only"], ["equal", "Equal weight"], ["momentum", "Last year's winners"], ["trend", "Trend (above 10-month average)"], ["market", "S&P 500"]];
  $("#btStats").innerHTML = `<thead><tr><th>Since ${st.compass.from.slice(0, 4)}</th><th>Per year</th><th>Worst fall</th></tr></thead><tbody>` +
    Rw.map(([k, n]) => st[k] ? `<tr class="${k === "compass" ? "me" : ""}"><td>${n}</td><td>${pct(st[k].cagr, 1)}</td><td>${pct(st[k].maxdd, 0)}</td></tr>` : "").join("") +
    (lg.compass && lg.equal ? `<tr><td colspan="3" style="font-size:12px;color:var(--ink3);text-align:left;padding-top:10px">Same test on industry indexes since ${lg.compass.from.slice(0, 4)}: ${pct(lg.compass.cagr, 1)} a year with the calls, ${pct(lg.investor ? lg.investor.cagr : null, 1)} playbook only, ${pct(lg.equal.cagr, 1)} equal weight.</td></tr>` : "") + "</tbody>";
  const hb = (lab, h, ok) => !h ? "" : `<div class="hit">${lab}<div><b class="num">${h.hit == null ? "–" : Math.round(h.hit) + "%"}</b> <span class="muted">of ${h.calls} calls ${ok}, vs ${Math.round(h.base)}% for any industry in any month</span></div>
    <div class="hitbar"><i style="width:${Math.round(h.hit || 0)}%;max-width:60%;background:var(--ink2)"></i><i style="width:${Math.round(h.base)}%;max-width:60%;background:var(--axis)"></i></div></div>`;
  $("#btHits").innerHTML = hb("Underweight calls", bt.hit.under, `lagged the market by ${band}%+`) + hb("Overweight calls", bt.hit.over, `beat the market by ${band}%+`) +
    hb("Playbook only, underweights", bt.hit.investor_under, `lagged by ${band}%+`) + hb("Playbook only, overweights", bt.hit.investor_over, `beat by ${band}%+`);
  const L = D.live, sc = L && L.scored && L.scored[H];
  $("#liveBox").innerHTML = !L || !L.rows ? `<div><h3>Live record</h3><p>Every month's state and calls are saved permanently once the month ends, starting with October 2026, so the record can't be edited later. First results: 6-month calls in April 2027, 12-month calls in October 2027.</p></div>`
    : `<div><h3>Live record since ${mlab(L.first)}</h3><p>${sc && (sc.over.calls + sc.under.calls) ? `Underweight calls lagged the market by ${band}%+ in ${sc.under.hit ?? "–"}% of ${sc.under.calls} cases; overweight calls beat it in ${sc.over.hit ?? "–"}% of ${sc.over.calls}.` : "No call has reached its end date yet."} ${sc ? `${sc.pending} calls still running.` : ""}</p></div>`;
}

/* ------------------------------------------------------------------ 5 how it works */
function renderHow(){
  const P = PIL(), rep = D.report || {}, S = D.settings;
  const rows = D.meta.indicators.filter(i => i.pillar).map(i => { const r = rep[i.id];
    return `<tr><td>${esc(i.name)}</td><td>${esc(P[i.pillar][1])}</td><td>${esc(whoText(i.who))}</td>
      <td class="r">${r && r.worst_fifth_fwd != null ? `${pct(r.worst_fifth_fwd, 1)} <span class="muted">vs ${pct(r.normal_fwd, 1)}</span>` : "–"}</td>
      <td class="r">${r && r.pre_recession != null ? `${r.pre_recession} <span class="muted">(${r.recessions})</span>` : "–"}</td></tr>`; }).join("");
  const nInv = new Set(D.meta.indicators.flatMap(i => i.who.map(w => w[0]))).size;
  const rr = STATES.map(k => { const r = D.meta.rules[k]; return `<tr><td><b>${D.meta.stages[k][0]}</b></td><td>${r.over.join(", ")}</td><td>${r.under.join(", ")}</td><td>${esc(r.why)}</td><td>${esc(whoText(r.who))}</td></tr>`; }).join("") +
    `<tr><td><b>Market stress</b> (on top)</td><td>${D.meta.stress_rule.over.join(", ")}</td><td>${D.meta.stress_rule.under.join(", ")}</td><td>${esc(D.meta.stress_rule.why)}</td><td>${esc(whoText(D.meta.stress_rule.who))}</td></tr>`;
  $("#how").innerHTML = `<ol>
    <li><b>Investors suggest the indicators.</b> ${D.meta.indicators.length} indicators from ${nInv} investors in our transcript library and Galt's X posts.</li>
    <li><b>Each reading gets a score from 0 to 100</b>: how it compares with all its own past readings up to that month. Economic data enter only once they were published.</li>
    <li><b>Three dials set the state.</b> Economy: growth and market health, 6-month average; high and rising pressure is Contraction, high and easing Recovery, low and easing Expansion, low and rising Late cycle. Inflation: hot from ${S.inflation_hot[0]} (turns Expansion and Late cycle into Overheating, Contraction into Stagflation). Market stress: risk-off from ${S.stress_high[0]}.</li>
    <li><b>The state picks the investors' playbook</b> (table below); market stress adds its own buy and avoid list on top. Where the two clash, they cancel out.</li>
    <li><b>History check.</b> A playbook call stands only if, in past months of the same situation, the industry ETF on average moved the same way against the S&P 500 over the next 6 or 12 months. At least ${S.evidence_min_months} past months are needed.</li>
    <li><b>Nothing is fitted to the whole history.</b> Each month uses only what was known then. The live record keeps scoring the calls as they come due.</li></ol>
    <div><h3 style="font-size:15px;margin:0 0 6px">The investors' playbook</h3></div>
    <div class="tablewrap"><table><thead><tr><th>State</th><th>Buy</th><th>Avoid</th><th>Why</th><th>From</th></tr></thead><tbody>${rr}</tbody></table></div>
    <div><h3 style="font-size:15px;margin:0 0 6px">Indicator report card</h3><p class="sub" style="font-size:13.5px">What followed when each indicator was in its worst fifth. Stocks = S&P 500 over the next 12 months. Before recessions = its average score 6 months before a recession began (number of recessions in brackets).</p></div>
    <div class="tablewrap"><table><thead><tr><th>Indicator</th><th>Area</th><th>Suggested by</th><th class="r">Stocks next 12 months</th><th class="r">Before recessions</th></tr></thead><tbody>${rows}</tbody></table></div>
    <p class="muted" style="font-size:12.5px;margin:0">Data: FRED (St. Louis Fed)${D.fred_key ? ", first-published values" : ""}, Kenneth French data library, Yahoo Finance, multpl.com. Version ${D.version}. Not investment advice.</p>`;
}

/* ------------------------------------------------------------------ boot */
function renderAll(){ renderStage(); renderPillars(); renderIndustries(); renderBacktest(); renderHow(); }
function setH(h){ H = h; store.set("mc-h", h); document.querySelectorAll("#horizon button").forEach(b => b.setAttribute("aria-pressed", b.dataset.h === H));
  renderIndustries(); renderBacktest(); }
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
