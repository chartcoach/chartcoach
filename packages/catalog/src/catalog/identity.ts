import { CatalogError } from "./errors";
import { isJsonObject, type JsonObject, type JsonValue } from "./json";
import type { Guideline } from "./model";

export async function catalogEntriesDigest(guidelines: readonly Guideline[]): Promise<string> {
  const rows = [...guidelines]
    .sort((left, right) => compareUnicode(left.id, right.id))
    .map(
      (guideline): JsonObject => ({
        id: guideline.id,
        title: guideline.title,
        description: guideline.description,
        labels: guideline.labels,
        sections: guideline.sections.map((section) => ({
          role: section.role,
          title: section.title,
          content: section.content,
        })),
        references: guideline.references,
      }),
    );
  return sha256Text(rows.map(canonicalJson).join(""));
}

export async function manifestDigest(markdown: string): Promise<string> {
  return sha256Text(markdown);
}

export function canonicalJson(value: JsonValue): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(",")}]`;
  if (!isJsonObject(value)) return JSON.stringify(value) ?? "null";
  return `{${Object.keys(value)
    .sort(compareUnicode)
    .map((key) => `${JSON.stringify(key)}:${canonicalJson(value[key]!)}`)
    .join(",")}}`;
}

export async function sha256Bytes(value: Uint8Array): Promise<string> {
  const subtle = globalThis.crypto?.subtle;
  if (!subtle) {
    throw new CatalogError("SHA-256 digest support is unavailable in this runtime.", {
      code: "unavailable_capability",
    });
  }
  const digest = await subtle.digest("SHA-256", value.slice().buffer);
  return [...new Uint8Array(digest)].map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

export function compareUnicode(left: string, right: string): number {
  const leftPoints = Array.from(left, (character) => character.codePointAt(0)!);
  const rightPoints = Array.from(right, (character) => character.codePointAt(0)!);
  const length = Math.min(leftPoints.length, rightPoints.length);
  for (let index = 0; index < length; index += 1) {
    const difference = leftPoints[index]! - rightPoints[index]!;
    if (difference !== 0) return difference;
  }
  return leftPoints.length - rightPoints.length;
}

async function sha256Text(value: string): Promise<string> {
  return sha256Bytes(new TextEncoder().encode(value));
}
