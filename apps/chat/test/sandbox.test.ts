import assert from "node:assert/strict";
import { mkdtemp, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { test } from "node:test";
import { relocateSandboxTemplates } from "../scripts/sandbox.ts";

await test("packaging relocates prepared sandbox files independently of the build directory", async () => {
  const directory = await mkdtemp(join(tmpdir(), "chartcoach-sandbox-"));
  const key = "a".repeat(24);
  const template = join(directory, "build", key);
  const bootstrap = join(directory, "bootstrap.mjs");
  const output = join(directory, "packaged");

  try {
    await mkdir(join(template, "fs/workspace"), { recursive: true });
    await writeFile(join(template, "fs/workspace/skill.md"), "canonical skill");

    const artifacts = {
      kind: "eve-sandbox-prepared-artifacts",
      version: 2,
      entries: [
        { nodeId: "root", providerName: "just-bash", artifact: { templateRootPath: template } },
      ],
    };

    const original = `const sandboxPreparedArtifacts = ${JSON.stringify(artifacts, null, 2)};\nexport { sandboxPreparedArtifacts };\n`;
    await writeFile(bootstrap, original);
    await relocateSandboxTemplates(bootstrap, output);
    await rm(join(directory, "build"), { recursive: true });

    assert.equal(
      await readFile(join(output, key, "fs/workspace/skill.md"), "utf8"),
      "canonical skill",
    );
    const relocated = await readFile(bootstrap, "utf8");
    assert.ok(!relocated.includes(template));
    assert.ok(relocated.includes(`.eve/sandbox-cache/just-bash/templates/${key}`));
    assert.ok(relocated.endsWith("export { sandboxPreparedArtifacts };\n"));

    await writeFile(bootstrap, "export {};\n");
    await assert.rejects(
      relocateSandboxTemplates(bootstrap, output),
      /missing prepared sandbox artifacts/,
    );
    assert.equal(await readFile(bootstrap, "utf8"), "export {};\n");
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});
