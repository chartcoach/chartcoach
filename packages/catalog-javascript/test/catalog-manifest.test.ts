import { describe, expect, it } from "vitest";

import {
  Catalog,
  CatalogError,
  parseManifest,
  type Guideline,
} from "@chartcoach/catalog";

const manifestMarkdown = `# Sample Catalog

## Section Roles

### advice

Actionable guidance.

## Label Families

### chart

Chart-family labels such as \`chart:bar\`.
`;

describe("catalog manifest", () => {
  it("parses required headings and subheadings", () => {
    const manifest = parseManifest(manifestMarkdown);

    expect(manifest.sectionRoles.advice?.description).toContain("Actionable");
    expect(manifest.labelFamilies.chart?.examples).toContain("chart:bar");
  });

  it("rejects catalog entries with undefined manifest vocabulary", () => {
    const manifest = parseManifest(manifestMarkdown);
    const guidelines: Guideline[] = [
      {
        id: "g1",
        title: "Title",
        description: "Description",
        labels: ["task:compare"],
        body: "Body",
        sections: [{ role: "reason", title: "Reason", content: "Because." }],
        references: [],
      },
    ];

    let error: unknown;
    try {
      new Catalog(guidelines, { manifest });
    } catch (caught) {
      error = caught;
    }

    expect(error).toBeInstanceOf(CatalogError);
    expect(error instanceof Error ? error.message : String(error)).toContain(
      "undefined section role",
    );
    expect(error instanceof Error ? error.message : String(error)).toContain(
      "undefined label family",
    );
  });
});
