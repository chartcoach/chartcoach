import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll, beforeAll, expect, it, vi } from "vite-plus/test";
import { defineChannel, POST, type RouteHandlerArgs } from "eve/channels";
import { routeAuth } from "eve/channels/auth";
import { browserIdentity } from "../lib/app/identity";
import { createThread, getThread } from "../lib/app/threads";
import { emptyCatalogFilters } from "../shared/catalog-filters";

let app: typeof import("../lib/app/runtime");
let catalogRouteAuth: typeof import("../agent/auth").catalogRouteAuth;
let reviewRouteAuth: typeof import("../agent/auth").reviewRouteAuth;
let withThreadPersistence: typeof import("../agent/thread-channel").withThreadPersistence;
let directory: string;
const unsupportedSessionOperation = () => {
  throw new Error("The admission handler must delegate session operations to Eve.");
};
const routeContext: RouteHandlerArgs = {
  params: {},
  requestIp: "127.0.0.1",
  from: unsupportedSessionOperation,
  to: unsupportedSessionOperation,
  resolveSession: unsupportedSessionOperation,
  attachSession: unsupportedSessionOperation,
  waitUntil: unsupportedSessionOperation,
};
beforeAll(async () => {
  vi.stubEnv("EVE_DEV", "1");
  directory = await mkdtemp(join(tmpdir(), "chartcoach-thread-route-"));
  vi.stubEnv("CHAT_DATA_DIR", directory);
  app = await import("../lib/app/runtime");
  ({ catalogRouteAuth, reviewRouteAuth } = await import("../agent/auth"));
  ({ withThreadPersistence } = await import("../agent/thread-channel"));
});
afterAll(async () => {
  await app.closeAppRuntime();
  await rm(directory, { recursive: true, force: true });
  vi.unstubAllEnvs();
});

async function setup() {
  const identity = await app.runApp(browserIdentity(new Request("http://localhost"), true));
  const cookie = identity!.cookie!.split(";")[0];
  const auth = await routeAuth(
    new Request("http://localhost", { headers: { cookie } }),
    catalogRouteAuth,
  );
  if (auth instanceof Response) throw new Error("Expected local caller");
  const owner = String(auth.attributes["chartcoach.owner"]);
  const catalogId = "a".repeat(64);
  const thread = await app.runApp(
    createThread(
      owner,
      {
        title: "Chart review",
        connectionId: "server",
        knowledge: {
          filters: emptyCatalogFilters(catalogId),
          selection: { catalogId, sql: "SELECT id FROM catalog_entries" },
          matchedGuidelines: 1,
        },
      },
      { catalogId, ids: ["labels"] },
    ),
  );
  const headers = { cookie, "x-chartcoach-thread": thread.id, "x-chartcoach-connection": "server" };
  return { owner, thread, headers };
}

it("binds an accepted session before streaming, independently of model execution", async () => {
  const { owner, thread, headers } = await setup();
  const native = POST("/eve/v1/session", async () =>
    Response.json({ ok: true }, { status: 202, headers: { "x-eve-session-id": "session-a" } }),
  );
  const route = withThreadPersistence(defineChannel({ routes: [native] })).routes[0];
  if (route.method !== "POST") throw new Error("Expected POST");
  const response = await route.handler(
    new Request("http://localhost/eve/v1/session", { method: "POST", headers }),
    routeContext,
  );
  expect(response.status).toBe(202);
  expect((await app.runApp(getThread(owner, thread.id))).detail.sessionId).toBe("session-a");
  const stream = (session: string, extra = {}) =>
    routeAuth(
      new Request(`http://localhost/eve/v1/session/${session}/stream`, {
        headers: { ...headers, ...extra },
      }),
      reviewRouteAuth,
    );
  expect(await stream("session-a")).toMatchObject({
    attributes: {
      "chartcoach.owner": owner,
      "chartcoach.thread": thread.id,
      "chartcoach.connection": "server",
    },
  });
  const mismatch = await stream("session-b");
  expect(mismatch).toBeInstanceOf(Response);
  if (mismatch instanceof Response)
    expect(await mismatch.json()).toMatchObject({
      code: "conversation_session_mismatch",
      error: expect.stringContaining("Reload the page"),
    });
});

it("does not bind rejected sessions or dispatch for another browser", async () => {
  const { owner, thread, headers } = await setup();
  const native = POST("/eve/v1/session", async (request) => {
    if (request.headers.get("cookie") !== headers.cookie)
      throw new Error("Dispatched for an unauthorized browser");
    return Response.json({ error: "Bad upload" }, { status: 415 });
  });
  const route = withThreadPersistence(defineChannel({ routes: [native] })).routes[0];
  if (route.method !== "POST") throw new Error("Expected POST");
  const send = (cookie: string) =>
    route.handler(
      new Request("http://localhost/eve/v1/session", {
        method: "POST",
        headers: { ...headers, cookie },
      }),
      routeContext,
    );
  expect((await send(headers.cookie)).status).toBe(415);
  expect((await app.runApp(getThread(owner, thread.id))).detail.sessionId).toBeNull();
  expect((await send("")).status).toBe(403);
  const other = await app.runApp(browserIdentity(new Request("http://localhost"), true));
  expect((await send(other!.cookie!.split(";")[0])).status).toBe(403);
});
