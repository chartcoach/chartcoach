import { readdir, readFile, stat } from "node:fs/promises";
import { join } from "node:path";
import { Catalog, type CatalogEntry } from "./model.js";
import { parseBibtex, parseGuideline } from "./parse.js";

export async function loadCatalogEntryFromFolder(entryDir: string): Promise<CatalogEntry> {
	const files = await readdir(entryDir);
	const mdFiles = files.filter((f) => f.endsWith(".md"));

	if (mdFiles.length === 0) {
		throw new Error(`No guideline markdown file found in catalog entry directory: ${entryDir}`);
	}
	if (mdFiles.length > 1) {
		throw new Error(
			`Multiple markdown files found in catalog entry directory: ${entryDir}. Expected only one.`,
		);
	}

	const guidelineMdPath = join(entryDir, mdFiles[0]!);
	const guidelineMd = await readFile(guidelineMdPath, "utf-8");
	const guideline = parseGuideline(guidelineMd);

	let references: string[] = [];
	if (guideline.bibliography) {
		try {
			const bibPath = join(entryDir, guideline.bibliography);
			const bib = await readFile(bibPath, "utf-8");
			references = parseBibtex(bib);
		} catch {
			guideline.bibliography = undefined;
		}
	}

	return { guideline, references };
}

export async function loadCatalogFromFolder(folderPath: string): Promise<Catalog> {
	const entries: CatalogEntry[] = [];

	const children = await readdir(folderPath);
	for (const name of children) {
		if (name === "__templates__") continue;
		const full = join(folderPath, name);
		let s;
		try {
			s = await stat(full);
		} catch {
			continue;
		}
		if (!s.isDirectory()) continue;

		try {
			const entry = await loadCatalogEntryFromFolder(full);
			entries.push(entry);
		} catch {
			// Match Python behavior: skip invalid entries (caller can validate separately if desired).
		}
	}

	return new Catalog(entries);
}
