import { renderToStaticMarkup } from "react-dom/server";
import { expect, it } from "vite-plus/test";
import { CatalogFiltersPanel } from "../components/catalog/filters";
import { AuthorFilters, SourceFilters, YearFilters } from "../components/catalog/facets";
import { emptyCatalogFilters, type CatalogMetadata } from "../shared/catalog-filters";

const metadata: CatalogMetadata = {
  catalogId: "a".repeat(64),
  totalGuidelines: 24,
  authors: [{ id: 1, name: "Example Author", guidelineCount: 8 }],
  sourceTypes: [{ id: 1, name: "article", guidelineCount: 12 }],
  years: { min: 1990, max: 2024, undatedGuidelines: 3 },
  tables: [],
};

it("shows the selected guideline count in the knowledge control", () => {
  const html = renderToStaticMarkup(
    <CatalogFiltersPanel
      metadata={metadata}
      value={{ ...emptyCatalogFilters(metadata.catalogId), includeAuthorIds: [1], yearFrom: 2000 }}
      matchedGuidelines={3}
      disabled={false}
      onApply={async () => {}}
      onReload={async () => {}}
    />,
  );
  expect(html).toContain('aria-label="Knowledge, 3 guidelines selected"');
  expect(html).toContain('aria-haspopup="dialog"');
  expect(html).toContain('aria-expanded="false"');
});

it("prevents changing knowledge while a review is running", () => {
  const html = renderToStaticMarkup(
    <CatalogFiltersPanel
      metadata={metadata}
      value={emptyCatalogFilters(metadata.catalogId)}
      matchedGuidelines={24}
      disabled
      onApply={async () => {}}
      onReload={async () => {}}
    />,
  );
  expect(html).toMatch(/<button[^>]*disabled=""/);
});

it("renders linked source counts and preserves a zero-match selected type", () => {
  const html = renderToStaticMarkup(
    <SourceFilters
      metadata={metadata}
      draft={{ ...emptyCatalogFilters(metadata.catalogId), sourceTypeIds: [1] }}
      counts={[]}
      onChange={() => {}}
    />,
  );
  expect(html).toContain('aria-label="Source type article"');
  expect(html).toContain('checked=""');
  expect(html).toMatch(/>0<\/span>/);
});

it("shows author exclusions alongside the linked guideline count", () => {
  const html = renderToStaticMarkup(
    <AuthorFilters
      metadata={metadata}
      draft={{ ...emptyCatalogFilters(metadata.catalogId), excludeAuthorIds: [1] }}
      counts={[{ id: 1, count: 3 }]}
      onChange={() => {}}
    />,
  );
  expect(html).toContain('aria-label="Filter author Example Author"');
  expect(html).toContain('<option value="exclude" selected="">Exclude</option>');
  expect(html).toMatch(/>3<\/span>/);
});

it("keeps author controls in place as linked counts and selections change", () => {
  const authors = [
    { id: 1, name: "Ada", guidelineCount: 12 },
    { id: 2, name: "Bea", guidelineCount: 8 },
    { id: 3, name: "Cy", guidelineCount: 7 },
    { id: 4, name: "Dee", guidelineCount: 6 },
    { id: 5, name: "Eli", guidelineCount: 4 },
  ];
  for (const draft of [
    emptyCatalogFilters(metadata.catalogId),
    { ...emptyCatalogFilters(metadata.catalogId), includeAuthorIds: [2] },
  ]) {
    const html = renderToStaticMarkup(
      <AuthorFilters
        metadata={{ ...metadata, authors }}
        draft={draft}
        counts={[
          { id: 5, count: 4 },
          { id: 2, count: 3 },
        ]}
        onChange={() => {}}
      />,
    );
    expect(
      [...html.matchAll(/aria-label="Filter author ([^"]+)"/g)].map((match) => match[1]),
    ).toEqual(["Ada", "Bea", "Cy", "Dee"]);
  }
});

it("exposes the catalog year range through keyboard sliders and exact numeric inputs", () => {
  const html = renderToStaticMarkup(
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
  expect(html).toContain('aria-label="Earliest publication year"');
  expect(html).toContain('aria-label="Latest publication year"');
  expect(html).toContain('min="1990" max="2024" placeholder="1990" value="2001"');
  expect(html).toContain('min="1990" max="2024" placeholder="2024" value="2018"');
});
