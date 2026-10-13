import { createServer, get, type IncomingMessage, type ServerResponse } from "node:http";
import { z } from "zod";
import { expect, it } from "vite-plus/test";
import { createGateway } from "../runtime/gateway";
import { loadConfig } from "../runtime/config";

const handlePage = async (request: IncomingMessage, response: ServerResponse) => {
  const path = new URL(request.url!, "http://localhost").pathname;

  if (path === "/duckdb/duckdb-eh.wasm") response.end("wasm");
  else if (path === "/" || path.startsWith("/chat/") || path === "/guidelines")
    response.end("<h1>chartcoach</h1>");
  else {
    response.writeHead(404);
    response.end("Page not found.");
  }
};

it("protects assets and streams authenticated requests through the same origin", async () => {
  const worker = createServer((request, response) => {
    response.setHeader("content-type", "application/json");
    response.end(
      JSON.stringify({
        authorization: request.headers.authorization,
        host: request.headers["x-forwarded-host"],
        protocol: request.headers["x-forwarded-proto"],
      }),
    );
  });

  await new Promise<void>((resolve) => worker.listen(0, "127.0.0.1", resolve));
  const address = z.object({ port: z.number() }).parse(worker.address());

  const config = loadConfig({
    environment: {},
    userConfig: "/missing/config.json",
    overrides: { server: { port: 0 } },
  });

  const gateway = createGateway({
    config,
    handlePage,
    agentURL: `http://127.0.0.1:${address.port}`,
    token: "private-worker-token",
    password: "private-password",
  });

  try {
    const url = await gateway.listen();
    expect((await fetch(url)).status).toBe(401);

    const headers = {
      authorization: `Basic ${Buffer.from("chartcoach:private-password").toString("base64")}`,
    };

    expect(await (await fetch(url, { headers })).text()).toContain("chartcoach");
    expect(
      (await fetch(url, { headers: { ...headers, origin: "https://attacker.example" } })).status,
    ).toBe(403);

    const hostileHost = await new Promise<number | undefined>((resolve, reject) => {
      get(url, { headers: { ...headers, host: "attacker.example" } }, (response) => {
        response.resume();
        resolve(response.statusCode);
      }).once("error", reject);
    });

    expect(hostileHost).toBe(403);

    const response = await fetch(new URL("eve/v1/preferences", url), {
      headers: { ...headers, "x-forwarded-host": "attacker.example", "x-forwarded-proto": "https" },
    });

    expect(await response.json()).toEqual({
      authorization: `Basic ${Buffer.from("chartcoach:private-worker-token").toString("base64")}`,
      host: new URL(url).host,
      protocol: "http",
    });
    expect((await fetch(new URL(".well-known/workflow/v1/flow", url), { headers })).status).toBe(
      404,
    );
    expect((await fetch(new URL("healthz", url))).status).toBe(200);
  } finally {
    await gateway.close();
    await new Promise<void>((resolve) => worker.close(() => resolve()));
  }
});

it("closes an active event stream before releasing the gateway", async () => {
  const worker = createServer((_request, response) => {
    response.writeHead(200, { "content-type": "text/event-stream" });
    response.write("data: ready\n\n");
  });

  await new Promise<void>((resolve) => worker.listen(0, "127.0.0.1", resolve));
  const address = z.object({ port: z.number() }).parse(worker.address());

  const gateway = createGateway({
    config: loadConfig({
      environment: {},
      userConfig: "/missing/config.json",
      overrides: { server: { port: 0 } },
    }),
    handlePage,
    agentURL: `http://127.0.0.1:${address.port}`,
    token: "private-worker-token",
  });

  try {
    const url = await gateway.listen();
    const response = await fetch(new URL("eve/v1/events", url));
    const reader = response.body!.getReader();
    expect(new TextDecoder().decode((await reader.read()).value)).toBe("data: ready\n\n");
    reader.releaseLock();
    await gateway.close();
    expect(gateway.server.listening).toBe(false);
    await expect(fetch(url)).rejects.toThrow();
    await response.body?.cancel().catch(() => {});
  } finally {
    await gateway.close();
    worker.closeAllConnections();
    await new Promise<void>((resolve) => worker.close(() => resolve()));
  }
});

async function embeddedGateway(
  server: { embedOrigins: string[] },
  secrets: Pick<Parameters<typeof createGateway>[0], "password" | "embedKey"> = {},
) {
  const worker = createServer((request, response) => {
    response.setHeader("content-type", "application/json");
    response.setHeader("access-control-allow-origin", "*");
    response.setHeader("x-eve-stream-version", "1");
    response.end(
      JSON.stringify({ origin: request.headers.origin, site: request.headers["sec-fetch-site"] }),
    );
  });

  await new Promise<void>((resolve) => worker.listen(0, "127.0.0.1", resolve));
  const address = z.object({ port: z.number() }).parse(worker.address());

  const gateway = createGateway({
    config: loadConfig({
      environment: {},
      userConfig: "/missing/config.json",
      overrides: { server: { port: 0, ...server } },
    }),
    handlePage,
    agentURL: `http://127.0.0.1:${address.port}`,
    token: "private-worker-token",
    ...secrets,
  });

  return {
    url: await gateway.listen(),
    async [Symbol.asyncDispose]() {
      await gateway.close();
      await new Promise<void>((resolve) => worker.close(() => resolve()));
    },
  };
}

it("denies framing and cross-site callers unless embedding is configured", async () => {
  await using app = await embeddedGateway({ embedOrigins: [] });
  const page = await fetch(app.url);

  expect(page.headers.get("x-frame-options")).toBe("DENY");
  expect(
    (
      await fetch(app.url, {
        headers: { "sec-fetch-site": "cross-site", "sec-fetch-dest": "iframe" },
      })
    ).status,
  ).toBe(403);
});

it("opens the app from a link on another site but refuses its cross-site calls", async () => {
  await using app = await embeddedGateway({ embedOrigins: [] });

  // fetch() overrides Sec-Fetch-Mode, so these requests set the browser's headers directly.
  const status = (path: string, headers: Record<string, string>) =>
    new Promise<number | undefined>((resolve, reject) => {
      get(new URL(path, app.url), { headers }, (response) => {
        response.resume();
        resolve(response.statusCode);
      }).once("error", reject);
    });

  const crossSite = { "sec-fetch-site": "cross-site" };

  expect(
    await status("/", { ...crossSite, "sec-fetch-mode": "navigate", "sec-fetch-dest": "document" }),
  ).toBe(200);
  expect(
    await status("/", { ...crossSite, "sec-fetch-mode": "navigate", "sec-fetch-dest": "iframe" }),
  ).toBe(403);
  expect(
    await status("/eve/v1/preferences", {
      ...crossSite,
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
    }),
  ).toBe(403);
});

it("lets listed origins frame the app and call its API with credentials", async () => {
  await using app = await embeddedGateway({ embedOrigins: ["https://slides.example"] });

  const page = await fetch(app.url, {
    headers: { "sec-fetch-site": "cross-site", "sec-fetch-dest": "iframe" },
  });

  expect(page.status).toBe(200);
  expect(page.headers.get("content-security-policy")).toBe(
    "frame-ancestors https://slides.example",
  );
  expect(page.headers.get("x-frame-options")).toBeNull();

  const preflight = await fetch(new URL("eve/v1/threads", app.url), {
    method: "OPTIONS",
    headers: {
      origin: "https://slides.example",
      "access-control-request-method": "POST",
      "access-control-request-headers": "content-type",
    },
  });

  expect(preflight.status).toBe(204);
  expect(preflight.headers.get("access-control-allow-origin")).toBe("https://slides.example");
  expect(preflight.headers.get("access-control-allow-headers")).toBe("content-type");

  const response = await fetch(new URL("eve/v1/preferences", app.url), {
    headers: { origin: "https://slides.example", "sec-fetch-site": "cross-site" },
  });

  expect(response.headers.get("access-control-allow-origin")).toBe("https://slides.example");
  expect(response.headers.get("access-control-allow-credentials")).toBe("true");
  expect(response.headers.get("access-control-expose-headers")).toContain("x-eve-stream-version");
  expect(await response.json()).toEqual({ origin: new URL(app.url).origin });
  expect((await fetch(app.url, { headers: { origin: "https://other.example" } })).status).toBe(403);
  expect((await fetch(app.url, { headers: { origin: "null" } })).status).toBe(403);
});

it("opens a password-protected app in sandboxed frames with the embed key", async () => {
  await using app = await embeddedGateway(
    { embedOrigins: ["*"] },
    { password: "private-password", embedKey: "private-embed-key-0123" },
  );

  const framed = { "sec-fetch-site": "cross-site", "sec-fetch-dest": "iframe" };
  const page = await fetch(app.url, { headers: framed });

  expect(page.status).toBe(401);
  expect(page.headers.get("x-frame-options")).toBeNull();
  expect(page.headers.get("content-security-policy")).toBeNull();
  expect(
    (await fetch(new URL("?embed_key=wrong-embed-key-0123", app.url), { headers: framed })).status,
  ).toBe(403);

  const exchange = await fetch(
    new URL("chat/72f8d8e1-340f-40ad-9891-84ef82204029?embed_key=private-embed-key-0123", app.url),
    {
      headers: framed,
      redirect: "manual",
    },
  );

  expect(exchange.status).toBe(303);
  expect(exchange.headers.get("location")).toBe("/chat/72f8d8e1-340f-40ad-9891-84ef82204029");
  const cookie = exchange.headers.get("set-cookie")!;

  expect(cookie).toContain("HttpOnly; SameSite=None; Secure; Partitioned");
  expect(cookie).not.toContain("private-embed-key-0123");
  const access = { cookie: cookie.split(";")[0] };

  expect(await (await fetch(app.url, { headers: { ...framed, ...access } })).text()).toContain(
    "chartcoach",
  );

  const api = await fetch(new URL("eve/v1/preferences", app.url), {
    headers: { origin: "null", "sec-fetch-site": "cross-site", ...access },
  });

  expect(api.headers.get("access-control-allow-origin")).toBe("null");
  expect(await api.json()).toEqual({ origin: new URL(app.url).origin });
  expect(
    (await fetch(new URL("eve/v1/preferences", app.url), { headers: { origin: "null" } })).status,
  ).toBe(401);

  const engine = await fetch(new URL("duckdb/duckdb-eh.wasm", app.url), {
    headers: { origin: "null", "sec-fetch-site": "cross-site" },
  });

  expect(engine.status).toBe(200);
  expect(engine.headers.get("access-control-allow-origin")).toBe("null");
});

it("preserves origin variation when the page renderer replaces Vary", async () => {
  const gateway = createGateway({
    config: loadConfig({
      environment: {},
      userConfig: "/missing/config.json",
      overrides: {
        server: { port: 0, embedOrigins: ["https://slides.example", "https://docs.example"] },
      },
    }),
    handlePage: async (_request, response) => {
      response.setHeader("vary", "rsc, Accept-Encoding");
      response.writeHead(200, { vary: "rsc, next-router-state-tree, Accept-Encoding" });
      response.end("chartcoach");
    },
    agentURL: "http://127.0.0.1:1",
    token: "private-worker-token",
  });

  try {
    const url = await gateway.listen();

    for (const origin of [undefined, "https://slides.example", "https://docs.example"]) {
      const response = await fetch(url, { headers: origin ? { origin } : {} });
      expect(response.headers.get("vary")?.toLowerCase().split(", ")).toEqual([
        "rsc",
        "next-router-state-tree",
        "accept-encoding",
        "origin",
      ]);
      expect(response.headers.get("access-control-allow-origin")).toBe(origin ?? null);
    }
  } finally {
    await gateway.close();
  }
});
