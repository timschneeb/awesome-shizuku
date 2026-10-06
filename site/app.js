(function () {
  const DATA = window.SHIZUKU_DATA;
  const apps = DATA.apps.map((a, i) => ({ ...a, i, hay: [a.name, a.desc, a.license, a.group, a.tags.join(" ")].join(" ").toLowerCase() }));
  const PAGE = 60;
  const KINDS = [
    ["open", "Open source"],
    ["closed", "Closed source"],
    ["archived", "Archived"],
  ];
  const $ = (id) => document.getElementById(id);
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  const state = { q: "", kind: "open", cat: "", sort: "list", tag: "", lic: "", limit: PAGE };

  function readHash() {
    const p = new URLSearchParams(location.hash.replace(/^#directory\??/, "").replace(/^#/, ""));
    if (location.hash.startsWith("#directory?")) {
      state.q = p.get("q") || "";
      state.kind = p.get("kind") || "open";
      state.cat = p.get("cat") || "";
      state.sort = p.get("sort") || "list";
      state.tag = p.get("tag") || "";
      state.lic = p.get("lic") || "";
    }
  }
  function writeHash() {
    const p = new URLSearchParams();
    if (state.q) p.set("q", state.q);
    if (state.kind !== "open") p.set("kind", state.kind);
    if (state.cat) p.set("cat", state.cat);
    if (state.sort !== "list") p.set("sort", state.sort);
    if (state.tag) p.set("tag", state.tag);
    if (state.lic) p.set("lic", state.lic);
    const s = p.toString();
    history.replaceState(null, "", s ? "#directory?" + s : location.pathname + location.search);
  }

  // ---- stats
  const open = apps.filter((a) => a.kind === "open");
  const groups = new Set(open.map((a) => a.group.split(" / ")[0]));
  $("count-total").textContent = apps.length;
  $("stats").innerHTML = [
    [open.length, "open-source entries"],
    [apps.filter((a) => a.kind === "closed").length, "closed-source apps"],
    [groups.size, "categories"],
    [apps.filter((a) => a.featured).length, "recommended ✨"],
  ].map(([n, l]) => `<div class="stat"><b>${n}</b><span>${l}</span></div>`).join("");

  // ---- sidebar
  function scoped() { return apps.filter((a) => a.kind === state.kind); }
  function renderSide() {
    $("kind-seg").innerHTML = KINDS.map(([k, l]) => {
      const n = apps.filter((a) => a.kind === k).length;
      return `<button class="opt ${state.kind === k ? "on" : ""}" data-kind="${k}">${l}<small>${n}</small></button>`;
    }).join("");
    const counts = new Map();
    const order = [];
    for (const a of scoped()) {
      const k = a.section + "\u0000" + a.group;
      if (!counts.has(k)) { counts.set(k, 0); order.push([a.section, a.group]); }
      counts.set(k, counts.get(k) + 1);
    }
    let html = `<button class="opt ${state.cat === "" ? "on" : ""}" data-cat="">All<small>${scoped().length}</small></button>`;
    let cur = null;
    for (const [sec, grp] of order) {
      if (sec !== cur && state.kind === "open") { html += `<div class="cat-head">${esc(sec)}</div>`; cur = sec; }
      const n = counts.get(sec + "\u0000" + grp);
      html += `<button class="opt ${state.cat === grp ? "on" : ""}" data-cat="${esc(grp)}">${esc(grp.replace("Vendor-specific / ", "Vendor · "))}<small>${n}</small></button>`;
    }
    $("cats").innerHTML = html;
  }

  // ---- filters
  function filtered() {
    const terms = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    let list = scoped().filter((a) => {
      if (state.cat && a.group !== state.cat) return false;
      if (state.tag === "featured" && !a.featured) return false;
      if (state.tag && state.tag !== "featured" && !a.tags.includes(state.tag)) return false;
      if (state.lic === "foss" && /^proprietary$|no license/i.test(a.license)) return false;
      if (state.lic === "proprietary" && !/^proprietary$/i.test(a.license)) return false;
      return terms.every((t) => a.hay.includes(t));
    });
    if (state.sort === "az") list.sort((x, y) => x.name.localeCompare(y.name, undefined, { sensitivity: "base" }));
    if (state.sort === "za") list.sort((x, y) => y.name.localeCompare(x.name, undefined, { sensitivity: "base" }));
    return list;
  }

  function badges(a) {
    const out = [];
    if (a.featured) out.push(`<span class="badge feat">✨ Recommended</span>`);
    if (a.kind === "closed") out.push(`<span class="badge closed">Closed source</span>`);
    if (a.kind === "archived") out.push(`<span class="badge arch">Archived</span>`);
    for (const t of a.tags) {
      const cls = /Paid|IAP/.test(t) ? "paid" : t === "Root" ? "root" : "";
      out.push(`<span class="badge ${cls}">${esc(t)}${/Paid|IAP/.test(t) ? " 💰" : ""}</span>`);
    }
    if (a.license) out.push(`<span class="badge">${esc(a.license)}</span>`);
    return out.join("");
  }

  function card(a) {
    const src = a.source ? `<a class="srclink" href="${esc(a.source)}" target="_blank" rel="noopener">Source ↗</a>` : "";
    return `<article class="card">
      <span class="grp">${esc(a.group.replace("Vendor-specific / ", "Vendor · "))}</span>
      <h3><a href="${esc(a.url)}" target="_blank" rel="noopener">${esc(a.name)}</a></h3>
      <p>${esc(a.desc) || "—"}</p>
      <div class="foot2">${badges(a)}${src}</div>
    </article>`;
  }

  function renderChips() {
    const chips = [
      ["featured", "✨ Recommended"], ["Root", "Root"], ["Paid", "Paid"], ["IAP", "IAP"], ["Ads", "Ads"],
    ].map(([k, l]) => `<button class="chip ${state.tag === k ? "on" : ""}" data-tag="${k}">${l}</button>`);
    chips.push(`<button class="chip ${state.lic === "foss" ? "on" : ""}" data-lic="foss">FOSS license</button>`);
    chips.push(`<button class="chip ${state.lic === "proprietary" ? "on" : ""}" data-lic="proprietary">Proprietary</button>`);
    $("chips").innerHTML = chips.join("");
  }

  function renderResults() {
    const list = filtered();
    const shown = list.slice(0, state.limit);
    $("grid").innerHTML = shown.map(card).join("");
    $("empty").hidden = list.length > 0;
    $("more-btn").hidden = list.length <= shown.length;
    $("more-btn").textContent = `Show more (${list.length - shown.length} left)`;
    $("meta").textContent = `${list.length} result${list.length === 1 ? "" : "s"}`;
  }

  function render() { renderSide(); renderChips(); renderResults(); writeHash(); }
  function reset() { state.limit = PAGE; render(); }

  // ---- events
  $("q").addEventListener("input", (e) => { state.q = e.target.value; state.limit = PAGE; renderResults(); writeHash(); });
  $("sort").addEventListener("change", (e) => { state.sort = e.target.value; reset(); });
  $("more-btn").addEventListener("click", () => { state.limit += PAGE; renderResults(); });
  $("side-toggle").addEventListener("click", () => $("side").classList.toggle("open"));
  $("side").addEventListener("click", (e) => {
    const b = e.target.closest("button");
    if (!b) return;
    if (b.dataset.kind) { state.kind = b.dataset.kind; state.cat = ""; }
    else if ("cat" in b.dataset) state.cat = b.dataset.cat;
    reset();
  });
  $("chips").addEventListener("click", (e) => {
    const b = e.target.closest("button");
    if (!b) return;
    if (b.dataset.tag) state.tag = state.tag === b.dataset.tag ? "" : b.dataset.tag;
    if (b.dataset.lic) state.lic = state.lic === b.dataset.lic ? "" : b.dataset.lic;
    reset();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "/" && !/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) {
      e.preventDefault(); $("q").focus(); $("directory").scrollIntoView();
    }
  });

  // ---- rish (tiny markdown renderer for pages/RISH.md)
  function inline(s) {
    return esc(s)
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');
  }
  function md(src) {
    const out = []; let list = 0, quote = [];
    const flushQuote = () => { if (quote.length) { out.push("<blockquote>" + quote.map((l) => `<p>${inline(l.replace(/^\[!NOTE\]$/, "Note"))}</p>`).join("") + "</blockquote>"); quote = []; } };
    const closeList = (to) => { while (list > to) { out.push("</ul>"); list--; } };
    for (const line of src.split("\n")) {
      const q = line.match(/^>\s?(.*)$/);
      if (q) { if (q[1]) quote.push(q[1]); continue; }
      flushQuote();
      const li = line.match(/^(\s*)\* (.*)$/);
      if (li) { const d = li[1].length ? 2 : 1; while (list < d) { out.push("<ul>"); list++; } closeList(d); out.push(`<li>${inline(li[2])}</li>`); continue; }
      closeList(0);
      const h = line.match(/^(#{1,4}) (.*)$/);
      if (h) { const n = Math.max(2, h[1].length); out.push(`<h${n}>${inline(h[2])}</h${n}>`); continue; }
      if (line.trim()) out.push(`<p>${inline(line)}</p>`);
    }
    flushQuote(); closeList(0);
    return out.join("\n");
  }
  $("rish-body").innerHTML = md(DATA.rish);

  readHash();
  $("q").value = state.q;
  $("sort").value = state.sort;
  render();
})();
