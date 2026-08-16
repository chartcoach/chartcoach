import {
  create as createOramaDb,
  insertMultiple as insertDocuments,
  save as saveOramaDb,
  type AnySchema,
} from "@orama/orama";
import type { AstroIntegration, HookParameters } from "astro";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

type BuildDoneOptions = HookParameters<"astro:build:done">;
type ServerSetupOptions = HookParameters<"astro:server:setup">;
type AstroPage = BuildDoneOptions["pages"][number];
type MaybePromise<T> = T | PromiseLike<T>;
type SearchMiddleware = (
  request: { url?: string },
  response: {
    statusCode: number;
    setHeader(name: string, value: string): void;
    end(value: string): void;
  },
  next: () => void,
) => Promise<void>;
type SearchDevServer = {
  watcher: {
    add(paths: string[]): void;
    on(event: "change", listener: (path: string) => void): void;
  };
  middlewares: {
    use(handler: SearchMiddleware): void;
  };
};
type SearchConfigDoneOptions = {
  config: { root: URL };
};
type SearchServerSetupOptions = {
  server: SearchDevServer;
  logger: ServerSetupOptions["logger"];
};
type SearchBuildDoneOptions = {
  pages: AstroPage[];
  dir: URL;
  logger: BuildDoneOptions["logger"];
};

export type SearchIndexDatabase = {
  schema: AnySchema;
  language?: string;
  include(pathname: string): boolean;
};

export type SearchIndexDocuments<Document extends object> = {
  load(context: { root: URL }): MaybePromise<readonly Document[]>;
  fromPage(context: { html: string; pathname: string }): MaybePromise<Document>;
  path(document: Document): string;
  watchFiles?(context: { root: URL }): readonly string[];
};

export type SearchIndexOptions<Document extends object> = {
  name?: string;
  databases: Record<string, SearchIndexDatabase>;
  documents: SearchIndexDocuments<Document>;
};

function pagePath(pathname: string) {
  return `/${pathname.replace(/^\/+/, "").replace(/\/?$/, "/")}`;
}

function generatedHtmlPath(dir: URL, pathname: string) {
  const cleanPathname = pathname.replace(/^\/+/, "").replace(/\/+$/, "");
  const relativePath = cleanPathname ? `${cleanPathname}/index.html` : "index.html";
  return fileURLToPath(new URL(relativePath, dir));
}

async function serializeDatabase<Document extends object>(
  config: SearchIndexDatabase,
  documents: readonly Document[],
) {
  const language = config.language ?? "english";
  const db = createOramaDb({ schema: config.schema, language });

  await Promise.resolve(insertDocuments(db, [...documents], undefined, language));

  return JSON.stringify(saveOramaDb(db));
}

async function loadPageDocuments<Document extends object>(
  config: SearchIndexDatabase,
  pages: AstroPage[],
  dir: URL,
  documents: SearchIndexDocuments<Document>,
  logger: BuildDoneOptions["logger"],
) {
  const indexed: Document[] = [];

  for (const page of pages) {
    const pathname = pagePath(page.pathname);
    if (!config.include(pathname)) continue;

    const filePath = generatedHtmlPath(dir, page.pathname);
    if (!existsSync(filePath)) {
      logger.warn(`Skipping missing search index source: ${filePath}`);
      continue;
    }

    indexed.push(
      await documents.fromPage({
        html: readFileSync(filePath, "utf8"),
        pathname,
      }),
    );
  }

  return indexed;
}

function requestedDatabase(requestUrl: string | undefined, names: string[]) {
  if (!requestUrl) return undefined;
  const pathname = new URL(requestUrl, "http://localhost").pathname;
  return names.find((name) => pathname.endsWith(`/assets/search-${name}.json`));
}

export function searchIndex<Document extends object>(options: SearchIndexOptions<Document>) {
  const integrationName = options.name ?? "chartcoach:search-index";
  let root: URL | undefined;
  const devDatabases = new Map<string, Promise<string>>();

  function devDatabase(
    name: string,
    config: SearchIndexDatabase,
    logger: ServerSetupOptions["logger"],
  ) {
    if (!root) throw new Error("Astro config root is unavailable.");

    const cached = devDatabases.get(name);
    if (cached) return cached;

    const serialized = Promise.resolve(options.documents.load({ root }))
      .then((loaded) =>
        loaded.filter((document) => config.include(options.documents.path(document))),
      )
      .then(async (documents) => {
        const json = await serializeDatabase(config, documents);
        logger
          .fork(integrationName)
          .info(
            `Prepared ${name} dev search DB with ${documents.length.toLocaleString()} entries.`,
          );
        return json;
      })
      .catch((cause: unknown) => {
        devDatabases.delete(name);
        throw cause;
      });

    devDatabases.set(name, serialized);
    return serialized;
  }

  return {
    name: integrationName,
    hooks: {
      "astro:config:done": ({ config }: SearchConfigDoneOptions) => {
        root = config.root;
      },
      "astro:server:setup": ({ server, logger }: SearchServerSetupOptions) => {
        if (root && options.documents.watchFiles) {
          const watchedFiles = [...options.documents.watchFiles({ root })];
          if (watchedFiles.length > 0) {
            server.watcher.add(watchedFiles);
            server.watcher.on("change", (changedPath) => {
              if (watchedFiles.includes(changedPath)) devDatabases.clear();
            });
          }
        }

        server.middlewares.use(async (request, response, next) => {
          const name = requestedDatabase(request.url, Object.keys(options.databases));
          const config = name ? options.databases[name] : undefined;
          if (!name || !config) {
            next();
            return;
          }

          try {
            const json = await devDatabase(name, config, logger);
            response.statusCode = 200;
            response.setHeader("Content-Type", "application/json; charset=utf-8");
            response.end(json);
          } catch (error) {
            logger
              .fork(integrationName)
              .error(error instanceof Error ? error.message : "Failed to prepare dev search DB.");
            response.statusCode = 500;
            response.setHeader("Content-Type", "application/json; charset=utf-8");
            response.end(JSON.stringify({ error: "Search index failed to load." }));
          }
        });
      },
      "astro:build:done": async ({ pages, dir, logger }: SearchBuildDoneOptions) => {
        const searchLogger = logger.fork(integrationName);
        const assetsDir = fileURLToPath(new URL("assets/", dir));
        if (!existsSync(assetsDir)) mkdirSync(assetsDir, { recursive: true });

        await Promise.all(
          Object.entries(options.databases).map(async ([name, config]) => {
            const documents = await loadPageDocuments(
              config,
              pages,
              dir,
              options.documents,
              searchLogger,
            );
            const outputPath = path.join(assetsDir, `search-${name}.json`);
            writeFileSync(outputPath, await serializeDatabase(config, documents), "utf8");
            searchLogger.info(
              `Wrote ${name} search DB with ${documents.length.toLocaleString()} entries.`,
            );
          }),
        );
      },
    },
  } satisfies AstroIntegration;
}
