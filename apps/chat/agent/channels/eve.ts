import { defaultEveAuth, eveChannel } from "eve/channels/eve";
import { ForbiddenError } from "eve/channels/auth";
import { withCatalogScope } from "../../lib/catalog/scope";
import { parseSelection } from "../selection-context";
import { reviewRouteAuth } from "../auth";
import { z } from "zod";
import { withThreadPersistence } from "../thread-channel";

export default withThreadPersistence(
  eveChannel({
    auth: reviewRouteAuth,
    async onMessage(ctx) {
      const caller = defaultEveAuth(ctx);

      if (!caller)
        throw new ForbiddenError({ message: "Authenticate before starting a chart review." });

      const context = [
        "Choose and load the workflow skill that fits this turn: visfeedback, visrec, or discuss.",
      ];

      const auth = caller;

      if (ctx.eve.sessionId !== undefined) return { auth, context };
      const header = ctx.eve.request.headers.get("x-chartcoach-selection");
      const hasSelection = header !== null || caller.attributes["chartcoach.thread"] !== undefined;

      const selection = hasSelection
        ? parseSelection(caller.attributes["chartcoach.selection"])
        : undefined;

      return withCatalogScope({ selection, signal: ctx.eve.request.signal }, async (scope) => {
        const attributes = {
          ...auth.attributes,
          "chartcoach.selection": JSON.stringify(scope.selection),
          "chartcoach.predicate": !hasSelection
            ? "SELECT id FROM catalog_entries"
            : z.string().parse(caller.attributes["chartcoach.predicate"]),
        };

        if (scope.catalog.release) {
          Object.assign(attributes, { "chartcoach.release": scope.catalog.release.digest });
        }

        return {
          auth: { ...caller, attributes },
          context: [
            ...context,
            `This review is restricted to ${scope.ids.size} eligible guidelines by the user's catalog filters. Tools enforce these filters for search, SQL, reads, and citations.`,
          ],
        };
      });
    },
  }),
);
