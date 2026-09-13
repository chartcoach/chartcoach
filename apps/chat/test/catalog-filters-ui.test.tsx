// @vitest-environment jsdom
import { expect, it } from "vite-plus/test";
import { GuidelinesPage } from "../components/catalog/filters";
import { SourceFilters, YearFilters } from "../components/catalog/facets";
import { AuthorFilters } from "../components/catalog/author-filters";
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

it("summarizes eligible authors and retains selection counts", () => {
  const page = renderDocument(
    <AuthorFilters
      metadata={metadata}
      draft={{ ...emptyCatalogFilters(metadata.catalogId), excludeAuthorIds: [1] }}
      counts={[]}
      onChange={() => {}}
    />,
  );

  expect(page.querySelector("button")?.textContent).toBe("Browse authors0");
  expect(page.querySelector('[role="status"]')?.textContent).toBe("0 included · 1 excluded");
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
