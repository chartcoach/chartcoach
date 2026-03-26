const RUNTIME_VERSION = "viewer-shell-v2";
const HOVER_HIDE_DELAY_MS = 140;

function createElement(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined && text !== null) node.textContent = text;
  return node;
}

function clearNode(node) {
  node.replaceChildren();
}

function clone(value) {
  return JSON.parse(JSON.stringify(value));
}

function toOptionValue(value) {
  return value === null ? "__none__" : String(value);
}

function fromOptionValue(value) {
  return value === "__none__" ? null : value;
}

function formatValue(value) {
  if (value === null || value === undefined || value === "") {
    return "none";
  }
  return String(value).replaceAll("_", " ");
}

function formatScore(value) {
  if (value === null || value === undefined || Number.isNaN(value)) {
    return null;
  }
  return Number(value).toFixed(2);
}

function truncateText(text, limit = 88) {
  if (!text || text.length <= limit) {
    return text;
  }
  return `${text.slice(0, limit - 1).trimEnd()}…`;
}

function pluralize(count, singular, plural = `${singular}s`) {
  return count === 1 ? singular : plural;
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

function renderKeyValueMap(values, emptyText) {
  if (!values || Object.keys(values).length === 0) {
    return createElement("p", "vg-copy", emptyText);
  }
  const list = createElement("dl", "vg-kv-list");
  Object.entries(values).forEach(([key, value]) => {
    list.appendChild(createElement("dt", "vg-kv-key", formatValue(key)));
    let formatted = value;
    if (Array.isArray(value)) {
      formatted = value.join(", ");
    } else if (value && typeof value === "object") {
      formatted = JSON.stringify(value);
    }
    list.appendChild(createElement("dd", "vg-kv-value", String(formatted)));
  });
  return list;
}

function renderCopyBlock(text, emptyText) {
  return createElement("p", "vg-copy", text || emptyText);
}

function renderMetaLine(text, extraClass = "") {
  return createElement("div", `vg-meta-line ${extraClass}`.trim(), text);
}

function renderSectionCard(title, child, aside = "") {
  const block = createElement("section", "vg-detail-block");
  block.appendChild(buildRuleTitle(title, aside));
  block.appendChild(child);
  return block;
}

function buildFilterControl(filter, onChange) {
  const group = createElement("label", "vg-control-group");
  group.appendChild(createElement("span", "vg-control-label", filter.label));
  const select = createElement("select", "vg-select");
  select.disabled = !!filter.disabled;
  filter.options.forEach((optionValue) => {
    const option = createElement("option");
    option.value = toOptionValue(optionValue.value);
    option.textContent = optionValue.label;
    option.selected = optionValue.value === filter.value;
    select.appendChild(option);
  });
  select.addEventListener("change", () => {
    onChange(filter.id, fromOptionValue(select.value));
  });
  group.appendChild(select);
  return group;
}

function createHoverCard() {
  const card = createElement("aside", "vg-hovercard");
  card.hidden = true;
  card.tabIndex = -1;
  return card;
}

function getFilteredCatalog(state) {
  const needle = state.searchTerm.trim().toLowerCase();
  if (!needle) {
    return state.catalog;
  }
  return state.catalog.filter((entry) => {
    return (
      entry.vis_id.toLowerCase().includes(needle) || entry.nl_query.toLowerCase().includes(needle)
    );
  });
}

function updateSelectOptions(select, entries, selectedValue) {
  clearNode(select);
  entries.forEach((entry) => {
    const option = createElement("option");
    option.value = entry.value;
    option.textContent = entry.label;
    option.title = entry.title || entry.label;
    option.selected = entry.value === selectedValue;
    select.appendChild(option);
  });
}

function createLoadingOverlay() {
  const overlay = createElement("div", "vg-content-overlay");
  const panel = createElement("div", "vg-loading-panel");
  const spinner = createElement("div", "vg-spinner");
  const message = createElement("p", "vg-muted");
  panel.appendChild(spinner);
  panel.appendChild(message);
  overlay.appendChild(panel);
  overlay.hidden = true;
  return { overlay, message };
}

function createShell(root, actions, state) {
  root.dataset.runtimeVersion = RUNTIME_VERSION;

  const shell = createElement("div", "vg-shell");
  root.appendChild(shell);

  const header = createElement("header", "vg-header");
  shell.appendChild(header);

  const topbar = createElement("section", "vg-topbar");
  shell.appendChild(topbar);

  const pager = createElement("div", "vg-pager");
  const previousButton = createElement("button", "vg-nav-button", "Previous");
  previousButton.type = "button";
  previousButton.addEventListener("click", () => actions.stepCase(-1));
  const nextButton = createElement("button", "vg-nav-button", "Next");
  nextButton.type = "button";
  nextButton.addEventListener("click", () => actions.stepCase(1));
  const pagerMeta = createElement("div", "vg-pager-meta");
  pager.append(previousButton, nextButton, pagerMeta);
  topbar.appendChild(pager);

  const searchGroup = createElement("div", "vg-search-group");
  const searchInput = createElement("input", "vg-search");
  searchInput.type = "search";
  searchInput.addEventListener("input", () => {
    state.searchTerm = searchInput.value;
    updateJumpSelect(state, refs);
  });
  const jumpSelect = createElement("select", "vg-select vg-case-select");
  jumpSelect.addEventListener("change", () => {
    actions.loadView({ vis_id: jumpSelect.value });
  });
  searchGroup.append(searchInput, jumpSelect);
  topbar.appendChild(searchGroup);

  const errorBanner = createElement("div", "vg-error-banner");
  errorBanner.hidden = true;
  shell.appendChild(errorBanner);

  const contentFrame = createElement("div", "vg-content-frame");
  shell.appendChild(contentFrame);
  const loading = createLoadingOverlay();
  contentFrame.appendChild(loading.overlay);

  const requestSection = createElement("section", "vg-section");
  const controlsSection = createElement("section", "vg-section");
  const matrixSection = createElement("section", "vg-section");
  const detailSection = createElement("section", "vg-section vg-detail-section");
  detailSection.hidden = true;
  contentFrame.append(requestSection, controlsSection, matrixSection, detailSection);

  const hoverCard = createHoverCard();
  hoverCard.addEventListener("pointerenter", () => actions.cancelHoverHide());
  hoverCard.addEventListener("pointerleave", () => actions.scheduleHoverHide());
  hoverCard.addEventListener("focusin", () => actions.cancelHoverHide());
  hoverCard.addEventListener("focusout", () => actions.scheduleHoverHide());
  root.appendChild(hoverCard);

  const refs = {
    root,
    shell,
    header,
    previousButton,
    nextButton,
    pagerMeta,
    searchInput,
    jumpSelect,
    errorBanner,
    contentFrame,
    loadingOverlay: loading.overlay,
    loadingMessage: loading.message,
    requestSection,
    controlsSection,
    matrixSection,
    detailSection,
    hoverCard,
  };
  return refs;
}

function updateHeader(state, refs) {
  if (!state.overview) {
    clearNode(refs.header);
    return;
  }
  const copy = state.overview.ui_schema.copy;
  clearNode(refs.header);
  refs.header.appendChild(buildRuleTitle(copy.case_label, `${state.overview.vis_id}`));
  refs.header.appendChild(createElement("h2", "vg-title", copy.title));
  refs.header.appendChild(createElement("p", "vg-subtitle", copy.subtitle));
}

function updateJumpSelect(state, refs) {
  const filteredCatalog = getFilteredCatalog(state);
  const entries = filteredCatalog.map((entry) => ({
    value: entry.vis_id,
    label: entry.search_label || `${entry.vis_id} · ${truncateText(entry.nl_query)}`,
    title: `${entry.vis_id} · ${entry.nl_query}`,
  }));
  if (entries.length === 0) {
    entries.push({
      value: "",
      label: "No matching cases",
      title: "No matching cases",
    });
  }
  updateSelectOptions(refs.jumpSelect, entries, state.value.vis_id);
  refs.jumpSelect.disabled = !!state.busy || entries[0].value === "";
  refs.jumpSelect.title =
    state.catalog.find((entry) => entry.vis_id === state.value.vis_id)?.nl_query || "";
}

function updateTopbar(state, refs) {
  if (!state.overview) {
    refs.previousButton.disabled = true;
    refs.nextButton.disabled = true;
    refs.pagerMeta.textContent = "";
    return;
  }
  const copy = state.overview.ui_schema.copy;
  refs.previousButton.disabled = state.value.page_index <= 0 || !!state.busy;
  refs.nextButton.disabled = state.value.page_index >= state.catalog.length - 1 || !!state.busy;
  refs.pagerMeta.textContent = `${copy.case_label.toLowerCase()} ${state.value.page_index + 1} of ${state.catalog.length}`;
  refs.searchInput.placeholder = copy.search_placeholder;
  if (refs.searchInput.value !== state.searchTerm) {
    refs.searchInput.value = state.searchTerm;
  }
  updateJumpSelect(state, refs);
}

function renderRequestSection(state, refs) {
  if (!state.overview) {
    clearNode(refs.requestSection);
    return;
  }
  const copy = state.overview.ui_schema.copy;
  clearNode(refs.requestSection);
  refs.requestSection.appendChild(buildRuleTitle(copy.request_label));
  const block = createElement("div", "vg-query-block");
  block.appendChild(createElement("p", "vg-query-text", state.overview.nl_query));
  refs.requestSection.appendChild(block);
}

function renderControlsSection(state, refs, actions) {
  if (!state.overview) {
    clearNode(refs.controlsSection);
    return;
  }
  const schema = state.overview.ui_schema;
  clearNode(refs.controlsSection);
  refs.controlsSection.appendChild(
    buildRuleTitle(schema.copy.controls_label, schema.copy.controls_aside),
  );
  const controls = createElement("div", "vg-controls");
  schema.filters.forEach((filter) => {
    controls.appendChild(
      buildFilterControl(filter, (filterId, value) => {
        actions.loadView({ [filterId]: value });
      }),
    );
  });
  refs.controlsSection.appendChild(controls);
}

function buildMatrixCell(cell, state, actions, focusedKey) {
  const candidate = cell.candidate;
  const key = candidate ? `${candidate.grounding_mode}::${candidate.model}` : null;
  const button = createElement(
    "button",
    `vg-matrix-cell ${key && key === focusedKey ? "is-focused" : ""}`.trim(),
  );
  button.type = "button";

  if (!candidate || cell.missing) {
    button.disabled = true;
    button.classList.add("is-missing");
    button.appendChild(
      createElement("span", "vg-missing-label", cell.placeholder_reason || "missing candidate"),
    );
    return button;
  }

  button.title = `${candidate.grounding_label} · ${candidate.model_label}`;
  button.ariaLabel = `${candidate.grounding_label} ${candidate.model_label} chart`;

  const frame = createElement("div", "vg-chart-frame");
  const canvas = createElement("div", "vg-chart-canvas");
  if (candidate.error) {
    canvas.appendChild(createElement("p", "vg-error", candidate.error));
  } else {
    setImage(
      canvas,
      candidate.hover_image_url || candidate.image_url,
      `${candidate.grounding_label} ${candidate.model_label}`,
    );
  }
  frame.appendChild(canvas);
  button.appendChild(frame);

  const meta = createElement("div", "vg-cell-meta");
  const guidelineLine =
    candidate.guideline_count > 0
      ? `${candidate.guideline_count} ${pluralize(candidate.guideline_count, "guideline")} used`
      : "No guidelines used";
  meta.appendChild(renderMetaLine(guidelineLine, "is-primary"));
  meta.appendChild(
    renderMetaLine(
      candidate.visualization_type
        ? `${formatValue(candidate.visualization_type)} chart`
        : "Chart type unavailable",
    ),
  );
  if (state.config.scores_enabled) {
    meta.appendChild(
      renderMetaLine(
        formatScore(candidate.overall_score)
          ? `Reviewer score ${formatScore(candidate.overall_score)}`
          : "Reviewer score unavailable",
      ),
    );
  }
  button.appendChild(meta);

  button.addEventListener("click", () => {
    actions.hideHover(true);
    actions.focusCell(candidate.grounding_mode, candidate.model);
  });
  button.addEventListener("pointerenter", () => actions.showHover(candidate, button));
  button.addEventListener("pointerleave", () => actions.scheduleHoverHide());
  button.addEventListener("focus", () => actions.showHover(candidate, button));
  button.addEventListener("blur", () => actions.scheduleHoverHide());

  return button;
}

function renderMatrixSection(state, refs, actions) {
  if (!state.overview) {
    clearNode(refs.matrixSection);
    return;
  }

  const schema = state.overview.ui_schema;
  const matrix = state.overview.matrix;
  const focusedKey =
    state.inspect && state.inspect.focused_candidate
      ? `${state.inspect.focused_grounding_mode}::${state.inspect.focused_model}`
      : null;

  clearNode(refs.matrixSection);
  refs.matrixSection.appendChild(
    buildRuleTitle(schema.copy.comparison_label, schema.copy.comparison_aside),
  );

  const wrap = createElement("div", "vg-matrix-wrap");
  const grid = createElement("div", "vg-matrix-grid");
  grid.style.setProperty("--vg-cols", String(matrix.columns.length));

  grid.appendChild(createElement("div", "vg-matrix-corner", schema.matrix_axes.row_label));

  matrix.columns.forEach((column) => {
    grid.appendChild(createElement("div", "vg-model-head", column.label));
  });

  matrix.rows.forEach((row) => {
    grid.appendChild(createElement("div", "vg-grounding-head", row.grounding_label));
    row.cells.forEach((cell) => {
      grid.appendChild(buildMatrixCell(cell, state, actions, focusedKey));
    });
  });

  wrap.appendChild(grid);
  refs.matrixSection.appendChild(wrap);
}

function buildReviewerSummary(candidate, copy) {
  const block = createElement("div", "vg-copy-block");
  const notes = [];
  const score = formatScore(candidate.overall_score);
  if (score) {
    notes.push(`Overall reviewer score ${score}.`);
  }
  (candidate.judgement_dimensions || [])
    .filter((dimension) => dimension.reasoning)
    .slice(0, 2)
    .forEach((dimension) => {
      notes.push(`${dimension.dimension_label}: ${dimension.reasoning}`);
    });

  if (notes.length === 0) {
    block.appendChild(createElement("p", "vg-copy", copy.empty_review));
    return block;
  }

  notes.forEach((note) => {
    block.appendChild(createElement("p", "vg-copy", note));
  });
  return block;
}

function renderJudgementBlock(candidate, copy) {
  if (!candidate.judgement_dimensions || candidate.judgement_dimensions.length === 0) {
    return createElement("p", "vg-copy", copy.empty_review);
  }
  const wrap = createElement("div", "vg-judgement-grid");
  candidate.judgement_dimensions.forEach((dimension) => {
    const card = createElement("div", "vg-judgement-card");
    const score = dimension.score ?? "—";
    card.appendChild(
      createElement("div", "vg-judgement-head", `${dimension.dimension_label} · ${score}`),
    );
    card.appendChild(createElement("p", "vg-copy", dimension.reasoning || copy.empty_review));
    wrap.appendChild(card);
  });
  return wrap;
}

function renderDetailSection(state, refs) {
  const inspect = state.inspect;
  const candidate = inspect?.focused_candidate;
  if (!candidate) {
    refs.detailSection.hidden = true;
    clearNode(refs.detailSection);
    return;
  }

  const copy = state.overview.ui_schema.copy;
  refs.detailSection.hidden = false;
  clearNode(refs.detailSection);
  refs.detailSection.appendChild(
    buildRuleTitle(copy.detail_label, `${candidate.grounding_label} · ${candidate.model_label}`),
  );

  const requestBlock = createElement("div", "vg-copy-block");
  requestBlock.appendChild(createElement("p", "vg-copy", candidate.nl_query));
  refs.detailSection.appendChild(renderSectionCard(copy.request_label, requestBlock));

  const hero = createElement("div", "vg-detail-hero");

  const previewBody = createElement("div", "vg-detail-preview");
  const previewFrame = createElement("div", "vg-detail-image-frame");
  const previewCanvas = createElement("div", "vg-chart-canvas is-detail");
  if (candidate.error) {
    previewCanvas.appendChild(createElement("p", "vg-error", candidate.error));
  } else {
    setImage(
      previewCanvas,
      candidate.image_url,
      `${candidate.grounding_label} ${candidate.model_label}`,
    );
  }
  previewFrame.appendChild(previewCanvas);
  previewBody.appendChild(previewFrame);
  hero.appendChild(renderSectionCard(copy.detail_preview_label, previewBody));

  const stack = createElement("div", "vg-detail-stack");

  const guidelines = createElement("div", "vg-copy-block");
  guidelines.appendChild(renderList(candidate.guideline_ids, copy.empty_guidelines));
  stack.appendChild(renderSectionCard(copy.detail_guidelines_label, guidelines));

  const story = createElement("div", "vg-copy-block");
  story.appendChild(renderList(candidate.grounding_story, copy.empty_grounding_story));
  stack.appendChild(renderSectionCard(copy.detail_story_label, story));

  const rationale = createElement("div", "vg-copy-block");
  rationale.appendChild(renderList(candidate.design_rationale, copy.empty_rationale));
  stack.appendChild(renderSectionCard(copy.detail_rationale_label, rationale));

  stack.appendChild(
    renderSectionCard(copy.detail_review_label, buildReviewerSummary(candidate, copy)),
  );
  hero.appendChild(stack);

  refs.detailSection.appendChild(hero);

  const advanced = createElement("details", "vg-advanced");
  const summary = createElement("summary", "vg-advanced-summary", copy.detail_advanced_label);
  advanced.appendChild(summary);
  const advancedGrid = createElement("div", "vg-advanced-grid");

  const interpretation = createElement("div", "vg-copy-block");
  interpretation.appendChild(
    renderCopyBlock(candidate.query_interpretation, copy.empty_interpretation),
  );
  advancedGrid.appendChild(renderSectionCard(copy.detail_interpretation_label, interpretation));

  const trace = createElement("div", "vg-copy-block");
  trace.appendChild(renderList(candidate.grounding_trace, copy.empty_grounding_story));
  advancedGrid.appendChild(renderSectionCard(copy.detail_trace_label, trace));

  advancedGrid.appendChild(
    renderSectionCard(copy.detail_judge_label, renderJudgementBlock(candidate, copy)),
  );

  advancedGrid.appendChild(
    renderSectionCard(
      copy.detail_metadata_label,
      renderKeyValueMap(candidate.data_profile, copy.empty_metadata),
    ),
  );

  const codeWrap = createElement("div", "vg-code-wrap");
  const code = createElement("pre", "vg-code");
  code.textContent = candidate.code || "";
  codeWrap.appendChild(code);
  advancedGrid.appendChild(renderSectionCard(copy.detail_code_label, codeWrap));

  advanced.appendChild(advancedGrid);
  refs.detailSection.appendChild(advanced);
}

function setContentBusy(state, refs) {
  const isBusy = !!state.busy;
  refs.loadingOverlay.hidden = !isBusy;
  refs.loadingMessage.textContent = state.busy || "";
  refs.contentFrame.classList.toggle("is-loading", isBusy);
}

function renderError(state, refs) {
  refs.errorBanner.hidden = !state.error;
  if (!state.error) {
    clearNode(refs.errorBanner);
    return;
  }
  clearNode(refs.errorBanner);
  refs.errorBanner.appendChild(createElement("strong", "", "Viewer error"));
  refs.errorBanner.appendChild(createElement("p", "vg-copy", state.error));
}

function showHoverCard(state, refs, candidate, anchor) {
  if (!state.overview || !candidate || !anchor) {
    hideHoverCard(state, refs, true);
    return;
  }
  const copy = state.overview.ui_schema.copy;
  const card = refs.hoverCard;
  clearNode(card);
  card.appendChild(
    buildRuleTitle(copy.hover_label, `${candidate.grounding_label} · ${candidate.model_label}`),
  );

  const preview = createElement("div", "vg-hover-image");
  const canvas = createElement("div", "vg-chart-canvas is-hover");
  if (candidate.error) {
    canvas.appendChild(createElement("p", "vg-error", candidate.error));
  } else {
    setImage(canvas, candidate.image_url, `${candidate.grounding_label} ${candidate.model_label}`);
  }
  preview.appendChild(canvas);
  card.appendChild(preview);

  const meta = createElement("div", "vg-hover-meta");
  const guidelineLine =
    candidate.guideline_count > 0
      ? `${candidate.guideline_count} ${pluralize(candidate.guideline_count, "guideline")} used`
      : "No guidelines used";
  meta.appendChild(renderMetaLine(guidelineLine, "is-primary"));
  card.appendChild(meta);

  const guidelines = createElement("div", "vg-copy-block");
  guidelines.appendChild(renderList(candidate.guideline_ids, copy.empty_guidelines));
  card.appendChild(renderSectionCard(copy.hover_guidelines_label, guidelines));

  const story = createElement("div", "vg-copy-block");
  story.appendChild(renderList(candidate.grounding_story, copy.empty_grounding_story));
  card.appendChild(renderSectionCard(copy.hover_story_label, story));

  state.hover = { candidate, anchor };
  card.hidden = false;
  positionHoverCard(refs);
}

function positionHoverCard(refs) {
  const card = refs.hoverCard;
  if (card.hidden || !refs.root.isConnected) {
    return;
  }
  const state = refs.root.__vg_state__;
  const anchor = state?.hover?.anchor;
  if (!anchor || !anchor.isConnected) {
    card.hidden = true;
    return;
  }

  const margin = 16;
  const anchorRect = anchor.getBoundingClientRect();
  card.style.top = "0px";
  card.style.left = "0px";
  const cardRect = card.getBoundingClientRect();

  let left = anchorRect.right + margin;
  if (left + cardRect.width > window.innerWidth - margin) {
    left = Math.max(margin, anchorRect.left - cardRect.width - margin);
  }

  let top = anchorRect.top;
  if (top + cardRect.height > window.innerHeight - margin) {
    top = Math.max(margin, window.innerHeight - cardRect.height - margin);
  }

  card.style.left = `${left}px`;
  card.style.top = `${top}px`;
}

function hideHoverCard(state, refs, immediate = false) {
  if (state.hoverHideTimer) {
    window.clearTimeout(state.hoverHideTimer);
    state.hoverHideTimer = null;
  }
  if (immediate) {
    refs.hoverCard.hidden = true;
    state.hover = null;
    return;
  }
  state.hoverHideTimer = window.setTimeout(() => {
    refs.hoverCard.hidden = true;
    state.hover = null;
    state.hoverHideTimer = null;
  }, HOVER_HIDE_DELAY_MS);
}

function syncOverview(state, refs, actions) {
  refs.root.dataset.assetVersion =
    state.overview?.ui_schema?.asset_version || state.config.asset_version || "";
  updateHeader(state, refs);
  updateTopbar(state, refs);
  renderError(state, refs);
  renderRequestSection(state, refs);
  renderControlsSection(state, refs, actions);
  renderMatrixSection(state, refs, actions);
  renderDetailSection(state, refs);
  setContentBusy(state, refs);

  if (!state.hover?.anchor?.isConnected) {
    hideHoverCard(state, refs, true);
  } else if (!refs.hoverCard.hidden) {
    positionHoverCard(refs);
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
      asset_version: "",
      scores_enabled: false,
    },
    value: clone(model.get("value") || {}),
    searchTerm: "",
    busy: "Loading comparison…",
    error: null,
    hover: null,
    hoverHideTimer: null,
    requestToken: 0,
  };
  root.__vg_state__ = state;

  function commitValue(nextValue) {
    state.value = clone(nextValue);
    model.set("value", state.value);
    model.save_changes();
  }

  const actions = {
    loadView(changes = {}) {
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
    showHover(candidate, anchor) {
      if (state.hoverHideTimer) {
        window.clearTimeout(state.hoverHideTimer);
        state.hoverHideTimer = null;
      }
      showHoverCard(state, refs, candidate, anchor);
    },
    scheduleHoverHide() {
      hideHoverCard(state, refs, false);
    },
    cancelHoverHide() {
      if (state.hoverHideTimer) {
        window.clearTimeout(state.hoverHideTimer);
        state.hoverHideTimer = null;
      }
    },
    hideHover(immediate = true) {
      hideHoverCard(state, refs, immediate);
    },
  };

  const refs = createShell(root, actions, state);

  function setBusy(message) {
    state.busy = message;
    setContentBusy(state, refs);
    updateTopbar(state, refs);
  }

  async function loadView(changes = {}) {
    const requestToken = ++state.requestToken;
    const message =
      changes.vis_id && changes.vis_id !== state.value.vis_id
        ? "Loading next case…"
        : "Updating comparison…";
    setBusy(message);
    state.error = null;
    renderError(state, refs);

    try {
      const payload = await invoke("load_view", {
        vis_id: changes.vis_id ?? state.value.vis_id,
        objective: Object.prototype.hasOwnProperty.call(changes, "objective")
          ? changes.objective
          : state.value.objective,
        grammar: Object.prototype.hasOwnProperty.call(changes, "grammar")
          ? changes.grammar
          : state.value.grammar,
        audience: Object.prototype.hasOwnProperty.call(changes, "audience")
          ? changes.audience
          : state.value.audience,
        view_mode: changes.view_mode ?? state.value.view_mode ?? "overview",
        focused_model: Object.prototype.hasOwnProperty.call(changes, "focused_model")
          ? changes.focused_model
          : state.value.focused_model,
        focused_grounding_mode: Object.prototype.hasOwnProperty.call(
          changes,
          "focused_grounding_mode",
        )
          ? changes.focused_grounding_mode
          : state.value.focused_grounding_mode,
      });

      if (requestToken !== state.requestToken) {
        return;
      }

      state.overview = payload.overview;
      state.inspect = payload.inspect;
      state.config = { ...state.config, ...payload.config };
      commitValue(payload.value);
      state.busy = null;
      syncOverview(state, refs, actions);
    } catch (error) {
      if (requestToken !== state.requestToken) {
        return;
      }
      state.busy = null;
      state.error = error instanceof Error ? error.message : String(error);
      renderError(state, refs);
      setContentBusy(state, refs);
      updateTopbar(state, refs);
    }
  }

  function onModelValueChange() {
    const nextValue = model.get("value");
    if (!nextValue) {
      return;
    }
    if (JSON.stringify(nextValue) === JSON.stringify(state.value)) {
      return;
    }
    state.value = clone(nextValue);
    loadView({
      vis_id: nextValue.vis_id,
      objective: nextValue.objective,
      grammar: nextValue.grammar,
      audience: nextValue.audience,
      view_mode: nextValue.view_mode,
      focused_model: nextValue.focused_model,
      focused_grounding_mode: nextValue.focused_grounding_mode,
    });
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

  function onViewportChange() {
    if (!refs.hoverCard.hidden) {
      positionHoverCard(refs);
    }
  }

  model.on("change:value", onModelValueChange);
  root.addEventListener("keydown", onKeydown);
  root.tabIndex = 0;
  window.addEventListener("resize", onViewportChange);
  window.addEventListener("scroll", onViewportChange, true);

  setContentBusy(state, refs);
  updateTopbar(state, refs);

  invoke("initialize", {})
    .then((payload) => {
      state.catalog = payload.catalog;
      state.overview = payload.overview;
      state.inspect = payload.inspect;
      state.config = { ...state.config, ...payload.config };
      state.value = clone(payload.value);
      state.busy = null;
      state.error = null;
      syncOverview(state, refs, actions);
    })
    .catch((error) => {
      state.busy = null;
      state.error = error instanceof Error ? error.message : String(error);
      renderError(state, refs);
      setContentBusy(state, refs);
    });

  return () => {
    model.off("change:value", onModelValueChange);
    root.removeEventListener("keydown", onKeydown);
    window.removeEventListener("resize", onViewportChange);
    window.removeEventListener("scroll", onViewportChange, true);
    hideHoverCard(state, refs, true);
  };
}

export default { render };
