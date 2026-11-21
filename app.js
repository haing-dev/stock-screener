/* Quality Triage - static front end for three triages (hidden, emerging, core), in the shape of the biotech
   crash/slide triage. Reads data/data.bin (gzip'd JSON, AES-GCM, key from the password via PBKDF2-SHA256), built by
   triage/build.py + triage/site.py. Nothing leaves the browser.
   Routes: #/<kind>/<view>  kind = hidden | emerging | core; view = screener (default) | backtest | track | method | c/<id> */
"use strict";
const $ = s => document.querySelector(s);
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const store = {get(k){ try { return localStorage.getItem(k); } catch(e){ return null; } },
  set(k,v){ try { localStorage.setItem(k, v); } catch(e){} }, del(k){ try { localStorage.removeItem(k); } catch(e){} }};
const ICON = {g:"✓", r:"✕", n:"–"};
const VERDICT = {
  overdone:["p-good","▲","Buy candidate"],
  close:["p-warn","●","Watch"],
  justified:["p-crit","■","Avoid"],
  tbu:["p-pend","","TBU"]};
const CALLS = ["overdone","close","justified"];
const OUTCOME = {Winner:"p-good", Gain:"p-warn", Loss:"p-crit"};
const KORDER = ["hidden","emerging","core"];
const pill = v => { const [c,i,t] = VERDICT[v] || VERDICT.tbu; return `<span class="pill ${c}">${i?`<i>${i}</i>`:""}${t}</span>`; };
const pct = v => { if (v == null) return "–"; const r = Math.round(v); return `${r > 0 ? "+" : r < 0 ? "−" : ""}${Math.abs(r)}%`; };
const money = v => v == null ? "N/A" : v >= 1e12 ? `$${(v/1e12).toFixed(2)}T` : v >= 1e9 ? `$${(v/1e9).toFixed(1)}B` : v >= 1e7 ? `$${(v/1e6).toFixed(0)}M` : `$${(v/1e6).toFixed(1)}M`;
const usd = v => v == null ? "–" : "$" + Math.round(v).toLocaleString("en-US");
const mcapBucket = v => v == null ? "N/A" : v < 3e8 ? "Under $300M" : v < 2e9 ? "$300M–2B" : v < 1e10 ? "$2–10B" : v < 1e11 ? "$10–100B" : "Over $100B";
const MCAPB = ["Under $300M","$300M–2B","$2–10B","$10–100B","Over $100B","N/A"];
let D = null, K = "hidden", SHOW = 60, MODE = "screener", SORT = 0, KEY = null, INFO = null;
const kd = () => D.kinds[K];
const items = () => kd().items;
const base = () => `#/${K}`;
const monthsAgo = c => Math.max(0, Math.round((Date.parse((D.mark || D.updated).slice(0, 10)) - Date.parse(c.date)) / (864e5 * 30.44)));
const cname = s => String(s || "").replace(/\s*\/[A-Z]{2,}\/?\s*$/, "").replace(/\b([A-Z])([A-Z&]+)\b/g, (m, a, b) => m.length <= 3 ? m : a + b.toLowerCase());

/* ------------------------------------------------------------------ crypto (same scheme as the archived portal) */
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
  tip.style.left = x + "px"; tip.style.top = (y < 8 ? e.clientY + 18 : y) + "px"; }
function hideTip(){ tip.style.opacity = 0; }

/* ------------------------------------------------------------------ the two tables */
function cell(f, wide){ const [k,v,n] = f || ["n","N/A",""], t = n ? ` title="${esc(n)}"` : "";
  return v === "N/A" ? `<td class="f f-na"${t}>N/A</td>` : `<td class="f f-${k}${n?" tip":""}"${t}><span class="ic">${ICON[k]||""}</span>${esc(v)}</td>`; }
const trigText = c => K === "hidden" ? `<span class="num">${pct(c.move)}</span><div class="muted sm">from 12-month high</div>`
  : `<span class="num">${c.p_own != null ? `${Math.round(c.p_own * 100)}%` : "–"}</span><span class="muted sm"> of own past</span>`
    + `<div class="muted sm">${c.p_peer != null ? `${Math.round(c.p_peer * 100)}% of peers` : "no peer group"}</div>`;
const retCell = c => c.ret == null ? `<td class="r muted">N/A</td>` :
  `<td class="r" style="white-space:nowrap" title="Bought at the open of ${esc(c.entry_date)}${c.upgraded ? " (the next entry day after the 13F that turned it Buy)" : ""}; valued at ${esc(c.ret_to)}">
   <span class="num" style="color:${c.ret >= 0 ? "var(--good)" : "var(--bad)"}">${pct(c.ret)}</span>
   <div class="muted sm">${c.ctrl_ret != null ? `similar ${pct(c.ctrl_ret)}` : ""}${c.idx_ret != null ? ` · index ${pct(c.idx_ret)}` : ""}${c.stopped ? `<br>stopped trading ${esc(c.stopped)}` : ""}</div></td>`;
const rowsFor = mode => items().filter(c => mode === "backtest" ? c.played : !c.played);
const bucketOf = (c, k) => k === "mcap" ? mcapBucket(c.mcap) : c.factors?.[k]?.[3] || "N/A";

function viewTable(mode){
  MODE = mode; SHOW = 60; SORT = 0;
  const k = kd(), rows = rowsFor(mode), bt = mode === "backtest";
  const years = [...new Set(rows.map(c => c.date.slice(0,4)))].sort().reverse();
  const opts = key => { const seen = new Set(rows.map(c => bucketOf(c, key))); const order = key === "mcap" ? MCAPB : [...seen].sort((a, b) => a === "N/A" ? 1 : b === "N/A" ? -1 : a.localeCompare(b)); return order.filter(o => seen.has(o)); };
  const sel = (id, list) => `<select class="hsel" id="${id}"><option value="">All</option>${list.map(([v,l]) => `<option value="${esc(v)}">${esc(l)}</option>`).join("")}</select>`;
  const nT = rows.filter(c => c.verdict === "tbu").length;
  $("#app").innerHTML = `
  <div class="toprow"><div class="lead"><h1>${bt ? "Backtest" : "Screener"} · ${esc(k.label)}</h1><div class="muted">${rows.length} times ${esc(k.event)}. ${bt
     ? "A full year since the call: total return if bought at the open of the next trading day and held 12 months · Winner +20% or more, Gain 0 to +20%, Loss below 0"
     : "Less than a year since the call: total return if bought at the open of the next trading day, to the latest close"} · a Watch turns Buy candidate when a top performer owner's 13F shows a 3%+ position${nT ? ` · ${nT} TBU: an input for that date is still being collected` : ""}</div></div>
   <div class="filters"><select id="fy"><option value="">All years</option>${years.map(y=>`<option>${y}</option>`).join("")}</select>
    <input id="fq" placeholder="Search company or ticker"></div></div>
  <div class="tablewrap"><table class="crash"><thead>
   <tr><th>Company</th><th class="r sortable" id="sort_t" title="Sort">${K === "hidden" ? "Fall" : "Cheaper than"} <span id="t_ic">⇅</span></th><th class="r">Market Cap at Event</th>
    ${k.cells.map(([key, label, w]) => `<th class="fh${key === "insider" ? " sortable" : ""}" ${key === "insider" ? 'id="sort_ins" title="Sort: biggest net buying first"' : ""}>${esc(label)}<div class="sm muted">weight ${w}</div></th>`).join("")}
    <th class="sortable" id="sort_s" title="Sort by score">Call <span id="s_ic">⇅</span></th><th class="r">${bt ? "1-Year Return" : "Return"}</th>${bt ? "<th>Outcome</th>" : ""}</tr>
   <tr class="frow"><th></th><th></th><th>${sel("f_mcap", opts("mcap").map(o => [o,o]))}</th>
    ${k.cells.map(([key]) => `<th>${sel("f_"+key, opts(key).map(o => [o,o]))}</th>`).join("")}
    <th>${sel("f_verdict", Object.entries(VERDICT).filter(([v]) => rows.some(c => (c.verdict||"tbu") === v)).map(([v,x]) => [v, x[2]]))}</th><th></th>
    ${bt ? `<th>${sel("f_outcome", ["Winner","Gain","Loss"].map(o => [o,o]))}</th>` : ""}</tr>
  </thead><tbody id="rows"></tbody></table></div>
  <div class="legend"><span class="lg f-g"><span class="ic">✓</span>Meets the thesis</span><span class="lg f-n"><span class="ic">–</span>In between</span><span class="lg f-r"><span class="ic">✕</span>Against the thesis</span>
   <span class="muted" id="cnt"></span></div><div class="more" id="more"></div>`;
  document.querySelectorAll("#fy,#fq,.hsel").forEach(el => el.addEventListener("input", () => { SHOW = 60; fill(); }));
  document.querySelectorAll(".hsel").forEach(el => el.addEventListener("click", e => e.stopPropagation()));
  const setSort = (v, ic) => { SORT = SORT === v ? -v : v; ["t_ic","s_ic"].forEach(i => $("#"+i).textContent = "⇅"); if (ic) $("#"+ic).textContent = SORT > 0 ? "↓" : "↑"; SHOW = 60; fill(); };
  $("#sort_t").onclick = () => setSort(1, "t_ic");
  $("#sort_s").onclick = () => setSort(2, "s_ic");
  if ($("#sort_ins")) $("#sort_ins").onclick = () => setSort(3, null);
  fill();
}
function fill(){
  const k = kd(), bt = MODE === "backtest", val = id => $("#"+id)?.value || "";
  const y = val("fy"), q = val("fq").trim().toLowerCase(), v = val("f_verdict"), o = val("f_outcome");
  const keys = ["mcap", ...k.cells.map(f => f[0])], fv = Object.fromEntries(keys.map(x => [x, val("f_"+x)]));
  const list = rowsFor(MODE).filter(c => (!y || c.date.startsWith(y)) && (!v || (c.verdict||"tbu") === v)
    && (!o || c.outcome === o) && keys.every(x => !fv[x] || bucketOf(c, x) === fv[x])
    && (!q || `${c.name} ${c.ticker}`.toLowerCase().includes(q)));
  const trig = c => K === "hidden" ? -(c.move ?? 0) : (c.p_own ?? c.p_peer ?? 0);
  if (Math.abs(SORT) === 1) list.sort((a, b) => Math.sign(SORT) * (trig(b) - trig(a)));
  if (Math.abs(SORT) === 2) list.sort((a, b) => Math.sign(SORT) * ((b.score ?? -9) - (a.score ?? -9)));
  if (Math.abs(SORT) === 3) list.sort((a, b) => Math.sign(SORT) * ((b.insider_net ?? 0) - (a.insider_net ?? 0)));
  $("#rows").innerHTML = list.slice(0, SHOW).map(c => `<tr data-id="${c.id}"><td class="co"><b>${esc(cname(c.name))}</b><div class="muted sm">${esc(c.ticker)} · ${esc(c.date)} · ${monthsAgo(c)} mo ago</div></td>
    <td class="r" style="white-space:nowrap">${trigText(c)}</td>
    <td class="r ${c.mcap == null ? "muted" : ""}" style="white-space:nowrap">${money(c.mcap)}${c.price != null ? `<div class="muted sm">$${c.price < 1 ? c.price.toFixed(3) : c.price.toFixed(2)}/share</div>` : ""}</td>
    ${k.cells.map(f => cell(c.factors?.[f[0]])).join("")}
    <td${c.why?.length ? ` title="${esc(c.why.join(" · "))}"` : ""}>${pill(c.verdict)}<div class="muted sm">${c.score != null && c.verdict !== "tbu" ? `score ${c.score >= 0 ? "+" : "−"}${Math.abs(c.score).toFixed(2)}` : ""}${c.upgraded ? `<br>from Watch, ${esc(c.call_date)}` : ""}</div></td>${retCell(c)}
    ${bt ? `<td>${c.outcome ? `<span class="pill ${OUTCOME[c.outcome]}">${c.outcome}</span>` : ""}</td>` : ""}</tr>`).join("") ||
    `<tr><td colspan="30" class="empty">${rowsFor(MODE).length ? "Nothing matches these filters." : MODE === "backtest" ? "No event has a full year yet." : "No open events."}</td></tr>`;
  $("#cnt").textContent = `Showing ${Math.min(SHOW, list.length)} of ${list.length}.`;
  $("#more").innerHTML = list.length > SHOW ? `<button id="mb">Show more</button>` : "";
  if (list.length > SHOW) $("#mb").onclick = () => { SHOW += 60; fill(); };
  document.querySelectorAll("#rows tr[data-id]").forEach(tr => tr.onclick = () => location.hash = `${base()}/c/${tr.dataset.id}`);
}

/* ------------------------------------------------------------------ one event */
function viewOne(id){
  const k = kd(), c = items().find(x => x.id === id);
  if (!c){ $("#app").innerHTML = `<p class="empty">Not found. <a href="${base()}">Back</a></p>`; return; }
  const back = c.played ? `${base()}/backtest` : base();
  const pts = {g: 1, r: -1};
  const cards = k.cells.map(([key, label, w]) => { const f = c.factors?.[key] || ["n","N/A",""];
    const contrib = f[1] === "N/A" ? 0 : (pts[f[0]] || 0) * w;
    const wl = `<span class="fw">${contrib > 0 ? "+" : contrib < 0 ? "−" : ""}${Math.abs(contrib)} of ${w}</span>`;
    if (f[1] === "N/A") return `<div class="fc f-na"><div class="fl"><span>${esc(label)}</span>${wl}</div><div class="fv">N/A</div><div class="fn">${esc(f[2]||"")}</div></div>`;
    return `<div class="fc f-${f[0]}"><div class="fl"><span>${esc(label)}</span>${wl}</div><div class="fv"><span class="ic">${ICON[f[0]]||""}</span>${esc(f[1])}</div><div class="fn">${esc(f[2]||"")}</div></div>`; }).join("");
  const after = c.ret == null ? "" : `<div class="card"><h4>What happened next</h4><div class="tiles">
     <div><b>${pct(c.ret)}</b><span>${c.played ? "12-month total return" : `total return to ${esc(c.ret_to)}`} if bought at the open of ${esc(c.entry_date)}${c.stopped ? `; stopped trading in ${esc(c.stopped)}, valued at its last close` : ""}</span></div>
     ${c.ctrl_ret == null ? "" : `<div><b>${pct(c.ctrl_ret)}</b><span>the 10 most similar US stocks bought the same day (market cap, 12-month price change, earnings yield)</span></div>`}
     ${c.idx_ret == null ? "" : `<div><b>${pct(c.idx_ret)}</b><span>${esc(k.index)} over the same months</span></div>`}
     ${c.outcome ? `<div><b><span class="pill ${OUTCOME[c.outcome]}">${c.outcome}</span></b><span>outcome</span></div>` : ""}</div><div id="onepath"></div></div>`;
  const head = K === "hidden" ? `Scan ${esc(c.date)}: ${pct(c.move)} from its 12-month high`
    : `Scan ${esc(c.date)}: ${c.p_own != null ? `cheaper than ${Math.round(c.p_own * 100)}% of its own past scans` : "own past N/A"} · ${c.p_peer != null ? `cheaper than ${Math.round(c.p_peer * 100)}% of its industry` : "no peer group"}`;
  const why = c.why?.length ? esc(c.why.join(" · ")) : c.verdict === "overdone" ? `Score ${c.score >= 0 ? "+" : "−"}${Math.abs(c.score).toFixed(2)} (Buy candidate from +${D.rules.buy_at.toFixed(2)}) and no hard Avoid` : "";
  $("#app").innerHTML = `
  <div class="vhead"><div><div class="muted">${head} · <a href="${back}">‹ ${c.played ? "Backtest" : "Screener"}</a></div>
    <h2>${esc(cname(c.name))} <span class="muted" style="font-size:18px">${esc(c.ticker)}</span><span class="muted" style="font-size:16px;margin-left:8px">${monthsAgo(c)} months ago</span></h2>
    <div class="what1">Market cap at the event ${money(c.mcap)}${c.price != null ? ` · $${c.price.toFixed(2)} a share` : ""} · industry code ${esc(c.sic || "–")}</div></div>
   <div class="vbox">${pill(c.verdict)}<div class="conf">${why}</div></div></div>
  <div class="fcs">${cards}</div>
  ${after}
  <div class="card srcs"><h4>Sources</h4><a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=${Number(c.cik)}&type=&dateb=&owner=include&count=40" target="_blank" rel="noopener">All SEC filings</a><a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=${Number(c.cik)}&type=4&dateb=&owner=only&count=40" target="_blank" rel="noopener">Insider filings (Form 4)</a></div>`;
  if (c.path && c.path.length > 1){
    const n = c.path.length, ser = [{l: esc(c.ticker), col: "var(--g-line)", path: c.path}];
    if (c.ctrl_path?.length === n) ser.push({l: "Similar stocks", col: "var(--idx)", path: c.ctrl_path, dash: true});
    if (c.idx_path?.length === n) ser.push({l: k.index, col: "var(--blue)", path: c.idx_path, dash: true});
    lineChart($("#onepath"), ser, n, xlab(n), {...PCT, at: j => j ? `Month ${j}` : "Bought"});
  }
}

/* ------------------------------------------------------------------ charts */
function lineChart(el, series, n, xl, fmt){
  const W = Math.max(520, el.clientWidth - 32), H = 320, left = 56, right = 150, top = 14, bot = 40;
  const all = series.flatMap(s => s.path), lo = fmt.lo(Math.min(...all)), hi = fmt.hi(Math.max(...all));
  const x = i => left + i / Math.max(1, n - 1) * (W - left - right), y = v => top + (hi - v) / (hi - lo) * (H - top - bot);
  let s = `<div class="chartleg">${series.map(r => `<span><i class="ln" style="background:${r.col}"></i>${esc(r.l)}</span>`).join("")}</div><svg width="${W}" height="${H}">`;
  fmt.ticks(lo, hi).forEach(t => s += `<line x1="${left}" x2="${W-right}" y1="${y(t)}" y2="${y(t)}" stroke="${t===fmt.zero?"var(--axis)":"var(--line)"}"/><text x="${left-8}" y="${y(t)+4}" text-anchor="end">${fmt.tick(t)}</text>`);
  xl.forEach(([i, l]) => s += `<text x="${x(i)}" y="${H-16}" text-anchor="middle">${esc(l)}</text>`);
  const ends = series.map((r,i) => ({i, y: y(r.path[r.path.length-1])})).sort((a,b) => a.y - b.y); let last = -1e9;
  ends.forEach(e => { e.ly = Math.max(e.y, last + 18); last = e.ly; });
  series.forEach((r, i) => { const m = r.path.length; s += `<path d="M${r.path.map((v,j)=>`${x(j).toFixed(1)},${y(v).toFixed(1)}`).join(" L")}" fill="none" stroke="${r.col}" stroke-width="2.5" ${r.dash?'stroke-dasharray="6 5"':""}/>`;
    const e = ends.find(z => z.i === i); s += `<circle cx="${x(m-1)}" cy="${y(r.path[m-1])}" r="4.5" fill="${r.col}"/><text class="lab" x="${x(m-1)+10}" y="${e.ly+4}" font-weight="700">${fmt.end(r.path[m-1])}</text>`; });
  s += `<line class="xh" y1="${top}" y2="${H-bot}" stroke="var(--axis)" opacity="0"/><rect x="${left}" y="${top}" width="${W-left-right}" height="${H-top-bot}" fill="transparent" class="hit"/></svg>`;
  el.insertAdjacentHTML("beforeend", s);
  const hit = el.querySelector(".hit"), xh = el.querySelector(".xh");
  hit.onmousemove = e => { const b = hit.getBoundingClientRect(), j = Math.max(0, Math.min(n-1, Math.round((e.clientX - b.left) / b.width * (n - 1))));
    xh.setAttribute("x1", x(j)); xh.setAttribute("x2", x(j)); xh.setAttribute("opacity", 1);
    showTip(e, `<b>${esc(fmt.at(j))}</b>` + series.map(r => `${esc(r.l)}: ${r.path[j] == null ? "–" : fmt.end(r.path[j])}`).join("<br>")); };
  hit.onmouseleave = () => { xh.setAttribute("opacity", 0); hideTip(); };
}
const PCT = {lo: v => Math.floor(Math.min(-10, v) / 10) * 10, hi: v => Math.ceil(Math.max(10, v) / 10) * 10, zero: 0,
  ticks: (lo, hi) => { const st = (hi - lo) > 120 ? 20 : 10, o = []; for (let t = lo; t <= hi; t += st) o.push(t); return o; },
  tick: t => t === 0 ? "0%" : (t > 0 ? "+" : "−") + Math.abs(t) + "%", end: v => pct(v)};
const xlab = n => [0,3,6,9,12].filter(i => i < n).map(i => [i, i ? `month ${i}` : "bought"]);

/* ------------------------------------------------------------------ track record */
const f1 = v => v == null ? "–" : pct(v);
const tstat = t => t == null ? "" : `<span class="muted sm"> (t ${t.toFixed(1)})</span>`;
function regTable(R){
  if (!R) return `<p class="muted">Factor data not loaded yet (Kenneth French data library).</p>`;
  const rows = [["overdone","Buy candidates"],["close","Watch"],["justified","Avoid"],["long_short","Buy minus Avoid"]].filter(([k]) => R[k]);
  if (!rows.length || rows.every(([k]) => R[k].alpha_m == null)) return `<p class="muted">Needs 12+ months of holdings (${Object.values(R.months_held||{}).join(" / ") || 0} so far).</p>`;
  const F = ["Mkt-RF","SMB","HML","RMW","CMA","UMD"];
  return `<div class="tablewrap"><table class="stats"><thead><tr><th>Portfolio</th><th class="r">Months</th><th class="r">Avg month</th><th class="r">Alpha / year</th>${F.map(f => `<th class="r">${f}</th>`).join("")}<th class="r">R²</th></tr></thead><tbody>
   ${rows.map(([k, l]) => { const r = R[k]; if (r.alpha_m == null) return `<tr><td>${l}</td><td class="r">${r.n}</td><td colspan="9" class="muted">too few months</td></tr>`;
     return `<tr><td>${l}</td><td class="r">${r.n}</td><td class="r">${r.mean_m >= 0 ? "+" : ""}${r.mean_m.toFixed(2)}%</td><td class="r"><b>${r.alpha_y >= 0 ? "+" : ""}${r.alpha_y.toFixed(1)}%</b>${tstat(r.t)}</td>
     ${F.map(f => `<td class="r">${r.betas[f][0].toFixed(2)}${tstat(r.betas[f][1])}</td>`).join("")}<td class="r">${r.r2 ?? "–"}</td></tr>`; }).join("")}</tbody></table></div>`;
}
function evidenceTable(E){
  const rows = Object.entries(E || {});
  if (!rows.length) return "";
  const c = (x, col) => x ? `<td class="r f f-${col}">${pct(x.median)}<div class="sm" style="font-weight:400">n ${x.n} · beat ${x.beat}%</div></td>` : `<td class="r muted">–</td>`;
  return `<div class="tablewrap"><table class="stats"><thead><tr><th>Cell</th><th class="r">Weight</th><th class="r">✓ green</th><th class="r">– between</th><th class="r">✕ red</th><th class="r">Green minus red</th><th class="r">N/A</th></tr></thead><tbody>
   ${rows.map(([k, e]) => { const g = e.cols.g, r = e.cols.r; return `<tr><td>${esc(e.label)}</td><td class="r">${e.weight}</td>${c(g,"g")}${c(e.cols.n,"n")}${c(r,"r")}
     <td class="r"><b>${g && r ? pct(g.median - r.median) : "–"}</b></td><td class="r muted">${e.na}</td></tr>`; }).join("")}</tbody></table></div>`;
}
function viewTrack(){
  const k = kd(), T = k.track, Y = k.years || {}, ys = Object.keys(Y).sort(), C = k.calls || {};
  const last = a => a?.length ? a[a.length - 1] : null;
  const live = (D.live || []).filter(r => r.kind === K).slice(0, 40);
  $("#app").innerHTML = `<div class="toprow"><div class="lead"><h1>Track record · ${esc(k.label)}</h1><div class="muted">Buy candidates bought at the open of the first trading day after the scan of the call and held 12 months, against the 10 most similar US stocks bought the same day and ${esc(k.index)} over the same months.</div></div></div>
   <div class="card" id="tr"><h4>Average return after buying${T ? ` · ${T.n} Buy candidates with a full year` : ""}</h4>${T ? `<div class="tiles" style="margin-bottom:12px">
     <div><b>${f1(last(T.own))}</b><span>Buy candidates, 12 months later</span></div><div><b>${f1(last(T.ctrl))}</b><span>similar stocks</span></div><div><b>${f1(last(T.idx))}</b><span>${esc(k.index)}</span></div></div>` : `<p class="empty">Appears once Buy candidates have a full year of prices.</p>`}</div>
   <div class="card"><h4>One year after the call, by call (events with a full year)</h4>${Object.keys(C).length ? `<div class="tablewrap"><table class="stats">
     <thead><tr><th>Call</th><th class="r">Events</th><th class="r">Median</th><th class="r">Average*</th><th class="r">Similar stocks</th><th class="r">Index</th><th class="r">Beat similar</th><th class="r">Up 20%+</th><th class="r">Down 50%+</th></tr></thead><tbody>
     ${CALLS.filter(v => C[v]).map(v => { const s = C[v]; return `<tr><td>${pill(v)}</td><td class="r">${s.n}</td><td class="r">${f1(s.median)}</td><td class="r"><b>${f1(s.mean)}</b></td><td class="r">${f1(s.ctrl_mean)}</td><td class="r">${f1(s.idx_mean)}</td><td class="r">${s.beat ?? "–"}%</td><td class="r">${s.up20}%</td><td class="r">${s.down50}%</td></tr>`; }).join("")}</tbody></table></div>` : `<p class="muted">No event has a full year yet.</p>`}</div>
   <div class="card" id="pf"><div class="toprow" style="margin-bottom:4px"><h4 style="margin:0">$10,000 test: all Buy candidates of one year, equal money in each, each held 12 months</h4>
     ${ys.length ? `<select id="py">${ys.map(y => `<option${y === ys[Math.max(0, ys.length - 2)] ? " selected" : ""}>${y}</option>`).join("")}</select>` : ""}</div><div id="pfb">${ys.length ? "" : `<p class="muted">No Buy candidates yet.</p>`}</div></div>
   <div class="card"><h4>Factor regression: is it more than market, size, value, profitability, investment and momentum?</h4>${regTable(k.regression)}
     <div class="fnote">Each month, the return of an equal-weighted portfolio of every event held (12 months after each call's entry; rebalanced at each scan), regressed on the Fama-French five factors and momentum (Kenneth French data library) with Newey-West t-statistics. Alpha = the average monthly return the factors don't explain, compounded to a year. |t| above 2 is the usual bar; a few years of data rarely clear it.</div></div>
   <div class="card"><h4>Which cells mattered: 12-month return minus the similar stocks', median, by the cell's colour (all calls with a full year)</h4>${evidenceTable(k.evidence) || `<p class="muted">No event has a full year yet.</p>`}
     <div class="fnote">The weights were set before any result was seen (Method). This table is the check on them: a cell whose green events don't beat its red ones isn't earning its weight.</div></div>
   <div class="card"><h4>Live calls (recorded when made, before the outcome was known)</h4>${live.length ? `<div class="tablewrap"><table class="stats"><thead><tr><th>Called</th><th>Company</th><th>Call then</th><th>Now</th><th class="r">Return since entry</th><th class="r">Similar stocks</th></tr></thead><tbody>
     ${live.map(r => `<tr><td>${esc(r.called_utc)}</td><td><a href="${base()}/c/${esc(r.id)}">${esc(cname(r.name))}</a> <span class="muted">${esc(r.ticker)}</span></td><td>${pill(r.call)}</td><td>${r.now ? pill(r.now) : ""}</td><td class="r">${f1(r.ret)}</td><td class="r">${f1(r.ctrl_ret)}</td></tr>`).join("")}</tbody></table></div>` : `<p class="muted">None yet: a call is recorded when an event within 45 days of the build gets one.</p>`}</div>
   <div class="fnote">*Each return capped at +500%. Total return: price change plus cash dividends; a company that stopped trading counts at its last close (−30% if none was found) and as cash after; splits are taken out. No trading costs. Similar stocks: the 10 closest US stocks of $100M+ on market cap, 12-month price change and earnings yield on the scan day, with no event of the same triage in the 6 months before.</div>`;
  if (T) lineChart($("#tr"), [{l: "Buy candidates", col: "var(--g-line)", path: T.own}, {l: "Similar stocks", col: "var(--idx)", path: T.ctrl, dash: true},
    {l: k.index, col: "var(--blue)", path: T.idx, dash: true}], T.own.length, xlab(T.own.length), {...PCT, at: j => j ? `Month ${j}` : "Bought"});
  const draw = () => { const y = $("#py").value, v = Y[y], n = v.path.own.length, m = a => a.map(q => 10000 * (1 + q / 100));
    $("#pfb").innerHTML = `<div class="tiles" style="margin:8px 0 10px"><div><b>${usd(v.own)}</b><span>in ${v.n} Buy candidates of ${y}</span></div><div><b>${usd(v.ctrl)}</b><span>in their similar stocks</span></div><div><b>${usd(v.idx)}</b><span>in ${esc(k.index)}</span></div></div>
      ${v.open ? `<div class="fnote" style="margin:0 0 8px">${v.open} of them bought less than a year ago: valued at the latest close.</div>` : ""}`;
    const ser = [{l: "Buy candidates", col: "var(--g-line)", path: m(v.path.own)}];
    if (v.path.ctrl.length === n) ser.push({l: "Similar stocks", col: "var(--idx)", path: m(v.path.ctrl), dash: true});
    if (v.path.idx.length === n) ser.push({l: k.index, col: "var(--blue)", path: m(v.path.idx), dash: true});
    if (n > 1) lineChart($("#pfb"), ser, n, xlab(n),
      {lo: v => Math.floor(Math.min(10000, v) / 2000) * 2000, hi: v => Math.ceil(Math.max(10000, v) / 2000) * 2000, zero: 10000,
       ticks: (lo, hi) => { const st = (hi - lo) > 16000 ? 4000 : 2000, o = []; for (let t = lo; t <= hi; t += st) o.push(t); return o; },
       tick: t => "$" + (t / 1000) + "k", end: v => usd(v), at: j => j ? `Month ${j}` : "Bought"}); };
  if (ys.length) { $("#py").onchange = draw; draw(); }
}

/* ------------------------------------------------------------------ method */
function viewMethod(){
  const k = kd(), b = k.backend;
  const bands = {g: "meets the thesis (+weight)", n: "in between or N/A (0)", r: "against it (−weight)"};
  $("#app").innerHTML = `<div class="method"><div class="toprow"><div class="lead"><h1>Method · ${esc(k.label)}</h1><p class="muted">${esc(k.thesis)}</p></div></div>
   <div class="grid2"><div class="card"><h3>1. Which stocks are covered (backend only, never part of the score)</h3><ul>
     <li>US common stock: a 10-K filer reporting in US dollars, listed on NYSE, Nasdaq or NYSE American; no funds, REITs, SPACs${K === "hidden" ? ", banks or insurers" : ", banks, insurers or excluded industries"}</li>
     <li>${b.min_years}+ years of SEC financial data; latest annual report at most 1.6 years old</li>
     <li>Market cap ${money(b.min_mcap)}${b.max_mcap ? `–${money(b.max_mcap)}` : "+"} (price × share count from SEC filings, cross-checked)${b.min_revenue ? `; revenue ${money(b.min_revenue)}+` : ""}</li>
     <li>Average daily value traded ${money(b.min_adv)}+</li>
     <li>Net debt at most ${b.max_lev}× EBITDA (net cash always passes)</li></ul></div>
   <div class="card"><h3>2. The event (the dated buy point)</h3><p>Scans run twice a month: the last trading day on or before the 15th, and the last trading day of the month. The event is the first scan on which ${esc(k.event)}, after a scan on which it didn't, and at least 6 months after the company's previous event in this triage. Only data filed or traded by that month-end is used.</p>
     <p>Entry: the open of the next trading day. Outcome: total return over the next 12 months.</p></div></div>
   <div class="card"><h3>3. The call: weighted cells</h3><p>Each cell scores +weight when green, −weight when red, 0 when in between or N/A; the score is the sum ÷ 100 (−1 to +1).
     <b>Buy candidate</b>: score ${D.rules.buy_at >= 0 ? "+" : ""}${D.rules.buy_at.toFixed(2)} or more and no hard Avoid · <b>Avoid</b>: a hard Avoid (${k.hard.map(esc).join("; ")}) or score ${D.rules.avoid_at.toFixed(2)} or less · <b>Watch</b>: the rest. A Watch turns Buy candidate when a top performer owner's 13F for the event's quarter reports it at 3%+ of its portfolio (its return counts from the next entry day). Weights were set before any backtest result was seen.</p>
     <div class="tablewrap"><table class="stats"><thead><tr><th>Cell</th><th class="r">Weight</th><th></th></tr></thead><tbody>
     ${k.cells.map(([key, label, w]) => `<tr><td>${esc(label)}</td><td class="r">${w}</td><td><span class="bar" style="width:${w * 4}px;background:var(--g-line)"></span></td></tr>`).join("")}</tbody></table></div>
     <p class="fnote">Owners and insiders, the same in all three triages: <b>High Conviction Owners</b> = 13F filers that aren't index funds, broker platforms, fund houses or quant funds, with a $100M+ stock portfolio, holding the company at 3%+ of it at the end of the last quarter whose 13F deadline had passed (green at 2+). <b>Top Performer Owners</b> = one of them ranks in the top 20 filers by their record on past events of all three triages (half hit rate weighted by conviction, half number of hits; a hit beat its similar stocks by 10+ points), using only events whose 12 months had ended. <b>Insider Buy/Sell</b> = open-market buys minus discretionary sales (10b5-1 plan sales and same-day option-exercise sales left out) in Form 4s filed in the 180 days to the scan; counts at the larger of $25K and 0.01% of market cap. Hover any cell for its exact source.</p></div>
   <div class="card"><h3>4. How it is checked</h3><ul>
     <li>Point in time: SEC financial data filed before the scan day (later restatements invisible), prices as printed that day, companies that later disappeared included.</li>
     <li>Against the 10 most similar US stocks (market cap, 12-month price change, earnings yield) and ${esc(k.index)} over the same months.</li>
     <li>Fama-French five factors + momentum regression of the calendar-time portfolios (Track record).</li>
     <li>Live calls are written to an append-only record when made (branch triage-record), so the forward record can't be edited after the fact.</li></ul></div></div>`;
}

/* ------------------------------------------------------------------ routing */
function route(){
  hideTip();
  let h = (location.hash || "#/").slice(2);
  if (!new RegExp(`^(${KORDER.join("|")})(/|$)`).test(h)) h = KORDER[0] + "/" + h;
  const [kind, ...rest] = h.split("/"), view = rest[0] || "screener";
  K = D.kinds[kind] ? kind : KORDER[0];
  document.querySelectorAll(".kind button").forEach(b => b.classList.toggle("on", b.dataset.kind === K));
  document.querySelectorAll("nav a[data-nav]").forEach(a => { a.href = `${base()}${a.dataset.nav === "screener" ? "" : "/" + a.dataset.nav}`;
    a.classList.toggle("on", a.dataset.nav === (view === "c" ? "screener" : view)); });
  document.title = `${kd().label} · Quality Triage`;
  if (view === "c") viewOne(decodeURIComponent(rest.slice(1).join("/")));
  else if (view === "track") viewTrack();
  else if (view === "method") viewMethod();
  else viewTable(view === "backtest" ? "backtest" : "screener");
  scrollTo(0, 0);
}
async function start(){
  const r = await fetch("data/data.bin", {cache: "no-cache"});
  D = await openBlob(await r.arrayBuffer());
  $("#lock").hidden = true; $("#shell").hidden = false;
  $(".kind").innerHTML = KORDER.filter(k => D.kinds[k]).map(k => `<button data-kind="${k}" role="tab">${esc(D.kinds[k].label)}</button>`).join("");
  document.querySelectorAll(".kind button").forEach(b => b.onclick = () => { location.hash = `#/${b.dataset.kind}`; });
  $("#foot").textContent = `Updated ${D.updated}${D.mark ? ` · prices to ${D.mark}` : ""} · months ${D.months ? D.months.join(" to ") : "–"} · v${D.version}. Data: SEC EDGAR (XBRL financial statements, filings, Form 4, Form 13F data sets), prices via Massive, factors from the Kenneth French data library. Not investment advice.`;
  addEventListener("hashchange", route); route();
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
  try { INFO = await (await fetch("data/keyinfo.json", {cache: "no-cache"})).json(); }
  catch(e){ showLock("No data yet: run the Triage workflow once (GitHub → Actions → Triage)."); return; }
  if (INFO.plain) { await start(); return; }
  const saved = store.get("qt-key");
  if (saved) { try { const {salt, k} = JSON.parse(saved);
      if (salt === INFO.salt) { const key = await crypto.subtle.importKey("raw", b64(k), {name: "AES-GCM"}, true, ["decrypt"]);
        if (await tryKey(key)) { await start(); return; } } } catch(e){}
    store.del("qt-key"); }
  showLock("");
})();
