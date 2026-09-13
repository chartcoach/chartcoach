import { expect, it } from "vite-plus/test";
import { guidelinePreview } from "../chat/tool-output";

it.each([
  "https://example.com/guidelines/labels",
  "https://chartcoach.dev/guidelines/other-id",
  "https://chartcoach.dev/guidelines/labels?redirect=elsewhere",
  "https://chartcoach.dev/guidelines/labels#details",
  "https://user:password@chartcoach.dev/guidelines/labels",
  "javascript:alert(1)",
])("rejects an unrelated or unsafe guideline URL: %s", (url) => {
  expect(guidelinePreview("labels", "Label series directly", url)).toBeUndefined();
});

it.each([
  [
    "Direct_Labels",
    "https://chartcoach.dev/guidelines/Direct_Labels/",
    "https://chartcoach.dev/guidelines/Direct_Labels",
  ],
  [
    "direct labels",
    "https://chartcoach.dev/guidelines/direct%20labels",
    "https://chartcoach.dev/guidelines/direct%20labels",
  ],
])("normalizes the canonical URL for %s", (id, input, url) => {
  expect(guidelinePreview(id, "Label series directly", input)).toEqual({
    id,
    title: "Label series directly",
    url,
  });
});

it.each([
  ["..", "https://chartcoach.dev/guidelines/.."],
  [".", "https://chartcoach.dev/guidelines/%2e/"],
  ["labels?redirect=elsewhere", "https://chartcoach.dev/guidelines/labels?redirect=elsewhere"],
])("rejects an ID that changes URL meaning: %s", (id, url) => {
  expect(guidelinePreview(id, "Label series directly", url)).toBeUndefined();
});
