import type { SearchIndexDocuments } from "../integrations/search-index";
import {
  createGuidelineSearchDocument,
  createGuidelineSearchModel,
  parseGuidelineSearchModel,
  type GuidelineSearchDocument,
} from "../lib/guideline-search-model";
import { catalogLocationWatchFiles, loadSiteCatalog } from "./catalog-location";

const searchEntryPattern =
  /<script\b(?=[^>]*\bdata-guideline-search-entry\b)[^>]*>([\s\S]*?)<\/script>/i;

export const guidelineSearchDocuments = {
  async load({ root }) {
    const catalog = await loadSiteCatalog(root);

    return Array.from(catalog, (guideline) =>
      createGuidelineSearchDocument(createGuidelineSearchModel(guideline)),
    );
  },
  fromPage({ html, pathname }) {
    const match = searchEntryPattern.exec(html);

    if (!match?.[1]) {
      throw new Error(`Missing structured guideline search entry for ${pathname}.`);
    }

    return createGuidelineSearchDocument(parseGuidelineSearchModel(match[1]), pathname);
  },
  path: (document) => document.path,
  watchFiles: ({ root }) => catalogLocationWatchFiles(root),
} satisfies SearchIndexDocuments<GuidelineSearchDocument>;
