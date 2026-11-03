(() => {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const el = (tag, attrs = {}, ...kids) => {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (k === "class") n.className = v; else if (k === "text") n.textContent = v;
      else if (k.startsWith("on")) n.addEventListener(k.slice(2), v); else n.setAttribute(k, v);
    }
    kids.flat().forEach(c => c != null && n.append(c));
    return n;
  };
  const post = (url, body) => fetch(url, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) }).then(r => r.json());

  /* ---- progress: saved in this browser, or on the server when logged in ---- */
  try { document.cookie = "th_tz=" + new Date().getTimezoneOffset() + ";path=/;max-age=31536000;SameSite=Lax"; } catch { /* ignore */ }
  const KEY = "techhub-done";
  let U = null;
  try { U = JSON.parse(document.getElementById("th-user").textContent); } catch { /* not logged in */ }
  let done = new Set();
  try { done = new Set(JSON.parse(localStorage.getItem(KEY) || "[]")); } catch { /* storage blocked */ }
  if (U) {
    const server = new Set(U.done), extra = [...done].filter(s => !server.has(s));
    done = new Set([...server, ...extra]);
    try { localStorage.removeItem(KEY); } catch { /* ignore */ }
    if (extra.length) post("/api/progress", { lessons: extra }).catch(() => {});
  }
  const save = () => { if (U) return; try { localStorage.setItem(KEY, JSON.stringify([...done])); } catch { /* ignore */ } };
  function paint() {
    const start = $("#startBtn");
    if (start && start.dataset.slugs) {
      const all = start.dataset.slugs.split(","), nx = all.find(s => !done.has(s));
      if (nx && done.size && nx !== all[0]) { start.href = `/${start.dataset.mod}/${nx}`; start.textContent = "Continue learning"; }
      return;
    }
    const links = $$("main a[data-slug]");
    if (start && done.size && links.length) { const nx = links.find(a => !done.has(a.dataset.slug)); if (nx) { start.href = nx.href; start.textContent = "Continue learning"; } }
  }
  const complete = slug => { if (done.has(slug)) return; done.add(slug); save(); paint(); if (U) post("/api/progress", { lesson: slug }).catch(() => {}); };
  paint();

  /* ---- menus: lesson list (small screens), site menu, dropdowns, lesson filter ---- */
  const side = $("#side"), scrim = $("#scrim"), lbtn = $("#lessonsBtn");
  if (side && lbtn) {
    const set = o => { side.classList.toggle("open", o); scrim.classList.toggle("on", o); lbtn.setAttribute("aria-expanded", String(o)); };
    lbtn.addEventListener("click", () => set(!side.classList.contains("open")));
    scrim.addEventListener("click", () => set(false));
    const on = $("#sideNav a.on"); if (on) side.scrollTop = Math.max(0, on.offsetTop - side.clientHeight / 2);
    $("#sideQ").addEventListener("input", e => {
      const f = e.target.value.trim().toLowerCase();
      $$("#sideNav .lgrp").forEach(g => {
        let any = false;
        $$("a", g).forEach(a => { const hit = !f || a.textContent.toLowerCase().includes(f); a.hidden = !hit; any = any || hit; });
        g.hidden = !any; if (f && any) g.open = true;
      });
    });
  }
  const nbtn = $("#navBtn"), smenu = $("#siteMenu");
  if (nbtn) nbtn.addEventListener("click", () => { smenu.hidden = !smenu.hidden; nbtn.setAttribute("aria-expanded", String(!smenu.hidden)); });
  const dds = $$("details.ndd");
  dds.forEach(d => d.addEventListener("toggle", () => { if (d.open) dds.forEach(o => { if (o !== d) o.open = false; }); }));
  document.addEventListener("click", e => dds.forEach(d => { if (!d.contains(e.target)) d.open = false; }));
  document.addEventListener("keydown", e => { if (e.key === "Escape") { dds.forEach(d => (d.open = false)); if (side) { side.classList.remove("open"); scrim.classList.remove("on"); } } });

  const pace = $("[data-pace]");
  if (pace) pace.addEventListener("change", async () => { await post("/api/pace", { pace: +pace.value }).catch(() => {}); location.reload(); });

  /* ---- progress widgets ---- */
  $$("[data-progress]").forEach(box => {
    const total = +box.dataset.total || 1, n = Math.min(done.size, total), pct = Math.round(n / total * 100);
    $$("[data-count]", box).forEach(e => (e.textContent = n)); $$("[data-of]", box).forEach(e => (e.textContent = total));
    $$("[data-pct]", box).forEach(e => (e.textContent = pct + "%"));
    $$("[data-barfill]", box).forEach(e => (e.style.width = pct + "%"));
    const ring = $("[data-ring]", box); if (ring) ring.style.setProperty("--p", pct);
  });

  /* ---- search (Python /api/search); works for the header box and the big home box ---- */
  $$("[data-search]").forEach(box => {
    const input = $("input", box), res = $(".gres", box); let timer;
    input.addEventListener("input", () => {
      clearTimeout(timer);
      timer = setTimeout(async () => {
        const q = input.value.trim();
        if (q.length < 2) { res.hidden = true; return; }
        try {
          const { results } = await (await fetch("/api/search?q=" + encodeURIComponent(q))).json();
          res.textContent = "";
          if (!results.length) res.append(el("p", { text: "No lessons found." }));
          results.forEach(r => res.append(el("a", { href: r.url, role: "option" }, el("span", { text: r.title }), el("small", { text: r.module }))));
          res.hidden = false;
        } catch { res.hidden = true; }
      }, 180);
    });
    input.addEventListener("keydown", e => { if (e.key === "Escape") { res.hidden = true; input.blur(); } });
    document.addEventListener("click", e => { if (!box.contains(e.target)) res.hidden = true; });
  });

  /* ---- Try it editor ----
     The preview iframe is sandboxed (scripts run, but no access to this site's cookies or storage).
     A small shim shows console output and errors under the result, and reports the page height so the
     iframe grows to fit (no inner scrollbar). */
  const PAGE_CSS = "html{scrollbar-width:thin}body{font:16px/1.6 system-ui,-apple-system,Segoe UI,sans-serif;color:#1c2536;margin:12px}";
  const SHIM = `<script>(function(){var box;function body(){return document.body||document.documentElement}
function out(c,a){if(!box){box=document.createElement('pre');box.id='th-console';box.style.cssText='margin:12px 0 0;padding:8px 10px;background:#17233d;color:#e6eeff;font:13px/1.5 ui-monospace,Consolas,monospace;border-radius:6px;white-space:pre-wrap;display:none';body().appendChild(box);}
box.style.display='block';var l=document.createElement('div');l.style.color=c;l.textContent=a.map(function(x){try{return typeof x==='object'&&x!==null?JSON.stringify(x):String(x)}catch(e){return String(x)}}).join(' ');box.appendChild(l);send();}
['log','info','warn','error'].forEach(function(k){var o=console[k];console[k]=function(){out(k==='error'?'#ff9b93':k==='warn'?'#ffd479':'#e6eeff',[].slice.call(arguments));o&&o.apply(console,arguments)}});
window.addEventListener('error',function(e){out('#ff9b93',['Error: '+e.message])});
window.addEventListener('unhandledrejection',function(e){out('#ff9b93',['Unhandled promise rejection: '+(e.reason&&e.reason.message||e.reason)])});
function send(){try{parent.postMessage({th:1,h:document.documentElement.scrollHeight},'*')}catch(e){}}
window.addEventListener('load',function(){send();setTimeout(send,300);setTimeout(send,1200);if(window.ResizeObserver)new ResizeObserver(send).observe(document.documentElement)});
})();<\/script>`;
  const buildDoc = c => {
    if (/<head[^>]*>/i.test(c)) return c.replace(/<head[^>]*>/i, m => m + SHIM);
    if (/<html[^>]*>/i.test(c)) return c.replace(/<html[^>]*>/i, m => m + SHIM);
    return `<!doctype html><meta charset="utf-8"><style>${PAGE_CSS}</style><body>${SHIM}${c}`;
  };
  /* ---- challenge checker: runs the learner's page, then the test expressions inside the sandbox ---- */
  const testRunner = (tests, nonce) => `<script>(function(){var L=window.__logs=[];function f(a){if(typeof a==='string')return a;try{return typeof a==='object'&&a!==null?JSON.stringify(a):String(a)}catch(e){return String(a)}}
var o=console.log;console.log=function(){L.push([].slice.call(arguments).map(f).join(' '));o.apply(console,arguments)};
var T=${JSON.stringify(tests).replace(/</g, "\\u003c")};
window.addEventListener('load',function(){setTimeout(async function(){
window.$=function(s){return document.querySelector(s)};window.$$=function(s){return [].slice.call(document.querySelectorAll(s))};
window.css=function(s,p,ps){var e=document.querySelector(s);return e?getComputedStyle(e,ps||null)[p]:''};
window.rgb=function(c){var d=document.createElement('div');d.style.color=c;document.body.appendChild(d);var v=getComputedStyle(d).color;d.remove();return v};
window.text=function(s){var e=document.querySelector(s);return e?e.textContent.trim():''};window.logs=L;
var R=[];for(var i=0;i<T.length;i++){var ok=false;try{ok=!!(await(0,eval)(T[i].js))}catch(e){ok=false}R.push({label:T[i].label,ok:ok})}
parent.postMessage({thCheck:1,nonce:${JSON.stringify(nonce)},results:R},'*')},650)});})();<\/script>`;

  const frames = new Map();
  addEventListener("message", e => {
    if (!e.data || e.data.th !== 1) return;
    const f = [...frames.keys()].find(fr => fr.contentWindow === e.source);
    if (f) { const min = frames.get(f); f.style.height = Math.min(Math.max(e.data.h + 2, min), 640) + "px"; }
  });
  $$("[data-editor]").forEach(box => {
    const ta = $("textarea", box), out = $("[data-out]", box);
    const min = box.classList.contains("big") ? 320 : 110;
    frames.set(out, min);
    const grow = () => { ta.style.height = "auto"; ta.style.height = Math.min(ta.scrollHeight + 2, 560) + "px"; };
    const run = () => { out.srcdoc = buildDoc(ta.value); };
    $("[data-run]", box).addEventListener("click", run);
    const orig = ta.value, rs = $("[data-reset]", box);
    if (rs) rs.addEventListener("click", () => { ta.value = orig; grow(); run(); });
    ta.addEventListener("input", grow);
    ta.addEventListener("keydown", e => {
      if ((e.ctrlKey || e.metaKey) && e.key === "Enter") { e.preventDefault(); run(); }
      else if (e.key === "Tab" && !e.shiftKey) { e.preventDefault(); ta.setRangeText("  ", ta.selectionStart, ta.selectionEnd, "end"); grow(); }
    });
    grow(); run();
    if (box.hasAttribute("data-challenge")) setupChallenge(box, ta, out, run, grow);
  });

  function setupChallenge(box, ta, out, run, grow) {
    const data = JSON.parse($("#ch-data").textContent);
    const list = $$("#checks li"), summary = $("#summary");
    let nonce = "";
    $("#checkBtn").addEventListener("click", () => {
      nonce = String(Math.random()).slice(2);
      list.forEach(li => { li.dataset.state = "idle"; $(".state", li).textContent = "Running"; });
      summary.textContent = "";
      const c = ta.value, shim = testRunner(data.tests, nonce);
      out.srcdoc = /<head[^>]*>/i.test(c) ? c.replace(/<head[^>]*>/i, m => m + SHIM + shim) : /<html[^>]*>/i.test(c) ? c.replace(/<html[^>]*>/i, m => m + SHIM + shim)
        : `<!doctype html><meta charset="utf-8"><style>${PAGE_CSS}</style><body>${SHIM}${shim}${c}`;
    });
    addEventListener("message", e => {
      const d = e.data;
      if (!d || !d.thCheck || d.nonce !== nonce || e.source !== out.contentWindow) return;
      let pass = 0;
      d.results.forEach((r, i) => { if (list[i]) { list[i].dataset.state = r.ok ? "pass" : "fail"; $(".state", list[i]).textContent = r.ok ? "Passed" : "Not yet"; } pass += r.ok ? 1 : 0; });
      summary.textContent = pass === d.results.length ? "All checks passed. Nice work!" : `${pass} of ${d.results.length} checks passed. Keep going.`;
      summary.className = "check-summary " + (pass === d.results.length ? "ok" : "no");
    });
    $("#hintBtn").addEventListener("click", () => { $("#hint").hidden = false; });
    $("#solBtn").addEventListener("click", () => { $("#solution").hidden = false; $("#solBtn").hidden = true; });
  }

  /* ---- home page: live CSS demo ---- */
  const demo = $("#demoCode");
  if (demo) {
    const sets = [["#2554F0", "8px", "12px 22px"], ["#0E8FB0", "999px", "12px 28px"], ["#5B3FE0", "2px", "14px 22px"]];
    const btn = $("#demoBtn"); let i = 0, timer;
    const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;");
    const draw = n => {
      const [c, r, p] = sets[n];
      demo.innerHTML = `<span class="sel">.button</span> {\n  <span class="p">background</span>: <span class="v">${esc(c)}</span>;\n  <span class="p">border-radius</span>: <span class="v">${esc(r)}</span>;\n  <span class="p">padding</span>: <span class="v">${esc(p)}</span>;\n  <span class="p">color</span>: <span class="v">white</span>;\n}`;
      btn.style.background = c; btn.style.borderRadius = r; btn.style.padding = p;
    };
    draw(0);
    if (!matchMedia("(prefers-reduced-motion: reduce)").matches) {
      const go = () => { timer = setInterval(() => { i = (i + 1) % sets.length; draw(i); }, 2600); };
      go(); const box = $("#heroDemo");
      box.addEventListener("mouseenter", () => clearInterval(timer)); box.addEventListener("mouseleave", go);
    }
  }

  /* ---- copy buttons on code blocks ---- */
  $$("[data-copy]").forEach(btn => btn.addEventListener("click", async () => {
    const text = $("pre", btn.closest(".codebox")).textContent;
    try { await navigator.clipboard.writeText(text); btn.textContent = "Copied"; }
    catch { btn.textContent = "Press Ctrl+C"; const r = document.createRange(); r.selectNodeContents($("pre", btn.closest(".codebox"))); getSelection().removeAllRanges(); getSelection().addRange(r); }
    setTimeout(() => (btn.textContent = "Copy"), 1500);
  }));

  /* ---- lesson exercises (checked by the Python server) ---- */
  const art = $("article[data-slug]");
  if (art) {
    const qs = $$(".q", art); let right = 0;
    qs.forEach(q => $$(".opt", q).forEach(b => b.addEventListener("click", async () => {
      const fb = $(".fb", q); let res;
      try { res = await post("/api/check", { id: q.dataset.id, choice: b.dataset.choice }); }
      catch { fb.className = "fb no"; fb.textContent = "Could not reach the server. Try again."; return; }
      if (res.correct) {
        b.classList.add("right"); $$(".opt", q).forEach(x => (x.disabled = true));
        fb.className = "fb ok"; fb.textContent = "Correct!";
        if (++right === qs.length) complete(art.dataset.slug);
      } else { b.classList.add("wrong"); b.disabled = true; fb.className = "fb no"; fb.textContent = "Not quite. Try another answer."; }
    })));
    $$("[data-next]", art).forEach(a => a.addEventListener("click", () => complete(art.dataset.slug)));
  }

  /* ---- quiz levels: best scores are remembered in this browser ---- */
  const BEST = "techhub-best";
  let best = {};
  try { best = JSON.parse(localStorage.getItem(BEST) || "{}"); } catch { /* ignore */ }
  $$("[data-best]").forEach(a => { const v = best[a.dataset.best]; if (v != null) $(".best", a).textContent = `Best score: ${v} / 10`; });

  const quiz = $("#quiz");
  if (quiz) {
    const { module, level, nextLevel, nextName, back } = quiz.dataset;
    let qs, i, picks;
    const start = async () => {
      quiz.textContent = "Loading questions...";
      try { qs = (await (await fetch(`/api/quiz?n=10&module=${module}&level=${level}`)).json()).questions; } catch { quiz.textContent = "Could not load the quiz. Please refresh."; return; }
      i = 0; picks = {}; show();
    };
    const show = () => {
      quiz.textContent = "";
      const q = qs[i], list = el("div", { class: "opts" });
      const next = el("button", { class: "btn", type: "button", style: "display:none;margin-top:14px", text: i + 1 === qs.length ? "See my score" : "Next question", onclick: () => (++i < qs.length ? show() : finish()) });
      q.options.forEach(o => list.append(el("button", { class: "opt", type: "button", text: o, onclick: e => {
        picks[q.id] = o; $$(".opt", list).forEach(x => (x.disabled = true)); e.currentTarget.classList.add("picked"); next.style.display = ""; next.focus();
      } })));
      quiz.append(el("div", { class: "scoreline" }, el("span", { text: `Question ${i + 1} of ${qs.length}` })),
        el("div", { class: "bar" }, el("i", { style: `width:${(i / qs.length) * 100}%` })), el("h3", { text: q.q }), list, next);
    };
    const finish = async () => {
      const res = await post("/api/quiz/check", { answers: picks });
      const key = `${module}:${level}`;
      if (!(best[key] >= res.score)) { best[key] = res.score; try { localStorage.setItem(BEST, JSON.stringify(best)); } catch { /* ignore */ } }
      const byId = Object.fromEntries(res.results.map(r => [r.id, r]));
      quiz.textContent = "";
      const passed = res.score >= 7;
      const msg = res.score >= 9 ? "Excellent work!" : passed ? "Good job. You passed this level." : "Keep going. Review the lessons and try again.";
      const actions = el("p", { class: "actions" }, el("button", { class: "btn", type: "button", text: "Try again", onclick: start }));
      if (passed && nextLevel) actions.append(el("a", { class: "btn ghost", href: `/quiz/${module}/${nextLevel}`, text: `Next level: ${nextName}` }));
      actions.append(el("a", { class: "btn ghost", href: back, text: "All levels" }));
      quiz.append(el("div", { class: "result-box" }, el("p", { class: "big-score", text: `${res.score} / ${res.total}` }), el("p", { text: msg }), actions),
        el("h3", { text: "Review" }),
        ...qs.map((q, n) => { const r = byId[q.id]; return el("p", {}, el("b", { text: `${n + 1}. ${q.q} ` }), r.correct ? el("span", { class: "fb ok", text: `Correct: ${r.answer}` }) : el("span", { class: "fb no", text: `You chose "${picks[q.id]}". Answer: ${r.answer}` })); }));
    };
    start();
  }

  /* ---- reference table filter ---- */
  const rq = $("#rq");
  if (rq) rq.addEventListener("input", () => {
    const f = rq.value.trim().toLowerCase(); let shown = 0;
    $$(".ref-group").forEach(g => {
      let any = false;
      $$("tbody tr", g).forEach(tr => { const hit = !f || tr.textContent.toLowerCase().includes(f); tr.hidden = !hit; any = any || hit; });
      g.hidden = !any; shown += any ? 1 : 0;
    });
    $("#rnone").hidden = shown > 0;
  });
  /* ---- theme toggle ---- */
  const themeBtn = $("#themeBtn");
  if (themeBtn) themeBtn.addEventListener("click", () => {
    const cur = document.documentElement.dataset.theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    const next = cur === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem("techhub-theme", next); } catch { /* ignore */ }
  });

  /* ---- lesson feedback (stored by the Python server) ---- */
  const fbBox = $("[data-feedback]");
  if (fbBox) {
    const slug = fbBox.dataset.feedback, msg = $(".fb-msg", fbBox), key = "techhub-voted";
    let voted = {}; try { voted = JSON.parse(localStorage.getItem(key) || "{}"); } catch { /* ignore */ }
    const lock = () => { $$("button", fbBox).forEach(b => (b.disabled = true)); msg.textContent = "Thanks for your feedback."; };
    if (voted[slug]) lock();
    $$("[data-vote]", fbBox).forEach(b => b.addEventListener("click", async () => {
      try {
        const res = await post("/api/feedback", { lesson: slug, helpful: b.dataset.vote === "yes" });
        if (res.ok) { voted[slug] = 1; try { localStorage.setItem(key, JSON.stringify(voted)); } catch { /* ignore */ } lock(); } else msg.textContent = res.error || "Could not save feedback.";
      } catch { msg.textContent = "Could not save feedback."; }
    }));
  }

  /* ---- glossary filter ---- */
  const gl = $("#gl");
  if (gl) gl.addEventListener("input", () => {
    const f = gl.value.trim().toLowerCase(); let shown = 0;
    $$("#gloss .gl-item").forEach(it => { const hit = !f || it.textContent.toLowerCase().includes(f); it.hidden = !hit; shown += hit ? 1 : 0; });
    $$("#gloss .gl-letter").forEach(h => { let n = h.nextElementSibling, any = false; while (n && n.classList.contains("gl-item")) { if (!n.hidden) any = true; n = n.nextElementSibling; } h.hidden = !any; });
    $("#gnone").hidden = shown > 0;
  });
})();
