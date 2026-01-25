import { describe, expect, it } from "vitest";

import { buildRetrievalRequestFromScenario, catalogEntriesFromWire } from "./wire";

describe("eval retrieval wire helpers", () => {
  it("builds a RetrievalRequestWire from a scenario", () => {
    const req = buildRetrievalRequestFromScenario({
      id: "s1",
      title: "T",
      lang: "en",
      chart: { uri: "https://example.invalid/chart.png", mime: "image/png" },
      query: "Q",
      designer_intent: "Intent",
    });

    expect(req.lang).toBe("en");
    expect(req.context.map((i) => i.kind)).toEqual(["image", "text", "text", "text"]);
    expect(req.context[1]?.role).toBe("situation");
  });

  it("maps retrieval response catalog rows to CatalogEntry", () => {
    const entries = catalogEntriesFromWire([
      {
        id: "g1",
        guideline: {
          id: "g1",
          title: "Title",
          description: "Desc",
          labels: ["a:b"],
          body: "Hello",
        },
        references: ["@misc{a}"],
      },
    ]);

    expect(entries).toHaveLength(1);
    expect(entries[0]?.guideline.id).toBe("g1");
    expect(entries[0]?.guideline.sections).toBeDefined();
  });
});
