import type { JsonObject, JsonValue } from "@chartcoach/catalog";

export type { JsonObject, JsonValue };

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

export function isJsonString(value: JsonValue | undefined): value is string {
  return Object.prototype.toString.call(value) === "[object String]";
}
