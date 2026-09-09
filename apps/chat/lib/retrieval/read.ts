import { assertCatalogIds, withCatalogScope, type ScopeOptions } from "../catalog/scope";

export function readGuidelines(ids: string[], options: ScopeOptions) {
  return withCatalogScope(options, async (scope) => {
    assertCatalogIds(scope, ids);
    return {
      guidelines: scope.catalog.read({ ids, sourceDetail: "minimal" }),
      citations: scope.catalog.cite({ ids }),
    };
  });
}
