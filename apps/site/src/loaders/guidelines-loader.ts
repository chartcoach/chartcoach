import type { Loader } from "astro/loaders";

import { toMarkdown } from "@chartcoach/catalog";

import {
  catalogLocationRecordPath,
  catalogLocationWatchFiles,
  loadSiteCatalog,
  resolveCatalogLocation,
  resolveSiteCatalogLocation,
} from "@/config/catalog-location";
import { renderGuidelineCitations } from "@/lib/guideline-citations";
import { createGuidelineRecord } from "@/lib/guideline-record";
import { createGuidelineSearchModel } from "@/lib/guideline-search-model";

type GuidelinesLoaderOptions = {
  location?: string;
};

export function guidelinesLoader({ location }: GuidelinesLoaderOptions = {}): Loader {
  return {
    name: "chartcoach-guidelines-loader",
    async load(context) {
      const catalogLocation = location
        ? resolveCatalogLocation(location, context.config.root)
        : resolveSiteCatalogLocation(context.config.root);

      const watchedFiles = catalogLocationWatchFiles(context.config.root, location);

      if (watchedFiles.length > 0) context.watcher?.add(watchedFiles);

      const catalog = await loadSiteCatalog(context.config.root, location);
      const guidelines = Array.from(catalog);
      context.store.clear();

      const storeEntries = await Promise.all(
        guidelines.map(async (guideline) => {
          const id = guideline.id;
          const references = [...guideline.references];
          const record = createGuidelineRecord(guideline);
          const referencesBib = references.length > 0 ? references.join("\n\n") : undefined;

          const citations = renderGuidelineCitations(
            [guideline.body, ...guideline.sections.map((section) => section.content)],
            references,
          );

          const renderedBody = citations.bodies[0];

          const sectionMarkdown = await Promise.all(
            citations.bodies.slice(1).map((body) => context.renderMarkdown(body)),
          );

          const sections = guideline.sections.map((section, index) => ({
            role: section.role,
            title: section.title,
            html: sectionMarkdown[index]?.html ?? "",
          }));

          const [data, rendered] = await Promise.all([
            context.parseData({
              id,
              data: {
                id: guideline.id,
                title: guideline.title,
                description: guideline.description || undefined,
                labels: [...guideline.labels],
                markdown: toMarkdown(guideline),
                record,
                search: createGuidelineSearchModel(guideline),
                sections,
                referencesBib,
                citations: citations.citedKeys,
                bibliographyHtml: citations.bibliographyHtml,
              },
            }),
            context.renderMarkdown(renderedBody),
          ]);

          const digest = context.generateDigest(`${renderedBody}\n\n${referencesBib ?? ""}`);
          const filePath = catalogLocationRecordPath(context.config.root, catalogLocation, id);

          return {
            id,
            data,
            body: renderedBody,
            rendered,
            digest,
            filePath,
            assetImports: rendered.metadata?.imagePaths,
          };
        }),
      );

      for (const entry of storeEntries) {
        context.store.set(entry);
      }
    },
  };
}
