// @vitest-environment jsdom
import { act, useLayoutEffect } from "react";
import { createRoot } from "react-dom/client";
import { expect, it, vi } from "vite-plus/test";
import { useAuthorPicker } from "../chat/use-author-picker";
import { emptyCatalogFilters, type CatalogMetadata } from "../shared/catalog-filters";

it("ranks the linked author pool by count while keeping out-of-scope selections editable", async () => {
  const metadata: CatalogMetadata = {
    catalogId: "a".repeat(64),
    totalGuidelines: 8,
    authors: [
      { id: 3, name: "Cy", guidelineCount: 5 },
      { id: 2, name: "Bea", guidelineCount: 2 },
      { id: 1, name: "Ada", guidelineCount: 1 },
    ],
    sourceTypes: [],
    years: { min: 2000, max: 2025, undatedGuidelines: 0 },
    tables: [],
  };

  const initial = emptyCatalogFilters(metadata.catalogId);
  const onChange = vi.fn();
  let picker: ReturnType<typeof useAuthorPicker> | undefined;

  function Probe({
    draft = initial,
    counts,
  }: {
    draft?: typeof initial;
    counts?: { id: number; count: number }[];
  }) {
    const current = useAuthorPicker(metadata, draft, counts, onChange);
    useLayoutEffect(() => {
      picker = current;
    });

    return null;
  }

  vi.stubGlobal("IS_REACT_ACT_ENVIRONMENT", true);
  const container = document.createElement("div");
  const root = createRoot(container);

  try {
    await act(async () => root.render(<Probe />));
    expect(picker!.available).toBe(0);
    expect(picker!.rows).toEqual([]);

    await act(async () =>
      root.render(
        <Probe
          counts={[
            { id: 3, count: 5 },
            { id: 1, count: 1 },
          ]}
        />,
      ),
    );
    expect(picker!.rows.map(({ name }) => name)).toEqual(["Cy", "Ada"]);
    expect(picker!.available).toBe(2);
    expect(picker!.maxCount).toBe(5);
    await act(async () => picker!.setQuery("Ada"));
    expect(picker!.rows.map(({ name }) => name)).toEqual(["Ada"]);
    expect(picker!.maxCount).toBe(5);
    await act(async () => picker!.setQuery(""));
    await act(async () =>
      root.render(
        <Probe
          counts={[
            { id: 3, count: 1 },
            { id: 2, count: 1 },
            { id: 1, count: 1 },
          ]}
        />,
      ),
    );
    expect(picker!.rows.map(({ name }) => name)).toEqual(["Ada", "Bea", "Cy"]);
    await act(async () => picker!.choose(3, "exclude"));
    const excluded = { ...initial, excludeAuthorIds: [3] };
    expect(onChange).toHaveBeenLastCalledWith(excluded);

    await act(async () => root.render(<Probe draft={excluded} counts={[{ id: 1, count: 1 }]} />));
    expect(picker!.available).toBe(1);
    expect(picker!.selected).toBe(1);
    expect(picker!.rows.map(({ name, count, choice }) => ({ name, count, choice }))).toEqual([
      { name: "Ada", count: 1, choice: "any" },
      { name: "Cy", count: 0, choice: "exclude" },
    ]);
    await act(async () => picker!.setQuery(" cY "));
    expect(picker!.rows.map(({ name }) => name)).toEqual(["Cy"]);
    await act(async () => {
      picker!.setQuery("");
      picker!.toggleSelected();
    });
    expect(picker!.rows.map(({ name }) => name)).toEqual(["Cy"]);
    await act(async () => picker!.choose(3, "include"));
    expect(onChange).toHaveBeenLastCalledWith({ ...initial, includeAuthorIds: [3] });
    await act(async () => picker!.choose(3, "any"));
    expect(onChange).toHaveBeenLastCalledWith(initial);
    await act(async () => root.render(<Probe counts={[]} />));
    expect(picker!.rows).toEqual([]);
  } finally {
    await act(async () => root.unmount());
    vi.unstubAllGlobals();
  }
});
