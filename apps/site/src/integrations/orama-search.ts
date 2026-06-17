import {
  create as createOramaDB,
  insertMultiple as insertMultipleIntoOramaDB,
  save as saveOramaDB,
} from "@orama/orama";
import type { AstroIntegration, HookParameters } from "astro";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { DEFAULT_CATALOG_METADATA_URL } from "@chartcoach/catalog";
import { readCatalog } from "@chartcoach/catalog/server";

import {
  createGuidelineSearchDocument,
  createGuidelineSearchModel,
  GUIDELINE_SEARCH_SCHEMA,
  parseGuidelineSearchModel,
} from "../lib/guideline-search-model";

type BuildDoneOptions = HookParameters<"astro:build:done">;
type ConfigDoneOptions = HookParameters<"astro:config:done">;
type ServerSetupOptions = HookParameters<"astro:server:setup">;
type AstroPage = BuildDoneOptions["pages"][number];

type OramaSearchDbOptions = {
  language?: string;
  pathMatcher: RegExp;
};
type OramaSearchOptions = Record<string, OramaSearchDbOptions>;
type SearchDocument = ReturnType<typeof createGuidelineSearchDocument>;

const searchRecordScriptPattern =
  /<script\b(?=[^>]*\bdata-guideline-search-record\b)[^>]*>([\s\S]*?)<\/script>/i;

function generatedHtmlPath(dir: URL, pathname: string) {
  const cleanPathname = pathname.replace(/^\/+/, "").replace(/\/+$/, "");
  const relativePath = cleanPathname ? `${cleanPathname}/index.html` : "index.html";
  return fileURLToPath(new URL(relativePath, dir));
}

function documentPath(pathname: string) {
  return `/${pathname.replace(/^\/+/, "").replace(/\/?$/, "/")}`;
}

function readGuidelineSearchDocument(filePath: string, pathname: string) {
  const htmlContent = readFileSync(filePath, { encoding: "utf8" });
  const match = searchRecordScriptPattern.exec(htmlContent);
  if (!match?.[1]) {
    throw new Error(`Missing structured guideline search record in ${filePath}.`);
  }

  const model = parseGuidelineSearchModel(match[1]);
  return createGuidelineSearchDocument(model, documentPath(pathname));
}

async function prepareOramaDbFromDocuments(
  dbConfig: OramaSearchDbOptions,
  documents: SearchDocument[],
) {
  const language = dbConfig.language || "english";
  const db = createOramaDB({ schema: GUIDELINE_SEARCH_SCHEMA, language });

  await Promise.resolve(insertMultipleIntoOramaDB(db, documents, undefined, language));

  return { db, indexedRecords: documents.length };
}

async function prepareOramaDbFromPages(
  dbConfig: OramaSearchDbOptions,
  pages: AstroPage[],
  dir: URL,
  logger: BuildDoneOptions["logger"],
) {
  const documents = [];

  for (const page of pages) {
    if (!dbConfig.pathMatcher.test(page.pathname)) continue;

    const filePath = generatedHtmlPath(dir, page.pathname);
    if (!existsSync(filePath)) {
      logger.warn(`Skipping missing search index source: ${filePath}`);
      continue;
    }

    documents.push(readGuidelineSearchDocument(filePath, page.pathname));
  }

  return prepareOramaDbFromDocuments(dbConfig, documents);
}

async function prepareOramaDbFromCatalog(
  dbConfig: OramaSearchDbOptions,
  root: URL,
) {
  const catalogSource = resolveCatalogSource(root);
  const catalog = await readCatalog(catalogSource);
  const documents: SearchDocument[] = [];

  for (const guideline of catalog) {
    const document = createGuidelineSearchDocument(createGuidelineSearchModel(guideline));
    if (dbConfig.pathMatcher.test(document.path)) documents.push(document);
  }

  return prepareOramaDbFromDocuments(dbConfig, documents);
}

function resolveCatalogSource(root: URL) {
  const source = process.env.CHARTCOACH_SITE_CATALOG_SOURCE ?? DEFAULT_CATALOG_METADATA_URL;
  return isHttpUrl(source) ? source : path.resolve(fileURLToPath(root), source);
}

function isHttpUrl(value: string): boolean {
  return value.startsWith("http://") || value.startsWith("https://");
}

function requestDbName(requestUrl: string | undefined, dbNames: string[]) {
  if (!requestUrl) return undefined;
  const pathname = new URL(requestUrl, "http://localhost").pathname;
  return dbNames.find((dbName) => pathname.endsWith(`/assets/oramaDB_${dbName}.json`));
}

function watchCatalogSource(root: URL, server: ServerSetupOptions["server"], onChange: () => void) {
  const catalogSource = resolveCatalogSource(root);
  if (isHttpUrl(catalogSource)) return;

  const watchedFiles = [
    path.join(catalogSource, "entries.parquet"),
    path.join(catalogSource, "MANIFEST.md"),
  ];
  server.watcher.add(watchedFiles);
  server.watcher.on("change", (changedPath) => {
    if (watchedFiles.includes(changedPath)) onChange();
  });
}

export function oramaSearch(options: OramaSearchOptions): AstroIntegration {
  let root: URL | undefined;
  const devDbCache = new Map<string, Promise<string>>();

  function getDevDbJson(
    dbName: string,
    dbConfig: OramaSearchDbOptions,
    logger: ServerSetupOptions["logger"],
  ) {
    if (!root) throw new Error("Astro config root is unavailable.");

    const cached = devDbCache.get(dbName);
    if (cached) return cached;

    const dbJson = prepareOramaDbFromCatalog(dbConfig, root)
      .then(({ db, indexedRecords }) => {
        logger
          .fork("chartcoach:orama-search")
          .info(`Prepared ${dbName} dev search DB with ${indexedRecords.toLocaleString()} records.`);
        return JSON.stringify(saveOramaDB(db));
      })
      .catch((error: unknown) => {
        devDbCache.delete(dbName);
        throw error;
      });

    devDbCache.set(dbName, dbJson);
    return dbJson;
  }

  return {
    name: "chartcoach:orama-search",
    hooks: {
      "astro:config:done": ({ config }: ConfigDoneOptions) => {
        root = config.root;
      },
      "astro:server:setup": ({ server, logger }: ServerSetupOptions) => {
        if (root) {
          watchCatalogSource(root, server, () => devDbCache.clear());
        }

        server.middlewares.use(async (request, response, next) => {
          const dbName = requestDbName(request.url, Object.keys(options));
          if (!dbName) {
            next();
            return;
          }

          const dbConfig = options[dbName];
          if (!dbConfig) {
            next();
            return;
          }

          try {
            const dbJson = await getDevDbJson(dbName, dbConfig, logger);
            response.statusCode = 200;
            response.setHeader("Content-Type", "application/json; charset=utf-8");
            response.end(dbJson);
          } catch (error) {
            logger
              .fork("chartcoach:orama-search")
              .error(error instanceof Error ? error.message : "Failed to prepare dev search DB.");
            response.statusCode = 500;
            response.setHeader("Content-Type", "application/json; charset=utf-8");
            response.end(JSON.stringify({ error: "Search index failed to load." }));
          }
        });
      },
      "astro:build:done": async ({ pages, dir, logger }) => {
        const searchLogger = logger.fork("chartcoach:orama-search");
        const assetsDir = fileURLToPath(new URL("assets/", dir));
        if (!existsSync(assetsDir)) mkdirSync(assetsDir, { recursive: true });

        await Promise.all(
          Object.entries(options).map(async ([dbName, dbConfig]) => {
            const { db, indexedRecords } = await prepareOramaDbFromPages(
              dbConfig,
              pages,
              dir,
              searchLogger,
            );
            const outputPath = path.join(assetsDir, `oramaDB_${dbName}.json`);
            writeFileSync(outputPath, JSON.stringify(saveOramaDB(db)), { encoding: "utf8" });
            searchLogger.info(
              `Wrote ${dbName} search DB with ${indexedRecords.toLocaleString()} records.`,
            );
          }),
        );
      },
    },
  };
}
