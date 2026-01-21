import { parquetReadObjects } from "hyparquet";
import { compressors } from "hyparquet-compressors";
import {
	Catalog,
	type CatalogEntry,
} from "./model.js";
import { indexGuidelineSections, parseGuidelineSections } from "./parse.js";

export type AsyncBuffer = {
	byteLength: number;
	slice(start: number, end?: number): ArrayBuffer | Promise<ArrayBuffer>;
};

export type ParquetBytes = ArrayBuffer | ArrayBufferView;

function normalizeParquetBytes(bytes: ParquetBytes): ArrayBuffer {
	if (bytes instanceof ArrayBuffer) return bytes;

	// TypedArray/DataView may be a view into a larger ArrayBuffer (or SharedArrayBuffer).
	// Copy to a standalone ArrayBuffer covering exactly the view range.
	const u8 = new Uint8Array(bytes.buffer, bytes.byteOffset, bytes.byteLength);
	return u8.slice().buffer;
}

export async function loadCatalogFromParquet(
	file: AsyncBuffer | ParquetBytes,
): Promise<Catalog> {
	const normalizedFile =
		file instanceof ArrayBuffer || ArrayBuffer.isView(file)
			? normalizeParquetBytes(file as ParquetBytes)
			: file;

	const rows = (await parquetReadObjects({
		file: normalizedFile,
		compressors,
	})) as Array<Record<string, unknown>>;

	const entries: CatalogEntry[] = [];
	for (const row of rows) {
		const guideline = row.guideline as Record<string, unknown> | undefined;
		const id = row.id;
		const references = row.references;

		if (typeof id !== "string" || !guideline || typeof guideline !== "object") continue;

		const entry: CatalogEntry = {
			guideline: {
				id,
				title: typeof guideline.title === "string" ? guideline.title : id,
				bibliography:
					typeof guideline.bibliography === "string" ? guideline.bibliography : undefined,
				description: typeof guideline.description === "string" ? guideline.description : "",
				labels: Array.isArray(guideline.labels)
					? guideline.labels.filter((l): l is string => typeof l === "string")
					: [],
				body: typeof guideline.body === "string" ? guideline.body : "",
				sections: [],
				sectionsIndex: { byRole: {} },
			},
			references: Array.isArray(references)
				? references.filter((r): r is string => typeof r === "string")
				: [],
		};

		entry.guideline.sections = parseGuidelineSections(entry.guideline.body);
		entry.guideline.sectionsIndex = indexGuidelineSections(entry.guideline.sections);
		entries.push(entry);
	}

	return new Catalog(entries);
}
