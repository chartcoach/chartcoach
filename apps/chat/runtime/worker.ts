import { once } from "node:events";
import { serve } from "srvx/node";
import { useNitroApp } from "nitro/app";

if (!process.send || !process.connected) throw new Error("Start ChatCoach with its CLI.");

const stopped = new AbortController();

const stop = () => {
  if (stopped.signal.aborted) return;
  stopped.abort();
  setTimeout(() => process.exit(1), 5000).unref();
};

process.on("SIGINT", stop);

process.on("SIGTERM", stop);

process.once("disconnect", stop);

await using resources = new AsyncDisposableStack();

const app = useNitroApp();

resources.defer(async () => {
  await app.hooks?.callHook("close");
});

const server = serve({
  hostname: "127.0.0.1",
  port: 0,
  fetch: app.fetch,
  silent: true,
  gracefulShutdown: false,
});

resources.defer(() => server.close(true));

await server.ready();

const url = server.url!;

process.env.WORKFLOW_LOCAL_BASE_URL = url;

const ready = await app.fetch(
  new Request(new URL("eve/v1/ready", url), {
    headers: {
      authorization: `Basic ${Buffer.from(`chartcoach:${process.env.CHARTCOACH_RUNTIME_TOKEN}`).toString("base64")}`,
    },
    signal: stopped.signal,
  }),
);

await ready.body?.cancel();

if (!ready.ok) throw new Error("The chat runtime could not prepare its storage and sandbox.");

stopped.signal.throwIfAborted();

process.send({ type: "ready", url });

await once(stopped.signal, "abort");
