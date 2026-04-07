import {
  decodeGuidelineLabelQueryValue,
  encodeGuidelineLabelQueryValue,
  formatGuidelineLabelFilter,
  normalizeGuidelineLabelFilter,
} from "@/lib/guidelines/labels";

type GuidelineCard = {
  el: HTMLElement;
  labels: string[];
};

type SuggestionsData = {
  families?: unknown;
  labels?: unknown;
};

const guidelineCardSelector = "[data-guideline-card]";
const suggestionOptionId = (index: number) => `guidelines-label-suggestion-${index}`;
const activeSuggestionSelector = '[aria-selected="true"]';
const filterChipButtonClasses =
  "inline-flex cursor-pointer items-center gap-[0.38rem] rounded-pill border border-chip-border bg-chip px-[0.45rem] py-[0.2rem] font-mono text-[0.68rem] font-medium leading-[1.15] text-muted-foreground transition-colors hover:bg-surface-strong focus-visible:bg-surface-strong";
const filterChipLabelClasses = "font-bold tracking-[0.02em]";
const filterChipDismissClasses = "text-muted-foreground";
const suggestionButtonClasses =
  "w-full rounded-none bg-transparent px-[0.62rem] py-2 text-left font-mono text-[0.82rem] font-medium leading-[1.3] text-foreground transition-colors hover:bg-surface-strong focus-visible:bg-surface-strong aria-selected:bg-surface-strong";

function readCards(grid: HTMLElement): GuidelineCard[] {
  return Array.from(grid.querySelectorAll<HTMLElement>(guidelineCardSelector)).map((el) => ({
    el,
    labels: (el.dataset.labels ?? "")
      .split("|")
      .map((label) => label.trim().toLowerCase())
      .filter(Boolean),
  }));
}

function matchesLabels(cardLabels: string[], active: Set<string>): boolean {
  for (const rawFilter of active) {
    const filter = normalizeGuidelineLabelFilter(rawFilter);
    if (!filter) continue;

    if (filter.includes(":")) {
      if (!cardLabels.includes(filter)) return false;
      continue;
    }

    const familyPrefix = `${filter}:`;
    if (!cardLabels.some((label) => label === filter || label.startsWith(familyPrefix)))
      return false;
  }

  return true;
}

function renderActiveFilters(container: HTMLElement, active: Set<string>) {
  const list = container.querySelector<HTMLUListElement>("#guidelines-filters-list");
  if (!list) return;

  const items = Array.from(active).map(normalizeGuidelineLabelFilter).filter(Boolean).sort();
  container.toggleAttribute("hidden", items.length === 0);
  list.textContent = "";

  for (const filter of items) {
    const label = formatGuidelineLabelFilter(filter);
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = filterChipButtonClasses;
    btn.dataset.filterValue = filter;
    btn.setAttribute("aria-label", `Remove filter ${label}`);

    const labelSpan = document.createElement("span");
    labelSpan.className = filterChipLabelClasses;
    labelSpan.textContent = label;

    const xSpan = document.createElement("span");
    xSpan.className = filterChipDismissClasses;
    xSpan.textContent = "×";
    xSpan.setAttribute("aria-hidden", "true");

    btn.append(labelSpan, xSpan);
    li.append(btn);
    list.append(li);
  }
}

function readSuggestions(): string[] {
  const el = document.getElementById("guidelines-label-suggestions-data");
  if (!(el instanceof HTMLScriptElement)) return [];
  const raw = el.textContent?.trim();
  if (!raw) return [];

  try {
    const parsed = JSON.parse(raw) as SuggestionsData;
    const families = Array.isArray(parsed.families) ? parsed.families : [];
    const labels = Array.isArray(parsed.labels) ? parsed.labels : [];
    const values = [...families, ...labels]
      .map((value) => (typeof value === "string" ? normalizeGuidelineLabelFilter(value) : ""))
      .filter(Boolean);
    return Array.from(new Set(values)).sort();
  } catch {
    return [];
  }
}

function getSuggestionMatches(all: string[], query: string, active: Set<string>): string[] {
  const startsWith: string[] = [];
  const contains: string[] = [];

  for (const value of all) {
    if (active.has(value)) continue;
    if (value.startsWith(query)) startsWith.push(value);
    else if (value.includes(query)) contains.push(value);
  }

  return [...startsWith, ...contains].slice(0, 12);
}

function scrollSuggestionIntoView(container: HTMLElement, el: HTMLElement) {
  const containerTop = container.scrollTop;
  const containerBottom = containerTop + container.clientHeight;
  const elTop = el.offsetTop;
  const elBottom = elTop + el.offsetHeight;

  if (elTop < containerTop) container.scrollTop = elTop;
  else if (elBottom > containerBottom) container.scrollTop = elBottom - container.clientHeight;
}

function updateUrl(active: Set<string>) {
  const url = new URL(window.location.href);
  url.searchParams.delete("q");
  url.searchParams.delete("label");

  for (const label of Array.from(active)
    .map(normalizeGuidelineLabelFilter)
    .filter(Boolean)
    .sort()) {
    url.searchParams.append("label", encodeGuidelineLabelQueryValue(label));
  }

  history.replaceState(null, "", url);
}

function updateCountLabel(
  countEl: HTMLElement,
  visible: number,
  total: number,
  hasFilters: boolean,
) {
  countEl.textContent = hasFilters
    ? `${visible.toLocaleString()} of ${total.toLocaleString()} guidelines`
    : `${total.toLocaleString()} guidelines`;
}

export function initGuidelineLabelFilters() {
  const grid = document.getElementById("guidelines-grid");
  const countEl = document.getElementById("guidelines-count");
  const filters = document.getElementById("guidelines-filters");
  const filtersClear = document.getElementById("guidelines-filters-clear");
  const form = document.getElementById("guidelines-filter-form");
  const input = document.getElementById("guidelines-filter-input");
  const suggestionsEl = document.getElementById("guidelines-label-suggestions");

  if (!(grid instanceof HTMLElement)) return;
  if (!(countEl instanceof HTMLElement)) return;
  if (!(filters instanceof HTMLElement)) return;
  if (!(filtersClear instanceof HTMLButtonElement)) return;
  if (!(form instanceof HTMLFormElement)) return;
  if (!(input instanceof HTMLInputElement)) return;
  if (!(suggestionsEl instanceof HTMLElement)) return;

  const gridEl = grid;
  const countLabelEl = countEl;
  const filtersEl = filters;
  const filtersClearButton = filtersClear;
  const formEl = form;
  const inputEl = input;
  const suggestionsListEl = suggestionsEl;

  const total = Number.parseInt(countLabelEl.dataset.totalGuidelines ?? "", 10) || 0;
  const cards = readCards(gridEl);
  const suggestions = readSuggestions();

  const state = {
    labels: new Set<string>(),
  };

  const params = new URLSearchParams(window.location.search);
  for (const value of params.getAll("label")) {
    const normalized = normalizeGuidelineLabelFilter(decodeGuidelineLabelQueryValue(value));
    if (normalized) state.labels.add(normalized);
  }

  function update() {
    let visible = 0;

    for (const card of cards) {
      const ok = matchesLabels(card.labels, state.labels);
      card.el.toggleAttribute("hidden", !ok);
      if (ok) visible += 1;
    }

    renderActiveFilters(filtersEl, state.labels);
    updateUrl(state.labels);
    updateCountLabel(countLabelEl, visible, total || cards.length, state.labels.size > 0);
  }

  const suggestionState = {
    open: false,
    activeIndex: -1,
    items: [] as string[],
  };

  function closeSuggestions() {
    suggestionState.open = false;
    suggestionState.activeIndex = -1;
    suggestionState.items = [];
    suggestionsListEl.textContent = "";
    suggestionsListEl.hidden = true;
    inputEl.setAttribute("aria-expanded", "false");
    inputEl.removeAttribute("aria-activedescendant");
  }

  function syncActiveDescendant() {
    if (suggestionState.activeIndex < 0) {
      inputEl.removeAttribute("aria-activedescendant");
      return;
    }

    inputEl.setAttribute("aria-activedescendant", suggestionOptionId(suggestionState.activeIndex));
  }

  function renderSuggestions() {
    suggestionsListEl.textContent = "";
    suggestionsListEl.hidden = suggestionState.items.length === 0;
    inputEl.setAttribute("aria-expanded", suggestionState.items.length ? "true" : "false");

    for (const [index, value] of suggestionState.items.entries()) {
      const btn = document.createElement("button");
      btn.id = suggestionOptionId(index);
      btn.type = "button";
      btn.className = suggestionButtonClasses;
      btn.role = "option";
      btn.dataset.value = value;
      btn.textContent = formatGuidelineLabelFilter(value);
      btn.tabIndex = -1;

      const selected = index === suggestionState.activeIndex;
      btn.setAttribute("aria-selected", selected ? "true" : "false");

      suggestionsListEl.append(btn);
    }

    syncActiveDescendant();
  }

  function applySuggestion(value: string) {
    const normalized = normalizeGuidelineLabelFilter(value);
    if (!normalized) return;

    state.labels.add(normalized);
    inputEl.value = "";
    closeSuggestions();
    update();
  }

  function updateSuggestions() {
    const query = normalizeGuidelineLabelFilter(inputEl.value);
    if (!query || suggestions.length === 0) {
      closeSuggestions();
      return;
    }

    const matches = getSuggestionMatches(suggestions, query, state.labels);
    suggestionState.items = matches;
    suggestionState.open = matches.length > 0;
    suggestionState.activeIndex = -1;
    renderSuggestions();

    const active = suggestionsListEl.querySelector<HTMLElement>(activeSuggestionSelector);
    if (active) scrollSuggestionIntoView(suggestionsListEl, active);
  }

  formEl.addEventListener("submit", (event) => {
    event.preventDefault();

    const parts = inputEl.value
      .split(/[,;\n]/)
      .map((part) => normalizeGuidelineLabelFilter(part))
      .filter(Boolean);

    if (parts.length === 0) return;
    let changed = false;
    for (const value of parts) {
      if (state.labels.has(value)) continue;
      state.labels.add(value);
      changed = true;
    }

    if (!changed) return;
    inputEl.value = "";
    closeSuggestions();
    update();
  });

  inputEl.addEventListener("input", () => {
    if (!suggestions.length) return;
    updateSuggestions();
  });

  inputEl.addEventListener("focus", () => {
    if (!suggestions.length) return;
    updateSuggestions();
  });

  inputEl.addEventListener("blur", () => {
    window.setTimeout(() => {
      if (formEl.contains(document.activeElement)) return;
      closeSuggestions();
    }, 0);
  });

  inputEl.addEventListener("keydown", (event) => {
    if (!suggestionState.open) {
      if (event.key === "ArrowDown" && suggestions.length) {
        updateSuggestions();
        if (suggestionState.items.length > 0) {
          suggestionState.activeIndex = 0;
          renderSuggestions();
          const active = suggestionsListEl.querySelector<HTMLElement>(activeSuggestionSelector);
          if (active) scrollSuggestionIntoView(suggestionsListEl, active);
        }
        event.preventDefault();
      }
      return;
    }

    if (event.key === "Escape") {
      closeSuggestions();
      return;
    }

    if (event.key === "ArrowDown") {
      event.preventDefault();
      if (suggestionState.activeIndex === -1) suggestionState.activeIndex = 0;
      else
        suggestionState.activeIndex = Math.min(
          suggestionState.activeIndex + 1,
          suggestionState.items.length - 1,
        );
      renderSuggestions();
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      if (suggestionState.activeIndex === -1) suggestionState.activeIndex = 0;
      else suggestionState.activeIndex = Math.max(suggestionState.activeIndex - 1, 0);
      renderSuggestions();
    } else if (event.key === "Enter" && suggestionState.activeIndex >= 0) {
      const value = suggestionState.items[suggestionState.activeIndex];
      if (value) {
        event.preventDefault();
        applySuggestion(value);
      }
      return;
    }

    const active = suggestionsListEl.querySelector<HTMLElement>(activeSuggestionSelector);
    if (active) scrollSuggestionIntoView(suggestionsListEl, active);
  });

  suggestionsListEl.addEventListener("click", (event) => {
    if (!(event.target instanceof Element)) return;
    const btn = event.target.closest("button[data-value]");
    if (!(btn instanceof HTMLButtonElement)) return;
    const value = btn.dataset.value ?? "";
    if (!value) return;
    applySuggestion(value);
  });

  document.addEventListener("click", (event) => {
    if (!(event.target instanceof Node)) return;
    if (formEl.contains(event.target)) return;
    closeSuggestions();
  });

  gridEl.addEventListener("click", (event) => {
    if (!(event.target instanceof Element)) return;
    if (event.metaKey || event.ctrlKey) return;

    const link = event.target.closest("a[data-filter-value]");
    if (!(link instanceof HTMLAnchorElement)) return;
    const value = normalizeGuidelineLabelFilter(link.dataset.filterValue ?? "");
    if (!value) return;

    event.preventDefault();
    if (state.labels.has(value)) state.labels.delete(value);
    else state.labels.add(value);
    closeSuggestions();
    update();
  });

  filtersEl.addEventListener("click", (event) => {
    if (!(event.target instanceof Element)) return;
    const btn = event.target.closest("button[data-filter-value]");
    if (!(btn instanceof HTMLButtonElement)) return;
    const value = normalizeGuidelineLabelFilter(btn.dataset.filterValue ?? "");
    if (!value) return;

    state.labels.delete(value);
    closeSuggestions();
    update();
  });

  filtersClearButton.addEventListener("click", () => {
    state.labels.clear();
    closeSuggestions();
    update();
  });

  update();
}
