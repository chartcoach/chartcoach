import { createAnthropic } from "@ai-sdk/anthropic";
import { createGoogle } from "@ai-sdk/google";
import { createOpenAI } from "@ai-sdk/openai";
import { createOpenAICompatible } from "@ai-sdk/openai-compatible";
import { Headers, HttpClient, HttpClientRequest } from "@effect/platform";
import { RequestInit as FetchHttpClientRequestInit } from "@effect/platform/FetchHttpClient";
import { Effect, Match, Redacted, Stream } from "effect";
import { z } from "zod";
import type { ConnectionInput, ModelChoice } from "../../shared/preferences";
import { providerNames, apiBaseURL } from "../../shared/model";
import { settings } from "../../runtime/settings";
import { AppError } from "./errors";

const endpoints = {
  anthropic: "https://api.anthropic.com/v1",
  openai: "https://api.openai.com/v1",
  google: "https://generativelanguage.googleapis.com/v1beta",
};

export function allowedModelOrigins() {
  return [
    ...new Set([
      ...settings.modelOrigins,
      ...(settings.model.baseURL ? [new URL(settings.model.baseURL).origin] : []),
    ]),
  ];
}

export function providerEndpoint(
  input: Pick<ConnectionInput, "provider" | "baseURL">,
  allowedOrigins: readonly string[] = allowedModelOrigins(),
) {
  if (input.provider !== "compatible") return endpoints[input.provider];
  const parsed = apiBaseURL.safeParse(input.baseURL);

  if (!parsed.success)
    throw new AppError({
      status: 400,
      message: "Enter an HTTP or HTTPS API base URL, including its version path.",
    });
  const url = new URL(parsed.data);

  if (!allowedOrigins.includes(url.origin))
    throw new AppError({
      status: 400,
      message: "This API origin is not allowed. Add it to CHARTCOACH_MODEL_ORIGINS on the server.",
    });

  return url.href.replace(/\/$/, "");
}

const directFetch =
  (connection: ConnectionInput): typeof fetch =>
  async (input, init) => {
    const response = await fetch(input, { ...init, redirect: "error" });

    if (response.ok) return response;
    await response.body?.cancel();

    const reason =
      response.status === 401 || response.status === 403
        ? "The provider rejected this key. Check its value and permissions in Model settings."
        : response.status === 404
          ? "This model was not found or is not available to this key. Load the model list in Model settings and choose an available model."
          : response.status === 429
            ? "The provider's quota or rate limit was reached. Check billing and quota, or wait before retrying."
            : response.status >= 500
              ? "The provider is temporarily unavailable. Try again, or select another model."
              : "The provider rejected the request. Check the key, model ID, image support, and context limit in Model settings.";

    const message = `${providerNames[connection.provider]} · ${connection.model} (HTTP ${response.status}): ${reason}`;

    // Keep the safe error parseable by every native adapter, including Gemini and Anthropic.
    return Response.json(
      {
        type: "error",
        error: { type: "provider_error", code: response.status, status: "ERROR", message },
      },
      { status: response.status },
    );
  };

export function languageModel(
  input: ConnectionInput,
  key: Redacted.Redacted<string>,
  allowedOrigins?: readonly string[],
) {
  const baseURL = providerEndpoint(input, allowedOrigins);
  const apiKey = input.auth === "none" ? undefined : Redacted.value(key);
  const options = { baseURL, apiKey, fetch: directFetch(input) };

  switch (input.provider) {
    case "anthropic":
      return createAnthropic(options)(input.model);
    case "google":
      return createGoogle(options)(input.model);
    case "openai":
      return createOpenAI(options).responses(input.model);
    case "compatible":
      return createOpenAICompatible({ ...options, name: "custom" }).chatModel(input.model);
  }
}

const apiModel = z.object({ id: z.string(), display_name: z.string().optional() });

const googleModel = z.object({
  name: z.string(),
  displayName: z.string().optional(),
  supportedGenerationMethods: z.array(z.string()).optional(),
});

export const listProviderModels = (input: ConnectionInput, key: Redacted.Redacted<string>) =>
  Effect.gen(function* () {
    const endpoint = yield* Effect.try({
      try: () => providerEndpoint(input),
      catch: (error) =>
        error instanceof AppError
          ? error
          : new AppError({ status: 400, message: "Check the API base URL." }),
    });

    const client = yield* HttpClient.HttpClient;

    const headers =
      input.auth === "none"
        ? {}
        : Match.value(input.provider).pipe(
            Match.when("anthropic", () => ({
              "x-api-key": Redacted.value(key),
              "anthropic-version": "2023-06-01",
            })),
            Match.when("google", () => ({ "x-goog-api-key": Redacted.value(key) })),
            Match.orElse(() => ({ authorization: `Bearer ${Redacted.value(key)}` })),
          );

    const models = new Map<string, ModelChoice>();
    const cursors = new Set<string>();
    let cursor: string | undefined;

    do {
      const url = new URL(`${endpoint}/models`);

      if (cursor)
        url.searchParams.set(input.provider === "google" ? "pageToken" : "after_id", cursor);
      const request = HttpClientRequest.get(url.href).pipe(HttpClientRequest.setHeaders(headers));

      const response = yield* client
        .execute(request)
        .pipe(Effect.provideService(FetchHttpClientRequestInit, { redirect: "error" }));

      const body = yield* response.stream.pipe(
        Stream.runFoldEffect({ chunks: new Array<Uint8Array>(), size: 0 }, (body, chunk) => {
          if (body.size + chunk.length > 2 * 1024 * 1024)
            return Effect.fail(
              new AppError({
                status: 502,
                message: "The provider's model list is too large. Enter a model ID directly.",
              }),
            );
          body.chunks.push(chunk);
          body.size += chunk.length;

          return Effect.succeed(body);
        }),
      );

      const json: unknown = yield* Effect.try(() =>
        JSON.parse(Buffer.concat(body.chunks).toString("utf8")),
      );

      if (response.status < 200 || response.status >= 300)
        return yield* new AppError({
          status: 502,
          message:
            "The provider rejected model discovery. Check your key and its permissions, or enter a model ID directly.",
        });

      if (input.provider === "google") {
        const page = yield* Effect.try(() =>
          z
            .object({ models: z.array(googleModel), nextPageToken: z.string().optional() })
            .parse(json),
        );

        for (const model of page.models) {
          if (
            model.supportedGenerationMethods &&
            !model.supportedGenerationMethods.includes("generateContent")
          )
            continue;
          const id = model.name.replace(/^models\//, "");
          models.set(id, { id, name: model.displayName ?? id });
        }

        cursor = page.nextPageToken;
      } else {
        const page = yield* Effect.try(() =>
          z
            .object({
              data: z.array(apiModel),
              has_more: z.boolean().optional(),
              last_id: z.string().optional(),
            })
            .parse(json),
        );

        for (const model of page.data)
          models.set(model.id, { id: model.id, name: model.display_name ?? model.id });
        cursor = page.has_more ? page.last_id : undefined;

        if (page.has_more && !cursor)
          return yield* new AppError({
            status: 502,
            message:
              "The provider returned incomplete model pagination. Enter a model ID directly.",
          });
      }

      if (cursor && (cursors.has(cursor) || cursors.size >= 20))
        return yield* new AppError({
          status: 502,
          message: "The model list is too large or repeated a page. Enter a model ID directly.",
        });

      if (cursor) cursors.add(cursor);
    } while (cursor);

    return [...models.values()].toSorted((a, b) => a.name.localeCompare(b.name));
  }).pipe(
    Effect.locallyWith(Headers.currentRedactedNames, (names) => [...names, "x-goog-api-key"]),
    Effect.timeout("15 seconds"),
    Effect.catchAll((error) =>
      Effect.fail(
        error instanceof AppError
          ? error
          : new AppError({
              status: 502,
              message:
                "Could not list models. Check the key and endpoint, or enter a model ID directly.",
            }),
      ),
    ),
    Effect.withSpan("provider.list_models"),
  );
