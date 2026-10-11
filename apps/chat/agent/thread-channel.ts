import type { Channel } from "eve/channels";
import { routeAuth } from "eve/channels/auth";
import { Effect } from "effect";
import { reviewRouteAuth } from "./auth";
import { appResponse } from "../lib/app/http";
import { bindThread, getThread } from "../lib/app/threads";
import { AppError } from "../lib/app/errors";
import { modelSelectionSchema } from "../shared/preferences";

// Persist the accepted session before its response lets the browser start streaming.
export function withThreadPersistence(channel: Channel): Channel {
  // One worker owns a locked data directory. Keep admission scoped to this
  // channel so two tabs cannot start different sessions for one conversation.
  const starting = new Set<string>();

  return {
    ...channel,
    routes: channel.routes.map((route) => {
      if (
        route.method !== "POST" ||
        !["/eve/v1/session", "/eve/v1/session/:sessionId"].includes(route.path)
      )
        return route;

      return {
        ...route,
        async handler(request, args) {
          if (!request.headers.has("x-chartcoach-thread")) return route.handler(request, args);
          const auth = await routeAuth(request, reviewRouteAuth);

          if (auth instanceof Response) return auth;

          const selection = modelSelectionSchema.safeParse({
            owner: auth.attributes["chartcoach.owner"],
            threadId: auth.attributes["chartcoach.thread"],
            connectionId: auth.attributes["chartcoach.connection"],
          });

          if (!selection.success)
            return Response.json(
              { error: "Choose an available model connection before sending." },
              { status: 400, headers: { "cache-control": "no-store" } },
            );

          const initial = route.path === "/eve/v1/session";
          const { owner, threadId, connectionId } = selection.data;

          if (initial && starting.has(threadId))
            return Response.json(
              { error: "This conversation is starting in another tab. Reload to reconnect." },
              { status: 409, headers: { "cache-control": "no-store" } },
            );

          if (initial) starting.add(threadId);

          try {
            const admitted = await appResponse(
              request,
              Effect.gen(function* () {
                const saved = yield* getThread(owner, threadId);

                if (initial && saved.detail.sessionId)
                  return yield* new AppError({
                    status: 409,
                    message: "This conversation already has a session. Reload to reconnect.",
                  });

                return new Response(null, { status: 204 });
              }),
            );

            if (!admitted.ok) return admitted;
            const response = await route.handler(request, args);

            if (!response.ok) return response;
            const sessionId = response.headers.get("x-eve-session-id") ?? args.params.sessionId;

            // Acceptance is durable. Commit its binding independently of the
            // browser's lifetime so refresh can always recover that session.
            return await appResponse(
              request,
              Effect.gen(function* () {
                if (!sessionId)
                  return yield* new AppError({
                    status: 502,
                    message: "The conversation could not start. Send your message again.",
                  });
                yield* bindThread(owner, threadId, sessionId, connectionId);

                return response;
              }),
              {},
            );
          } finally {
            if (initial) starting.delete(threadId);
          }
        },
      };
    }),
  };
}
