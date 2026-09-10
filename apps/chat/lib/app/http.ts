import { Effect, Exit, Cause } from "effect";
import { z } from "zod";
import { runApp } from "./runtime";
import { AppError } from "./errors";

export function checkOrigin(request: Request) {
  const origin = request.headers.get("origin");
  if (origin && !URL.canParse(origin))
    throw new AppError({ status: 403, message: "Open these settings from ChartCoach." });
  const host =
    request.headers.get("x-forwarded-host") ??
    request.headers.get("host") ??
    new URL(request.url).host;
  if (
    request.headers.get("sec-fetch-site") === "cross-site" ||
    (origin && new URL(origin).host !== host)
  )
    throw new AppError({ status: 403, message: "Open these settings from ChartCoach." });
}

export const readJson = <T>(request: Request, schema: z.ZodType<T>, maxBytes = 64_000) =>
  Effect.tryPromise({
    try: async () => {
      checkOrigin(request);
      if (!request.headers.get("content-type")?.startsWith("application/json"))
        throw new AppError({ status: 415, message: "Send JSON for this request." });
      const reader = request.body?.getReader();
      if (!reader) throw new AppError({ status: 400, message: "A request body is required." });
      const chunks: Uint8Array[] = [];
      let size = 0;
      try {
        while (true) {
          const { value, done } = await reader.read();
          if (done) break;
          size += value.byteLength;
          if (size > maxBytes)
            throw new AppError({ status: 413, message: "This request is too large." });
          chunks.push(value);
        }
      } finally {
        await reader.cancel();
      }
      return schema.parse(JSON.parse(Buffer.concat(chunks).toString("utf8")));
    },
    catch: (error) =>
      error instanceof AppError
        ? error
        : new AppError({ status: 400, message: "Check the submitted fields." }),
  });

export async function appResponse<E>(
  request: Request,
  effect: Parameters<typeof runApp<Response, E>>[0],
) {
  const result = await runApp(
    Effect.exit(effect.pipe(Effect.timeout("30 seconds"), Effect.withSpan("chat.app.request"))),
    { signal: request.signal },
  );
  if (Exit.isSuccess(result)) return result.value;
  const error = Cause.failureOption(result.cause);
  const failure =
    error._tag === "Some" && error.value instanceof AppError ? error.value : undefined;
  return Response.json(
    { error: failure?.message ?? "The request could not be completed. Try again." },
    { status: failure?.status ?? 500, headers: { "cache-control": "no-store" } },
  );
}
export function jsonResponse<T>(value: T, cookie?: string) {
  const headers = new Headers({ "cache-control": "no-store" });
  if (cookie) headers.set("set-cookie", cookie);
  return Response.json(value, { headers });
}
