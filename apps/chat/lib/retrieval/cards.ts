import { settings } from "../../runtime/settings";
import { guidelineURLs } from "../../shared/guideline-links";
import type { CatalogScope } from "../catalog/scope";
import { assertCatalogIds } from "../catalog/scope";

export function guidelineCitations(scope: CatalogScope, ids: readonly string[]) {
  assertCatalogIds(scope, ids);

  return scope.catalog.cite({ ids: [...ids] }).map((citation) => {
    const urls = guidelineURLs(citation.id, settings.guidelines);

    if (!urls) throw new Error(`Invalid guideline ID: ${citation.id}`);

    return {
      ...citation,
      ...urls,
      guideline_citation: `[${citation.title}](${urls.url}) (\`${citation.id}\`)`,
    };
  });
}

export function guidelineCards(scope: CatalogScope, ids: readonly string[]) {
  return guidelineCitations(scope, ids).map(({ id, title, url, imageURL }) => ({
    id,
    title,
    description: scope.catalog.require(id).description,
    url,
    imageURL,
  }));
}
