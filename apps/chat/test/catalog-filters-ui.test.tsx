// @vitest-environment jsdom
import { act } from "react";
import { createRoot } from "react-dom/client";
import { expect, it, vi } from "vite-plus/test";
import { GuidelinesPage } from "../components/catalog/filters";
import { AuthorFilters, SourceFilters, YearFilters } from "../components/catalog/facets";
import { emptyCatalogFilters, type CatalogMetadata } from "../shared/catalog-filters";
import { renderDocument } from "./render-document";

const metadata: CatalogMetadata = {
  catalogId: "a".repeat(64),
  totalGuidelines: 24,
  authors: [{ id: 1, name: "Example Author", guidelineCount: 8 }],
  sourceTypes: [{ id: 1, name: "article", guidelineCount: 12 }],
  years: { min: 1990, max: 2024, undatedGuidelines: 3 },
  tables: [],
};

it("shows the guideline pool in the guidelines settings page", () => {
  const page = renderDocument(
    <GuidelinesPage
      open
      onClose={() => {}}
      metadata={metadata}
      value={{ ...emptyCatalogFilters(metadata.catalogId), includeAuthorIds: [1], yearFrom: 2000 }}
      matchedGuidelines={3}
      disabled={false}
      onApply={async () => {}}
      onReload={async () => {}}
    />,
  );

  expect(page.querySelector('main[aria-label="Guidelines settings"]')).not.toBeNull();
  expect(page.querySelector('main > footer [role="status"]')?.textContent).toBe(
    "3 guidelines selected",
  );
  expect(
    Array.from(page.querySelectorAll("button"), (button) => button.textContent?.trim()),
  ).toContain("Back to chat");
});

it("prevents changing guidelines while a review is running", () => {
  const page = renderDocument(
    <GuidelinesPage
      open
      onClose={() => {}}
      metadata={metadata}
      value={emptyCatalogFilters(metadata.catalogId)}
      matchedGuidelines={24}
      disabled
      onApply={async () => {}}
      onReload={async () => {}}
    />,
  );

  const controls = Array.from(page.querySelectorAll("input, select"));
  expect(controls.length).toBeGreaterThan(0);
  expect(controls.every((control) => control.matches(":disabled"))).toBe(true);
});

it("renders linked source counts and preserves a zero-match selected type", () => {
  const page = renderDocument(
    <SourceFilters
      metadata={metadata}
      draft={{ ...emptyCatalogFilters(metadata.catalogId), sourceTypeIds: [1] }}
      counts={[]}
      onChange={() => {}}
    />,
  );

  const source = page.querySelector<HTMLInputElement>('[aria-label="Source type article"]')!;
  expect(source.checked).toBe(true);
  expect(source.labels?.[0]?.textContent).toMatch(/^article\s*0$/);
});

it("preserves focused author controls as linked counts and selections change", async () => {
  const authors = [
    { id: 1, name: "Ada", guidelineCount: 12 },
    { id: 2, name: "Bea", guidelineCount: 8 },
    { id: 3, name: "Cy", guidelineCount: 7 },
    { id: 4, name: "Dee", guidelineCount: 6 },
    { id: 5, name: "Eli", guidelineCount: 4 },
  ];

  vi.stubGlobal("IS_REACT_ACT_ENVIRONMENT", true);
  const container = document.createElement("div");
  document.body.append(container);
  const root = createRoot(container);
  const onChange = vi.fn();
  const draft = { ...emptyCatalogFilters(metadata.catalogId), includeAuthorIds: [2] };

  try {
    await act(async () =>
      root.render(
        <AuthorFilters metadata={{ ...metadata, authors }} draft={draft} onChange={onChange} />,
      ),
    );
    const controls = Array.from(container.querySelectorAll("select"));
    expect(controls.map((control) => control.getAttribute("aria-label"))).toEqual([
      "Filter author Ada",
      "Filter author Bea",
      "Filter author Cy",
      "Filter author Dee",
    ]);
    const bea = controls[1]!;
    bea.focus();
    expect(bea.value).toBe("include");

    await act(async () => {
      bea.value = "exclude";
      bea.dispatchEvent(new Event("change", { bubbles: true }));
    });
    const excluded = { ...draft, includeAuthorIds: [], excludeAuthorIds: [2] };
    expect(onChange).toHaveBeenCalledExactlyOnceWith(excluded);

    await act(async () =>
      root.render(
        <AuthorFilters
          metadata={{ ...metadata, authors }}
          draft={excluded}
          counts={[
            { id: 5, count: 4 },
            { id: 2, count: 3 },
          ]}
          onChange={onChange}
        />,
      ),
    );
    const updated = Array.from(container.querySelectorAll("select"));
    updated.forEach((control, index) => expect(control).toBe(controls[index]));
    expect(updated).toHaveLength(4);
    expect(document.activeElement).toBe(bea);
    expect(bea.value).toBe("exclude");
    expect(bea.labels?.[0]?.textContent).toContain("Bea3");
  } finally {
    await act(async () => root.unmount());
    container.remove();
    vi.unstubAllGlobals();
  }
});

it("exposes the catalog year range through keyboard sliders and exact numeric inputs", () => {
  const page = renderDocument(
    <YearFilters
      metadata={metadata}
      draft={{ ...emptyCatalogFilters(metadata.catalogId), yearFrom: 2001, yearTo: 2018 }}
      bins={[
        { from: 1990, to: 1999, count: 4 },
        { from: 2000, to: 2024, count: 17 },
      ]}
      onChange={() => {}}
    />,
  );

  expect(
    Array.from(page.querySelectorAll('[role="slider"]'), (slider) =>
      slider.getAttribute("aria-label"),
    ),
  ).toEqual(["Earliest publication year", "Latest publication year"]);
  expect(
    Array.from(
      page.querySelectorAll<HTMLInputElement>('input[type="number"]'),
      ({ name, min, max, valueAsNumber }) => ({ name, min, max, value: valueAsNumber }),
    ),
  ).toEqual([
    { name: "yearFrom", min: "1990", max: "2024", value: 2001 },
    { name: "yearTo", min: "1990", max: "2024", value: 2018 },
  ]);
});
