import { describe, expect, it } from "vitest";

import { Catalog, CatalogError, type Guideline } from "@chartcoach/catalog";

const guidelines: Guideline[] = [
  {
    id: "axis-bars",
    title: "Use full axes",
    description: "Start bar axes at zero.",
    labels: ["chart:bar", "task:compare"],
    body: "## Advice <!-- role: advice -->\nStart at zero.",
    sections: [{ role: "advice", title: "Advice", content: "Start at zero." }],
    references: [],
  },
  {
    id: "line-labels",
    title: "Label lines directly",
    description: "Place labels near the lines.",
    labels: ["chart:line", "task:compare"],
    body: "## Reason <!-- role: reason -->\nLegends add lookup work.",
    sections: [{ role: "reason", title: "Reason", content: "Legends add lookup work." }],
    references: ["@article{labels,title={Labels}}"],
  },
];

describe("Catalog", () => {
  it("indexes and summarizes loaded guidelines", () => {
    const catalog = new Catalog(guidelines);

    expect(catalog.length).toBe(2);
    expect(catalog.size).toBe(2);
    expect(catalog.get("axis-bars")?.title).toBe("Use full axes");
    expect(catalog.require("line-labels").references).toEqual(["@article{labels,title={Labels}}"]);
    expect([...catalog].map((guideline) => guideline.id)).toEqual(["axis-bars", "line-labels"]);
    expect(catalog.labels()).toEqual(["chart:bar", "chart:line", "task:compare"]);
    expect(catalog.sectionRoles()).toEqual(["advice", "reason"]);
  });

  it("rejects duplicate guideline ids", () => {
    expect(() => new Catalog([guidelines[0]!, guidelines[0]!])).toThrow(CatalogError);
  });
});
