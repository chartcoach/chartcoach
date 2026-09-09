import { defaultEveAuth, eveChannel } from "eve/channels/eve";
import { ForbiddenError } from "eve/channels/auth";
import { withCatalogScope } from "../../lib/catalog/scope";
import { parseSelection } from "../selection-context";
import { reviewRouteAuth } from "../auth";

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
    return withCatalogScope({ selection, signal: ctx.eve.request.signal }, async (scope) => ({
      auth: {
        ...caller,
        attributes: {
          ...caller.attributes,
          "chartcoach.selection": JSON.stringify(scope.selection),
        },
      },
      context: [
        `This review is restricted to ${scope.ids.size} eligible guidelines by the user's catalog filters. Tools enforce these filters for search, SQL, reads, and citations.`,
      ],
    }));
  },
});
