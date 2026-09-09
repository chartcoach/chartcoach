import { Library, cite } from "refkit-js";

import { truncateOgText } from "./text";
import type { OgReferenceSummary } from "./schema";

export function summarizeGuidelineReferences(references: readonly string[]): OgReferenceSummary[] {
  return references
    .flatMap((bibtex) => {
      const library = Library.parseBibtex(bibtex, { recovery: "report" });
      return library
        .values()
        .filter((reference) => reference.title)
        .map((reference) => ({
          title: truncateOgText(reference.title!, 132),
          meta: [
            cite(library, reference.key).text.replace(/^\(|\)$/g, ""),
            reference.parents.find((parent) => parent.title)?.title,
          ]
            .filter(Boolean)
            .join(" · "),
        }));
    })
    .slice(0, 2);
}
