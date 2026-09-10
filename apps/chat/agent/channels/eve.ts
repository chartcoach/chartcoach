import { defaultEveAuth, eveChannel } from "eve/channels/eve";
import { ForbiddenError } from "eve/channels/auth";
import { withCatalogScope } from "../../lib/catalog/scope";
import { parseSelection } from "../selection-context";
import { reviewRouteAuth } from "../auth";
import { z } from "zod";

export default eveChannel({
  auth: reviewRouteAuth,
  async onMessage(ctx) {
    const caller = defaultEveAuth(ctx);
    if (!caller)
      throw new ForbiddenError({ message: "Authenticate before starting a chart review." });
    if (ctx.eve.sessionId !== undefined) return { auth: caller };
    const header = ctx.eve.request.headers.get("x-chartcoach-selection");
    const selection =
      header === null ? undefined : parseSelection(caller.attributes["chartcoach.selection"]);
    return withCatalogScope({ selection, signal: ctx.eve.request.signal }, async (scope) => {
      const attributes = {
        ...caller.attributes,
        "chartcoach.selection": JSON.stringify(scope.selection),
        "chartcoach.predicate":
          header === null
            ? "SELECT id FROM catalog_entries"
            : z.string().parse(caller.attributes["chartcoach.predicate"]),
      };
      if (scope.catalog.release) {
        Object.assign(attributes, { "chartcoach.release": scope.catalog.release.digest });
      }
      return {
        auth: { ...caller, attributes },
        context: [
          `This review is restricted to ${scope.ids.size} eligible guidelines by the user's catalog filters. Tools enforce these filters for search, SQL, reads, and citations.`,
        ],
      };
    });
  },
});
