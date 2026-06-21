import { toMarkdown } from "@chartcoach/catalog";

import type { LlmPageSource, LlmPageSourceContext } from "../integrations/llms";
import { serializeGuidelineMarkdown } from "../lib/guideline-markdown";
import { loadSiteCatalog } from "./catalog-source";

export async function chartcoachLlmPages({ root }: LlmPageSourceContext): Promise<LlmPageSource[]> {
  const catalog = await loadSiteCatalog(root);
  const guidelines = Array.from(catalog).sort((a, b) => a.title.localeCompare(b.title));
  const guidelinePages = guidelines.map((guideline): LlmPageSource => {
    const referencesBib = guideline.references.length > 0 ? guideline.references.join("\n\n") : "";

    return {
      pathname: `/guidelines/${guideline.id}/`,
      title: guideline.title,
      description: guideline.description,
      markdown: serializeGuidelineMarkdown(toMarkdown(guideline), referencesBib),
      markdownPathname: `/guidelines/${guideline.id}.md`,
      writeMarkdown: false,
    };
  });

  return [...sitePages(guidelines.length), ...guidelinePages];
}

function sitePages(guidelineCount: number): LlmPageSource[] {
  return [
    {
      pathname: "/",
      title: "chartcoach",
      description:
        "chartcoach turns visualization design knowledge into source-traced records for chart agents.",
      markdownPathname: "/index.md",
      markdown: [
        "# chartcoach",
        "",
        "chartcoach turns visualization design knowledge into source-traced records that agents can retrieve, cite, apply, and improve. Use it to review charts, recommend encodings, evaluate trade-offs, and explain where guidance comes from.",
        "",
        "## Resources",
        "",
        "- [Browse the Guideline Catalog](/guidelines/)",
        "- [Read docs](https://docs.chartcoach.dev)",
        "- [Catalog repository](https://github.com/chartcoach/catalog)",
        "- [Agent skills](https://github.com/chartcoach/skills)",
        "",
        "## What the catalog provides",
        "",
        "- Human-readable guideline Markdown",
        "- Structured guideline records for Python, TypeScript, and CLI workflows",
        "- Section roles for advice, reason, context, exceptions, costs, mistakes, checks, and fixes",
        "- Source references for grounded responses",
        "- Section text that can be embedded for search, clustering, and coverage analysis",
      ].join("\n"),
    },
    {
      pathname: "/guidelines/",
      title: "Guideline Catalog",
      description: `Browse ${guidelineCount.toLocaleString()} chartcoach guideline records with labels, role-marked sections, source references, and Markdown and JSON routes.`,
      markdownPathname: "/guidelines.md",
      markdown: [
        "# Guideline Catalog",
        "",
        `The Guideline Catalog contains ${guidelineCount.toLocaleString()} visualization guideline records.`,
        "",
        "Each guideline is available as a public page, Markdown route, and JSON route. Records include labels, role-marked sections, source references, and the distilled guideline text.",
        "",
        "Use `/guidelines/{id}.md` for the Markdown representation and `/guidelines/{id}.json` for the structured representation.",
      ].join("\n"),
    },
  ];
}
