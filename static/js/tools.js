(() => {
  "use strict";
  const root = document.querySelector("[data-tool]");
  if (!root) return;
  const kind = root.dataset.tool;
  const stage = root.querySelector("[data-stage]");
  const cssOut = root.querySelector("[data-css]");
  const state = {};
  root.querySelectorAll("[data-prop]").forEach(s => (state[s.dataset.prop] = s.value));
  root.querySelectorAll("[data-range]").forEach(r => (state[r.dataset.range] = +r.value));
  root.querySelectorAll("[data-text]").forEach(t => (state[t.dataset.text] = t.value));

  const palette = ["#1D4ED8", "#0891B2", "#4F46E5", "#0EA5E9", "#2563EB", "#6366F1", "#0E7490", "#3B82F6", "#1E40AF", "#38BDF8", "#4338CA", "#0284C7"];
  const sizes = [44, 70, 52, 90, 60, 48, 80, 56, 66, 50, 74, 58];

  function items(n, tall) {
    stage.textContent = "";
    for (let i = 0; i < n; i++) {
      const d = document.createElement("div");
      d.className = "demo-item"; d.textContent = String(i + 1);
      d.style.background = palette[i % palette.length];
      if (tall) { d.style.height = sizes[i % sizes.length] + "px"; d.style.minWidth = (sizes[(i + 3) % sizes.length] + 10) + "px"; }
      stage.append(d);
    }
  }

  function renderFlex() {
    Object.assign(stage.style, { display: "flex", flexDirection: state["flex-direction"], justifyContent: state["justify-content"], alignItems: state["align-items"], flexWrap: state["flex-wrap"], gap: state.gap + "px" });
    if (stage.children.length !== state.count) items(state.count, true);
    cssOut.textContent = `.container {\n  display: flex;\n  flex-direction: ${state["flex-direction"]};\n  justify-content: ${state["justify-content"]};\n  align-items: ${state["align-items"]};\n  flex-wrap: ${state["flex-wrap"]};\n  gap: ${state.gap}px;\n}`;
  }

  function renderGrid() {
    stage.style.display = "grid";
    stage.style.gridTemplateColumns = ""; stage.style.gridTemplateRows = "";
    stage.style.gridTemplateColumns = state.columns; stage.style.gridTemplateRows = state.rows;
    Object.assign(stage.style, { justifyItems: state["justify-items"], alignItems: state["align-items"], gap: state.gap + "px" });
    if (stage.children.length !== state.count) items(state.count, false);
    cssOut.textContent = `.container {\n  display: grid;\n  grid-template-columns: ${state.columns};\n  grid-template-rows: ${state.rows};\n  justify-items: ${state["justify-items"]};\n  align-items: ${state["align-items"]};\n  gap: ${state.gap}px;\n}`;
  }

  function renderBox() {
    const q = s => root.querySelector(s), bs = state["box-sizing"], w = state.width, h = state.height, p = state.padding, b = state.border, m = state.margin;
    const set = (sel, css) => Object.assign(q(sel).style, css);
    set('[data-bm="margin"]', { padding: m + "px" });
    set('[data-bm="border"]', { borderWidth: b + "px" });
    set('[data-bm="padding"]', { padding: p + "px" });
    const cw = bs === "border-box" ? Math.max(0, w - 2 * p - 2 * b) : w, ch = bs === "border-box" ? Math.max(0, h - 2 * p - 2 * b) : h;
    set('[data-bm="content"]', { width: cw + "px", height: ch + "px" });
    const totalW = cw + 2 * p + 2 * b + 2 * m, totalH = ch + 2 * p + 2 * b + 2 * m;
    q("[data-total]").textContent = `Content ${cw} x ${ch}px. Visible box (content + padding + border): ${cw + 2 * p + 2 * b} x ${ch + 2 * p + 2 * b}px. Space taken including margin: ${totalW} x ${totalH}px.`;
    cssOut.textContent = `.box {\n  box-sizing: ${bs};\n  width: ${w}px;\n  height: ${h}px;\n  padding: ${p}px;\n  border: ${b}px solid;\n  margin: ${m}px;\n}`;
  }

  const render = { flexbox: renderFlex, grid: renderGrid, "box-model": renderBox }[kind];
  root.querySelectorAll("[data-prop]").forEach(s => s.addEventListener("change", () => { state[s.dataset.prop] = s.value; render(); }));
  root.querySelectorAll("[data-range]").forEach(r => r.addEventListener("input", () => {
    state[r.dataset.range] = +r.value;
    const o = root.querySelector(`[data-out="${r.dataset.range}"]`); if (o) o.textContent = r.value + (r.dataset.range === "count" ? "" : "px");
    render();
  }));
  root.querySelectorAll("[data-text]").forEach(t => t.addEventListener("input", () => { state[t.dataset.text] = t.value; render(); }));
  if (kind !== "box-model") items(state.count, kind === "flexbox");
  render();
})();
