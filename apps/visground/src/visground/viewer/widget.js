function createElement(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined && text !== null) node.textContent = text;
  return node;
}

function clone(value) {
  return JSON.parse(JSON.stringify(value));
}

function formatValue(value) {
  if (value === null || value === undefined || value === "") {
    return "none";
  }
  return String(value).replaceAll("_", " ");
}

function formatHeading(value) {
  return formatValue(value).toUpperCase();
}

function formatScore(value) {
  if (value === null || value === undefined || Number.isNaN(value)) {
    return null;
  }
  return Number(value).toFixed(2);
}

function createCommandInvoker(model) {
  let nextId = 0;
  return function invoke(name, msg = {}) {
    return new Promise((resolve, reject) => {
      const requestId = `cmd-${Date.now()}-${nextId++}`;
      const timer = window.setTimeout(() => {
        model.off("msg:custom", onMessage);
        reject(new Error(`Command timed out: ${name}`));
      }, 60000);

      function onMessage(content) {
        if (!content || content.kind !== "anywidget-command-response") {
          return;
        }
        if (content.id !== requestId) {
          return;
        }
        window.clearTimeout(timer);
        model.off("msg:custom", onMessage);
        resolve(content.response);
      }

      model.on("msg:custom", onMessage);
      try {
        model.send({
          kind: "anywidget-command",
          id: requestId,
          name,
          msg,
        });
      } catch (error) {
        window.clearTimeout(timer);
        model.off("msg:custom", onMessage);
        reject(error);
      }
    });
  };
}

function buildRuleTitle(label, aside = "") {
  const row = createElement("div", "vg-rule-row");
  row.appendChild(createElement("span", "vg-rule-label", label));
  if (aside) {
    row.appendChild(createElement("span", "vg-rule-aside", aside));
  }
  return row;
}

function buildSelectControl({ label, options, value, onChange, disabled = false }) {
  const group = createElement("label", "vg-control-group");
  group.appendChild(createElement("span", "vg-control-label", label));
  const select = createElement("select", "vg-select");
  select.disabled = disabled;
  options.forEach((optionValue) => {
    const option = createElement("option");
    option.value = optionValue === null ? "__none__" : String(optionValue);
    option.textContent = formatValue(optionValue);
    option.selected = optionValue === value;
    select.appendChild(option);
  });
  select.addEventListener("change", () => {
    onChange(select.value === "__none__" ? null : select.value);
  });
  group.appendChild(select);
  return group;
}

function setImage(node, imageUrl, alt) {
  if (!imageUrl) {
    return;
  }
  const image = createElement("img", "vg-image");
  image.src = imageUrl;
  image.alt = alt;
  image.loading = "lazy";
  node.appendChild(image);
}

function renderMatrixCell(cell, focusedKey, actions) {
  const key =
    cell.candidate === null ? null : `${cell.candidate.grounding_mode}::${cell.candidate.model}`;
  const button = createElement(
    "button",
    `vg-matrix-cell ${key && key === focusedKey ? "is-focused" : ""}`.trim(),
  );
  button.type = "button";

  if (cell.missing || !cell.candidate) {
    button.disabled = true;
    button.classList.add("is-missing");
    button.appendChild(
      createElement("span", "vg-missing-label", cell.placeholder_reason || "missing candidate"),
    );
    return button;
  }

  button.addEventListener("click", () => {
    actions.focusCell(cell.candidate.grounding_mode, cell.candidate.model);
  });

  const frame = createElement("div", "vg-chart-frame");
  if (cell.candidate.error) {
    frame.appendChild(createElement("p", "vg-error", cell.candidate.error));
  } else {
    setImage(frame, cell.candidate.image_url, cell.candidate.visgen_id);
  }
  button.appendChild(frame);

  const meta = createElement("div", "vg-cell-meta");
  meta.appendChild(
    createElement("div", "vg-meta-line", `type ${formatValue(cell.candidate.visualization_type)}`),
  );
  meta.appendChild(
    createElement(
      "div",
      "vg-meta-line",
      formatScore(cell.candidate.overall_score)
        ? `score ${formatScore(cell.candidate.overall_score)}`
        : "score unavailable",
    ),
  );
  button.appendChild(meta);
  return button;
}

function renderMatrix(payload, root, actions, focusedKey) {
  const section = createElement("section", "vg-section");
  section.appendChild(
    buildRuleTitle("comparison", "one request, three grounding modes, three model outputs"),
  );

  const grid = createElement("div", "vg-matrix-grid");
  grid.style.setProperty("--vg-cols", String(payload.models.length));

  grid.appendChild(createElement("div", "vg-matrix-corner", "grounding"));
  payload.models.forEach((model) => {
    grid.appendChild(createElement("div", "vg-model-head", formatValue(model)));
  });

  payload.rows.forEach((row) => {
    grid.appendChild(createElement("div", "vg-grounding-head", formatValue(row.grounding_mode)));
    row.cells.forEach((cell) => {
      grid.appendChild(renderMatrixCell(cell, focusedKey, actions));
    });
  });

  section.appendChild(grid);
  root.appendChild(section);
}

function renderDetailBlock(title, child) {
  const block = createElement("section", "vg-detail-block");
  block.appendChild(buildRuleTitle(title));
  block.appendChild(child);
  return block;
}

function renderList(items, emptyText) {
  if (!items || items.length === 0) {
    return createElement("p", "vg-copy", emptyText);
  }
  const list = createElement("ul", "vg-list");
  items.forEach((item) => {
    list.appendChild(createElement("li", "vg-copy", item));
  });
  return list;
}

function renderJudgementBlock(candidate) {
  if (!candidate.judgement_dimensions || candidate.judgement_dimensions.length === 0) {
    return createElement("p", "vg-copy", "No judgement available for this cell.");
  }
  const wrap = createElement("div", "vg-judgement-grid");
  candidate.judgement_dimensions.forEach((dimension) => {
    const card = createElement("div", "vg-judgement-card");
    card.appendChild(
      createElement(
        "div",
        "vg-judgement-head",
        `${formatValue(dimension.dimension)} · ${dimension.score ?? "—"}`,
      ),
    );
    card.appendChild(
      createElement("p", "vg-copy", dimension.reasoning || "No reasoning available."),
    );
    wrap.appendChild(card);
  });
  return wrap;
}

function renderInspectSection(inspect, root) {
  const candidate = inspect.focused_candidate;
  if (!candidate) {
    return;
  }

  const section = createElement("section", "vg-section vg-detail-section");
  section.appendChild(
    buildRuleTitle(
      "focused chart",
      `${formatHeading(inspect.focused_grounding_mode)} · ${formatValue(inspect.focused_model)}`,
    ),
  );

  const grid = createElement("div", "vg-detail-grid");

  const query = createElement("div", "vg-copy-block");
  query.appendChild(createElement("p", "vg-copy", candidate.nl_query));
  grid.appendChild(renderDetailBlock("request", query));

  const interpretation = createElement("div", "vg-copy-block");
  interpretation.appendChild(
    createElement("p", "vg-copy", candidate.query_interpretation || "No interpretation available."),
  );
  grid.appendChild(renderDetailBlock("interpretation", interpretation));

  const trace = createElement("div", "vg-copy-block");
  trace.appendChild(renderList(candidate.grounding_trace, "No grounding trace recorded."));
  grid.appendChild(renderDetailBlock("grounding trace", trace));

  const rationale = createElement("div", "vg-copy-block");
  rationale.appendChild(renderList(candidate.design_rationale, "No design rationale recorded."));
  grid.appendChild(renderDetailBlock("design rationale", rationale));

  const guidelines = createElement("div", "vg-copy-block");
  guidelines.appendChild(
    renderList(candidate.guideline_ids, "No retrieved guideline IDs for this cell."),
  );
  grid.appendChild(renderDetailBlock("retrieved guideline ids", guidelines));

  const judgement = createElement("div", "vg-copy-block");
  judgement.appendChild(renderJudgementBlock(candidate));
  grid.appendChild(renderDetailBlock("judge feedback", judgement));

  section.appendChild(grid);

  const codeShell = createElement("details", "vg-code-shell");
  const summary = createElement("summary", "vg-code-summary", "generated code");
  codeShell.appendChild(summary);
  const code = createElement("pre", "vg-code");
  code.textContent = candidate.code || "";
  codeShell.appendChild(code);
  section.appendChild(codeShell);

  root.appendChild(section);
}

function renderHeader(overview, root) {
  const header = createElement("header", "vg-header");
  header.appendChild(buildRuleTitle("case", `vis ${overview.vis_id}`));
  header.appendChild(createElement("h2", "vg-title", "How grounding changes the result"));
  header.appendChild(
    createElement(
      "p",
      "vg-subtitle",
      "Compare the same request across grounding strategies and model outputs to see where structure improves consistency.",
    ),
  );
  root.appendChild(header);
}

function renderTopbar(state, root, actions) {
  const topbar = createElement("section", "vg-topbar");

  const pager = createElement("div", "vg-pager");
  const previous = createElement("button", "vg-nav-button", "Previous");
  previous.type = "button";
  previous.disabled = state.value.page_index <= 0 || !!state.busy;
  previous.addEventListener("click", () => actions.stepCase(-1));
  pager.appendChild(previous);

  const next = createElement("button", "vg-nav-button", "Next");
  next.type = "button";
  next.disabled = state.value.page_index >= state.catalog.length - 1 || !!state.busy;
  next.addEventListener("click", () => actions.stepCase(1));
  pager.appendChild(next);

  pager.appendChild(
    createElement(
      "div",
      "vg-pager-meta",
      `case ${state.value.page_index + 1} of ${state.catalog.length}`,
    ),
  );
  topbar.appendChild(pager);

  const searchGroup = createElement("div", "vg-search-group");
  const search = createElement("input", "vg-search");
  search.type = "search";
  search.placeholder = "Search case ID or request";
  search.value = state.searchTerm;
  search.addEventListener("input", () => {
    state.searchTerm = search.value;
    actions.render();
  });
  searchGroup.appendChild(search);

  const jump = createElement("select", "vg-select vg-case-select");
  const filteredCatalog = state.catalog.filter((entry) => {
    const needle = state.searchTerm.trim().toLowerCase();
    if (!needle) {
      return true;
    }
    return (
      entry.vis_id.toLowerCase().includes(needle) || entry.nl_query.toLowerCase().includes(needle)
    );
  });
  filteredCatalog.forEach((entry) => {
    const option = createElement("option");
    option.value = entry.vis_id;
    option.textContent = `${entry.vis_id} · ${entry.nl_query}`;
    option.selected = entry.vis_id === state.value.vis_id;
    jump.appendChild(option);
  });
  jump.disabled = !!state.busy || filteredCatalog.length === 0;
  jump.addEventListener("change", () => actions.loadView({ vis_id: jump.value }));
  searchGroup.appendChild(jump);
  topbar.appendChild(searchGroup);

  root.appendChild(topbar);
}

function renderQueryBlock(overview, root) {
  const section = createElement("section", "vg-section");
  section.appendChild(buildRuleTitle("request"));
  const block = createElement("div", "vg-query-block");
  block.appendChild(createElement("p", "vg-query-text", overview.nl_query));
  section.appendChild(block);
  root.appendChild(section);
}

function renderControls(overview, root, actions) {
  const section = createElement("section", "vg-section");
  section.appendChild(buildRuleTitle("controls", "choose the request framing"));
  const controls = createElement("div", "vg-controls");

  controls.appendChild(
    buildSelectControl({
      label: "objective",
      options: overview.options.objectives,
      value: overview.selection.objective,
      onChange: (objective) => actions.loadView({ objective }),
    }),
  );

  controls.appendChild(
    buildSelectControl({
      label: "grammar",
      options: overview.options.grammars,
      value: overview.selection.grammar,
      onChange: (grammar) => actions.loadView({ grammar }),
    }),
  );

  controls.appendChild(
    buildSelectControl({
      label: "audience",
      options: overview.options.audiences,
      value: overview.selection.audience,
      onChange: (audience) => actions.loadView({ audience }),
      disabled: !overview.options.audience_enabled,
    }),
  );

  section.appendChild(controls);
  root.appendChild(section);
}

function renderBusy(root, message) {
  const loading = createElement("div", "vg-loading");
  const spinner = createElement("div", "vg-spinner");
  loading.appendChild(spinner);
  loading.appendChild(createElement("p", "vg-muted", message));
  root.appendChild(loading);
}

function renderError(root, message) {
  const banner = createElement("div", "vg-error-banner");
  banner.appendChild(createElement("strong", "", "Viewer error"));
  banner.appendChild(createElement("p", "vg-copy", message));
  root.appendChild(banner);
}

function renderApp(state, root, actions) {
  root.innerHTML = "";
  const shell = createElement("div", "vg-shell");
  root.appendChild(shell);

  if (state.error) {
    renderError(shell, state.error);
    return;
  }
  if (state.busy) {
    renderBusy(shell, state.busy);
    return;
  }
  if (!state.overview) {
    renderBusy(shell, "Loading comparison…");
    return;
  }

  renderHeader(state.overview, shell);
  renderTopbar(state, shell, actions);
  renderQueryBlock(state.overview, shell);
  renderControls(state.overview, shell, actions);

  const focusedKey =
    state.inspect && state.inspect.focused_candidate
      ? `${state.inspect.focused_grounding_mode}::${state.inspect.focused_model}`
      : null;
  renderMatrix(state.overview, shell, actions, focusedKey);

  if (state.value.view_mode === "inspect" && state.inspect) {
    renderInspectSection(state.inspect, shell);
  }
}

function render({ model, el }) {
  const invoke = createCommandInvoker(model);
  const root = createElement("div", "vg-root");
  el.appendChild(root);

  const state = {
    catalog: [],
    overview: null,
    inspect: null,
    config: {
      grounding_modes: [],
      scores_enabled: false,
    },
    value: clone(model.get("value") || {}),
    searchTerm: "",
    busy: "Loading comparison…",
    error: null,
  };

  function commitValue(nextValue) {
    state.value = clone(nextValue);
    model.set("value", state.value);
    model.save_changes();
  }

  async function loadView(changes = {}) {
    state.busy = "Loading comparison…";
    state.error = null;
    renderApp(state, root, actions);
    try {
      const payload = await invoke("load_view", {
        vis_id: changes.vis_id ?? state.value.vis_id,
        objective: changes.objective ?? state.value.objective,
        grammar: changes.grammar ?? state.value.grammar,
        audience: Object.prototype.hasOwnProperty.call(changes, "audience")
          ? changes.audience
          : state.value.audience,
        view_mode: changes.view_mode ?? state.value.view_mode ?? "overview",
        focused_model: changes.focused_model ?? state.value.focused_model,
        focused_grounding_mode:
          changes.focused_grounding_mode ?? state.value.focused_grounding_mode,
      });
      state.overview = payload.overview;
      state.inspect = payload.inspect;
      commitValue(payload.value);
      state.busy = null;
      renderApp(state, root, actions);
    } catch (error) {
      state.busy = null;
      state.error = error instanceof Error ? error.message : String(error);
      renderApp(state, root, actions);
    }
  }

  const actions = {
    render() {
      renderApp(state, root, actions);
    },
    loadView(changes) {
      loadView(changes);
    },
    stepCase(delta) {
      const nextEntry = state.catalog[state.value.page_index + delta];
      if (!nextEntry) {
        return;
      }
      loadView({
        vis_id: nextEntry.vis_id,
        objective: null,
        grammar: null,
        audience: null,
        view_mode: "overview",
        focused_model: null,
        focused_grounding_mode: null,
      });
    },
    focusCell(groundingMode, modelName) {
      loadView({
        view_mode: "inspect",
        focused_grounding_mode: groundingMode,
        focused_model: modelName,
      });
    },
  };

  function onModelValueChange() {
    const nextValue = model.get("value");
    if (!nextValue || nextValue.vis_id === state.value.vis_id) {
      return;
    }
    state.value = clone(nextValue);
    loadView({ vis_id: nextValue.vis_id });
  }

  function onKeydown(event) {
    if (
      event.target instanceof HTMLInputElement ||
      event.target instanceof HTMLSelectElement ||
      event.target instanceof HTMLTextAreaElement
    ) {
      return;
    }
    if (event.key === "ArrowRight") {
      event.preventDefault();
      actions.stepCase(1);
    } else if (event.key === "ArrowLeft") {
      event.preventDefault();
      actions.stepCase(-1);
    } else if (event.key === "Escape" && state.value.view_mode === "inspect") {
      event.preventDefault();
      loadView({
        view_mode: "overview",
        focused_model: null,
        focused_grounding_mode: null,
      });
    }
  }

  model.on("change:value", onModelValueChange);
  root.addEventListener("keydown", onKeydown);
  root.tabIndex = 0;

  invoke("initialize", {})
    .then((payload) => {
      state.catalog = payload.catalog;
      state.overview = payload.overview;
      state.inspect = payload.inspect;
      state.config = payload.config;
      state.value = clone(payload.value);
      state.busy = null;
      renderApp(state, root, actions);
    })
    .catch((error) => {
      state.busy = null;
      state.error = error instanceof Error ? error.message : String(error);
      renderApp(state, root, actions);
    });

  renderApp(state, root, actions);

  return () => {
    model.off("change:value", onModelValueChange);
    root.removeEventListener("keydown", onKeydown);
  };
}

export default { render };
