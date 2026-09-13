import { defineChannel, GET } from "eve/channels";
import { routeAuth } from "eve/channels/auth";
import { getCatalogMetadata } from "../../lib/catalog/metadata";
import { getCatalog } from "../../lib/catalog/open";
import { catalogRouteAuth } from "../auth";

export default defineChannel({
  routes: [
    GET("/eve/v1/guidelines/:id", async (request) => {
      const auth = await routeAuth(request, catalogRouteAuth);

      if (auth instanceof Response) return auth;
      const id = decodeURIComponent(new URL(request.url).pathname.split("/").at(-1)!);
      const catalog = await getCatalog();
      const guideline = catalog.get(id);

      if (!guideline)
        return Response.json(
          { error: "This guideline is not in the selected catalog." },
          { status: 404 },
        );

      return Response.json(
        {
          ...guideline,
          sources: catalog.cite({ ids: [id] })[0]!.sources,
          release: catalog.release?.digest ?? null,
        },
        { headers: { "cache-control": "no-store" } },
      );
    }),
    GET("/eve/v1/catalog/:digest/:file", async (request) => {
      const auth = await routeAuth(request, catalogRouteAuth);

      if (auth instanceof Response) return auth;
      const parts = new URL(request.url).pathname.split("/");
      const file = parts.at(-1);
      const digest = parts.at(-2);

      if (!file || !["release.json", "entries.parquet", "MANIFEST.md"].includes(file))
        return new Response("Catalog file not found.", { status: 404 });
      const catalog = await getCatalog();

      if (!catalog.release || catalog.release.digest !== digest)
        return new Response("The catalog changed. Reload the catalog.", { status: 409 });

      if (file === "release.json")
        return Response.json(catalog.release, {
          headers: { "cache-control": "private, no-cache" },
        });
      const bytes = await catalog.artifact(file, { signal: request.signal });

      return new Response(Uint8Array.from(bytes), {
        headers: {
          "content-type":
            file === "MANIFEST.md" ? "text/markdown; charset=utf-8" : "application/octet-stream",
          "content-length": String(bytes.byteLength),
          "cache-control": "private, max-age=31536000, immutable",
          etag: `"${catalog.release.artifacts[file]!.sha256}"`,
        },
      });
    }),
    GET("/eve/v1/catalog", async (request) => {
      const auth = await routeAuth(request, catalogRouteAuth);

      if (auth instanceof Response) return auth;

      return Response.json(await getCatalogMetadata(undefined, request.signal), {
        headers: { "cache-control": "no-store" },
      });
    }),
  ],
});
