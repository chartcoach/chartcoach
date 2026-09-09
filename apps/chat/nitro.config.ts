import { defineNitroConfig } from "nitro/config";
import { fileURLToPath } from "node:url";

export default defineNitroConfig({
  // The workspace link resolves outside node_modules during Nitro externalization.
  traceDeps: ["@chartcoach/catalog/node", "@chartcoach/catalog/duckdb"].map((specifier) =>
    fileURLToPath(import.meta.resolve(specifier)),
  ),
  hooks: {
    "build:before"(nitro) {
      // Runtime caches are host data. Trace deployable files within the workspace.
      nitro.options.traceOpts ??= {};
      nitro.options.traceOpts.nft = {
        ...nitro.options.traceOpts.nft,
        base: nitro.options.workspaceDir,
      };
    },
  },
});
