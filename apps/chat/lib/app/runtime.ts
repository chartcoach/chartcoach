import { Effect, Layer, ManagedRuntime } from "effect";
import { FetchHttpClient } from "@effect/platform";
import * as OtelTracer from "@effect/opentelemetry/Tracer";
import { context, trace, type Tracer } from "@opentelemetry/api";
import { join } from "node:path";
import envPaths from "env-paths";
import { databaseLayer } from "./database";
import { Secrets } from "./secrets";
import { env } from "../env";

export function createAppRuntime(
  directory: string,
  tracer: Tracer = trace.getTracer("chartcoach.app"),
) {
  const tracing = OtelTracer.layerWithoutOtelTracer.pipe(
    Layer.provide(Layer.succeed(OtelTracer.OtelTracer, tracer)),
  );

  return ManagedRuntime.make(
    Layer.mergeAll(
      databaseLayer(join(directory, "chat.sqlite")),
      Secrets.Default(directory),
      FetchHttpClient.layer,
      tracing,
    ),
  );
}

let runtime: ReturnType<typeof createAppRuntime> | undefined;

export function runApp<A, E>(
  effect: Effect.Effect<
    A,
    E,
    ManagedRuntime.ManagedRuntime.Context<ReturnType<typeof createAppRuntime>>
  >,
  options?: { signal?: AbortSignal },
) {
  runtime ??= createAppRuntime(env.CHAT_DATA_DIR ?? envPaths("chartcoach-chat").data);
  const parent = trace.getSpan(context.active())?.spanContext();

  return runtime.runPromise(
    parent ? effect.pipe(OtelTracer.withSpanContext(parent)) : effect,
    options,
  );
}

export async function closeAppRuntime() {
  const current = runtime;
  runtime = undefined;
  await current?.dispose();
}
