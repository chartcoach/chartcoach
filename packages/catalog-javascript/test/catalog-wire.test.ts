import { describe, expect, it } from "vitest";

import {
  catalogEntryFromWire,
  isCatalogEntryWire,
  requireCatalogEntryFromWire,
} from "@chartcoach/catalog";

describe("catalog wire helpers", () => {
  it("converts valid wire entries and computes sections", () => {
    const wire = {
      id: "g1",
      guideline: {
        title: "T",
        description: "D",
        labels: ["topic:x"],
        body: "## Advice <!-- role: advice -->\nDo it.\n",
        bibliography: null,
      },
      references: ["@article{a,title={A}}"],
    };

    expect(isCatalogEntryWire(wire)).toBe(true);

    const entry = requireCatalogEntryFromWire(wire);
    expect(entry.guideline.id).toBe("g1");
    expect(entry.guideline.sections.length).toBeGreaterThan(0);
    expect(entry.guideline.sectionsIndex.byRole.advice?.length).toBeGreaterThan(0);
    expect(entry.references).toEqual(["@article{a,title={A}}"]);
  });

  it("returns null for invalid wire entries", () => {
    expect(catalogEntryFromWire(null)).toBeNull();
    expect(catalogEntryFromWire({})).toBeNull();
    expect(catalogEntryFromWire({ id: "g1", guideline: {} })).toBeNull();
  });

  it("throws with helpful context for invalid wire entries", () => {
    expect(() => requireCatalogEntryFromWire({ id: "g1", guideline: {} }, "bundle")).toThrow(
      /bundle/,
    );
  });
});
