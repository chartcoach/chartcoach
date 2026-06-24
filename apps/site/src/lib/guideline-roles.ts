import type { CollectionEntry } from "astro:content";

type GuidelineEntry = CollectionEntry<"guidelines">;

export function collectGuidelineRoles(guidelines: readonly GuidelineEntry[]): string[] {
  const roles = new Set<string>();

  for (const guideline of guidelines) {
    for (const section of guideline.data.record.sections) {
      if (section.role) roles.add(section.role);
    }
  }

  return Array.from(roles);
}
