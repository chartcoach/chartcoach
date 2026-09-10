import type { Channel } from "eve/channels";
import { routeAuth } from "eve/channels/auth";
import { Effect } from "effect";
import { reviewRouteAuth } from "./auth";
import { appResponse } from "../lib/app/http";
import { bindThread } from "../lib/app/threads";
import { AppError } from "../lib/app/errors";
import { modelSelectionSchema } from "../shared/preferences";

// Persist the accepted session before its response lets the browser start streaming.
export function withThreadPersistence(channel: Channel): Channel {
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
          return appResponse(
            request,
            Effect.gen(function* () {
              if (!selection.success)
                return yield* new AppError({
                  status: 400,
                  message: "Choose an available model connection before sending.",
                });
              const response = yield* Effect.promise(() =>
                Promise.resolve(route.handler(request, args)),
              );
              if (!response.ok) return response;
              const sessionId = response.headers.get("x-eve-session-id") ?? args.params.sessionId;
              if (!sessionId)
                return yield* new AppError({
                  status: 502,
                  message: "The conversation could not start. Send your message again.",
                });
              const { owner, threadId, connectionId } = selection.data;
              yield* bindThread(owner, threadId, sessionId, connectionId);
              return response;
            }),
          );
        },
      };
    }),
  };
}
