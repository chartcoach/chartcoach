import { describe, expect, it } from "vitest";

import { guidelineToMarkdown, parseGuideline } from "@chartcoach/catalog";

describe("guideline markdown serialization", () => {
  it("serializes catalog guideline records back to markdown", () => {
    const markdown = guidelineToMarkdown({
      id: "adapt-framing",
      title: "Adapt framing",
      bibliography: "references.bib",
      description: "Use the outlet to choose framing.",
      labels: ["purpose:refine", "task:distribute"],
      body: "## Advice <!-- role: advice -->\nAdapt the chart.\n",
    });

    expect(markdown).toContain("id: adapt-framing");
    expect(markdown).toContain("title: Adapt framing");
    expect(markdown).toContain("bibliography: references.bib");
    expect(markdown).toContain("## Advice <!-- role: advice -->");

    const parsed = parseGuideline(markdown);
    expect(parsed.id).toBe("adapt-framing");
    expect(parsed.title).toBe("Adapt framing");
    expect(parsed.description).toBe("Use the outlet to choose framing.");
    expect(parsed.labels).toEqual(["purpose:refine", "task:distribute"]);
    expect(parsed.sectionsIndex.byRole.advice?.[0]?.content).toBe("Adapt the chart.");
  });
});
