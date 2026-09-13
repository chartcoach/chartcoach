import { describe, expect, expectTypeOf, it } from "vite-plus/test";
import { Catalog, type CatalogTables } from "@chartcoach/catalog";
import operations from "../../../fixtures/catalog-contract/operations.json";
import { fixtureCatalog } from "./catalog-testkit";

describe("catalog tables", () => {
  it("projects guideline records, sections, and parsed labels", async () => {
    const fixture = await fixtureCatalog();

    const catalog = new Catalog(
      [
        {
          id: "chart",
          title: "A chart",
          description: "Chart guidance.",
          labels: ["chart:line:dashed", "chart:line", "chart:line"],
          sections: [
            { role: "__dangling__", title: "", content: "Intro." },
            { role: "advice", title: "Advice", content: "Use readable labels." },
          ],
          references: [],
        },
      ],
      fixture.manifest,
    );

    expect(catalog.table("guidelines")).toEqual([
      {
        id: "chart",
        title: "A chart",
        description: "Chart guidance.",
        labels: ["chart:line:dashed", "chart:line", "chart:line"],
        body: "Intro.\n\n## Advice <!-- role: advice -->\n\nUse readable labels.",
        sections: [
          { role: "__dangling__", title: "", content: "Intro." },
          { role: "advice", title: "Advice", content: "Use readable labels." },
        ],
      },
    ]);
    expect(catalog.table("sections")).toEqual([
      { guideline_id: "chart", role: "__dangling__", title: "", content: "Intro." },
      { guideline_id: "chart", role: "advice", title: "Advice", content: "Use readable labels." },
    ]);
    expect(catalog.table("guideline_labels")).toEqual([
      {
        guideline_id: "chart",
        label: "chart:line",
        family: "chart",
        category: "line",
        modifier: null,
      },
      {
        guideline_id: "chart",
        label: "chart:line:dashed",
        family: "chart",
        category: "line",
        modifier: "dashed",
      },
    ]);
  });

  it("deduplicates source definitions and edges with deterministic authored BibTeX", async () => {
    const fixture = await fixtureCatalog();

    const records = ["second", "first"].map((id, index) => ({
      ...fixture.guidelines[0]!,
      id,
      references: [
        operations.bibliography.equivalent[index]!,
        operations.bibliography.equivalent[index]!,
      ],
    }));

    const catalog = new Catalog(records, fixture.manifest);
    const references = catalog.table("references");

    expect(references).toEqual([
      {
        id: "shared2024",
        source_type: "article",
        authors: ["Smith, Ada"],
        authors_text: "Smith, Ada",
        year: "2024",
        title: "Readable charts",
        journal: "Journal of Charts",
        booktitle: null,
        publisher: null,
        url: null,
        doi: null,
        bibtex: operations.bibliography.equivalent[1],
      },
    ]);
    expect(catalog.table("guideline_references")).toEqual([
      { guideline_id: "first", reference_id: "shared2024" },
      { guideline_id: "second", reference_id: "shared2024" },
    ]);
    expect(catalog.table("guideline_sources")).toEqual(
      ["first", "second"].map((guideline_id) => ({
        guideline_id,
        reference_id: "shared2024",
        source_type: "article",
        authors: ["Smith, Ada"],
        authors_text: "Smith, Ada",
        year: "2024",
        source_title: "Readable charts",
        journal: "Journal of Charts",
        booktitle: null,
        publisher: null,
        url: null,
        doi: null,
        bibtex: operations.bibliography.equivalent[1],
      })),
    );
    const reversed = new Catalog([...records].reverse(), fixture.manifest);
    expect(reversed.table("references")).toEqual(references);
    expect(catalog.cite({ ids: ["first"] })[0]?.sources[0]?.reference_id).toBe("shared2024");
  });

  it("keeps nested table values and metadata immutable across consumers", async () => {
    const catalog = await fixtureCatalog();
    const guidelines = catalog.table("guidelines");
    const references = catalog.table("references");
    const info = await catalog.describe();

    expectTypeOf(guidelines).toEqualTypeOf<CatalogTables["guidelines"]>();
    expectTypeOf(references).toEqualTypeOf<CatalogTables["references"]>();
    expect(Reflect.set(guidelines[0]!, "title", "Changed")).toBe(false);
    expect(Reflect.set(guidelines[0]!.sections[0]!, "content", "Changed")).toBe(false);
    expect(Reflect.set(guidelines[0]!.labels, "0", "Changed")).toBe(false);
    expect(Reflect.set(references[0]!.authors, "0", "Changed")).toBe(false);
    expect(Reflect.set(guidelines, "0", null)).toBe(false);
    expect(Reflect.set(info.tables, "0", null)).toBe(false);
    expect(Reflect.set(info.tables[0]!.columns[0]!, "type", "Changed")).toBe(false);
    expect(catalog.read({ ids: [guidelines[0]!.id] })[0]?.title).toBe(guidelines[0]?.title);
  });

  it("describes typed empty tables and reports unknown table names", async () => {
    const fixture = await fixtureCatalog();
    const catalog = new Catalog([], fixture.manifest);
    const info = await catalog.describe();
    expect(info.tables.map(({ name, rows }) => ({ name, rows }))).toEqual([
      { name: "guidelines", rows: 0 },
      { name: "sections", rows: 0 },
      { name: "guideline_labels", rows: 0 },
      { name: "references", rows: 0 },
      { name: "guideline_references", rows: 0 },
      { name: "guideline_sources", rows: 0 },
    ]);

    for (const table of info.tables) expect(catalog.table(table.name)).toEqual([]);
    expect(info.tables[0]?.columns).toEqual([
      { name: "id", type: "String" },
      { name: "title", type: "String" },
      { name: "description", type: "String" },
      { name: "labels", type: "List(String)" },
      { name: "body", type: "String" },
      {
        name: "sections",
        type: "List(Struct({'role': String, 'title': String, 'content': String}))",
      },
    ]);

    for (const name of ["missing", "constructor"]) {
      // @ts-expect-error Plain JavaScript callers can supply unknown table names.
      expect(() => catalog.table(name)).toThrow(
        expect.objectContaining({
          name: "CatalogError",
          code: "lookup",
          message: `Unknown table: ${name}`,
          details: expect.objectContaining({ table: name }),
          hints: ["Call catalog.describe() to inspect catalog tables."],
        }),
      );
    }
  });
});
