export type GuidelineSection = {
	role: string;
	title: string;
	content: string;
};

export const DANGLING_ROLE = "__dangling__";

export type GuidelineSectionIndex = {
	byRole: Record<string, GuidelineSection[]>;
};

export type Guideline = {
	id: string;
	title: string;
	bibliography?: string;
	description: string;
	labels: string[];
	body: string;
};

export type ParsedGuideline = Guideline & {
	sections: GuidelineSection[];
	sectionsIndex: GuidelineSectionIndex;
};

export type CatalogEntry = {
	guideline: ParsedGuideline;
	/** BibTeX entries split at `@...` */
	references: string[];
};

export class Catalog {
	readonly entries: CatalogEntry[];

	constructor(entries: CatalogEntry[] = []) {
		this.entries = entries;
	}

	get length(): number {
		return this.entries.length;
	}

	[Symbol.iterator](): Iterator<CatalogEntry> {
		return this.entries[Symbol.iterator]();
	}
}
