import { Command, Loader2, Search, X } from "lucide-react";
import { useCallback, useEffect, useId, useRef } from "react";

import { normalizedSearchBase, useGuidelineSearch } from "@/components/use-guideline-search";

import type { IndexStatus, SearchResult, SearchStatus } from "@/components/use-guideline-search";
import type { KeyboardEvent, RefObject } from "react";

const EXCERPT_RADIUS = 92;
const EXAMPLE_QUERIES = ["color vision deficiency", "tooltip values", "uncertainty"] as const;
const RESULT_LABEL_LIMIT = 3;

function classNames(...values: Array<string | false | null | undefined>) {
  return values.filter(Boolean).join(" ");
}

function iconClassName(active: boolean) {
  return classNames("size-4 shrink-0", active ? "text-fg" : "text-muted");
}

function normalizeResultHref(path: string) {
  const normalizedPath = `/${path.replace(/^\/+/, "")}`;
  if (!normalizedSearchBase) return normalizedPath;
  if (normalizedPath.startsWith(`${normalizedSearchBase}/`)) return normalizedPath;
  return `${normalizedSearchBase}${normalizedPath}`;
}

function cleanTitle(result: SearchResult) {
  return (result.document.title || "Untitled guideline").replace(/\s+\|\s+chartcoach$/i, "").trim();
}

function normalizeText(value: string) {
  return value.replace(/\s+/g, " ").trim();
}

function queryTerms(query: string) {
  return query
    .toLowerCase()
    .split(/\s+/)
    .map((term) => term.trim())
    .filter((term) => term.length > 1);
}

function searchTextSources(result: SearchResult) {
  const document = result.document;
  return [
    document.slug,
    document.description,
    ...document.sectionTitles,
    document.body,
    ...document.sectionContent,
    ...document.labels,
    document.bibliography,
    ...document.references,
  ];
}

function createExcerpt(result: SearchResult, query: string) {
  const source =
    searchTextSources(result)
      .map(normalizeText)
      .find((candidate) =>
        queryTerms(query).some((term) => candidate.toLowerCase().includes(term)),
      ) ??
    normalizeText(result.document.description || result.document.body || result.document.title);

  if (!source) return "";

  const lowerSource = source.toLowerCase();
  const matchIndex = queryTerms(query).reduce<number | null>((bestIndex, term) => {
    const index = lowerSource.indexOf(term);
    if (index === -1) return bestIndex;
    if (bestIndex === null) return index;
    return Math.min(bestIndex, index);
  }, null);

  if (matchIndex === null) return source.slice(0, EXCERPT_RADIUS * 2);

  const start = Math.max(0, matchIndex - EXCERPT_RADIUS);
  const end = Math.min(source.length, matchIndex + EXCERPT_RADIUS);
  const prefix = start > 0 ? "... " : "";
  const suffix = end < source.length ? " ..." : "";
  return `${prefix}${source.slice(start, end)}${suffix}`;
}

function matchingLabels(result: SearchResult, query: string) {
  const terms = queryTerms(query);
  if (terms.length === 0) return [];

  return result.document.labels
    .filter((label) => {
      const lowerLabel = label.toLowerCase();
      return terms.some((term) => lowerLabel.includes(term));
    })
    .slice(0, RESULT_LABEL_LIMIT);
}

function escapeRegExp(value: string) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function HighlightedText({ text, query }: { text: string; query: string }) {
  const terms = queryTerms(query);
  if (terms.length === 0) return <>{text}</>;

  const pattern = new RegExp(`(${terms.map(escapeRegExp).join("|")})`, "gi");
  const parts = text.split(pattern);

  return (
    <>
      {parts.map((part, index) => {
        const matched = terms.includes(part.toLowerCase());
        return matched ? (
          <mark key={`${part}-${index}`} className="rounded-sm bg-fg/10 px-[0.08em] text-fg">
            {part}
          </mark>
        ) : (
          <span key={`${part}-${index}`}>{part}</span>
        );
      })}
    </>
  );
}

function useSearchShortcut(onOpen: () => void) {
  useEffect(() => {
    function handleShortcut(event: globalThis.KeyboardEvent) {
      if (event.defaultPrevented) return;
      if (event.key.toLowerCase() !== "k") return;
      if (!event.metaKey && !event.ctrlKey) return;

      event.preventDefault();
      onOpen();
    }

    window.addEventListener("keydown", handleShortcut);
    return () => window.removeEventListener("keydown", handleShortcut);
  }, [onOpen]);
}

function SearchShortcutHint() {
  const keyClassName =
    "grid h-5 place-items-center border border-border bg-bg font-mono text-[11px] font-medium leading-none text-muted";

  return (
    <span
      className="hidden items-center sm:inline-flex"
      aria-hidden="true"
      data-search-shortcut
    >
      <kbd
        className={classNames(
          keyClassName,
          "guideline-search-shortcut__modifier--control min-w-8 rounded-l border-r-0 px-1.5",
        )}
        data-search-shortcut-key="control"
      >
        Ctrl
      </kbd>
      <kbd
        className={classNames(
          keyClassName,
          "guideline-search-shortcut__modifier--command w-5 rounded-l border-r-0 p-0",
        )}
        data-search-shortcut-key="command"
      >
        <Command aria-hidden="true" className="size-3" strokeWidth={2} />
      </kbd>
      <kbd
        className={classNames(keyClassName, "w-5 rounded-r border-l-0 p-0")}
        data-search-shortcut-key="k"
      >
        K
      </kbd>
    </span>
  );
}

function SearchStatusText({
  indexStatus,
  searchStatus,
  query,
  resultCount,
}: {
  indexStatus: IndexStatus;
  searchStatus: SearchStatus;
  query: string;
  resultCount: number;
}) {
  let message = "Search guideline titles, slugs, labels, and section text.";

  if (indexStatus === "loading") message = "Loading search index...";
  if (indexStatus === "failed") message = "Search index failed to load.";
  if (indexStatus === "ready" && searchStatus === "searching") message = "Searching...";
  if (indexStatus === "ready" && searchStatus === "empty")
    message = `No guidelines found for "${query}".`;
  if (indexStatus === "ready" && searchStatus === "ready") {
    message = `${resultCount.toLocaleString()} result${resultCount === 1 ? "" : "s"} for "${query}".`;
  }

  return <p className="m-0 min-h-5 text-sm leading-5 text-muted">{message}</p>;
}

function SearchTrigger({ open, onOpen }: { open: boolean; onOpen: () => void }) {
  return (
    <button
      type="button"
      className="flex h-8 shrink-0 items-center justify-center gap-2 rounded-md border border-border bg-surface-muted px-2.5 text-sm text-muted transition-colors hover:border-fg/25 hover:text-fg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20 min-[520px]:px-3"
      aria-label="Search guidelines"
      aria-keyshortcuts="Meta+K Control+K"
      aria-expanded={open}
      aria-controls={open ? "guideline-search-dialog" : undefined}
      onClick={onOpen}
    >
      <Search aria-hidden="true" className={iconClassName(false)} />
      <span className="hidden whitespace-nowrap min-[520px]:inline">Search guidelines</span>
      <SearchShortcutHint />
    </button>
  );
}

function SearchInputRow({
  inputId,
  inputRef,
  indexStatus,
  onInputKeyDown,
  query,
  onClose,
  onQueryChange,
}: {
  inputId: string;
  inputRef: RefObject<HTMLInputElement | null>;
  indexStatus: IndexStatus;
  onInputKeyDown: (event: KeyboardEvent<HTMLInputElement>) => void;
  query: string;
  onClose: () => void;
  onQueryChange: (query: string) => void;
}) {
  return (
    <div className="flex h-14 items-center gap-3 border-b border-border px-3 sm:px-4">
      <Search aria-hidden="true" className={iconClassName(true)} />
      <h2 id="guideline-search-title" className="sr-only">
        Search guidelines
      </h2>
      <label className="sr-only" htmlFor={inputId}>
        Search guideline records
      </label>
      <input
        id={inputId}
        ref={inputRef}
        className="min-w-0 flex-1 border-0 bg-transparent p-0 text-[1rem] text-fg outline-none placeholder:text-muted"
        value={query}
        placeholder="Search guidelines"
        autoComplete="off"
        onChange={(event) => onQueryChange(event.target.value)}
        onKeyDown={onInputKeyDown}
      />
      {indexStatus === "loading" ? (
        <Loader2 aria-hidden="true" className="size-4 shrink-0 animate-spin text-muted" />
      ) : null}
      <button
        type="button"
        className="flex size-8 shrink-0 items-center justify-center rounded-md text-muted transition-colors hover:bg-surface-muted hover:text-fg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20"
        aria-label="Close search"
        onClick={onClose}
      >
        <X aria-hidden="true" className="size-4" />
      </button>
    </div>
  );
}

function SearchResultItem({
  active,
  query,
  result,
  onActivate,
  onKeyDown,
}: {
  active: boolean;
  query: string;
  result: SearchResult;
  onActivate: (id: string) => void;
  onKeyDown: (event: KeyboardEvent<HTMLAnchorElement>) => void;
}) {
  const title = cleanTitle(result);
  const excerpt = createExcerpt(result, query);
  const labels = matchingLabels(result, query);

  return (
    <li>
      <a
        data-search-result-link
        data-search-result-id={result.id}
        data-active={active ? "true" : "false"}
        href={normalizeResultHref(result.document.path)}
        className={classNames(
          "block rounded-md px-3 py-3 text-fg no-underline transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20",
          active ? "bg-surface-muted" : "hover:bg-surface-muted/70",
        )}
        onMouseMove={() => onActivate(result.id)}
        onFocus={() => onActivate(result.id)}
        onKeyDown={onKeyDown}
      >
        <span className="block text-[0.95rem] font-semibold leading-snug">
          <HighlightedText text={title} query={query} />
        </span>
        {excerpt ? (
          <span className="mt-1.5 block text-[0.8125rem] leading-[1.55] text-muted">
            <HighlightedText text={excerpt} query={query} />
          </span>
        ) : null}
        {labels.length > 0 ? (
          <span className="mt-2 flex flex-wrap gap-1.5">
            {labels.map((label) => (
              <span
                key={label}
                className="rounded-md bg-surface px-1.5 py-0.5 font-mono text-[0.6875rem] leading-4 text-muted"
              >
                <HighlightedText text={label} query={query} />
              </span>
            ))}
          </span>
        ) : null}
      </a>
    </li>
  );
}

function SearchResultsList({
  activeResultId,
  query,
  results,
  onActivate,
  onResultKeyDown,
}: {
  activeResultId: string | null;
  query: string;
  results: SearchResult[];
  onActivate: (id: string) => void;
  onResultKeyDown: (event: KeyboardEvent<HTMLAnchorElement>) => void;
}) {
  return (
    <ol className="guideline-search-results max-h-[min(56vh,28rem)] list-none space-y-1 overflow-y-auto p-1">
      {results.map((result) => (
        <SearchResultItem
          key={result.id}
          active={result.id === activeResultId}
          query={query}
          result={result}
          onActivate={onActivate}
          onKeyDown={onResultKeyDown}
        />
      ))}
    </ol>
  );
}

function SearchExamples({ onSelect }: { onSelect: (query: string) => void }) {
  return (
    <div className="flex flex-col items-center gap-3">
      <p className="m-0 text-[0.6875rem] font-medium uppercase leading-none tracking-[0.18em] text-muted">
        Try searching for
      </p>
      <div className="flex flex-wrap justify-center gap-2.5">
        {EXAMPLE_QUERIES.map((query) => (
          <button
            key={query}
            type="button"
            className="h-9 rounded-md border border-border bg-surface px-3.5 text-sm text-fg transition-colors hover:bg-surface-muted focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20"
            onClick={() => onSelect(query)}
          >
            {query}
          </button>
        ))}
      </div>
    </div>
  );
}

function SearchEmptyState({
  indexStatus,
  onQueryChange,
  onRetry,
  searchStatus,
  query,
}: {
  indexStatus: IndexStatus;
  onQueryChange: (query: string) => void;
  onRetry: () => void;
  searchStatus: SearchStatus;
  query: string;
}) {
  const showExamples = indexStatus === "ready" && searchStatus === "idle" && query.length === 0;
  const showRetry = indexStatus === "failed";

  return (
    <div className="flex min-h-44 items-center justify-center px-6 py-9 text-center">
      <div className="flex max-w-lg flex-col items-center gap-7">
        <SearchStatusText
          indexStatus={indexStatus}
          searchStatus={searchStatus}
          query={query}
          resultCount={0}
        />
        {showExamples ? <SearchExamples onSelect={onQueryChange} /> : null}
        {showRetry ? (
          <button
            type="button"
            className="rounded-md border border-border bg-surface px-3 py-1.5 text-sm font-medium text-fg transition-colors hover:bg-surface-muted focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20"
            onClick={onRetry}
          >
            Retry
          </button>
        ) : null}
      </div>
    </div>
  );
}

function SearchFooter({
  indexStatus,
  query,
  resultCount,
  searchStatus,
}: {
  indexStatus: IndexStatus;
  query: string;
  resultCount: number;
  searchStatus: SearchStatus;
}) {
  return (
    <div className="px-4 py-3">
      <SearchStatusText
        indexStatus={indexStatus}
        searchStatus={searchStatus}
        query={query}
        resultCount={resultCount}
      />
    </div>
  );
}

function resultLinks(dialog: HTMLDialogElement | null) {
  if (!dialog) return [];
  return Array.from(dialog.querySelectorAll<HTMLAnchorElement>("[data-search-result-link]"));
}

export function GuidelineSearch() {
  const generatedId = useId().replace(/[^a-zA-Z0-9_-]/g, "");
  const inputId = `chartcoach-search-${generatedId}`;
  const dialogRef = useRef<HTMLDialogElement | null>(null);
  const dialogCleanupRef = useRef<(() => void) | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const searchState = useGuidelineSearch();
  const hasResults = searchState.results.length > 0;

  useSearchShortcut(searchState.openSearch);

  const setDialogElement = useCallback(
    (node: HTMLDialogElement | null) => {
      dialogCleanupRef.current?.();
      dialogCleanupRef.current = null;
      dialogRef.current = node;
      if (!node) return;

      function handleClose() {
        searchState.closeSearch();
      }

      node.addEventListener("close", handleClose);
      dialogCleanupRef.current = () => node.removeEventListener("close", handleClose);
      if (!node.open) node.showModal();
      setTimeout(() => inputRef.current?.focus(), 0);
    },
    [searchState.closeSearch],
  );

  function focusAdjacentResult(direction: 1 | -1) {
    const links = resultLinks(dialogRef.current);
    if (links.length === 0) return;

    const activeElement = document.activeElement;
    const activeLinkIndex = links.findIndex((link) => link === activeElement);

    if (direction === 1 && (activeElement === inputRef.current || activeLinkIndex === -1)) {
      const firstLink = links[0];
      firstLink?.focus();
      searchState.setActiveResultId(firstLink?.dataset.searchResultId ?? null);
      return;
    }

    if (direction === -1 && activeElement === inputRef.current) {
      const lastLink = links.at(-1);
      lastLink?.focus();
      searchState.setActiveResultId(lastLink?.dataset.searchResultId ?? null);
      return;
    }

    let nextIndex = activeLinkIndex === -1 ? 0 : activeLinkIndex + direction;
    nextIndex = Math.min(Math.max(nextIndex, 0), links.length - 1);
    links[nextIndex]?.focus();
    searchState.setActiveResultId(links[nextIndex]?.dataset.searchResultId ?? null);
  }

  function openActiveResult() {
    if (!searchState.activeResult) return;
    window.location.href = normalizeResultHref(searchState.activeResult.document.path);
  }

  function handleSearchKeyDown(event: KeyboardEvent<HTMLInputElement | HTMLAnchorElement>) {
    if (event.key === "Escape") {
      searchState.closeSearch();
      return;
    }

    if (event.key === "ArrowDown") {
      event.preventDefault();
      focusAdjacentResult(1);
      return;
    }

    if (event.key === "ArrowUp") {
      event.preventDefault();
      focusAdjacentResult(-1);
      return;
    }

    if (event.key === "Enter" && event.currentTarget === inputRef.current && hasResults) {
      event.preventDefault();
      openActiveResult();
    }
  }

  return (
    <div>
      <SearchTrigger open={searchState.open} onOpen={searchState.openSearch} />
      {searchState.open ? (
        <dialog
          id="guideline-search-dialog"
          ref={setDialogElement}
          aria-labelledby="guideline-search-title"
          tabIndex={-1}
          className="guideline-search-dialog fixed left-1/2 top-16 z-50 m-0 max-h-[calc(100vh-5rem)] w-[calc(100vw-1.5rem)] max-w-2xl -translate-x-1/2 overflow-hidden rounded-lg border border-border bg-bg p-0 text-fg shadow-2xl sm:top-24 sm:max-h-[calc(100vh-7rem)] sm:w-[calc(100vw-2rem)]"
        >
          <SearchInputRow
            inputId={inputId}
            inputRef={inputRef}
            indexStatus={searchState.indexStatus}
            onInputKeyDown={handleSearchKeyDown}
            query={searchState.query}
            onClose={searchState.closeSearch}
            onQueryChange={searchState.setQuery}
          />
          <div className="min-h-44 border-b border-border p-2">
            {hasResults ? (
              <SearchResultsList
                activeResultId={searchState.activeResultId}
                query={searchState.trimmedQuery}
                results={searchState.results}
                onActivate={searchState.setActiveResultId}
                onResultKeyDown={handleSearchKeyDown}
              />
            ) : (
              <SearchEmptyState
                indexStatus={searchState.indexStatus}
                onQueryChange={searchState.setQuery}
                onRetry={searchState.retrySearch}
                searchStatus={searchState.searchStatus}
                query={searchState.trimmedQuery}
              />
            )}
          </div>
          {hasResults ? (
            <SearchFooter
              indexStatus={searchState.indexStatus}
              query={searchState.trimmedQuery}
              resultCount={searchState.results.length}
              searchStatus={searchState.searchStatus}
            />
          ) : null}
        </dialog>
      ) : null}
    </div>
  );
}
