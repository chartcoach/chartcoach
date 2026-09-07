import { create, load, search, type RawData } from "zbsearch";
import { startTransition, useEffect, useMemo } from "react";
import { create as createZustandStore } from "zustand";
import { useShallow } from "zustand/react/shallow";

import {
  GUIDELINE_SEARCH_BOOST,
  GUIDELINE_SEARCH_PROPERTIES,
  GUIDELINE_SEARCH_SCHEMA,
  type GuidelineSearchDocument,
} from "@/lib/guideline-search-model";

export type IndexStatus = "idle" | "loading" | "ready" | "failed";
export type SearchStatus = "idle" | "searching" | "ready" | "empty";

export type SearchResult = {
  id: string;
  score: number;
  document: GuidelineSearchDocument;
};

const RESULT_LIMIT = 8;
const INDEX_REQUEST_TIMEOUT_MS = 30_000;
const baseUrl = import.meta.env.BASE_URL;
export const normalizedSearchBase = baseUrl.replace(/\/$/, "");
const dbUrl = `${normalizedSearchBase}/assets/search-guidelines.json`;

function createSearchDatabase() {
  return create({ schema: GUIDELINE_SEARCH_SCHEMA, language: "english" });
}

type GuidelineSearchDatabase = ReturnType<typeof createSearchDatabase>;

let databasePromise: Promise<GuidelineSearchDatabase> | undefined;

async function loadSearchDatabase() {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), INDEX_REQUEST_TIMEOUT_MS);

  try {
    const response = await fetch(dbUrl, { signal: controller.signal });
    if (!response.ok) throw new Error(`Search index request failed: ${response.status}`);

    const rawData: RawData = JSON.parse(await response.text());
    const db = createSearchDatabase();
    load(db, rawData);
    return db;
  } finally {
    clearTimeout(timeout);
  }
}

function getSearchDatabase() {
  databasePromise ??= loadSearchDatabase();
  return databasePromise;
}

function resetSearchDatabase() {
  databasePromise = undefined;
}

async function searchGuidelines(db: GuidelineSearchDatabase, term: string) {
  return search<GuidelineSearchDatabase, GuidelineSearchDocument>(db, {
    term,
    limit: RESULT_LIMIT,
    properties: [...GUIDELINE_SEARCH_PROPERTIES],
    boost: GUIDELINE_SEARCH_BOOST,
  });
}

type GuidelineSearchHit = Awaited<ReturnType<typeof searchGuidelines>>["hits"][number];

function normalizeHits(hits: readonly GuidelineSearchHit[]): SearchResult[] {
  return hits.map((hit) => ({
    id: hit.id,
    score: hit.score,
    document: hit.document,
  }));
}

type GuidelineSearchState = {
  open: boolean;
  query: string;
  indexStatus: IndexStatus;
  searchStatus: SearchStatus;
  results: SearchResult[];
  activeResultId: string | null;
};

type GuidelineSearchStore = GuidelineSearchState & {
  openSearch: () => void;
  closeSearch: () => void;
  retrySearch: () => void;
  setQuery: (query: string) => void;
  setActiveResultId: (id: string | null) => void;
  markIndexLoading: () => void;
  markIndexReady: () => void;
  markIndexFailed: () => void;
  markSearchStarted: () => void;
  markSearchReady: (results: SearchResult[]) => void;
  markSearchFailed: () => void;
};

const initialSearchState: GuidelineSearchState = {
  open: false,
  query: "",
  indexStatus: "idle",
  searchStatus: "idle",
  results: [],
  activeResultId: null,
};

const useGuidelineSearchStore = createZustandStore<GuidelineSearchStore>((set) => ({
  ...initialSearchState,
  openSearch: () =>
    set((state) => ({
      open: true,
      indexStatus: state.indexStatus === "failed" ? "idle" : state.indexStatus,
    })),
  closeSearch: () => set({ open: false }),
  retrySearch: () => {
    resetSearchDatabase();
    set((state) => ({
      indexStatus: "idle",
      searchStatus: state.query.trim() ? "searching" : "idle",
      results: [],
      activeResultId: null,
    }));
  },
  setQuery: (query) =>
    set((state) => {
      const trimmedQuery = query.trim();
      return {
        query,
        searchStatus: trimmedQuery ? "searching" : "idle",
        results: trimmedQuery ? state.results : [],
        activeResultId: trimmedQuery ? state.activeResultId : null,
      };
    }),
  setActiveResultId: (id) => set({ activeResultId: id }),
  markIndexLoading: () => set({ indexStatus: "loading" }),
  markIndexReady: () => set({ indexStatus: "ready" }),
  markIndexFailed: () =>
    set({
      indexStatus: "failed",
      searchStatus: "idle",
      results: [],
      activeResultId: null,
    }),
  markSearchStarted: () =>
    set((state) => ({
      indexStatus: state.indexStatus === "ready" ? "ready" : "loading",
      searchStatus: "searching",
    })),
  markSearchReady: (results) =>
    set({
      indexStatus: "ready",
      searchStatus: results.length === 0 ? "empty" : "ready",
      results,
      activeResultId: results[0]?.id ?? null,
    }),
  markSearchFailed: () =>
    set({
      indexStatus: "failed",
      searchStatus: "idle",
      results: [],
      activeResultId: null,
    }),
}));

export function useGuidelineSearch() {
  const { activeResultId, indexStatus, open, query, results, searchStatus } =
    useGuidelineSearchStore(
      useShallow((state) => ({
        activeResultId: state.activeResultId,
        indexStatus: state.indexStatus,
        open: state.open,
        query: state.query,
        results: state.results,
        searchStatus: state.searchStatus,
      })),
    );
  const {
    closeSearch,
    markIndexFailed,
    markIndexLoading,
    markIndexReady,
    markSearchFailed,
    markSearchReady,
    markSearchStarted,
    openSearch,
    retrySearch,
    setActiveResultId,
    setQuery,
  } = useGuidelineSearchStore(
    useShallow((state) => ({
      closeSearch: state.closeSearch,
      markIndexFailed: state.markIndexFailed,
      markIndexLoading: state.markIndexLoading,
      markIndexReady: state.markIndexReady,
      markSearchFailed: state.markSearchFailed,
      markSearchReady: state.markSearchReady,
      markSearchStarted: state.markSearchStarted,
      openSearch: state.openSearch,
      retrySearch: state.retrySearch,
      setActiveResultId: state.setActiveResultId,
      setQuery: state.setQuery,
    })),
  );
  const trimmedQuery = query.trim();

  const activeResult = useMemo(
    () => results.find((result) => result.id === activeResultId) ?? results[0] ?? null,
    [activeResultId, results],
  );

  useEffect(() => {
    if (indexStatus !== "idle") return;

    markIndexLoading();

    getSearchDatabase()
      .then(() => {
        startTransition(markIndexReady);
      })
      .catch(() => {
        resetSearchDatabase();
        startTransition(markIndexFailed);
      });
  }, [indexStatus, markIndexFailed, markIndexLoading, markIndexReady]);

  useEffect(() => {
    if (!open || trimmedQuery.length === 0) return;

    let cancelled = false;
    markSearchStarted();

    getSearchDatabase()
      .then((db) => searchGuidelines(db, trimmedQuery))
      .then((searchResults) => {
        if (cancelled) return;

        const nextResults = normalizeHits(searchResults.hits);
        startTransition(() => {
          markSearchReady(nextResults);
        });
      })
      .catch(() => {
        resetSearchDatabase();
        if (!cancelled) {
          startTransition(() => {
            markSearchFailed();
          });
        }
      });

    return () => {
      cancelled = true;
    };
  }, [markSearchFailed, markSearchReady, markSearchStarted, open, trimmedQuery]);

  return {
    activeResult,
    activeResultId,
    closeSearch,
    indexStatus,
    open,
    openSearch,
    query,
    results,
    retrySearch,
    searchStatus,
    setActiveResultId,
    setQuery,
    trimmedQuery,
  };
}
