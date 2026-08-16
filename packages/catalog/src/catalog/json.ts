export type JsonScalar = boolean | null | number | string;

export interface JsonObject {
  [key: string]: JsonValue;
}

export type JsonValue = JsonScalar | JsonObject | readonly JsonValue[];

export function parseJson(text: string): JsonValue {
  return JSON.parse(text);
}

export function isJsonObject(value: JsonValue | undefined): value is JsonObject {
  return (
    value !== null &&
    value !== undefined &&
    !Array.isArray(value) &&
    Object.prototype.toString.call(value) === "[object Object]"
  );
}

export function isJsonNumber(value: JsonValue | undefined): value is number {
  return Object.prototype.toString.call(value) === "[object Number]";
}

export function isJsonString(value: JsonValue | undefined): value is string {
  return Object.prototype.toString.call(value) === "[object String]";
}
