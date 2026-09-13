import { createServer, get } from "node:http";
import { mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { z } from "zod";
import { expect, it } from "vite-plus/test";
import { createGateway } from "../runtime/gateway";
import { loadConfig } from "../runtime/config";

it("protects assets and streams authenticated requests through the same origin", async () => {
  const directory = await mkdtemp(join(tmpdir(), "chartcoach-gateway-"));
  await writeFile(join(directory, "index.html"), "<h1>ChartCoach</h1>");

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
    assets: directory,
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

    expect(await (await fetch(url, { headers })).text()).toContain("ChartCoach");
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
    await rm(directory, { recursive: true, force: true });
  }
});
