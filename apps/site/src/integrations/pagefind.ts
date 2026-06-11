import type { HookParameters } from "astro";
import type { AstroIntegration } from "astro";
import { fileURLToPath } from "node:url";
import * as pagefind from "pagefind";

type PagefindResponse = {
  errors: string[];
};

type PagefindOptions = Pick<HookParameters<"astro:build:done">, "dir" | "logger">;

function assertPagefindResponse<T extends PagefindResponse>(
  response: T,
  { logger }: PagefindOptions,
): asserts response is Required<T> {
  if (response.errors.length === 0) return;

  for (const error of response.errors) {
    logger.error(`Pagefind error: ${error}`);
  }
  throw new Error("Pagefind response contained errors.");
}

export function pagefindSearch(): AstroIntegration {
  return {
    name: "chartcoach-pagefind",
    hooks: {
      "astro:build:done": async ({ dir, logger }) => {
        const pagefindLogger = logger.fork("chartcoach:pagefind");
        const options = { dir, logger: pagefindLogger };

        try {
          const startedAt = performance.now();
          pagefindLogger.info("Building search index with Pagefind...");

          const newIndexResponse = await pagefind.createIndex();
          assertPagefindResponse(newIndexResponse, options);

          const indexingResponse = await newIndexResponse.index.addDirectory({
            path: fileURLToPath(dir),
          });
          assertPagefindResponse(indexingResponse, options);
          pagefindLogger.info(`Found ${indexingResponse.page_count} HTML files.`);

          const writeFilesResponse = await newIndexResponse.index.writeFiles({
            outputPath: fileURLToPath(new URL("./pagefind/", dir)),
          });
          assertPagefindResponse(writeFilesResponse, options);

          const elapsed = performance.now() - startedAt;
          const duration =
            elapsed < 750 ? `${Math.round(elapsed)}ms` : `${(elapsed / 1000).toFixed(2)}s`;
          pagefindLogger.info(`Finished building search index in ${duration}.`);
        } catch (cause) {
          throw new Error("Failed to run Pagefind.", { cause });
        } finally {
          await pagefind.close();
        }
      },
    },
  };
}
