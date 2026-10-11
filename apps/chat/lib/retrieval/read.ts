import { guidelineCitations } from "./cards";
import { withCatalogScope, type ScopeOptions } from "../catalog/scope";

export function readGuidelines(ids: string[], options: ScopeOptions) {
  return withCatalogScope(options, async (scope) => {
    const citations = guidelineCitations(scope, ids);

    return {
      guidelines: scope.catalog.read({ ids, sourceDetail: "minimal" }),
      citations,
    };
  });
}
