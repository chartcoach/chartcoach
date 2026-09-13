import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll, beforeAll, expect, it, vi } from "vite-plus/test";
import { defineChannel, POST, type RouteHandlerArgs } from "eve/channels";
import { routeAuth } from "eve/channels/auth";
import { browserIdentity } from "../lib/app/identity";
import { createThread, getThread } from "../lib/app/threads";
import { connectionSchema, type ConnectionInput } from "../shared/preferences";
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
  vi.stubEnv("CHARTCOACH_MODEL_ORIGINS", "https://compatible.example,https://another.example");
  directory = await mkdtemp(join(tmpdir(), "chartcoach-thread-route-"));
  vi.stubEnv("CHARTCOACH_DATA_DIR", directory);
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

it("discovers and saves models under the same credential and owner policy", async () => {
  const { default: preferences } = await import("../agent/channels/preferences");
  const identity = await app.runApp(browserIdentity(new Request("http://localhost"), true));
  const other = await app.runApp(browserIdentity(new Request("http://localhost"), true));
  const cookie = identity!.cookie!.split(";")[0];

  const post = (path: string, input: ConnectionInput, browser = cookie) => {
    const route = preferences.routes.find(
      (route) => route.method === "POST" && route.path === path,
    );

    if (!route || route.method !== "POST") throw new Error(`Missing POST ${path}`);

    return route.handler(
      new Request(`http://localhost${path}`, {
        method: "POST",
        headers: { cookie: browser, "content-type": "application/json" },
        body: JSON.stringify(input),
      }),
      routeContext,
    );
  };

  vi.stubGlobal("fetch", async (input: RequestInfo | URL, init?: RequestInit) => {
    const request = new Request(input, init);
    expect(request.url).toBe("https://another.example/v1/models");
    expect(request.headers.get("authorization")).toBeNull();

    return Response.json({ data: [{ id: "vision" }] });
  });

  try {
    const input: ConnectionInput = {
      provider: "compatible",
      name: "Local model",
      baseURL: "https://compatible.example/v1",
      model: "vision",
      contextWindow: 32000,
      auth: "none",
    };

    const saved = connectionSchema.parse(await (await post("/eve/v1/connections", input)).json());
    const moved = { ...input, id: saved.id, baseURL: "https://another.example/v1" };
    expect(await (await post("/eve/v1/connections/models", moved)).json()).toEqual([
      { id: "vision", name: "vision" },
    ]);
    expect(await (await post("/eve/v1/connections", moved)).json()).toMatchObject({
      id: saved.id,
      baseURL: moved.baseURL,
    });

    for (const path of ["/eve/v1/connections", "/eve/v1/connections/models"]) {
      const missingKey = await post(path, { ...moved, auth: "api-key" });
      expect(missingKey.status).toBe(400);
      expect(await missingKey.json()).toMatchObject({
        error: expect.stringContaining("Enter an API key"),
      });
      expect((await post(path, moved, other!.cookie!.split(";")[0])).status).toBe(404);
    }
  } finally {
    vi.unstubAllGlobals();
  }
});
