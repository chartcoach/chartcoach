import { createHash, timingSafeEqual } from "node:crypto";
import { createServer, type IncomingMessage, type ServerResponse } from "node:http";
import type { Socket } from "node:net";
import { ProxyServer } from "http-proxy-3";
import { z } from "zod";
import type { Config } from "./schema";

const accessCookie = "chartcoach_embed";

function equal(left: string, right: string) {
  return timingSafeEqual(
    createHash("sha256").update(left).digest(),
    createHash("sha256").update(right).digest(),
  );
}

function cookie(request: Pick<IncomingMessage, "headers">, name: string) {
  return request.headers.cookie
    ?.split(";")
    .map((value) => value.trim())
    .find((value) => value.startsWith(`${name}=`))
    ?.slice(name.length + 1);
}

/** Pages that may frame chartcoach and call it from inside that frame. */
function embedding(origins: string[]) {
  const any = origins.includes("*");

  return {
    enabled: origins.length > 0,
    any,
    // A sandboxed frame has an opaque origin, which browsers send as `null`.
    admits: (origin: string | undefined) =>
      origin !== undefined && (any || origins.includes(origin)),
    // Browsers match no frame-ancestors source against an opaque ancestor, so `*` sends none.
    framing: any
      ? {}
      : origins.length > 0
        ? { "content-security-policy": `frame-ancestors ${origins.join(" ")}` }
        : { "x-frame-options": "DENY" },
  };
}

type Embedding = ReturnType<typeof embedding>;

function requestAllowed(
  request: Pick<IncomingMessage, "headers" | "method">,
  origin: URL,
  embed: Embedding,
  admitted: boolean,
) {
  if (request.headers.host !== origin.host) return 403;

  const framed = embed.enabled && request.headers["sec-fetch-dest"] === "iframe";

  // A link from another site opens the app in its own tab. Cross-site frames and
  // API calls stay limited to embedding origins.
  const opened =
    request.headers["sec-fetch-mode"] === "navigate" &&
    request.headers["sec-fetch-dest"] === "document" &&
    (request.method === "GET" || request.method === "HEAD");

  if (
    request.headers["sec-fetch-site"] === "cross-site" &&
    !embed.any &&
    !framed &&
    !admitted &&
    !opened
  )
    return 403;

  if (request.headers.origin && request.headers.origin !== origin.origin && !admitted) return 403;

  return undefined;
}

function signedIn(
  request: Pick<IncomingMessage, "headers">,
  password: string,
  username: string,
  access?: string,
) {
  const expected = `Basic ${Buffer.from(`${username}:${password}`, "utf8").toString("base64")}`;
  const presented = cookie(request, accessCookie);

  return (
    equal(request.headers.authorization ?? "", expected) ||
    (access !== undefined && presented !== undefined && equal(presented, access))
  );
}

/** Versioned build files that sandboxed frames request without cookies, such as fonts. */
function buildAsset(pathname: string) {
  return pathname.startsWith("/_next/static/") || pathname.startsWith("/duckdb/");
}

export function createGateway({
  config,
  handlePage,
  agentURL,
  token,
  password,
  embedKey,
}: {
  config: Config;
  handlePage: (request: IncomingMessage, response: ServerResponse) => Promise<void>;
  agentURL: string;
  token: string;
  password?: string;
  embedKey?: string;
}) {
  const proxy = new ProxyServer({ target: agentURL, changeOrigin: false });
  const embed = embedding(config.server.embedOrigins);
  const access = embedKey ? createHash("sha256").update(embedKey).digest("hex") : undefined;
  const sockets = new Set<Socket>();
  let publicURL: URL;

  proxy.on("proxyRes", (proxyResponse, _request, response) => {
    if (!response.hasHeader("access-control-allow-origin")) return;
    // The gateway owns CORS for embedded callers. A credentialed response also hides
    // headers it does not name, such as Eve's stream version.
    delete proxyResponse.headers["access-control-allow-origin"];
    delete proxyResponse.headers["access-control-allow-credentials"];
    proxyResponse.headers["access-control-expose-headers"] = Object.keys(
      proxyResponse.headers,
    ).join(", ");
  });

  const server = createServer((request, response) => {
    if (request.url === "/healthz" && (request.method === "GET" || request.method === "HEAD")) {
      response.writeHead(200, { "content-type": "application/json", "cache-control": "no-store" });
      response.end('{"ok":true}');

      return;
    }

    const url = new URL(request.url ?? "/", publicURL);
    const origin = request.headers.origin;
    const admitted = origin !== publicURL.origin && embed.admits(origin);

    if (requestAllowed(request, publicURL, embed, admitted)) {
      response.writeHead(403, { "cache-control": "no-store" });
      response.end("Open chartcoach at its configured URL.");

      return;
    }

    if (embed.enabled) {
      // Next and proxied responses supply their own Vary fields. Preserve Origin
      // for both direct and embedded requests so shared caches separate them.
      const setHeader = response.setHeader.bind(response);
      response.setHeader = (name, value) => {
        if (name.toLowerCase() === "vary") {
          const text = Array.isArray(value) ? value.join(", ") : String(value);
          const fields = text.split(",").map((field) => field.trim().toLowerCase());

          if (!fields.includes("*") && !fields.includes("origin")) value = `${text}, origin`;
        }

        return setHeader(name, value);
      };

      response.setHeader("vary", "origin");
    }

    if (admitted) {
      response.setHeader("access-control-allow-origin", origin!);
      response.setHeader("access-control-allow-credentials", "true");

      // Preflights never carry credentials, so they are answered before sign-in.
      if (request.method === "OPTIONS" && request.headers["access-control-request-method"]) {
        response.writeHead(204, {
          "access-control-allow-methods": request.headers["access-control-request-method"],
          "access-control-allow-headers": request.headers["access-control-request-headers"] ?? "",
          "access-control-max-age": "600",
        });
        response.end();

        return;
      }
    }

    const offered = url.searchParams.get("embed_key");

    if (embedKey && access && offered !== null) {
      if (!equal(offered, embedKey)) {
        response.writeHead(403, { "cache-control": "no-store" });
        response.end("This embed key is not valid.");

        return;
      }

      url.searchParams.delete("embed_key");
      response.writeHead(303, {
        location: `${url.pathname}${url.search}`,
        "set-cookie": `${accessCookie}=${access}; Path=/; HttpOnly; SameSite=None; Secure; Partitioned`,
        "cache-control": "no-store",
      });
      response.end();

      return;
    }

    if (
      password &&
      !(embed.any && buildAsset(url.pathname)) &&
      !signedIn(request, password, config.server.username, access)
    ) {
      response.writeHead(401, {
        "cache-control": "no-store",
        "www-authenticate": 'Basic realm="chartcoach", charset="UTF-8"',
      });
      response.end("Sign in to chartcoach.");

      return;
    }

    response.setHeader("x-content-type-options", "nosniff");
    response.setHeader("referrer-policy", "same-origin");

    for (const [name, value] of Object.entries(embed.framing)) response.setHeader(name, value);
    const { pathname } = url;

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

      // The worker accepts same-origin calls only. The gateway has admitted this caller.
      if (admitted) {
        request.headers.origin = publicURL.origin;
        delete request.headers["sec-fetch-site"];
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
        response.end('{"error":"The chat runtime is unavailable. Restart chartcoach."}');
      });

      return;
    }

    if (request.method !== "GET" && request.method !== "HEAD") {
      response.writeHead(405);
      response.end();

      return;
    }

    // Next owns page routing, RSC navigation, public files, and real 404 responses.
    // Workflow callbacks are private even when Next receives an unknown path.
    if (pathname.startsWith("/.well-known/workflow/")) {
      response.writeHead(404);
      response.end("Page not found.");

      return;
    }

    void handlePage(request, response).catch(() => {
      if (response.headersSent) {
        response.destroy();

        return;
      }

      response.writeHead(500, { "cache-control": "no-store" });
      response.end("Could not open this page. Try again.");
    });
  });

  server.on("connection", (socket) => {
    sockets.add(socket);
    socket.once("close", () => sockets.delete(socket));
  });

  return {
    server,
    async listen(port = config.server.port) {
      await new Promise<void>((resolve, reject) => {
        const ready = () => {
          server.off("error", failed);
          resolve();
        };

        const failed = (error: Error) => {
          server.off("listening", ready);
          reject(error);
        };

        server.once("error", failed);
        server.once("listening", ready);
        server.listen(port, config.server.host);
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

      // Bun can retain proxy event streams after closeAllConnections.
      for (const socket of sockets) socket.destroy();
      await closed;
    },
  };
}
