import { describe, expect, it } from "vite-plus/test";
import { parse as parseYaml } from "yaml";

import { toMarkdown } from "@chartcoach/catalog";

describe("guideline markdown serialization", () => {
  it("serializes catalog guideline records back to markdown", () => {
    const markdown = toMarkdown({
      id: "adapt-framing",
      title: "Adapt framing",
      description: "Use the outlet to choose framing.",
      labels: ["purpose:refine", "task:distribute"],
      body: "## Advice <!-- role: advice -->\nAdapt the chart.\n",
      sections: [{ role: "advice", title: "Advice", content: "Adapt the chart." }],
      references: [],
    });

    const [, frontmatter, body] = markdown.split("---");
    expect(parseYaml(frontmatter ?? "")).toEqual({
      id: "adapt-framing",
      title: "Adapt framing",
      description: "Use the outlet to choose framing.",
      labels: ["purpose:refine", "task:distribute"],
    });
    expect(body?.trim()).toBe("## Advice <!-- role: advice -->\nAdapt the chart.");
  });
});
