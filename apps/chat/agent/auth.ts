import {
  ForbiddenError,
  localDev,
  placeholderAuth,
  vercelOidc,
  type AuthFn,
} from "eve/channels/auth";
import { decodeSelection } from "./selection-context";
import { resolveCatalogSelection } from "../lib/catalog/selection";
import { Effect, Either } from "effect";
import { runApp } from "../lib/app/runtime";
import { browserIdentity, ownerId } from "../lib/app/identity";
import { getThread } from "../lib/app/threads";
import { ownerSchema } from "../shared/preferences";

export const accessRouteAuth = [vercelOidc(), localDev(), placeholderAuth()];

export const catalogRouteAuth = accessRouteAuth.map(
  (authenticate): AuthFn<Request> =>
    async (request) => {
      const principal = await authenticate(request);

      if (!principal || !request.headers.get("cookie")) return principal;
      const browser = await runApp(browserIdentity(request), { signal: request.signal });

      if (!browser) return principal;
      const owner = ownerId(principal, browser.id);

      return {
        ...principal,
        principalId: owner,
        attributes: { ...principal.attributes, "chartcoach.owner": owner },
      };
    },
);

// Eve maps onMessage exceptions to HTTP 500, so reject invalid headers during its auth walk.
export const reviewRouteAuth = catalogRouteAuth.map(
  (authenticate): AuthFn<Request> =>
    async (request) => {
      const principal = await authenticate(request);

      if (!principal) return principal;
      const caller = principal;
      const threadId = request.headers.get("x-chartcoach-thread");
      const connectionId = request.headers.get("x-chartcoach-connection");

      if (threadId) {
        const owner = ownerSchema.safeParse(caller.attributes["chartcoach.owner"]);

        if (!owner.success)
          throw new ForbiddenError({ message: "Open the conversation from your history." });

        const saved = await runApp(getThread(owner.data, threadId).pipe(Effect.either), {
          signal: request.signal,
        });

        if (Either.isLeft(saved)) throw new ForbiddenError({ message: "Conversation not found." });
        const sessionId = new URL(request.url).pathname.match(/\/session\/([^/]+)/)?.[1];

        if (sessionId && saved.right.detail.sessionId !== decodeURIComponent(sessionId))
          throw new ForbiddenError({
            code: "conversation_session_mismatch",
            message:
              "This conversation lost its session connection. Reload the page to reconnect; your saved messages and model key are unchanged.",
          });

        return {
          ...caller,
          attributes: {
            ...caller.attributes,
            "chartcoach.thread": threadId,
            "chartcoach.connection": connectionId ?? saved.right.detail.connectionId,
            "chartcoach.selection": JSON.stringify(saved.right.resolved),
            "chartcoach.predicate": saved.right.detail.knowledge.selection.sql,
          },
        };
      }

      const header = request.headers.get("x-chartcoach-selection");

      if (
        !caller ||
        header === null ||
        request.method !== "POST" ||
        !new URL(request.url).pathname.endsWith("/session")
      )
        return caller;

      try {
        const query = await decodeSelection(header);

        const selection = await resolveCatalogSelection(query, {
          signal: request.signal,
        });

        return {
          ...caller,
          attributes: {
            ...caller.attributes,
            "chartcoach.selection": JSON.stringify(selection),
            "chartcoach.predicate": query.sql,
          },
        };
      } catch (error) {
        throw new ForbiddenError({
          code: "invalid_catalog_selection",
          message: error instanceof Error ? error.message : "Check your guideline selection.",
        });
      }
    },
);
