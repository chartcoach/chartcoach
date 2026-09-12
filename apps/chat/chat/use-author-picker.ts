import { useMemo, useRef, useState } from "react";
import type { VListHandle } from "virtua";
import type { CatalogFilters, CatalogMetadata } from "../shared/catalog-filters";

const authorOrder = new Intl.Collator(undefined, { sensitivity: "base", ignorePunctuation: true });

export function useAuthorPicker(
  metadata: CatalogMetadata,
  draft: CatalogFilters,
  counts: { id: number; count: number }[] | undefined,
  onChange: (filters: CatalogFilters) => void,
) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [selectedOnly, setSelectedOnly] = useState(false);
  const [focused, setFocused] = useState<number>();
  const list = useRef<VListHandle>(null);
  const search = useRef<HTMLInputElement>(null);

  const authors = useMemo(() => {
    const lookup = new Map(counts?.map(({ id, count }) => [id, count]));
    const included = new Set(draft.includeAuthorIds);
    const excluded = new Set(draft.excludeAuthorIds);

    return metadata.authors
      .map((author) => ({
        ...author,
        count: lookup.get(author.id) ?? 0,
        choice: excluded.has(author.id) ? "exclude" : included.has(author.id) ? "include" : "any",
      }))
      .toSorted((a, b) => b.count - a.count || authorOrder.compare(a.name, b.name) || a.id - b.id);
  }, [metadata.authors, counts, draft.includeAuthorIds, draft.excludeAuthorIds]);

  const available = authors.filter((author) => author.count > 0);
  const selected = authors.filter((author) => author.choice !== "any");
  const term = query.trim().toLocaleLowerCase();

  const rows = authors.filter(
    (author) =>
      (selectedOnly ? author.choice !== "any" : author.count > 0 || author.choice !== "any") &&
      author.name.toLocaleLowerCase().includes(term),
  );

  const focusIndex = rows.findIndex((author) => author.id === focused);

  return {
    open,
    setOpen: (value: boolean) => {
      setOpen(value);

      if (value) {
        setQuery("");
        setSelectedOnly(false);
      }
    },
    query,
    setQuery: (value: string) => {
      setQuery(value);
      list.current?.scrollTo(0);
    },
    selectedOnly,
    toggleSelected: () => {
      setSelectedOnly((value) => !value);
      list.current?.scrollTo(0);
    },
    available: available.length,
    maxCount: authors[0]?.count ?? 0,
    selected: selected.length,
    rows,
    list,
    search,
    keepMounted: focusIndex < 0 ? undefined : [focusIndex],
    focus: setFocused,
    blur: () => setFocused(undefined),
    choose: (id: number, choice: string) => {
      onChange({
        ...draft,
        includeAuthorIds: [
          ...draft.includeAuthorIds.filter((value) => value !== id),
          ...(choice === "include" ? [id] : []),
        ],
        excludeAuthorIds: [
          ...draft.excludeAuthorIds.filter((value) => value !== id),
          ...(choice === "exclude" ? [id] : []),
        ],
      });

      if (choice === "any" && (selectedOnly || !available.some((author) => author.id === id))) {
        search.current?.focus();
      }
    },
  };
}
