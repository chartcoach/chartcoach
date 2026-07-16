import type { AstroIntegration, HookParameters } from "astro";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";

import { afterEach, describe, expect, it, vi } from "vite-plus/test";

import { llms } from "../../src/integrations/llms";

const temporaryDirectories: string[] = [];

afterEach(async () => {
  await Promise.all(
    temporaryDirectories.splice(0).map((directory) =>
      fs.rm(directory, {
        force: true,
        recursive: true,
      }),
    ),
  );
});

describe("llms", () => {
  it("writes the index, summaries, full text, and page Markdown", async () => {
    const { dist, root } = await createBuild();
    await fs.mkdir(path.join(dist, "rendered"), { recursive: true });
    await fs.writeFile(
      path.join(dist, "rendered", "index.html"),
      [
        "<!doctype html>",
        '<html><head><meta name="description" content="Rendered description."></head>',
        "<body><main><header>Navigation</header><h1>Rendered page</h1>",
        "<p>Read <strong>this</strong>.</p><script>ignored()</script></main></body></html>",
      ].join(""),
    );

    const integration = llms({
      site: "https://example.com/",
      title: "Example docs",
      description: "Example documentation.",
      pages: [
        {
          pathname: "/guide/",
          title: "Guide",
          description: "Guide description.",
          markdown: "# Guide\n\nUse the guide.",
        },
        "/rendered/",
      ],
    });

    await runBuild(integration, root, dist);

    await expect(fs.readFile(path.join(dist, "llms.txt"), "utf-8")).resolves.toBe(
      [
        "# Example docs",
        "> Example documentation.",
        "",
        "This file helps language models discover the most relevant content on this site.",
        "",
        "## Pages",
        "",
        "- [Guide](guide.md): Guide description.",
        "- [Rendered page](rendered.md): Rendered description.",
        "",
      ].join("\n"),
    );
    await expect(fs.readFile(path.join(dist, "llms-small.txt"), "utf-8")).resolves.toContain(
      "## Rendered page\nhttps://example.com/rendered/\n> Rendered description.",
    );
    await expect(fs.readFile(path.join(dist, "llms-full.txt"), "utf-8")).resolves.toContain(
      "Markdown: https://example.com/rendered.md\n\n> Rendered description.\n\n# Rendered page\n\nRead **this**.",
    );
    await expect(fs.readFile(path.join(dist, "rendered.md"), "utf-8")).resolves.toBe(
      [
        "---",
        'title: "Rendered page"',
        'url: "https://example.com/rendered/"',
        'description: "Rendered description."',
        "---",
        "",
        "# Rendered page",
        "",
        "Read **this**.",
        "",
      ].join("\n"),
    );
  });

  it("supports custom output paths and disabling generated files", async () => {
    const { dist, root } = await createBuild();
    const integration = llms({
      name: "example:llms",
      site: "https://example.com/",
      title: "Example docs",
      description: "Example documentation.",
      pages: [{ pathname: "/guide/", title: "Guide", markdown: "# Guide" }],
      output: {
        files: {
          index: "/agents.txt",
          small: false,
          full: false,
        },
        pageMarkdown: false,
      },
    });

    expect(integration.name).toBe("example:llms");
    await runBuild(integration, root, dist);

    await expect(fs.readFile(path.join(dist, "agents.txt"), "utf-8")).resolves.toContain(
      "- [Guide](guide.md)",
    );
    await expect(fs.stat(path.join(dist, "llms-small.txt"))).rejects.toMatchObject({
      code: "ENOENT",
    });
    await expect(fs.stat(path.join(dist, "llms-full.txt"))).rejects.toMatchObject({
      code: "ENOENT",
    });
    await expect(fs.stat(path.join(dist, "guide.md"))).rejects.toMatchObject({ code: "ENOENT" });
  });
});

async function createBuild() {
  const directory = await fs.mkdtemp(path.join(os.tmpdir(), "astro-llms-"));
  temporaryDirectories.push(directory);
  const root = pathToFileURL(`${path.join(directory, "site")}/`);
  const dist = path.join(directory, "dist");
  await fs.mkdir(dist, { recursive: true });
  return { dist, root };
}

async function runBuild(integration: AstroIntegration, root: URL, dist: string) {
  const configDone = requireHook(integration, "astro:config:done");
  const buildDone = requireHook(integration, "astro:build:done");
  const info = vi.fn();
  const logger = {
    fork: () => ({ info }),
  } as unknown as HookParameters<"astro:build:done">["logger"];

  await configDone({ config: { root } } as HookParameters<"astro:config:done">);
  await buildDone({
    pages: [],
    dir: pathToFileURL(`${dist}/`),
    assets: new Map(),
    logger,
  } as HookParameters<"astro:build:done">);

  expect(info).toHaveBeenCalledOnce();
}

function requireHook<Hook extends keyof AstroIntegration["hooks"]>(
  integration: AstroIntegration,
  name: Hook,
): NonNullable<AstroIntegration["hooks"][Hook]> {
  const hook = integration.hooks[name];
  if (typeof hook !== "function") throw new Error(`Missing ${name} hook.`);
  return hook;
}
