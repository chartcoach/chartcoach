import assert from "node:assert/strict";
import { spawn, spawnSync } from "node:child_process";
import { once } from "node:events";
import { setTimeout as delay } from "node:timers/promises";
import { cp, mkdtemp, readFile, rm, writeFile, stat } from "node:fs/promises";
import { createServer } from "node:http";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright";
import { verifyPicker } from "./verify-picker.mjs";
import { verifyModelSettings } from "./verify-model-settings.mjs";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "../..");

const [chatArchive, catalogArchive, catalogLocation] = process.argv.slice(2);

if (!chatArchive || !catalogArchive)
  throw new Error("Usage: verify:chat <chat.tgz> <catalog.tgz> [catalog-location]");

const directory =
  process.env.CHARTCOACH_TEST_DIRECTORY ?? (await mkdtemp(join(tmpdir(), "chartcoach-installed-")));

let child;

let runtimeOutput = "";

let browser;

let page;

let model;

let modelURL;

const calls = [];

function run(command, args) {
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
    process.kill(-child.pid, "SIGTERM");
    const force = setTimeout(() => process.kill(-child.pid, "SIGKILL"), 10_000);

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

async function start(environmentOnly = false) {
  const flags = [
    "--catalog",
    catalogLocation ?? "./catalog",
    "--data-dir",
    "./data",
    "--cache-dir",
    "./cache",
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
    PATH: process.env.PATH,
    HOME: directory,
    NODE_PATH: "",
    CHARTCOACH_PASSWORD: "package-test-password",
  };

  if (environmentOnly)
    Object.assign(environment, {
      CHARTCOACH_CATALOG: catalogLocation ?? "./catalog",
      CHARTCOACH_DATA_DIR: "./data",
      CHARTCOACH_CACHE_DIR: "./cache",
      CHARTCOACH_PORT: "0",
      CHARTCOACH_PROVIDER: "compatible",
      CHARTCOACH_BASE_URL: modelURL,
      CHARTCOACH_MODEL: "package-test-model",
      CHARTCOACH_MODEL_AUTH: "none",
      CHARTCOACH_OPEN: "false",
    });
  child = spawn(
    "npx",
    ["--no-install", "chartcoach", ...(environmentOnly ? [] : flags), "--verbose"],
    {
      cwd: directory,
      detached: true,
      stdio: ["ignore", "pipe", "pipe"],
      env: environment,
    },
  );
  let output = "";

  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error(`Startup timed out: ${output}`)), 75_000);

    const inspect = (chunk) => {
      output = (output + chunk.toString()).slice(-8192);
      runtimeOutput = (runtimeOutput + chunk.toString()).slice(-16000);
      const url = output.match(/➜\s+(http:\/\/[^\s]+)/)?.[1];

      if (url) {
        clearTimeout(timer);
        resolve(url);
      }
    };

    child.stderr.on("data", inspect);
    child.stdout.on("data", inspect);
    child.once("exit", (code) => {
      clearTimeout(timer);
      reject(new Error(`CLI exited (${code}): ${output}`));
    });
  });
}

try {
  await writeFile(
    join(directory, "package.json"),
    '{"name":"chartcoach-consumer","private":true,"type":"module"}',
  );
  run("npm", [
    "install",
    "--ignore-scripts",
    "--no-audit",
    "--no-fund",
    resolve(root, chatArchive),
    resolve(root, catalogArchive),
  ]);
  assert.match(run("npx", ["--no-install", "chartcoach", "--help"]), /Start the chat app/);

  const version = JSON.parse(
    await readFile(join(directory, "node_modules/chartcoach/package.json"), "utf8"),
  ).version;

  assert.equal(run("npx", ["--no-install", "chartcoach", "--version"]).trim(), version);
  await cp(join(root, "fixtures/catalog-release"), join(directory, "catalog"), { recursive: true });

  const { openCatalog } = await import(
    new URL(`file://${directory}/node_modules/@chartcoach/catalog/dist/node.js`)
  );

  const catalog = await openCatalog(catalogLocation ?? join(directory, "catalog"));
  const id = [...catalog][0].id;
  const title = [...catalog][0].title;
  model = createServer(async (request, response) => {
    let body = "";

    for await (const chunk of request) body += chunk;

    if (request.url === "/v1/models") {
      response.end(JSON.stringify({ data: [{ id: "package-test-model" }] }));

      return;
    }

    const input = JSON.parse(body);
    assert.equal(
      request.headers.authorization,
      undefined,
      "Keyless connections send no credential",
    );
    calls.push(input);
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
          tool_calls: [{ index: 0, id: `call_${completed}`, type: "function", function: action }],
        }
      : { role: "assistant", content: "Done." };

    response.write(
      `data: ${JSON.stringify({ id: `completion_${calls.length}`, object: "chat.completion.chunk", created: 0, model: "package-test-model", choices: [{ index: 0, delta, finish_reason: null }] })}\n\n`,
    );
    response.write(
      `data: ${JSON.stringify({ id: `completion_${calls.length}`, choices: [{ index: 0, delta: {}, finish_reason: action ? "tool_calls" : "stop" }] })}\n\n`,
    );
    response.end("data: [DONE]\n\n");
  });
  await new Promise((resolve) => model.listen(0, "127.0.0.1", resolve));
  const modelPort = model.address().port;

  modelURL = `http://127.0.0.1:${modelPort}/v1`;

  const diagnostic = JSON.parse(
    run("npx", [
      "--no-install",
      "chartcoach",
      "doctor",
      "--catalog",
      catalogLocation ?? "./catalog",
      "--cache-dir",
      "./cache",
      "--json",
    ]),
  );

  assert.equal(diagnostic.ok, true);
  assert.equal(diagnostic.catalog.guidelines, catalog.length);
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

  const errors = [];
  context.on("page", (opened) => opened.on("pageerror", (error) => errors.push(error.message)));
  page = await context.newPage();
  await page.goto(url);
  assert.equal(await page.getByText("Saved for this browser", { exact: true }).count(), 0);
  assert.equal(
    await page.getByText("Conversation tracing is enabled", { exact: false }).count(),
    0,
  );
  await page.getByRole("button", { name: "Close sidebar", exact: true }).click();
  const mark = page.getByRole("button", { name: "Open sidebar", exact: true });

  const markSize = await mark.locator("span").evaluate((element) => ({
    clientWidth: element.clientWidth,
    scrollWidth: element.scrollWidth,
  }));

  assert.deepEqual(markSize, { clientWidth: 32, scrollWidth: 32 });
  assert.equal(await mark.locator("img").count(), 2);
  assert.equal(
    await mark
      .locator("img")
      .evaluateAll((images) =>
        images.some((image) => image.getAttribute("src")?.includes("chartcoach-horizontal")),
      ),
    false,
  );
  await page.screenshot({
    path: join(root, ".context/chat-package-sidebar-collapsed.png"),
    fullPage: true,
    animations: "disabled",
  });
  await page.emulateMedia({ colorScheme: "dark" });
  const darkMark = mark.locator("img:visible");

  assert.equal(await darkMark.count(), 1);
  assert.match(await darkMark.getAttribute("src"), /chartcoach-mark-white/);
  await page.screenshot({
    path: join(root, ".context/chat-package-sidebar-collapsed-dark.png"),
    fullPage: true,
    animations: "disabled",
  });
  await page.emulateMedia({ colorScheme: "light" });
  await mark.click();
  await verifyModelSettings(page, join(root, ".context/chat-package-model-settings.png"), modelURL);
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
    join(root, ".context/chat-package-picker.png"),
  );

  assert.equal(
    await page
      .getByRole("textbox", { name: /message|ask|chart/i })
      .first()
      .inputValue(),
    "Discuss clear labels in a comparison.",
  );
  await page.getByRole("button", { name: "Remove image", exact: true }).waitFor();
  await page.getByRole("button", { name: /send/i }).click();
  await page
    .getByText("Use clear labels for the comparison.", { exact: true })
    .waitFor({ timeout: 90_000 });
  await page.getByRole("link", { name: `Primary: ${title}`, exact: true }).waitFor();
  assert.deepEqual(await page.locator("article > header > h2").allTextContents(), [
    "You",
    "ChartCoach",
  ]);
  await page.getByText("1 primary · 1 found", { exact: true }).waitFor();
  await page.getByText("Response complete.", { exact: true }).waitFor({ state: "attached" });
  await page.screenshot({
    path: join(root, ".context/chat-package-desktop.png"),
    fullPage: true,
    animations: "disabled",
  });
  await page.setViewportSize({ width: 390, height: 844 });
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
  await page.screenshot({
    path: join(root, ".context/chat-package-mobile.png"),
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
  await citationPage.goto(new URL(`/guideline?id=${encodeURIComponent(id)}`, url).href);
  await citationPage.getByRole("heading", { name: title, exact: true }).waitFor();
  await citationPage.getByRole("heading", { name: "Sources", exact: true }).waitFor();
  await citationPage.close();
  assert.ok(
    calls.some((call) => JSON.stringify(call.messages).includes("image_url")),
    "The model receives the uploaded chart",
  );
  const cookies = await context.cookies();
  const threadQuery = new URL(page.url()).search;
  assert.match(threadQuery, /thread=/);

  const saved = await page.evaluate(async () => {
    const thread = new URL(location.href).searchParams.get("thread");

    return (await fetch(`/eve/v1/threads/${thread}`)).json();
  });

  assert.equal(saved.knowledge.matchedGuidelines, selected.length);
  assert.equal(saved.knowledge.selection.catalogId, catalog.release.digest);
  assert.equal(saved.knowledge.filters.sourceTypeIds.length, 1);
  await stop();
  url = await start(true);
  // Cookies are host-scoped, so port allocation preserves the signed browser owner.
  await context.addCookies(cookies);
  await page.goto(`${url}${threadQuery}`);
  await page
    .getByText("Use clear labels for the comparison.", { exact: true })
    .waitFor({ timeout: 30_000 });
  await page
    .getByRole("textbox", { name: /message|ask|chart/i })
    .first()
    .fill("Explain the labels again.");
  await page.getByRole("button", { name: /send/i }).click();
  await page
    .getByText("Use clear labels for the comparison.", { exact: true })
    .nth(1)
    .waitFor({ timeout: 90_000 });
  await page.getByRole("button", { name: "Open sidebar", exact: true }).click();
  await page.getByRole("button", { name: "Guidelines", exact: true }).click();
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
  assert.equal(errors.length, 0, errors.join("\n"));
  assert.ok(selected.includes(id));
  console.log(
    "Verified file-free npx startup through flags and environment, authenticated UI, native catalog loading, browser picker filtering and scope, chart upload, grounded answer, local citations, narrow layout, and restart persistence.",
  );
} catch (error) {
  if (page) {
    console.error(
      (
        await page
          .locator("body")
          .innerText()
          .catch(() => "")
      ).slice(-6000),
    );
    await page
      .screenshot({ path: join(root, ".context/chat-package-failure.png"), fullPage: true })
      .catch(() => {});
  }

  console.error(`Model requests: ${calls.length}`);
  console.error(runtimeOutput);
  throw error;
} finally {
  await browser?.close();
  await stop();

  if (model) {
    model.closeAllConnections();
    await new Promise((resolve) => model.close(resolve));
  }

  if (process.env.CHARTCOACH_KEEP_TEST_DATA) console.log(`Consumer: ${directory}`);
  else await rm(directory, { recursive: true, force: true });
}
