import { count, create, load, search as query } from "zbsearch";
import { afterEach, describe, expect, it, vi } from "vite-plus/test";
import { mkdtempSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";

import { searchIndex } from "../../src/integrations/search-index";
import { createTestLogger } from "../astro";

type Document = { path: string; title: string };
type TestResponse = {
  statusCode: number;
  setHeader(name: string, value: string): void;
  end(value: string): void;
};
type TestMiddleware = (
  request: { url?: string },
  response: TestResponse,
  next: () => void,
) => Promise<void>;

const temporaryDirectories: string[] = [];

afterEach(() => {
  for (const directory of temporaryDirectories.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

function temporaryDirectory() {
  const directory = mkdtempSync(path.join(os.tmpdir(), "chartcoach-search-index-"));
  temporaryDirectories.push(directory);
  return directory;
}

function integration(documents: {
  load: () => readonly Document[];
  watchFiles?: () => readonly string[];
}) {
  return searchIndex<Document>({
    name: "test:search",
    databases: {
      guidelines: {
        schema: { path: "string", title: "string" },
        include: (pathname) => pathname.startsWith("/guidelines/"),
      },
    },
    documents: {
      load: documents.load,
      fromPage: ({ html, pathname }) => ({ path: pathname, title: html }),
      path: (document) => document.path,
      watchFiles: documents.watchFiles,
    },
  });
}

describe("searchIndex", () => {
  it("writes a database from matching generated pages", async () => {
    const output = temporaryDirectory();
    const pageDirectory = path.join(output, "guidelines", "axes");
    mkdirSync(pageDirectory, { recursive: true });
    writeFileSync(path.join(pageDirectory, "index.html"), "Use full axes", "utf8");
    const search = integration({ load: () => [] });
    const build = search.hooks["astro:build:done"];
    const { logger } = createTestLogger();

    await build({
      dir: pathToFileURL(`${output}/`),
      logger,
      pages: [{ pathname: "guidelines/axes" }, { pathname: "about" }],
    });

    const raw = JSON.parse(
      readFileSync(path.join(output, "assets", "search-guidelines.json"), "utf8"),
    );
    const db = create({ schema: { path: "string", title: "string" } });
    load(db, raw);
    expect(count(db)).toBe(1);
    const results = await query(db, { term: "axes" });
    expect(results.hits.map((hit) => hit.document)).toEqual([
      { path: "/guidelines/axes/", title: "Use full axes" },
    ]);
  });

  it("serves and invalidates the development database when a source changes", async () => {
    const root = pathToFileURL(`${temporaryDirectory()}/`);
    const watchFile = path.join(temporaryDirectory(), "entries.parquet");
    const loadDocuments = vi
      .fn<() => readonly Document[]>()
      .mockReturnValue([{ path: "/guidelines/axes/", title: "Use full axes" }]);
    const search = integration({
      load: loadDocuments,
      watchFiles: () => [watchFile],
    });
    const configDone = search.hooks["astro:config:done"];
    const serverSetup = search.hooks["astro:server:setup"];
    const changeListeners: Array<(path: string) => void> = [];
    let middleware: TestMiddleware | undefined;
    const server = {
      watcher: {
        add: vi.fn(),
        on: vi.fn((event: string, listener: (path: string) => void) => {
          if (event === "change") changeListeners.push(listener);
        }),
      },
      middlewares: {
        use: vi.fn((handler: TestMiddleware) => {
          middleware = handler;
        }),
      },
    };

    const { logger } = createTestLogger();
    configDone({ config: { root } });
    serverSetup({ server, logger });
    expect(server.watcher.add).toHaveBeenCalledWith([watchFile]);

    async function request() {
      let body = "";
      const response = {
        statusCode: 0,
        setHeader: vi.fn(),
        end: vi.fn((value: string) => {
          body = value;
        }),
      };
      await middleware?.({ url: "/assets/search-guidelines.json" }, response, vi.fn());
      return { body, response };
    }

    expect((await request()).response.statusCode).toBe(200);
    expect((await request()).response.statusCode).toBe(200);
    expect(loadDocuments).toHaveBeenCalledTimes(1);

    changeListeners[0]?.(watchFile);
    const refreshed = await request();
    expect(refreshed.response.statusCode).toBe(200);
    const db = create({ schema: { path: "string", title: "string" } });
    load(db, JSON.parse(refreshed.body));
    expect(count(db)).toBe(1);
    expect(loadDocuments).toHaveBeenCalledTimes(2);
  });
});
