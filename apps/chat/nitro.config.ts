import { defineNitroConfig } from "nitro/config";
import { fileURLToPath } from "node:url";
import { cp } from "node:fs/promises";
import { join } from "node:path";
import { relocateSandboxTemplates } from "./scripts/sandbox.ts";

export default defineNitroConfig({
  entry: fileURLToPath(new URL("./runtime/worker.ts", import.meta.url)),
  // The workspace link resolves outside node_modules during Nitro externalization.
  traceDeps: ["@chartcoach/catalog/node", "@chartcoach/catalog/duckdb"].map((specifier) =>
    fileURLToPath(import.meta.resolve(specifier)),
  ),
  hooks: {
    async "build:before"(nitro) {
      // Runtime caches are host data. Trace deployable files within the workspace.
      nitro.options.traceOpts ??= {};
      nitro.options.traceOpts.nft = {
        ...nitro.options.traceOpts.nft,
        base: nitro.options.workspaceDir,
      };

      if (nitro.options.dev) return;

      const bootstrap = nitro.options.plugins.find((path) =>
        path.endsWith("compiled-artifacts-bootstrap.mjs"),
      );

      if (!bootstrap) throw new Error("Eve's build is missing its compiled bootstrap.");
      await relocateSandboxTemplates(bootstrap, join(nitro.options.buildDir, "chartcoach-sandbox"));
    },
    async compiled(nitro) {
      if (nitro.options.dev) return;
      await cp(
        join(nitro.options.buildDir, "chartcoach-sandbox"),
        join(nitro.options.output.dir, "sandbox"),
        { recursive: true },
      );
    },
  },
});
