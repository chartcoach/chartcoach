import { describe, expect, it } from "vite-plus/test";

import { Catalog, CatalogError, type Guideline } from "@chartcoach/catalog";
import invalidRowsFixture from "../../../fixtures/catalog-contract/invalid-catalog-rows.json";
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
  it("indexes compiled guidelines and derives markdown bodies", async () => {
    const catalog = new Catalog(guidelines, manifest);
    const description = await catalog.describe();

    expect(catalog.length).toBe(2);
    expect(catalog.get("axis-bars")?.body).toBe(
      "## Advice <!-- role: advice -->\n\nStart at zero.",
    );
    expect(catalog.require("line-labels").references).toEqual(["@article{labels,title={Labels}}"]);
    expect([...catalog].map((guideline) => guideline.id)).toEqual(["axis-bars", "line-labels"]);
    expect(catalog.labels()).toEqual(["chart:bar", "chart:line", "task:compare"]);
    expect(catalog.sectionRoles()).toEqual(["advice", "reason"]);
    expect(description).toEqual({
      resolved_location: null,
      release_digest: null,
      entries_digest: expect.stringMatching(/^[a-f0-9]{64}$/),
      manifest_digest: expect.stringMatching(/^[a-f0-9]{64}$/),
      section_roles: [
        { name: "advice", description: "Actionable guidance.", examples: [] },
        { name: "reason", description: "Supporting rationale.", examples: [] },
      ],
      label_families: [
        {
          name: "chart",
          description: "Chart labels such as `chart:bar`.",
          examples: ["chart:bar"],
        },
        {
          name: "task",
          description: "Task labels such as `task:compare`.",
          examples: ["task:compare"],
        },
      ],
      profiles: [],
      profile: null,
    });
  });

  it("rejects duplicate guideline entry IDs", () => {
    expect(() => new Catalog([guidelines[0]!, guidelines[0]!], manifest)).toThrow(CatalogError);
  });

  it("owns immutable guideline and manifest values", () => {
    const input = {
      ...guidelines[0]!,
      labels: [...guidelines[0]!.labels],
      sections: guidelines[0]!.sections.map((section) => ({ ...section })),
      references: [...guidelines[0]!.references],
    };
    const mutableManifest = {
      markdown: manifest.markdown,
      sectionRoles: { ...manifest.sectionRoles },
      labelFamilies: { ...manifest.labelFamilies },
    };
    const catalog = new Catalog([input], mutableManifest);
    const record = catalog.require("axis-bars");

    input.id = "changed";
    input.sections[0]!.content = "Changed content.";
    delete mutableManifest.sectionRoles.advice;

    expect(catalog.require("axis-bars").body).toBe(
      "## Advice <!-- role: advice -->\n\nStart at zero.",
    );
    expect(catalog.get("changed")).toBeUndefined();
    expect(catalog.manifest.sectionRoles.advice?.name).toBe("advice");
    expect(Object.getPrototypeOf(catalog.manifest.sectionRoles)).toBeNull();
    expect(Object.isFrozen(catalog.guidelines)).toBe(true);
    expect(Object.isFrozen(record)).toBe(true);
    expect(Object.isFrozen(record.labels)).toBe(true);
    expect(Object.isFrozen(record.sections)).toBe(true);
    expect(Object.isFrozen(record.sections[0])).toBe(true);
    expect(Object.isFrozen(catalog.manifest.sectionRoles.advice)).toBe(true);
  });

  it("applies wire semantics to direct construction", () => {
    for (const testCase of invalidRowsFixture.cases) {
      const record = { ...invalidRowsFixture.row, ...testCase.patch };
      expect(() => Reflect.construct(Catalog, [[record], manifest]), testCase.name).toThrow(
        "Invalid guideline record",
      );
    }
  });

  it.each([
    {
      name: "inherited section role",
      guideline: {
        ...guidelines[0]!,
        sections: [{ role: "constructor", title: "Constructor", content: "Content." }],
      },
      error: "undefined section role(s): constructor",
    },
    {
      name: "inherited label family",
      guideline: { ...guidelines[0]!, labels: ["constructor:value"] },
      error: "undefined label family/families: constructor",
    },
  ])("rejects $name", ({ guideline, error }) => {
    expect(() => new Catalog([guideline], manifest)).toThrow(error);
  });
});
