import type { CatalogScope } from "../catalog/scope";
import { assertCatalogIds } from "../catalog/scope";

export function guidelineCards(scope: CatalogScope, ids: readonly string[]) {
  assertCatalogIds(scope, ids);
  return scope.catalog.cite({ ids: [...ids] }).map(({ id, title, url }) => ({
    id,
    title,
    description: scope.catalog.require(id).description,
    url,
  }));
}
