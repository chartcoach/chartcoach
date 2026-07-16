import { describe, expect, it } from "vite-plus/test";

import { Catalog, CatalogError, type Guideline } from "@chartcoach/catalog";
import { parseCatalogManifest } from "../src/catalog/manifest";

const guidelines: Array<Omit<Guideline, "body">> = [
  {
    id: "axis-bars",
    title: "Use full axes",
    description: "Start bar axes at zero.",
    labels: ["chart:bar", "task:compare"],
    sections: [{ role: "advice", title: "Advice", content: "Start at zero." }],
    references: [],
  },
  {
    id: "line-labels",
    title: "Label lines directly",
    description: "Place labels near the lines.",
    labels: ["chart:line", "task:compare"],
    sections: [{ role: "reason", title: "Reason", content: "Legends add lookup work." }],
    references: ["@article{labels,title={Labels}}"],
  },
];

const manifest = parseCatalogManifest(`# Catalog

## Section Roles

### advice

Actionable guidance.

### reason

Supporting rationale.

## Label Families

### chart

Chart labels such as \`chart:bar\`.

### task

Task labels such as \`task:compare\`.
`);

describe("Catalog", () => {
  it("indexes compiled guidelines and derives markdown bodies", () => {
    const catalog = new Catalog(guidelines, manifest);

    expect(catalog.length).toBe(2);
    expect(catalog.get("axis-bars")?.body).toBe(
      "## Advice <!-- role: advice -->\n\nStart at zero.",
    );
    expect(catalog.require("line-labels").references).toEqual(["@article{labels,title={Labels}}"]);
    expect([...catalog].map((guideline) => guideline.id)).toEqual(["axis-bars", "line-labels"]);
    expect(catalog.labels()).toEqual(["chart:bar", "chart:line", "task:compare"]);
    expect(catalog.sectionRoles()).toEqual(["advice", "reason"]);
  });

  it("rejects duplicate guideline ids", () => {
    expect(() => new Catalog([guidelines[0]!, guidelines[0]!], manifest)).toThrow(CatalogError);
  });
});
