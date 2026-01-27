import type { CatalogEntry } from "./model.js";
import { indexGuidelineSections, parseGuidelineSections } from "./parse.js";

export type CatalogEntryWire = {
	id: string;
	guideline: {
		title?: string;
		bibliography?: string | null;
		description?: string;
		labels?: unknown;
		body: string;
	};
	references?: unknown;
};

function isRecord(value: unknown): value is Record<string, unknown> {
	return Boolean(value && typeof value === "object" && !Array.isArray(value));
}

function toStringArray(value: unknown): string[] {
	return Array.isArray(value) ? value.filter((v): v is string => typeof v === "string") : [];
}

export function isCatalogEntryWire(value: unknown): value is CatalogEntryWire {
	if (!isRecord(value)) return false;
	if (typeof value.id !== "string" || value.id.length === 0) return false;
	if (!isRecord(value.guideline)) return false;
	return typeof value.guideline.body === "string";
}

export function catalogEntryFromWire(value: unknown): CatalogEntry | null {
	if (!isCatalogEntryWire(value)) return null;

	const { id, guideline, references } = value;

	const entry: CatalogEntry = {
		guideline: {
			id,
			title: typeof guideline.title === "string" && guideline.title.length > 0 ? guideline.title : id,
			bibliography: typeof guideline.bibliography === "string" ? guideline.bibliography : undefined,
			description: typeof guideline.description === "string" ? guideline.description : "",
			labels: toStringArray(guideline.labels),
			body: guideline.body,
			sections: [],
			sectionsIndex: { byRole: {} },
		},
		references: toStringArray(references),
	};

	entry.guideline.sections = parseGuidelineSections(entry.guideline.body);
	entry.guideline.sectionsIndex = indexGuidelineSections(entry.guideline.sections);
	return entry;
}

export function requireCatalogEntryFromWire(value: unknown, context?: string): CatalogEntry {
	const entry = catalogEntryFromWire(value);
	if (entry) return entry;

	const suffix = context ? ` (${context})` : "";
	throw new Error(`Invalid CatalogEntry wire format${suffix}.`);
}

