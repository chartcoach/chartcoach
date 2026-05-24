import { describe, expect, it } from "vitest";

import {
  catalogEntryFromWire,
  isCatalogEntryWire,
  requireCatalogEntryFromWire,
} from "@chartcoach/catalog";

describe("catalog wire validation", () => {
  it("converts valid wire entries and computes sections", () => {
    const wire = {
      id: "g1",
      guideline: {
        id: "g1",
        title: "T",
        description: "D",
        labels: ["topic:x"],
        body: "## Advice <!-- role: advice -->\nDo it.\n",
        sections: [{ role: "advice", title: "Advice", content: "Do it." }],
        bibliography: null,
      },
      references: ["@article{a,title={A}}"],
    };

    expect(isCatalogEntryWire(wire)).toBe(true);

    const entry = requireCatalogEntryFromWire(wire);
    expect(entry.guideline.id).toBe("g1");
    expect(entry.guideline.sections).toEqual([{ role: "advice", title: "Advice", content: "Do it." }]);
    expect(entry.guideline.sectionsIndex.byRole.advice?.length).toBe(1);
    expect(entry.references).toEqual(["@article{a,title={A}}"]);
  });

  it("returns null for invalid wire entries", () => {
    expect(catalogEntryFromWire(null)).toBeNull();
    expect(catalogEntryFromWire({})).toBeNull();
    expect(catalogEntryFromWire({ id: "g1", guideline: {} })).toBeNull();
    expect(
      catalogEntryFromWire({
        id: "g1",
        guideline: {
          id: "g1",
          title: "T",
          description: "D",
          labels: ["topic:x", 1],
          body: "Body",
          sections: [{ role: "advice", title: "Advice", content: "Do it." }],
        },
        references: [],
      }),
    ).toBeNull();
    expect(
      catalogEntryFromWire({
        id: "g1",
        guideline: {
          id: "g1",
          description: "D",
          labels: [],
          body: "Body",
          sections: [],
        },
        references: [],
      }),
    ).toBeNull();
  });

  it("throws with helpful context for invalid wire entries", () => {
    expect(() => requireCatalogEntryFromWire({ id: "g1", guideline: {} }, "bundle")).toThrow(
      /bundle/,
    );
  });
});
