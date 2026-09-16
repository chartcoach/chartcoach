import { Library, cite, type Text } from "refkit-js";

import { truncateOgText } from "./text";
import type { OgReferenceSummary } from "./schema";

export function summarizeGuidelineReferences(references: readonly string[]): OgReferenceSummary[] {
  return references
    .flatMap((bibtex) => {
      const library = Library.parseBibtex(bibtex, { recovery: "report" });

      return library
        .values()
        .filter((reference) => plainText(reference.title))
        .map((reference) => ({
          title: truncateOgText(plainText(reference.title), 132),
          meta: [
            cite(library, reference.key).text.replace(/^\(|\)$/g, ""),
            reference.parents?.map((parent) => plainText(parent.title)).find(Boolean),
          ]
            .filter(Boolean)
            .join(" · "),
        }));
    })
    .slice(0, 2);
}

function plainText(value: Text | null | undefined): string {
  return value?.chunks.map((chunk) => chunk.text).join("") ?? "";
}
