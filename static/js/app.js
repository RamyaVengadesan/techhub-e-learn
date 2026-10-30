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

  /* ---- progress, saved in this browser ---- */
  const KEY = "techhub-done";
  let done = new Set();
  try { done = new Set(JSON.parse(localStorage.getItem(KEY) || "[]")); } catch { /* storage blocked */ }
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify([...done])); } catch { /* ignore */ } };
  function paint() {
    $$("[data-slug]").forEach(a => a.classList.toggle("done", done.has(a.dataset.slug)));
    $$("[data-progress]").forEach(bar => {
      const slugs = bar.dataset.progress.split(","), n = slugs.filter(s => done.has(s)).length, pct = Math.round(n / slugs.length * 100);
      bar.style.width = pct + "%";
      $$(`[data-progress-text="${bar.dataset.progress}"]`).forEach(t => (t.textContent = `${n} of ${slugs.length} lessons completed (${pct}%)`));
    });
    const start = $("#startBtn"), side = $$(".side nav a[data-slug]");
    if (start && done.size && side.length) { const nx = side.find(a => !done.has(a.dataset.slug)); if (nx) { start.href = nx.href; start.textContent = "Continue the course"; } }
  }
  const complete = slug => { done.add(slug); save(); paint(); };
  paint();

  /* ---- mobile menu + sidebar filter ---- */
  const side = $("#side"), scrim = $("#scrim"), menu = $("#menuBtn");
  if (side && menu) {
    const set = o => { side.classList.toggle("open", o); scrim.classList.toggle("on", o); menu.setAttribute("aria-expanded", String(o)); };
    menu.addEventListener("click", () => set(!side.classList.contains("open")));
    scrim.addEventListener("click", () => set(false));
    const on = $(".side nav a.on"); if (on) on.scrollIntoView({ block: "center" });
    $("#sideQ").addEventListener("input", e => {
      const f = e.target.value.trim().toLowerCase();
      $$(".side nav a").forEach(a => (a.hidden = f && !a.textContent.toLowerCase().includes(f)));
      $$(".side .grp").forEach(g => (g.hidden = !$$("a", g).some(a => !a.hidden)));
    });
  }

  /* ---- global search (Python /api/search) ---- */
  const gq = $("#gq"), gres = $("#gres"); let timer;
  gq.addEventListener("input", () => {
    clearTimeout(timer);
    timer = setTimeout(async () => {
      const q = gq.value.trim();
      if (q.length < 2) { gres.hidden = true; return; }
      try {
        const { results } = await (await fetch("/api/search?q=" + encodeURIComponent(q))).json();
        gres.textContent = "";
        if (!results.length) gres.append(el("p", { text: "No lessons found." }));
        results.forEach(r => gres.append(el("a", { href: r.url, role: "option" }, el("span", { text: r.title }), el("small", { text: r.module }))));
        gres.hidden = false;
      } catch { gres.hidden = true; }
    }, 180);
  });
  document.addEventListener("click", e => { if (!e.target.closest(".gsearch")) gres.hidden = true; });
  gq.addEventListener("keydown", e => { if (e.key === "Escape") { gres.hidden = true; gq.blur(); } });

  /* ---- Try it editor ---- */
  const PAGE_CSS = "body{font:16px/1.6 system-ui,-apple-system,Segoe UI,sans-serif;color:#1b2a46;margin:14px}";
  $$("[data-editor]").forEach(box => {
    const ta = $("textarea", box), out = $("[data-out]", box);
    const run = () => { const c = ta.value; out.srcdoc = /<!doctype|<html/i.test(c) ? c : `<!doctype html><meta charset="utf-8"><style>${PAGE_CSS}</style>${c}`; };
    $("[data-run]", box).addEventListener("click", run);
    ta.addEventListener("keydown", e => {
      if ((e.ctrlKey || e.metaKey) && e.key === "Enter") { e.preventDefault(); run(); }
      else if (e.key === "Tab" && !e.shiftKey) { e.preventDefault(); ta.setRangeText("  ", ta.selectionStart, ta.selectionEnd, "end"); }
    });
    run();
  });

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

  /* ---- quiz ---- */
  const quiz = $("#quiz");
  if (quiz) {
    let qs, i, picks;
    const start = async () => {
      quiz.textContent = "Loading questions...";
      try { qs = (await (await fetch("/api/quiz?n=10&module=" + quiz.dataset.module)).json()).questions; } catch { quiz.textContent = "Could not load the quiz. Please refresh."; return; }
      i = 0; picks = {}; show();
    };
    const show = () => {
      quiz.textContent = "";
      const q = qs[i], list = el("div", { class: "opts" });
      const next = el("button", { class: "btn", type: "button", style: "display:none;margin-top:14px", text: i + 1 === qs.length ? "See my score" : "Next question", onclick: () => (++i < qs.length ? show() : finish()) });
      q.options.forEach(o => list.append(el("button", { class: "opt", type: "button", text: o, onclick: e => {
        picks[q.id] = o; $$(".opt", list).forEach(x => (x.disabled = true)); e.currentTarget.classList.add("picked"); next.style.display = ""; next.focus();
      } })));
      quiz.append(el("div", { class: "scoreline" }, el("span", { text: `Question ${i + 1} of ${qs.length}` })), el("h3", { text: q.q }), list, next);
    };
    const finish = async () => {
      const res = await post("/api/quiz/check", { answers: picks });
      const byId = Object.fromEntries(res.results.map(r => [r.id, r]));
      quiz.textContent = "";
      const msg = res.score >= 9 ? "Excellent work!" : res.score >= 6 ? "Good job. A little more practice and you will have it." : "Keep going. Review the lessons and try again.";
      quiz.append(el("div", { class: "result-box" }, el("p", { class: "big-score", text: `${res.score} / ${res.total}` }), el("p", { text: msg }),
        el("button", { class: "btn", type: "button", text: "Try again", onclick: start }), " ", el("a", { class: "btn ghost", href: "/quiz", text: "All quizzes" })),
        el("h3", { text: "Review" }),
        ...qs.map((q, n) => { const r = byId[q.id]; return el("p", {}, el("b", { text: `${n + 1}. ${q.q} ` }), r.correct ? el("span", { class: "fb ok", text: `Correct: ${r.answer}` }) : el("span", { class: "fb no", text: `You chose "${picks[q.id]}". Answer: ${r.answer}` })); }));
    };
    start();
  }
})();
