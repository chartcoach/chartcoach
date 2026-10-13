import assert from "node:assert/strict";
import { spawn, spawnSync, type ChildProcess } from "node:child_process";
import { once } from "node:events";
import { setTimeout as delay } from "node:timers/promises";
import { cp, mkdtemp, readFile, rm, writeFile, stat } from "node:fs/promises";
import { createServer, type Server } from "node:http";
import type { AddressInfo } from "node:net";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { parseArgs } from "node:util";
import { chromium, type Browser, type Page, type Route } from "playwright";
import { tracingProbe } from "./tracing-probe.ts";
import { verifyPicker } from "./verify-picker.ts";
import { verifyModelSettings } from "./verify-model-settings.ts";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "../..");

const { positionals, values } = parseArgs({
  allowPositionals: true,
  options: { runner: { type: "string", default: "npx" } },
});

const [chatArchive, catalogArchive, catalogLocation] = positionals;

const runners = {
  npx: ["npx", "--no-install", "chartcoach"],
  bunx: ["bunx", "--no-install", "chartcoach"],
  bun: ["bunx", "--bun", "--no-install", "chartcoach"],
  deno: [
    "deno",
    "x",
    "--no-lock",
    "--node-modules-dir=manual",
    "--ignore-scripts",
    "--no-prompt",
    "-A",
    "chartcoach",
  ],
} as const;

if (!values.runner || !Object.hasOwn(runners, values.runner))
  throw new Error("Choose --runner npx, bunx, bun, or deno.");

// SAFETY: the own-key check restricts the runner to this command table.
const [runner, ...runnerArgs] = runners[values.runner as keyof typeof runners];

if (!chatArchive || !catalogArchive)
  throw new Error(
    "Usage: verify:chat <chat.tgz> <catalog.tgz> [catalog-location] [--runner npx|bunx|bun|deno]",
  );

const directory =
  process.env.CHARTCOACH_TEST_DIRECTORY ?? (await mkdtemp(join(tmpdir(), "chartcoach-installed-")));

const tracing = await tracingProbe(
  await readFile(join(root, "apps/chat/public/examples/bicycle-trips.png")),
);

let child: ChildProcess | undefined;

let runtimeOutput = "";

let browser: Browser | undefined;

let page: Page | undefined;

let model: Server | undefined;

const browserErrors: string[] = [];

let modelURL = "";

type CompletionRequest = { messages: { role: string }[]; stream?: boolean };

const calls: CompletionRequest[] = [];

function run(command: string, args: readonly string[]) {
  const result = spawnSync(command, args, {
    cwd: directory,
    encoding: "utf8",
    env: { ...process.env, NODE_PATH: "", NODE_OPTIONS: "" },
  });

  assert.equal(result.status, 0, result.stderr || result.stdout);

  return result.stdout;
}

async function stop() {
  if (child && child.exitCode === null && child.signalCode === null) {
    const exited = once(child, "exit");
    const pid = child.pid;
    assert.ok(pid);
    process.kill(-pid, "SIGTERM");
    const force = setTimeout(() => process.kill(-pid, "SIGKILL"), 10_000);

    try {
      await exited;
    } finally {
      clearTimeout(force);
    }

    const deadline = Date.now() + 10_000;

    while (
      await stat(join(directory, "data/.lock")).then(
        () => true,
        () => false,
      )
    ) {
      if (Date.now() > deadline)
        throw new Error("The CLI did not release its workspace after shutdown.");
      await delay(50);
    }
  }
}

async function start(environmentOnly = false): Promise<string> {
  const flags = [
    "--catalog",
    catalogLocation ?? "./catalog",
    "--data-dir",
    "./data",
    "--port",
    "0",
    "--provider",
    "compatible",
    "--base-url",
    modelURL,
    "--model",
    "package-test-model",
    "--model-auth",
    "none",
    "--no-open",
  ];

  const environment = {
    ...tracing.environment,
    PATH: process.env.PATH,
    HOME: directory,
    NODE_PATH: "",
    CHARTCOACH_PASSWORD: "package-test-password",
    CHARTCOACH_EMBED_ORIGINS: "*",
    CHARTCOACH_EMBED_KEY: "package-test-embed-key",
    CHARTCOACH_CACHE_DIR: "./cache",
    CHARTCOACH_GUIDELINE_URL_TEMPLATE: "https://guidelines.example/entries/{id}",
  };

  if (environmentOnly) {
    const settings = {
      CHARTCOACH_CATALOG: catalogLocation ?? "./catalog",
      CHARTCOACH_DATA_DIR: "./data",
      CHARTCOACH_CACHE_DIR: "./cache",
      CHARTCOACH_PORT: "0",
      CHARTCOACH_TEXT_PROVIDER: "compatible",
      CHARTCOACH_TEXT_BASE_URL: modelURL,
      CHARTCOACH_TEXT_MODEL: "package-test-model",
      CHARTCOACH_TEXT_AUTH: "none",
      CHARTCOACH_OPEN: "false",
    };

    await writeFile(
      join(directory, ".env"),
      Object.entries(settings)
        .map(([name, value]) => `${name}=${JSON.stringify(value)}`)
        .join("\n") + "\n",
    );
  }

  const launched = spawn(runner, [...runnerArgs, ...(environmentOnly ? [] : flags), "--verbose"], {
    cwd: directory,
    detached: true,
    stdio: ["ignore", "pipe", "pipe"],
    env: environment,
  });

  child = launched;
  let output = "";

  return new Promise<string>((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error(`Startup timed out: ${output}`)), 75_000);

    const inspect = (chunk: Buffer) => {
      output = (output + chunk.toString()).slice(-8192);
      runtimeOutput = (runtimeOutput + chunk.toString()).slice(-16000);
      const url = output.match(/➜\s+(http:\/\/[^\s]+)/)?.[1];

      if (url) {
        clearTimeout(timer);
        resolve(url);
      }
    };

    launched.stderr.on("data", inspect);
    launched.stdout.on("data", inspect);
    launched.once("exit", (code) => {
      clearTimeout(timer);
      reject(new Error(`CLI exited (${code}): ${output}`));
    });
  });
}

try {
  await writeFile(
    join(directory, "package.json"),
    JSON.stringify({
      name: "chartcoach-consumer",
      private: true,
      type: "module",
      dependencies: { "@chartcoach/catalog": `file:${resolve(root, catalogArchive)}` },
      // Preview URLs become available only after verification. Test the retained
      // SDK bytes here; release preparation checks the shipped dependency URL.
      overrides: { "@chartcoach/catalog": "$@chartcoach/catalog" },
    }),
  );
  run("npm", [
    "install",
    "--ignore-scripts",
    "--no-audit",
    "--no-fund",
    resolve(root, chatArchive),
    resolve(root, catalogArchive),
  ]);
  // An installing Next app's configuration must not change ChartCoach's routes.
  await writeFile(
    join(directory, "next.config.mjs"),
    'export default { basePath: "/host-app", output: "export", poweredByHeader: true };\n',
  );
  assert.match(run(runner, [...runnerArgs, "--help"]), /Start the chat app/);

  const version = JSON.parse(
    await readFile(join(directory, "node_modules/chartcoach/package.json"), "utf8"),
  ).version;

  assert.equal(run(runner, [...runnerArgs, "--version"]).trim(), version);
  await cp(join(root, "fixtures/catalog-release"), join(directory, "catalog"), { recursive: true });

  // SAFETY: the URL identifies the Node entry of the SDK installed from the verified tarball.
  const { openCatalog } = (await import(
    pathToFileURL(join(directory, "node_modules/@chartcoach/catalog/dist/node.js")).href
  )) as typeof import("@chartcoach/catalog/node");

  const catalog = await openCatalog(catalogLocation ?? join(directory, "catalog"));
  const first = [...catalog][0];
  assert.ok(first && catalog.release);
  const { id, title } = first;
  model = createServer(async (request, response) => {
    let body = "";

    for await (const chunk of request) body += chunk;

    if (request.url === "/v1/models") {
      response.end(JSON.stringify({ data: [{ id: "package-test-model" }] }));

      return;
    }

    const input: CompletionRequest = JSON.parse(body);
    assert.equal(
      request.headers.authorization,
      undefined,
      "Keyless connections send no credential",
    );
    calls.push(input);

    if (!input.stream) {
      response.setHeader("content-type", "application/json");
      response.end(
        JSON.stringify({
          id: `summary_${calls.length}`,
          object: "chat.completion",
          created: 0,
          model: "package-test-model",
          choices: [
            {
              index: 0,
              message: { role: "assistant", content: "Retain the clear-label recommendation." },
              finish_reason: "stop",
            },
          ],
          usage: {
            prompt_tokens: 1200,
            completion_tokens: 40,
            total_tokens: 1240,
            prompt_tokens_details: { cached_tokens: 200 },
          },
        }),
      );

      return;
    }

    const latestUser = input.messages.findLastIndex((message) => message.role === "user");

    const completed = input.messages
      .slice(latestUser + 1)
      .filter((message) => message.role === "tool").length;

    const action =
      completed === 0
        ? { name: "read_guidelines", arguments: JSON.stringify({ ids: [id] }) }
        : completed === 1
          ? {
              name: "present_answer",
              arguments: JSON.stringify({
                workflow: "discuss",
                status: "answer",
                points: [
                  {
                    primary_guideline_id: id,
                    supporting_guideline_ids: [],
                    assessment: null,
                    context: "This comparison needs readable labels.",
                    recommendation: "Use clear labels for the comparison.",
                  },
                ],
                question: null,
              }),
            }
          : undefined;

    response.writeHead(200, { "content-type": "text/event-stream" });

    const delta = action
      ? {
          role: "assistant",
          tool_calls: [
            { index: 0, id: `call_${calls.length}`, type: "function", function: action },
          ],
        }
      : { role: "assistant", content: "Done." };

    response.write(
      `data: ${JSON.stringify({ id: `completion_${calls.length}`, object: "chat.completion.chunk", created: 0, model: "package-test-model", choices: [{ index: 0, delta, finish_reason: null }] })}\n\n`,
    );
    response.write(
      `data: ${JSON.stringify({ id: `completion_${calls.length}`, choices: [{ index: 0, delta: {}, finish_reason: action ? "tool_calls" : "stop" }], usage: { prompt_tokens: 1200, completion_tokens: 40, total_tokens: 1240, prompt_tokens_details: { cached_tokens: 200 } } })}\n\n`,
    );
    response.end("data: [DONE]\n\n");
  });
  const modelServer = model;
  await new Promise<void>((resolve) => modelServer.listen(0, "127.0.0.1", resolve));
  // SAFETY: the listening server binds a numeric TCP port, which yields AddressInfo.
  const address = model.address() as AddressInfo;
  const modelPort = address.port;

  modelURL = `http://127.0.0.1:${modelPort}/v1`;

  const launchEnvironment = join(directory, "launch.env");
  await writeFile(
    launchEnvironment,
    [
      `CHARTCOACH_CATALOG=${JSON.stringify(catalogLocation ?? "./catalog")}`,
      "CHARTCOACH_CACHE_DIR=./cache",
      "CHARTCOACH_TEXT_PROVIDER=openrouter",
      "CHARTCOACH_TRACING=false",
      "CHARTCOACH_GUIDELINE_URL_TEMPLATE=https://guidelines.example/entries/{id}",
    ].join("\n"),
  );
  const help = run(runner, [...runnerArgs, "chat", "--help"]);
  assert.match(help, /CHARTCOACH_TEXT_PROVIDER/);
  assert.match(help, /openrouter/);

  const diagnostic = JSON.parse(
    run(runner, [...runnerArgs, "doctor", "--env-file", launchEnvironment, "--json"]),
  );

  assert.equal(diagnostic.ok, true);
  assert.equal(diagnostic.catalog.guidelines, catalog.length);
  assert.equal(diagnostic.model.baseURL, "https://openrouter.ai/api/v1");
  assert.equal(diagnostic.guidelines.urlTemplate, "https://guidelines.example/entries/{id}");
  assert.deepEqual(diagnostic.tracing, { enabled: false });

  const remoteEnvironment = join(directory, "remote.env");
  await writeFile(
    remoteEnvironment,
    (await readFile(launchEnvironment, "utf8")) +
      "\n" +
      "CHARTCOACH_EMBEDDING_MODEL=consumer-embedding-model\n" +
      "CHARTCOACH_EMBEDDING_BASE_URL=https://vectors.example/v1\n" +
      "CHARTCOACH_EMBEDDING_DIMENSIONS=4\n" +
      "CHARTCOACH_EMBEDDING_API_KEY_ENV=VECTOR_TOKEN\n" +
      "VECTOR_TOKEN=consumer-private-embedding-key\n",
  );

  const remoteReport = run(runner, [
    ...runnerArgs,
    "doctor",
    "--env-file",
    remoteEnvironment,
    "--json",
  ]);

  const remoteDiagnostic = JSON.parse(remoteReport);

  assert.equal(remoteDiagnostic.ok, true);
  assert.deepEqual(remoteDiagnostic.embedding, {
    model: "consumer-embedding-model",
    baseURL: "https://vectors.example/v1",
    dimensions: 4,
  });
  assert.equal(remoteReport.includes("consumer-private-embedding-key"), false);

  let url = await start();
  assert.match(runtimeOutput, /✓ ChartCoach is ready/);
  assert.equal(runtimeOutput.includes("\u001B["), false, "Redirected CLI output contains no color");
  assert.equal((await fetch(url)).status, 401);
  browser = await chromium.launch({
    headless: true,
    executablePath: process.env.PLAYWRIGHT_EXECUTABLE_PATH,
  });

  const context = await browser.newContext({
    httpCredentials: { username: "chartcoach", password: "package-test-password" },
  });

  const errors = browserErrors;
  context.on("page", (opened) => {
    opened.on("pageerror", (error) => errors.push(error.message));
  });
  await context.route("https://guidelines.example/**", (route) =>
    route.fulfill({ contentType: "text/html", body: "<p>Guideline destination</p>" }),
  );
  page = await context.newPage();
  await page.goto(url);
  assert.equal(new URL(page.url()).pathname, "/");
  assert.equal(new URL(page.url()).search, "");
  const rootResponse = await context.request.get(url);
  assert.equal(rootResponse.headers()["x-powered-by"], undefined);
  assert.equal(await page.getByText("Saved for this browser", { exact: true }).count(), 0);
  await page.getByText("Sent to your AI provider · Tracing on", { exact: true }).waitFor();
  await page
    .getByRole("button", { name: "Sent to your AI provider · Tracing on", exact: true })
    .click();
  await page.getByText("Conversation tracing is enabled", { exact: false }).waitFor();
  await page.getByRole("button", { name: "Close privacy details", exact: true }).click();
  await page.getByRole("button", { name: "Close sidebar", exact: true }).click();
  const mark = page.getByRole("button", { name: "Open sidebar", exact: true });

  const markSize = await mark.locator("span").evaluate((element) => ({
    clientWidth: element.clientWidth,
    scrollWidth: element.scrollWidth,
  }));

  assert.deepEqual(markSize, { clientWidth: 32, scrollWidth: 32 });
  const brandMark = mark.locator("svg[aria-hidden=true]");

  assert.equal(await brandMark.isVisible(), true);

  const lightFill = await brandMark
    .locator("rect")
    .first()
    .evaluate((rect) => getComputedStyle(rect).fill);

  await page.screenshot({
    path: join(root, `.context/chat-package-${values.runner}-sidebar-collapsed.png`),
    fullPage: true,
    animations: "disabled",
  });
  await page.emulateMedia({ colorScheme: "dark" });
  assert.equal(await brandMark.isVisible(), true);

  const darkFill = await brandMark
    .locator("rect")
    .first()
    .evaluate((rect) => getComputedStyle(rect).fill);

  assert.notEqual(
    darkFill,
    lightFill,
    "The compact brand follows the color scheme without fetching another image",
  );
  await page.screenshot({
    path: join(root, `.context/chat-package-${values.runner}-sidebar-collapsed-dark.png`),
    fullPage: true,
    animations: "disabled",
  });
  await page.emulateMedia({ colorScheme: "light" });
  await mark.click();
  await verifyModelSettings(
    page,
    join(root, `.context/chat-package-${values.runner}-model-settings.png`),
    modelURL,
  );
  const choosing = page.waitForEvent("filechooser");
  await page.getByRole("button", { name: "Add chart", exact: true }).click();
  await (await choosing).setFiles(join(root, "apps/chat/public/examples/bicycle-trips.png"));
  await page.getByRole("button", { name: "Remove image", exact: true }).waitFor();
  await page
    .getByRole("textbox", { name: /message|ask|chart/i })
    .first()
    .fill("Discuss clear labels in a comparison.");

  const selected = await verifyPicker(
    page,
    catalog,
    join(root, `.context/chat-package-${values.runner}-picker.png`),
  );

  assert.equal(
    await page
      .getByRole("textbox", { name: /message|ask|chart/i })
      .first()
      .inputValue(),
    "Discuss clear labels in a comparison.",
  );
  const composer = page.getByRole("textbox", { name: /message|ask|chart/i }).first();
  const initialComposer = await composer.elementHandle();

  assert.ok(initialComposer);
  await page.getByRole("button", { name: "Remove image", exact: true }).waitFor();
  await page.getByRole("button", { name: /send/i }).click();
  await page
    .getByText("Use clear labels for the comparison.", { exact: true })
    .waitFor({ timeout: 90_000 });
  assert.equal(
    await composer.evaluate((element, before) => element === before, initialComposer),
    true,
    "Saving the first message preserves the composer element",
  );
  const primaryCitation = page.getByRole("link", { name: `Primary: ${title}`, exact: true });
  await primaryCitation.waitFor();
  assert.equal(
    await primaryCitation.getAttribute("href"),
    `https://guidelines.example/entries/${encodeURIComponent(id)}`,
  );
  assert.deepEqual(await page.locator("article > header > h2").allTextContents(), [
    "You",
    "ChartCoach",
  ]);
  await page.getByText("1 primary · 1 found", { exact: true }).waitFor();
  await page.getByText("Response complete.", { exact: true }).waitFor({ state: "attached" });
  await page.screenshot({
    path: join(root, `.context/chat-package-${values.runner}-desktop.png`),
    fullPage: true,
    animations: "disabled",
  });
  await page.setViewportSize({ width: 390, height: 844 });
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
  await page.screenshot({
    path: join(root, `.context/chat-package-${values.runner}-mobile.png`),
    fullPage: true,
    animations: "disabled",
  });
  assert.ok(calls.length >= 3);
  assert.ok(
    calls.some((call) =>
      JSON.stringify(call.messages).includes(
        `This review is restricted to ${selected.length} eligible guidelines`,
      ),
    ),
    "The server applies the browser's selected scope to the model turn",
  );
  const citationPage = await context.newPage();
  await citationPage.goto(new URL(`/guideline/${encodeURIComponent(id)}`, url).href);
  await citationPage.getByRole("heading", { name: title, exact: true }).waitFor();
  await citationPage.getByRole("heading", { name: "Sources", exact: true }).waitFor();
  await citationPage.close();
  assert.ok(
    calls.some((call) => JSON.stringify(call.messages).includes("image_url")),
    "The model receives the uploaded chart",
  );
  const cookies = await context.cookies();
  const threadPath = new URL(page.url()).pathname;
  assert.match(threadPath, /^\/chat\/[a-f0-9-]{36}$/);
  assert.equal(new URL(page.url()).search, "");

  const saved = await page.evaluate(async (threadId) => {
    return (await fetch(`/eve/v1/threads/${encodeURIComponent(threadId)}`)).json();
  }, threadPath.split("/").at(-1)!);

  assert.equal(saved.guidelines.matchedGuidelines, selected.length);
  assert.equal(saved.guidelines.selection.catalogId, catalog.release.digest);
  assert.equal(saved.guidelines.filters.sourceTypeIds.length, 1);
  await stop();
  url = await start(true);
  // Cookies are host-scoped, so port allocation preserves the signed browser owner.
  await context.addCookies(cookies);
  await page.goto(new URL(threadPath, url).href);
  await page
    .getByText("Use clear labels for the comparison.", { exact: true })
    .waitFor({ timeout: 30_000 });
  await page
    .getByRole("textbox", { name: /message|ask|chart/i })
    .first()
    .fill("Explain the labels again.");
  const resumedTurnURL = new URL(`/eve/v1/session/${saved.sessionId}`, url).href;
  const releaseTurn = Promise.withResolvers<void>();

  const holdTurn = async (route: Route) => {
    if (route.request().method() === "POST") await releaseTurn.promise;
    await route.continue();
  };

  await page.route(resumedTurnURL, holdTurn);

  const resumedRequest = page.waitForRequest(
    (request) => request.url() === resumedTurnURL && request.method() === "POST",
  );

  try {
    await page.getByRole("button", { name: /send/i }).click();
    await resumedRequest;
    await page.getByRole("button", { name: "Open sidebar", exact: true }).click();

    const historyDrawer = page.getByRole("dialog", { name: "Your conversations", exact: true });

    const currentHistory = historyDrawer.getByRole("link", {
      name: "Discuss clear labels in a comparison.",
      exact: true,
    });

    assert.equal(await currentHistory.getAttribute("aria-disabled"), "true");
    // Hover waits for the drawer to settle without requiring the disabled link to be enabled.
    await currentHistory.hover();
    await currentHistory.click({ force: true });
    await historyDrawer.waitFor();
    assert.equal(new URL(page.url()).pathname, threadPath);
    await page.getByRole("button", { name: "Close sidebar", exact: true }).click();
  } finally {
    releaseTurn.resolve();
    await page.unrouteAll({ behavior: "wait" });
  }

  await page
    .getByText("Use clear labels for the comparison.", { exact: true })
    .nth(1)
    .waitFor({ timeout: 90_000 });
  await page.getByRole("button", { name: "Send message", exact: true }).waitFor();
  await page.getByRole("button", { name: "Open sidebar", exact: true }).click();
  await page.getByRole("link", { name: "Guidelines", exact: true }).click();
  await page
    .locator('footer [role="status"][aria-busy="false"]')
    .filter({ hasText: `${selected.length.toLocaleString()} guidelines selected` })
    .waitFor();
  await page
    .getByRole("list", { name: "Matched guideline results" })
    .getByRole("link")
    .first()
    .waitFor();
  assert.equal(await page.getByRole("checkbox", { checked: true }).count(), 1);
  assert.equal(new URL(page.url()).pathname, `${threadPath}/guidelines`);
  assert.equal(new URL(page.url()).search, "");
  await page.reload();
  await page
    .locator('footer [role="status"][aria-busy="false"]')
    .filter({ hasText: `${selected.length.toLocaleString()} guidelines selected` })
    .waitFor();
  await page.getByRole("button", { name: "Back to chat", exact: true }).click();
  await page.waitForURL(new URL(threadPath, url).href);
  await page.getByText("Use clear labels for the comparison.", { exact: true }).nth(1).waitFor();
  await page.goBack();
  await page.waitForURL(new URL(`${threadPath}/guidelines`, url).href);
  await page.getByRole("heading", { name: "Guidelines", exact: true }).waitFor();
  await page.goForward();
  await page.waitForURL(new URL(threadPath, url).href);
  await page.getByText("Use clear labels for the comparison.", { exact: true }).nth(1).waitFor();
  await page.getByRole("button", { name: "Open sidebar", exact: true }).click();
  const renamedTitle = "Readable comparison labels";
  await page
    .getByRole("button", { name: "Options for Discuss clear labels in a comparison.", exact: true })
    .click();
  await page.getByRole("menuitem", { name: "Rename", exact: true }).click();
  await page.getByRole("textbox", { name: "Conversation title", exact: true }).fill(renamedTitle);
  await page.getByRole("button", { name: "Save", exact: true }).click();
  await page.waitForFunction((title) => document.title === `${title} · ChartCoach`, renamedTitle);
  const historyLink = page.getByRole("link", { name: renamedTitle, exact: true });
  assert.equal(await historyLink.getAttribute("href"), threadPath);
  await page.getByRole("link", { name: "New chat", exact: true }).click();
  await page.waitForURL(new URL("/", url).href);
  assert.equal(await page.locator("article > header > h2").count(), 0);
  assert.equal(
    await page
      .getByRole("textbox", { name: /message|ask|chart/i })
      .first()
      .inputValue(),
    "",
  );
  await page.getByRole("button", { name: "Open sidebar", exact: true }).click();
  await page.getByRole("link", { name: renamedTitle, exact: true }).click();
  await page.waitForURL(new URL(threadPath, url).href);
  await page.getByText("Use clear labels for the comparison.", { exact: true }).nth(1).waitFor();
  const draft = "Keep this draft while changing guidelines.";
  await page
    .getByRole("textbox", { name: /message|ask|chart/i })
    .first()
    .fill(draft);
  await page.getByRole("button", { name: "Open sidebar", exact: true }).click();
  await page.getByRole("link", { name: "Guidelines", exact: true }).click();
  await page
    .locator('footer [role="status"][aria-busy="false"]')
    .filter({ hasText: `${selected.length.toLocaleString()} guidelines selected` })
    .waitFor();
  await page.getByRole("button", { name: "Select all", exact: true }).click();
  await page.getByRole("button", { name: "Use these guidelines", exact: true }).click();
  await page.waitForURL(new URL("/", url).href);
  assert.equal(
    await page
      .getByRole("textbox", { name: /message|ask|chart/i })
      .first()
      .inputValue(),
    draft,
  );
  await page.getByRole("button", { name: "Remove image", exact: true }).waitFor();

  const unchangedScope = await page.evaluate(
    async (id) => (await fetch(`/eve/v1/threads/${id}`)).json(),
    saved.id,
  );

  assert.deepEqual(unchangedScope.guidelines, saved.guidelines);

  const unknownPage = await context.newPage();
  const missing = await unknownPage.goto(new URL("/missing-page", url).href);
  assert.equal(missing?.status(), 404);
  await unknownPage.getByRole("heading", { name: "We couldn’t find that page." }).waitFor();
  await unknownPage.getByRole("link", { name: "Back to chat", exact: true }).click();
  await unknownPage.waitForURL(new URL("/", url).href);

  for (const path of [
    "/chat/invalid-id",
    "/chat/c3666202-50b1-449c-ac0c-9d458e936f92",
    "/chat/c3666202-50b1-449c-ac0c-9d458e936f92/guidelines",
  ]) {
    await unknownPage.goto(new URL(path, url).href);
    await unknownPage.waitForURL(new URL("/", url).href);
    await unknownPage
      .getByRole("textbox", { name: /message|ask|chart/i })
      .first()
      .waitFor();
    assert.equal(await unknownPage.locator("article > header > h2").count(), 0);
  }

  await unknownPage.close();

  const otherOwner = await browser.newContext({
    httpCredentials: { username: "chartcoach", password: "package-test-password" },
  });

  const privatePage = await otherOwner.newPage();
  privatePage.on("pageerror", (error) => errors.push(error.message));
  await privatePage.goto(new URL(threadPath, url).href);
  await privatePage.waitForURL(new URL("/", url).href);
  await privatePage
    .getByRole("textbox", { name: /message|ask|chart/i })
    .first()
    .waitFor();
  assert.equal(await privatePage.locator("article > header > h2").count(), 0);

  const privateRead = await privatePage.evaluate(
    async (id) => (await fetch(`/eve/v1/threads/${id}`)).status,
    saved.id,
  );

  assert.equal(privateRead, 404);
  await otherOwner.close();

  const embedURL = new URL(url);
  embedURL.searchParams.set("embed_key", "package-test-embed-key");

  const embedHost = createServer((_request, response) => {
    response.setHeader("content-type", "text/html");
    response.end(
      `<iframe title="ChartCoach" sandbox="allow-scripts allow-forms" style="width:100%;height:900px" src="${embedURL.href}"></iframe>`,
    );
  });

  await new Promise<void>((resolve) => embedHost.listen(0, "127.0.0.1", resolve));
  // SAFETY: the listening server binds a numeric TCP port, which yields AddressInfo.
  const hostAddress = embedHost.address() as AddressInfo;
  const embeddedContext = await browser.newContext();

  try {
    const embeddedPage = await embeddedContext.newPage();
    embeddedPage.on("pageerror", (error) => errors.push(error.message));
    await embeddedPage.goto(`http://localhost:${hostAddress.port}`);
    const embedded = embeddedPage.frameLocator('iframe[title="ChartCoach"]');
    await embedded
      .getByRole("textbox", { name: /message|ask|chart/i })
      .first()
      .fill("Keep my embedded draft.");
    const chooseEmbeddedChart = embeddedPage.waitForEvent("filechooser");
    await embedded.getByRole("button", { name: "Add chart", exact: true }).click();
    await (
      await chooseEmbeddedChart
    ).setFiles(join(root, "apps/chat/public/examples/bicycle-trips.png"));
    await embedded.getByRole("button", { name: "Remove image", exact: true }).waitFor();
    await embedded.getByRole("link", { name: "Guidelines", exact: true }).click();
    await embedded.getByRole("heading", { name: "Guidelines", exact: true }).waitFor();
    await embedded.getByRole("button", { name: "Back to chat", exact: true }).click();
    assert.equal(
      await embedded
        .getByRole("textbox", { name: /message|ask|chart/i })
        .first()
        .inputValue(),
      "Keep my embedded draft.",
    );
    await embedded.getByRole("button", { name: "Remove image", exact: true }).waitFor();
  } finally {
    await embeddedContext.close();
    embedHost.closeAllConnections();
    await new Promise<void>((resolve) => embedHost.close(() => resolve()));
  }

  assert.equal(errors.length, 0, errors.join("\n"));
  assert.ok(selected.includes(id));
  assert.ok(saved.sessionId);
  await page.evaluate(async (sessionId: string) => {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 30_000);

    try {
      const path = `/eve/v1/session/${encodeURIComponent(sessionId)}`;
      const stream = await fetch(`${path}/stream?startIndex=-1`, { signal: controller.signal });

      if (!stream.ok || !stream.body) throw new Error(`Compaction stream failed: ${stream.status}`);
      const compact = await fetch(`${path}/compact`, { method: "POST", signal: controller.signal });
      const result = await compact.json();

      if (!compact.ok || result.status !== "accepted")
        throw new Error(`Compaction request failed: ${compact.status} ${result.status}`);
      const reader = stream.body.getReader();
      const decoder = new TextDecoder();
      let text = "";

      for (;;) {
        const { done, value } = await reader.read();

        if (done) throw new Error("Compaction stream ended before completion.");
        text = (text + decoder.decode(value, { stream: true })).slice(-16_000);
        const completed = text.indexOf("compaction.completed");

        if (completed >= 0 && text.slice(completed).includes("session.waiting")) return;
      }
    } finally {
      clearTimeout(timeout);
      controller.abort();
    }
  }, saved.sessionId);
  await stop();
  tracing.verify();
  console.log(
    `Verified ${values.runner} startup through flags and environment, authenticated UI, native catalog loading, browser picker filtering and scope, chart upload, grounded answer, local citations, narrow layout, and restart persistence.`,
  );
} catch (error) {
  if (page) {
    console.error(`Browser URL: ${page.url()}`);
    console.error(`Browser errors: ${browserErrors.join("\n")}`);
    console.error(
      (
        await page
          .locator("body")
          .innerText()
          .catch(() => "")
      ).slice(-6000),
    );
    await page
      .screenshot({
        path: join(root, `.context/chat-package-${values.runner}-failure.png`),
        fullPage: true,
        timeout: 5000,
      })
      .catch(() => {});
  }

  console.error(`Model requests: ${calls.length}`);
  console.error(runtimeOutput);
  throw error;
} finally {
  try {
    await browser?.close();
  } finally {
    try {
      await stop();
    } finally {
      try {
        await tracing.close();

        if (model) {
          model.closeAllConnections();
          const modelServer = model;
          await new Promise<void>((resolve) => modelServer.close(() => resolve()));
        }
      } finally {
        if (process.env.CHARTCOACH_KEEP_TEST_DATA) console.log(`Consumer: ${directory}`);
        else await rm(directory, { recursive: true, force: true });
      }
    }
  }
}
