import { createHash, timingSafeEqual } from "node:crypto";
import { createServer, type IncomingMessage } from "node:http";
import { ProxyServer } from "http-proxy-3";
import sirv from "sirv";
import { z } from "zod";
import type { Config } from "./schema";

function equal(left: string, right: string) {
  return timingSafeEqual(
    createHash("sha256").update(left).digest(),
    createHash("sha256").update(right).digest(),
  );
}

function requestAllowed(
  request: Pick<IncomingMessage, "headers">,
  origin: URL,
  password?: string,
  username = "chartcoach",
) {
  if (request.headers.host !== origin.host) return 403;

  if (request.headers["sec-fetch-site"] === "cross-site") return 403;

  if (request.headers.origin && request.headers.origin !== origin.origin) return 403;

  if (password) {
    const authorization = request.headers.authorization ?? "";
    const expected = `Basic ${Buffer.from(`${username}:${password}`, "utf8").toString("base64")}`;

    if (!equal(authorization, expected)) return 401;
  }

  return undefined;
}

export function createGateway({
  config,
  assets,
  agentURL,
  token,
  password,
}: {
  config: Config;
  assets: string;
  agentURL: string;
  token: string;
  password?: string;
}) {
  const proxy = new ProxyServer({ target: agentURL, changeOrigin: false });
  const files = sirv(assets, { etag: true, maxAge: 0, single: false });
  let publicURL: URL;

  const server = createServer((request, response) => {
    if (request.url === "/healthz" && (request.method === "GET" || request.method === "HEAD")) {
      response.writeHead(200, { "content-type": "application/json", "cache-control": "no-store" });
      response.end('{"ok":true}');

      return;
    }

    const denied = requestAllowed(request, publicURL, password, config.server.username);

    if (denied) {
      response.setHeader("cache-control", "no-store");

      if (denied === 401)
        response.setHeader("www-authenticate", 'Basic realm="ChartCoach", charset="UTF-8"');
      response.writeHead(denied);
      response.end(
        denied === 401 ? "Sign in to ChartCoach." : "Open ChartCoach at its configured URL.",
      );

      return;
    }

    response.setHeader("x-content-type-options", "nosniff");
    response.setHeader("referrer-policy", "same-origin");
    response.setHeader("x-frame-options", "DENY");
    const pathname = new URL(request.url ?? "/", publicURL).pathname;

    if (pathname.startsWith("/eve/")) {
      // The worker trusts this credential and the public origin supplied by this gateway.
      for (const name of Object.keys(request.headers)) {
        if (
          name.startsWith("x-forwarded-") ||
          name.startsWith("x-chartcoach-runtime") ||
          name === "forwarded"
        )
          delete request.headers[name];
      }

      request.headers.authorization = `Basic ${Buffer.from(`chartcoach:${token}`).toString("base64")}`;
      request.headers["x-forwarded-host"] = publicURL.host;
      request.headers["x-forwarded-proto"] = publicURL.protocol.slice(0, -1);
      proxy.web(request, response, {}, () => {
        if (response.headersSent) {
          response.destroy();

          return;
        }

        response.writeHead(502, { "content-type": "application/json" });
        response.end('{"error":"The chat runtime is unavailable. Restart ChartCoach."}');
      });

      return;
    }

    if (request.method !== "GET" && request.method !== "HEAD") {
      response.writeHead(405);
      response.end();

      return;
    }

    files(request, response, () => {
      response.writeHead(404);
      response.end("Page not found.");
    });
  });

  return {
    server,
    async listen() {
      await new Promise<void>((resolve, reject) => {
        server.once("error", reject);
        server.listen(config.server.port, config.server.host, () => {
          server.off("error", reject);
          resolve();
        });
      });
      const address = z.object({ port: z.number() }).parse(server.address());
      const host = config.server.host.includes(":") ? "[::1]" : "127.0.0.1";
      publicURL = new URL(config.server.publicURL ?? `http://${host}:${address.port}`);

      return publicURL.href;
    },
    async close() {
      const closed = new Promise<void>((resolve) => server.close(() => resolve()));
      server.closeAllConnections();
      proxy.close();
      await closed;
    },
  };
}
