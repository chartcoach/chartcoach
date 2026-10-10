import assert from "node:assert/strict";
import { mkdtemp, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { JustBashSandbox } from "eve/sandbox/just-bash";
import type { SandboxSession } from "eve/sandbox";

await test("legacy conversations retain chart bytes when their sandbox upgrades", async () => {
  const directory = await mkdtemp(join(tmpdir(), "chartcoach-sandbox-upgrade-"));
  const originalDirectory = process.cwd();
  const legacyRoot = join(directory, "legacy");
  const templateRoot = join(directory, "template");
  const imagePath = "/workspace/.eve/attachments/chart/chart.png";
  const bytes = Buffer.from("previous chart image");
  const environment = JustBashSandbox.environment({ autoInstall: false });

  const input = {
    compiledArtifactsSource: { kind: "bundled" },
    nodeId: "__root__",
    sessionId: "old-conversation",
    state: {
      initialized: true,
      session: {
        backendName: "just-bash",
        sessionKey: "old-key",
        metadata: { rootPath: legacyRoot },
      },
    },
    registry: {
      sandbox: {
        definition: {
          kind: "independent",
          logicalPath: "sandbox",
          environment,
          selector: () => environment.open(),
        },
      },
    },
  };

  // SAFETY: This regression exercises Eve's pinned internal migration boundary,
  // whose current types exclude the historical state intentionally supplied here.
  const { ensureSandboxAccess } = (await import(
    new URL("./execution/sandbox/ensure.js", import.meta.resolve("eve")).href
  )) as {
    ensureSandboxAccess(
      this: void,
      request: typeof input,
    ): Promise<{
      get(): Promise<SandboxSession | null>;
      stop(): Promise<void>;
    }>;
  };

  const artifacts = {
    manifest: {},
    metadata: {},
    moduleMap: {},
    sandboxPreparedArtifacts: {
      kind: "eve-sandbox-prepared-artifacts",
      version: 2,
      entries: [
        {
          nodeId: "__root__",
          providerName: "just-bash",
          artifact: { templateRootPath: templateRoot },
        },
      ],
    },
  };

  // SAFETY: The bundled loader registers the same artifact shape emitted by Eve's build.
  const { installBundledCompiledArtifacts } = (await import(
    new URL("./runtime/loaders/bundled-artifacts.js", import.meta.resolve("eve")).href
  )) as { installBundledCompiledArtifacts(this: void, input: typeof artifacts): void };

  let access: Awaited<ReturnType<typeof ensureSandboxAccess>> | undefined;

  try {
    await mkdir(dirname(join(legacyRoot, "fs", imagePath)), { recursive: true });
    await writeFile(join(legacyRoot, "fs", imagePath), bytes);
    await mkdir(join(templateRoot, "fs/workspace"), { recursive: true });
    await writeFile(join(templateRoot, "fs/workspace/skill.md"), "current skill");
    await writeFile(join(legacyRoot, "fs/workspace/skill.md"), "old skill");
    installBundledCompiledArtifacts(artifacts);
    process.chdir(directory);
    access = await ensureSandboxAccess(input);
    const sandbox = await access.get();

    assert.ok(sandbox);
    const restored = await sandbox.readBinaryFile({ path: imagePath });

    assert.ok(restored);
    assert.deepEqual(Buffer.from(restored), bytes);
    assert.equal(await sandbox.readTextFile({ path: "/workspace/skill.md" }), "current skill");
    assert.deepEqual(await readFile(join(legacyRoot, "fs", imagePath)), bytes);
  } finally {
    await access?.stop();
    process.chdir(originalDirectory);
    await rm(directory, { recursive: true, force: true });
  }
});
