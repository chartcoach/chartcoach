import "@pagefind/default-ui/css/ui.css";

import { Search, X } from "lucide-react";
import { useEffect, useId, useRef, useState } from "react";

import type { KeyboardEvent } from "react";
import type { PagefindResult } from "@pagefind/default-ui";

type SearchStatus = "idle" | "loading" | "ready" | "unavailable" | "failed";

const STATUS_MESSAGES: Record<SearchStatus, string> = {
  idle: "",
  loading: "Loading search...",
  ready: "",
  unavailable: "Search is available after a static build.",
  failed: "Search failed to load.",
};

const baseUrl = import.meta.env.BASE_URL;
const normalizedBase = baseUrl.replace(/\/$/, "");
const bundlePath = `${normalizedBase}/pagefind/`;

function normalizePagefindUrl(url: string) {
  if (normalizedBase === "" || url.startsWith(normalizedBase)) return url;
  return `${normalizedBase}${url}`;
}

function normalizeResult(result: PagefindResult) {
  result.url = normalizePagefindUrl(result.url);

  for (const subResult of result.sub_results ?? []) {
    subResult.url = normalizePagefindUrl(subResult.url);
  }
}

function iconClassName(active: boolean) {
  return ["size-4", "shrink-0", active ? "text-fg" : "text-muted"].join(" ");
}

function SearchFallback({ message }: { message: string }) {
  return (
    <div className="space-y-3">
      <div className="flex h-14 items-center gap-3 rounded-md border border-border bg-bg px-4 text-sm text-muted">
        <Search aria-hidden="true" className={iconClassName(false)} />
        <input
          className="min-w-0 flex-1 border-0 bg-transparent p-0 text-fg outline-none placeholder:text-muted"
          placeholder="Search guidelines"
          readOnly
          tabIndex={-1}
          aria-disabled="true"
        />
      </div>
      <p className="min-h-5 px-1 text-sm leading-5 text-muted">{message}</p>
    </div>
  );
}

export function GuidelineSearch() {
  const generatedId = useId().replace(/[^a-zA-Z0-9_-]/g, "");
  const searchRootId = `chartcoach-search-${generatedId}`;
  const [open, setOpen] = useState(false);
  const [status, setStatus] = useState<SearchStatus>("idle");
  const dialogRef = useRef<HTMLDivElement>(null);
  const searchRootRef = useRef<HTMLDivElement>(null);
  const searchMountedRef = useRef(false);

  function prepareSearchInput() {
    window.setTimeout(() => {
      const input = searchRootRef.current?.querySelector<HTMLInputElement>(
        ".pagefind-ui__search-input",
      );

      if (!input) return;

      input.placeholder = "Search guidelines";
      input.focus();
    }, 0);
  }

  function openSearch() {
    setOpen(true);
  }

  function closeSearch() {
    setOpen(false);
  }

  function focusAdjacentResult(direction: 1 | -1) {
    const dialog = dialogRef.current;
    if (!dialog) return;

    const input = dialog.querySelector<HTMLInputElement>(".pagefind-ui__search-input");
    const links = Array.from(
      dialog.querySelectorAll<HTMLAnchorElement>(".pagefind-ui__result-link"),
    );

    if (links.length === 0) return;

    const activeElement = document.activeElement;
    const activeLinkIndex = links.findIndex((link) => link === activeElement);

    if (direction === 1 && (activeElement === input || activeLinkIndex === -1)) {
      links[0]?.focus();
      return;
    }

    if (direction === -1 && activeElement === input) {
      links.at(-1)?.focus();
      return;
    }

    let nextIndex = activeLinkIndex === -1 ? 0 : activeLinkIndex + direction;
    nextIndex = Math.min(Math.max(nextIndex, 0), links.length - 1);
    links[nextIndex]?.focus();
  }

  function handleDialogKeyDown(event: KeyboardEvent<HTMLDivElement>) {
    if (event.key === "Escape") {
      closeSearch();
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
    }
  }

  useEffect(() => {
    function handleShortcut(event: globalThis.KeyboardEvent) {
      if (event.key.toLowerCase() !== "k") return;
      if (!event.metaKey && !event.ctrlKey) return;

      event.preventDefault();
      openSearch();
    }

    window.addEventListener("keydown", handleShortcut);
    return () => window.removeEventListener("keydown", handleShortcut);
  }, []);

  useEffect(() => {
    if (!open) return;

    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";

    return () => {
      document.body.style.overflow = previousOverflow;
    };
  }, [open]);

  useEffect(() => {
    if (!open) return;

    if (searchMountedRef.current) {
      prepareSearchInput();
      return;
    }

    if (!import.meta.env.PROD) {
      setStatus("unavailable");
      return;
    }

    let cancelled = false;
    setStatus("loading");

    import("@pagefind/default-ui")
      .then(({ PagefindUI }) => {
        if (cancelled) return;

        new PagefindUI({
          element: `#${searchRootId}`,
          bundlePath,
          baseUrl,
          showImages: false,
          showSubResults: true,
          resetStyles: false,
          translations: {
            placeholder: "Search guidelines",
            zero_results: "No guidelines found",
          },
          processResult: normalizeResult,
        });

        searchMountedRef.current = true;
        setStatus("ready");
        prepareSearchInput();
      })
      .catch(() => {
        if (!cancelled) setStatus("failed");
      });

    return () => {
      cancelled = true;
    };
  }, [open, searchRootId]);

  const statusMessage = STATUS_MESSAGES[status];
  const showFallback = open && status !== "ready" && !searchMountedRef.current;
  const overlayClassName = open
    ? "fixed inset-0 z-50 flex items-start justify-center px-4 pt-24 sm:pt-28"
    : "hidden";

  return (
    <div data-pagefind-ignore>
      <button
        type="button"
        className="hidden items-center gap-2 rounded-md border border-border bg-surface-muted px-3 py-1.5 text-sm text-muted transition-colors hover:border-fg/25 hover:text-fg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20 sm:flex"
        onClick={openSearch}
      >
        <Search aria-hidden="true" className={iconClassName(false)} />
        <span>Search guidelines</span>
        <kbd className="rounded border border-border bg-bg px-1.5 py-0.5 font-mono text-[11px] leading-none text-muted">
          ⌘K
        </kbd>
      </button>
      <button
        type="button"
        className="flex size-8 items-center justify-center rounded-md border border-border bg-surface-muted text-muted transition-colors hover:border-fg/25 hover:text-fg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20 sm:hidden"
        aria-label="Search guidelines"
        onClick={openSearch}
      >
        <Search aria-hidden="true" className={iconClassName(false)} />
      </button>
      <div
        aria-hidden={!open}
        className={overlayClassName}
        onMouseDown={(event) => {
          if (event.target === event.currentTarget) closeSearch();
        }}
      >
        <div
          ref={dialogRef}
          role="dialog"
          aria-modal="true"
          aria-labelledby="guideline-search-title"
          className="w-full max-w-2xl overflow-hidden rounded-lg border border-border bg-bg shadow-2xl"
          onKeyDown={handleDialogKeyDown}
        >
          <div className="flex items-center justify-between border-b border-border px-4 py-3">
            <div className="flex items-center gap-2 text-sm font-medium text-fg">
              <Search aria-hidden="true" className={iconClassName(true)} />
              <h2 id="guideline-search-title">Search guidelines</h2>
            </div>
            <button
              type="button"
              className="flex size-8 items-center justify-center rounded-md text-muted transition-colors hover:bg-surface-muted hover:text-fg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-fg/20"
              aria-label="Close search"
              onClick={closeSearch}
            >
              <X aria-hidden="true" className="size-4" />
            </button>
          </div>
          <div className="min-h-[8.5rem] p-4">
            <div id={searchRootId} ref={searchRootRef} className="chartcoach-search" />
            {showFallback ? <SearchFallback message={statusMessage} /> : null}
          </div>
        </div>
      </div>
    </div>
  );
}
