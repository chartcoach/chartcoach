import {
  indexGuidelineSections,
  parseGuidelineSections,
  type CatalogEntry,
} from "@chartcoach/catalog";

import type { ScenarioSpec } from "@chartcoach/eval-ui/eval/schemas";
import type { RetrievalRequestWire } from "@chartcoach/eval-ui/eval/retrieval/chartcoach-retrieval-client";

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value && typeof value === "object" && !Array.isArray(value));
}

export function buildRetrievalRequestFromScenario(scenario: ScenarioSpec): RetrievalRequestWire {
  const lang = scenario.lang ?? "en";
  const context: Array<Record<string, unknown>> = [];

  if (scenario.chart?.uri && scenario.chart?.mime) {
    context.push({
      kind: "image",
      role: "chart",
      uri: scenario.chart.uri,
      mime: scenario.chart.mime,
    });
  }

  const situation = scenario.designer_intent?.trim();
  if (!situation) {
    throw new Error(`Scenario ${scenario.id} is missing designer_intent.`);
  }

  context.push({ kind: "text", role: "situation", text: situation, lang });
  context.push({ kind: "text", role: "chart_spec", text: "{}", lang });

  if (scenario.query?.trim()) {
    context.push({ kind: "text", role: "query", text: scenario.query.trim(), lang });
  }

  return {
    context,
    lang,
    meta: { scenarioId: scenario.id },
    k: 10,
  };
}

export function catalogEntriesFromWire(rows: unknown[]): CatalogEntry[] {
  const entries: CatalogEntry[] = [];

  for (const row of rows) {
    if (!isRecord(row)) continue;

    const id = row.id;
    const guideline = row.guideline;
    const references = row.references;

    if (typeof id !== "string" || !isRecord(guideline)) continue;

    const entry: CatalogEntry = {
      guideline: {
        id,
        title: typeof guideline.title === "string" ? guideline.title : id,
        bibliography:
          typeof guideline.bibliography === "string" ? guideline.bibliography : undefined,
        description: typeof guideline.description === "string" ? guideline.description : "",
        labels: Array.isArray(guideline.labels)
          ? guideline.labels.filter((l): l is string => typeof l === "string")
          : [],
        body: typeof guideline.body === "string" ? guideline.body : "",
        sections: [],
        sectionsIndex: { byRole: {} },
      },
      references: Array.isArray(references)
        ? references.filter((r): r is string => typeof r === "string")
        : [],
    };

    entry.guideline.sections = parseGuidelineSections(entry.guideline.body);
    entry.guideline.sectionsIndex = indexGuidelineSections(entry.guideline.sections);
    entries.push(entry);
  }

  return entries;
}
