import { defineChannel, GET, POST } from "eve/channels";
import { routeAuth } from "eve/channels/auth";
import { Effect, Redacted } from "effect";
import { z } from "zod";
import { accessRouteAuth, catalogRouteAuth } from "../auth";
import { browserIdentity, ownerId } from "../../lib/app/identity";
import { appResponse, checkOrigin, jsonResponse, readJson } from "../../lib/app/http";
import { AppError } from "../../lib/app/errors";
import { allowedModelOrigins, listProviderModels, providerEndpoint } from "../../lib/app/providers";
import {
  deleteConnection,
  listConnections,
  resolveConnection,
  saveConnection,
} from "../../lib/app/connections";
import {
  createThread,
  getThread,
  listThreads,
  updateThread,
  saveImage,
  getImage,
  imageInputSchema,
} from "../../lib/app/threads";
import { connectionInputSchema, threadInputSchema, ownerSchema } from "../../shared/preferences";
import { resolveCatalogSelection } from "../../lib/catalog/selection";

const owner = (request: Request) =>
  Effect.gen(function* () {
    const auth = yield* Effect.promise(() => routeAuth(request, catalogRouteAuth));
    if (auth instanceof Response)
      return yield* new AppError({
        status: auth.status,
        message: "Authenticate before opening your settings.",
      });
    const value = ownerSchema.safeParse(auth.attributes["chartcoach.owner"]);
    if (!value.success)
      return yield* new AppError({
        status: 401,
        message: "Reload ChartCoach to open your settings.",
      });
    return value.data;
  });
const pathId = (request: Request, offset = 1) =>
  new URL(request.url).pathname.split("/").at(-offset)!;

async function authenticatedResponse<E>(
  request: Request,
  effect: Parameters<typeof appResponse<E>>[1],
) {
  const auth = await routeAuth(request, accessRouteAuth);
  if (auth instanceof Response) return auth;
  return appResponse(request, effect);
}

export default defineChannel({
  routes: [
    GET("/eve/v1/preferences", (request) =>
      authenticatedResponse(
        request,
        Effect.gen(function* () {
          yield* Effect.try({
            try: () => checkOrigin(request),
            catch: () =>
              new AppError({
                status: 403,
                message: "Open ChartCoach directly to load your settings.",
              }),
          });
          const auth = yield* Effect.promise(() => routeAuth(request, accessRouteAuth));
          if (auth instanceof Response) return auth;
          const browser = yield* browserIdentity(request, true);
          if (!browser)
            return yield* new AppError({
              status: 500,
              message: "Could not start browser settings.",
            });
          const connections = yield* listConnections(ownerId(auth, browser.id));
          return jsonResponse(
            { connections, allowedOrigins: allowedModelOrigins() },
            browser.cookie,
          );
        }),
      ),
    ),
    POST("/eve/v1/connections", (request) =>
      authenticatedResponse(
        request,
        Effect.gen(function* () {
          const identity = yield* owner(request);
          const input = yield* readJson(request, connectionInputSchema);
          return jsonResponse(yield* saveConnection(identity, input));
        }),
      ),
    ),
    POST("/eve/v1/connections/models", (request) =>
      authenticatedResponse(
        request,
        Effect.gen(function* () {
          const identity = yield* owner(request);
          const input = yield* readJson(request, connectionInputSchema);
          const saved = input.id ? yield* resolveConnection(identity, input.id) : undefined;
          const endpoint = yield* Effect.try({
            try: () => providerEndpoint(input),
            catch: (error) =>
              error instanceof AppError
                ? error
                : new AppError({ status: 400, message: "Check the API base URL." }),
          });
          if (
            saved &&
            !input.apiKey &&
            (input.provider !== saved.connection.provider || endpoint !== saved.connection.baseURL)
          )
            return yield* new AppError({
              status: 400,
              message: "Enter the key again for this provider or endpoint.",
            });
          const key = input.apiKey ? Redacted.make(input.apiKey) : saved?.key;
          if (!key)
            return yield* new AppError({
              status: 400,
              message: "Enter an API key to list models.",
            });
          return jsonResponse(yield* listProviderModels(input, key));
        }),
      ),
    ),
    POST("/eve/v1/connections/:id/remove", (request) =>
      authenticatedResponse(
        request,
        Effect.gen(function* () {
          const identity = yield* owner(request);
          yield* readJson(request, z.strictObject({}));
          yield* deleteConnection(identity, pathId(request, 2));
          return jsonResponse({ ok: true });
        }),
      ),
    ),
    GET("/eve/v1/threads", (request) =>
      authenticatedResponse(
        request,
        Effect.gen(function* () {
          return jsonResponse(yield* listThreads(yield* owner(request)));
        }),
      ),
    ),
    POST("/eve/v1/threads", (request) =>
      authenticatedResponse(
        request,
        Effect.gen(function* () {
          const identity = yield* owner(request);
          const input = yield* readJson(request, threadInputSchema);
          yield* resolveConnection(identity, input.connectionId);
          const resolved = yield* Effect.tryPromise({
            try: (signal) => resolveCatalogSelection(input.knowledge.selection, { signal }),
            catch: () =>
              new AppError({
                status: 400,
                message: "Reload your knowledge selection before starting a conversation.",
              }),
          });
          if (!resolved.ids.length)
            return yield* new AppError({
              status: 400,
              message: "Broaden your knowledge selection.",
            });
          return jsonResponse(yield* createThread(identity, input, resolved));
        }),
      ),
    ),
    GET("/eve/v1/threads/:id", (request) =>
      authenticatedResponse(
        request,
        Effect.gen(function* () {
          return jsonResponse((yield* getThread(yield* owner(request), pathId(request))).detail);
        }),
      ),
    ),
    POST("/eve/v1/threads/:id", (request) =>
      authenticatedResponse(
        request,
        Effect.gen(function* () {
          const identity = yield* owner(request);
          const input = yield* readJson(
            request,
            z.strictObject({
              title: z.string().trim().min(1).max(160).optional(),
              archived: z.boolean().optional(),
            }),
          );
          yield* updateThread(identity, pathId(request), input);
          return jsonResponse({ ok: true });
        }),
      ),
    ),
    POST("/eve/v1/threads/:id/images", (request) =>
      authenticatedResponse(
        request,
        Effect.gen(function* () {
          const identity = yield* owner(request);
          const input = yield* readJson(request, imageInputSchema, 4_200_000);
          yield* saveImage(identity, pathId(request, 2), input);
          return jsonResponse({ ok: true });
        }),
      ),
    ),
    GET("/eve/v1/threads/:id/images/:filename", (request) =>
      authenticatedResponse(
        request,
        Effect.gen(function* () {
          const image = yield* getImage(
            yield* owner(request),
            pathId(request, 3),
            decodeURIComponent(pathId(request)),
          );
          return new Response(Uint8Array.from(image.bytes), {
            headers: {
              "content-type": image.media_type,
              "cache-control": "private, max-age=3600",
              "x-content-type-options": "nosniff",
            },
          });
        }),
      ),
    ),
  ],
});
