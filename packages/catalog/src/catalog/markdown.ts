import { stringify as stringifyYaml } from "yaml";

import type { Guideline } from "./model";

export function toMarkdown(
  guideline: Pick<Guideline, "id" | "title" | "description" | "labels" | "body">,
): string {
  const frontmatter = {
    id: guideline.id,
    title: guideline.title,
    description: guideline.description,
    labels: [...guideline.labels],
  };

  const frontmatterYaml = stringifyYaml(frontmatter, { sortMapEntries: false }).trim();
  const body = guideline.body.trim();

  return ["---", frontmatterYaml, "---", "", body, ""].join("\n");
}
