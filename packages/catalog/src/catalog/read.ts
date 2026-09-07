import { CatalogError } from "./errors";
import { isJsonString } from "./json";
import type { Catalog, GuidelineSection } from "./model";
import { sourceRecords, type FullSourceRecord, type MinimalSourceRecord } from "./references";

export type SourceDetail = "none" | "minimal" | "full";

export type ReadOptions = Readonly<{
  ids: readonly string[];
  roles?: readonly string[];
  sourceDetail?: SourceDetail;
}>;

export type GuidelineEntryRecord = Readonly<{
  id: string;
  title: string;
  description: string;
  labels: readonly string[];
  sections: readonly GuidelineSection[];
  sources: readonly (MinimalSourceRecord | FullSourceRecord)[];
  references?: readonly string[];
}>;

export function readCatalog(
  catalog: Catalog,
  options: ReadOptions,
): readonly GuidelineEntryRecord[] {
  if (Object.prototype.toString.call(options) !== "[object Object]") {
    throw new CatalogError("Read options must be an object.");
  }
  if (!Array.isArray(options.ids) || !options.ids.every(isJsonString)) {
    throw new CatalogError("ids must be an array of strings.");
  }
  const roles = options.roles ?? [];
  if (!Array.isArray(roles) || !roles.every(isJsonString)) {
    throw new CatalogError("roles must be an array of strings.");
  }
  const sourceDetail = options.sourceDetail ?? "minimal";
  if (sourceDetail !== "none" && sourceDetail !== "minimal" && sourceDetail !== "full") {
    throw new CatalogError(`Unknown source detail: ${JSON.stringify(sourceDetail)}.`, {
      hints: ["Choose one of: none, minimal, full."],
    });
  }
  const missingRoles = Array.from(
    new Set(roles.filter((role) => !Object.hasOwn(catalog.manifest.sectionRoles, role))),
  ).sort();
  if (missingRoles.length > 0) {
    throw new CatalogError(`Unknown section role(s): ${missingRoles.join(", ")}`, {
      code: "lookup",
      details: { roles: missingRoles },
      hints: ["Call `await catalog.describe()` to inspect section roles."],
    });
  }
  if (options.ids.length === 0) return Object.freeze([]);

  const roleSet = roles.length > 0 ? new Set(roles) : undefined;
  return Object.freeze(
    options.ids.map((id) => {
      const guideline = catalog.require(id);
      const sections = Object.freeze(
        guideline.sections
          .filter((section) => roleSet === undefined || roleSet.has(section.role))
          .map((section) =>
            Object.freeze({
              role: section.role,
              title: section.title,
              content: section.content,
            }),
          ),
      );
      const record = {
        id: guideline.id,
        title: guideline.title,
        description: guideline.description,
        labels: Object.freeze([...guideline.labels]),
        sections,
        sources:
          sourceDetail === "none"
            ? Object.freeze([])
            : sourceRecords(catalog, guideline.id, sourceDetail),
      };
      return Object.freeze(
        sourceDetail === "full"
          ? { ...record, references: Object.freeze([...guideline.references]) }
          : record,
      );
    }),
  );
}
