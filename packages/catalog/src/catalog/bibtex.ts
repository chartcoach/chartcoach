// @ts-expect-error bibtex-parse 2.1.0 does not publish TypeScript declarations.
import { entries } from "bibtex-parse";

export interface BibtexEntry {
  readonly key: string;
  readonly type: string;
  readonly [field: string]: bigint | null | number | string;
}

type ParseEntries = (
  input: string,
  options: Readonly<{ number: "string" }>,
) => readonly BibtexEntry[];

export function parseBibtexEntries(input: string): readonly BibtexEntry[] {
  const parse: ParseEntries = entries;
  return parse(input, { number: "string" });
}
