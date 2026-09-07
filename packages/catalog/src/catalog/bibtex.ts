// @ts-expect-error bibtex-parse 2.1.0 does not publish TypeScript declarations.
import { parse } from "bibtex-parse";

export interface BibtexEntry {
  readonly key: string;
  readonly type: string;
  readonly [field: string]: bigint | null | number | string;
}

type BibtexValue =
  | { datatype: "number" | "quoted" | "braced" | "identifier"; value: string }
  | { datatype: "concatinate"; value: readonly BibtexValue[] }
  | { datatype: "null"; value: null };

type BibtexItem =
  | {
      itemtype: "entry";
      key: string;
      type: string;
      fields: readonly (BibtexValue & { name: string })[];
    }
  | ({ itemtype: "string"; name: string } & BibtexValue)
  | { itemtype: "comment" | "preamble" };

type ParseBibtex = (input: string, options: { number: "string" }) => readonly BibtexItem[];

export function parseBibtexEntries(input: string): readonly BibtexEntry[] {
  const parseItems: ParseBibtex = parse;
  const strings = new Map([
    ["jan", "January"],
    ["feb", "February"],
    ["mar", "March"],
    ["apr", "April"],
    ["may", "May"],
    ["jun", "June"],
    ["jul", "July"],
    ["aug", "August"],
    ["sep", "September"],
    ["oct", "October"],
    ["nov", "November"],
    ["dec", "December"],
  ]);
  const result: BibtexEntry[] = [];
  for (const item of parseItems(input, { number: "string" })) {
    if (item.itemtype === "string")
      strings.set(item.name.toLowerCase(), fieldValue(item, strings) ?? "");
    if (item.itemtype === "entry") {
      result.push({
        key: item.key,
        type: item.type,
        ...Object.fromEntries(
          item.fields.map((field) => [field.name.toUpperCase(), fieldValue(field, strings)]),
        ),
      });
    }
  }
  return result;
}

function fieldValue(field: BibtexValue, strings: ReadonlyMap<string, string>): string | null {
  if (field.datatype === "null") return null;
  if (field.datatype === "concatinate")
    return field.value.map((value) => fieldValue(value, strings)).join("");
  if (field.datatype === "identifier") {
    const value = strings.get(field.value.toLowerCase());
    if (value === undefined) throw new Error(`Undefined BibTeX string: ${field.value}`);
    return value;
  }
  // Preserve grouping braces and escapes as the Python source-record parser does.
  return field.value;
}
