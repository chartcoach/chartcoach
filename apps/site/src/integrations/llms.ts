import type { AstroIntegration, HookParameters } from "astro";
import { JSDOM, VirtualConsole } from "jsdom";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import TurndownService from "turndown";

type BuildDoneOptions = HookParameters<"astro:build:done">;
type ServerSetupOptions = HookParameters<"astro:server:setup">;
type AstroPage = BuildDoneOptions["pages"][number];
type MaybePromise<T> = T | Promise<T>;
type LlmConfigDoneOptions = {
  config: { root: URL };
};
type LlmBuildDoneOptions = {
  pages: AstroPage[];
  dir: URL;
  logger: BuildDoneOptions["logger"];
};

export type LlmFileKind = "index" | "small" | "full";

export type LlmPageEntry = {
  pathname: string;
  title: string;
  description?: string;
  markdown: string;
  markdownPathname: string;
};

export type LlmPageSource = {
  pathname: string;
  title?: string;
  description?: string;
  markdown?: string;
  markdownPathname?: string;
  writeMarkdown?: boolean;
};

export type LlmPageSourceContext = {
  pages?: readonly AstroPage[];
  root: URL;
};

export type LlmsIntegrationOptions = {
  site: string | URL;
  title: string;
  description: string;
  name?: string;
  loadPages?: (context: LlmPageSourceContext) => MaybePromise<readonly LlmPageSource[]>;
  includePage?: (pathname: string) => boolean;
  content?: {
    selector?: string;
    titleSelector?: string;
    removeSelectors?: readonly string[];
  };
  output?: {
    files?: Partial<Record<LlmFileKind, string | false>>;
    pageMarkdown?:
      | false
      | {
          include?: (entry: LlmPageEntry, source: LlmPageSource) => boolean;
          pathname?: (entry: LlmPageEntry, source: LlmPageSource) => string;
        };
  };
};

const LLM_FILE_KINDS = ["index", "small", "full"] as const;
const DEFAULT_FILE_PATHNAMES = {
  index: "/llms.txt",
  small: "/llms-small.txt",
  full: "/llms-full.txt",
} satisfies Record<LlmFileKind, string>;
const PAGE_SEPARATOR = "\n\n---\n\n";
const defaultRemoveSelectors = ["script", "style", "header", "footer"];
const jsdomVirtualConsole = new VirtualConsole();

function createTurndown() {
  return new TurndownService({
    bulletListMarker: "-",
    codeBlockStyle: "fenced",
    headingStyle: "atx",
  });
}

function normalizePagePathname(pathname: string) {
  const clean = pathname.trim() || "/";
  const withLeadingSlash = clean.startsWith("/") ? clean : `/${clean}`;
  if (withLeadingSlash === "/") return "/";
  if (path.extname(withLeadingSlash)) return withLeadingSlash;
  return withLeadingSlash.replace(/\/?$/, "/");
}

function normalizeFilePathname(pathname: string) {
  const clean = pathname.trim();
  const withLeadingSlash = clean.startsWith("/") ? clean : `/${clean}`;
  return withLeadingSlash.replace(/\/+$/, "");
}

function isHtmlPagePathname(pathname: string) {
  return !path.extname(normalizePagePathname(pathname));
}

function pageUrl(site: string | URL, pathname: string) {
  return new URL(normalizePagePathname(pathname).replace(/^\//, ""), site).toString();
}

function fileUrl(site: string | URL, pathname: string) {
  return new URL(normalizeFilePathname(pathname).replace(/^\//, ""), site).toString();
}

function relativeFilePathname(pathname: string) {
  return normalizeFilePathname(pathname).replace(/^\/+/, "");
}

function defaultMarkdownPathname(pathname: string) {
  const normalized = normalizePagePathname(pathname);
  if (normalized === "/") return "/index.md";
  return `/${normalized.replace(/^\/+/, "").replace(/\/+$/, "")}.md`;
}

function pageHtmlOutputPath(distDir: string, pathname: string) {
  const normalized = normalizePagePathname(pathname);
  const cleanPathname = normalized.replace(/^\/+/, "").replace(/\/+$/, "");
  const relativePath = cleanPathname ? `${cleanPathname}/index.html` : "index.html";
  return path.join(distDir, relativePath);
}

function fileOutputPath(distDir: string, pathname: string) {
  return path.join(distDir, normalizeFilePathname(pathname).replace(/^\/+/, ""));
}

function normalizePageSource(source: LlmPageSource): LlmPageSource {
  return {
    ...source,
    pathname: normalizePagePathname(source.pathname),
    markdownPathname: source.markdownPathname
      ? normalizeFilePathname(source.markdownPathname)
      : undefined,
  };
}

function sourceMarkdownPathname(
  entry: LlmPageEntry,
  source: LlmPageSource,
  options: LlmsIntegrationOptions,
) {
  if (options.output?.pageMarkdown && options.output.pageMarkdown.pathname) {
    return normalizeFilePathname(options.output.pageMarkdown.pathname(entry, source));
  }
  return source.markdownPathname ?? defaultMarkdownPathname(source.pathname);
}

function shouldWritePageMarkdown(
  entry: LlmPageEntry,
  source: LlmPageSource,
  options: LlmsIntegrationOptions,
) {
  if (source.writeMarkdown !== undefined) return source.writeMarkdown;
  const pageMarkdown = options.output?.pageMarkdown;
  if (pageMarkdown === false) return false;
  if (pageMarkdown?.include) return pageMarkdown.include(entry, source);
  return true;
}

function llmFilePathnames(options: LlmsIntegrationOptions) {
  const files = options.output?.files ?? {};
  return LLM_FILE_KINDS.map((kind) => {
    const pathname = files[kind] ?? DEFAULT_FILE_PATHNAMES[kind];
    return pathname === false ? null : ([kind, normalizeFilePathname(pathname)] as const);
  }).filter((value): value is readonly [LlmFileKind, string] => Boolean(value));
}

async function resolveSources(
  options: LlmsIntegrationOptions,
  context: LlmPageSourceContext,
): Promise<LlmPageSource[]> {
  const sourceInput = options.loadPages ? await options.loadPages(context) : undefined;

  if (sourceInput) {
    return sourceInput
      .map(normalizePageSource)
      .sort((a, b) => a.pathname.localeCompare(b.pathname));
  }

  const includePage = options.includePage ?? isHtmlPagePathname;
  const sources: LlmPageSource[] = [];

  for (const page of context.pages ?? []) {
    if (!includePage(page.pathname)) continue;
    sources.push(normalizePageSource({ pathname: page.pathname }));
  }

  return sources.sort((a, b) => a.pathname.localeCompare(b.pathname));
}

function extractEntryFromHtml(
  source: LlmPageSource,
  html: string,
  turndown: TurndownService,
  options: LlmsIntegrationOptions,
): LlmPageEntry | null {
  const dom = new JSDOM(html, { virtualConsole: jsdomVirtualConsole });
  const document = dom.window.document;
  const selector = options.content?.selector ?? "main";
  const content = document.querySelector(selector);
  if (!content) return null;

  const removeSelectors = options.content?.removeSelectors ?? defaultRemoveSelectors;
  if (removeSelectors.length > 0) {
    content.querySelectorAll(removeSelectors.join(", ")).forEach((node) => {
      node.remove();
    });
  }

  const titleSelector = options.content?.titleSelector ?? "h1";
  const title =
    source.title ??
    content.querySelector(titleSelector)?.textContent?.trim() ??
    document.querySelector("title")?.textContent?.trim() ??
    source.pathname;
  const description =
    source.description ??
    document.querySelector('meta[name="description"]')?.getAttribute("content")?.trim() ??
    undefined;
  const markdown = turndown.turndown(content.innerHTML).trim();
  const entry = {
    pathname: source.pathname,
    title,
    description,
    markdown,
    markdownPathname: source.markdownPathname ?? defaultMarkdownPathname(source.pathname),
  };

  return {
    ...entry,
    markdownPathname: sourceMarkdownPathname(entry, source, options),
  };
}

async function entryFromSource(
  source: LlmPageSource,
  turndown: TurndownService,
  options: LlmsIntegrationOptions,
  readHtml: (pathname: string) => Promise<string>,
) {
  if (source.markdown !== undefined) {
    const entry = {
      pathname: source.pathname,
      title: source.title ?? source.pathname,
      description: source.description,
      markdown: source.markdown.trim(),
      markdownPathname: source.markdownPathname ?? defaultMarkdownPathname(source.pathname),
    };
    return {
      ...entry,
      markdownPathname: sourceMarkdownPathname(entry, source, options),
    };
  }

  return extractEntryFromHtml(source, await readHtml(source.pathname), turndown, options);
}

function buildLlmFile(
  kind: LlmFileKind,
  entries: readonly LlmPageEntry[],
  options: LlmsIntegrationOptions,
) {
  switch (kind) {
    case "index":
      return buildIndex(entries, options);
    case "small":
      return buildSmall(entries, options);
    case "full":
      return buildFull(entries, options);
  }
}

function buildIndex(entries: readonly LlmPageEntry[], options: LlmsIntegrationOptions) {
  const lines = [
    `# ${options.title}`,
    `> ${options.description}`,
    "",
    "This file helps language models discover the most relevant content on this site.",
    "",
    "## Pages",
    "",
    ...entries.map((entry) => {
      const suffix = entry.description ? `: ${entry.description}` : "";
      return `- [${entry.title}](${relativeFilePathname(entry.markdownPathname)})${suffix}`;
    }),
  ];
  return `${lines.join("\n").trim()}\n`;
}

function buildSmall(entries: readonly LlmPageEntry[], options: LlmsIntegrationOptions) {
  const lines = [
    `# ${options.title}`,
    `> ${options.description}`,
    "",
    ...entries.flatMap((entry) => [
      `## ${entry.title}`,
      pageUrl(options.site, entry.pathname),
      entry.description ? `> ${entry.description}` : "",
      "",
    ]),
  ];

  return `${lines
    .filter((line, index, all) => line || all[index - 1])
    .join("\n")
    .trim()}\n`;
}

function buildFull(entries: readonly LlmPageEntry[], options: LlmsIntegrationOptions) {
  const content = entries
    .map((entry) => {
      const parts = [
        `# ${entry.title}`,
        `URL: ${pageUrl(options.site, entry.pathname)}`,
        `Markdown: ${fileUrl(options.site, entry.markdownPathname)}`,
        entry.description ? `> ${entry.description}` : "",
        entry.markdown,
      ];
      return parts.filter(Boolean).join("\n\n");
    })
    .join(PAGE_SEPARATOR);

  return `# ${options.title}\n\n> ${options.description}\n\n${content}\n`;
}

function serializePageMarkdown(entry: LlmPageEntry, options: LlmsIntegrationOptions) {
  const frontmatter = [
    "---",
    `title: ${JSON.stringify(entry.title)}`,
    `url: ${JSON.stringify(pageUrl(options.site, entry.pathname))}`,
    entry.description ? `description: ${JSON.stringify(entry.description)}` : undefined,
    "---",
  ]
    .filter(Boolean)
    .join("\n");

  return `${frontmatter}\n\n${entry.markdown.trim()}\n`;
}

async function writePageMarkdown(
  distDir: string,
  entry: LlmPageEntry,
  options: LlmsIntegrationOptions,
) {
  const outputPath = fileOutputPath(distDir, entry.markdownPathname);
  await fs.mkdir(path.dirname(outputPath), { recursive: true });
  await fs.writeFile(outputPath, serializePageMarkdown(entry, options), "utf-8");
}

function devOrigin(server: ServerSetupOptions["server"]) {
  const localUrl = server.resolvedUrls?.local[0];
  if (localUrl) return localUrl;

  const port = server.config.server.port ?? 4321;
  return `http://localhost:${port}/`;
}

async function buildEntries(
  sources: readonly LlmPageSource[],
  turndown: TurndownService,
  options: LlmsIntegrationOptions,
  readHtml: (pathname: string) => Promise<string>,
) {
  const entries = await Promise.all(
    sources.map((source) => entryFromSource(source, turndown, options, readHtml)),
  );

  return entries
    .filter((entry): entry is LlmPageEntry => Boolean(entry))
    .sort((a, b) => a.pathname.localeCompare(b.pathname));
}

function requestPathname(requestUrl: string | undefined) {
  return new URL(requestUrl ?? "/", "http://localhost").pathname;
}

export function llms(options: LlmsIntegrationOptions) {
  let root: URL | undefined;
  const integrationName = options.name ?? "astro-llms";

  return {
    name: integrationName,
    hooks: {
      "astro:config:done": ({ config }: LlmConfigDoneOptions) => {
        root = config.root;
      },
      "astro:server:setup": ({ server, logger }: ServerSetupOptions) => {
        server.middlewares.use((request, response, next) => {
          const rootUrl = root;
          const pathname = requestPathname(request.url);
          const llmFile = llmFilePathnames(options).find(
            ([, filePathname]) => filePathname === pathname,
          );
          const wantsMarkdown = pathname.endsWith(".md");
          if (!rootUrl || (!llmFile && !wantsMarkdown)) {
            next();
            return;
          }

          const llmLogger = logger.fork(integrationName);
          const origin = devOrigin(server);
          const turndown = createTurndown();

          void (async () => {
            const sources = await resolveSources(options, { root: rootUrl });
            const entries = await buildEntries(sources, turndown, options, async (pagePathname) => {
              const response = await fetch(new URL(pagePathname.replace(/^\//, ""), origin));
              if (!response.ok) {
                throw new Error(
                  `Failed to render '${pagePathname}' for LLM output: ${response.status} ${response.statusText}`,
                );
              }
              return response.text();
            });

            if (llmFile) {
              const [kind] = llmFile;
              response.statusCode = 200;
              response.setHeader("Content-Type", "text/plain; charset=utf-8");
              response.end(buildLlmFile(kind, entries, options));
              return;
            }

            const entry = entries.find((candidate) => candidate.markdownPathname === pathname);
            const source = sources.find((candidate) => candidate.pathname === entry?.pathname);
            if (!entry || !source || !shouldWritePageMarkdown(entry, source, options)) {
              next();
              return;
            }

            response.statusCode = 200;
            response.setHeader("Content-Type", "text/markdown; charset=utf-8");
            response.end(serializePageMarkdown(entry, options));
          })().catch((cause: unknown) => {
            const message = cause instanceof Error ? cause.message : String(cause);
            llmLogger.error(`Failed to generate '${pathname}' in dev: ${message}`);
            response.statusCode = 500;
            response.setHeader("Content-Type", "text/plain; charset=utf-8");
            response.end(message);
          });
        });
      },
      "astro:build:done": async ({ pages, dir, logger }: LlmBuildDoneOptions) => {
        if (!root) throw new Error("Astro config root is unavailable.");

        const distDir = fileURLToPath(dir);
        const llmLogger = logger.fork(integrationName);
        const sources = await resolveSources(options, { pages, root });
        const turndown = createTurndown();
        const entries = await buildEntries(sources, turndown, options, async (pathname) =>
          fs.readFile(pageHtmlOutputPath(distDir, pathname), "utf-8"),
        );
        const sourceByPathname = new Map(sources.map((source) => [source.pathname, source]));

        await Promise.all([
          ...llmFilePathnames(options).map(([kind, pathname]) =>
            fs.writeFile(
              fileOutputPath(distDir, pathname),
              buildLlmFile(kind, entries, options),
              "utf-8",
            ),
          ),
          ...entries.map((entry) => {
            const source = sourceByPathname.get(entry.pathname);
            if (!source || !shouldWritePageMarkdown(entry, source, options))
              return Promise.resolve();
            return writePageMarkdown(distDir, entry, options);
          }),
        ]);

        llmLogger.info(
          `Generated ${llmFilePathnames(options)
            .map(([, pathname]) => pathname.replace(/^\//, ""))
            .join(", ")} from ${entries.length.toLocaleString()} page(s).`,
        );
      },
    },
  } satisfies AstroIntegration;
}
