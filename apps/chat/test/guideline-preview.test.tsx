import { expect, it } from "vite-plus/test";
import { guidelinePreview } from "../chat/tool-output";

it.each([
  ["Direct_Labels", "https://chartcoach.dev/guidelines/Direct_Labels"],
  ["direct labels", "https://chartcoach.dev/guidelines/direct%20labels"],
  ["labels?redirect=elsewhere", "https://chartcoach.dev/guidelines/labels%3Fredirect%3Delsewhere"],
  ["labels/path", "https://chartcoach.dev/guidelines/labels%2Fpath"],
])("builds a guideline destination from its encoded ID: %s", (id, url) => {
  expect(guidelinePreview(id, "Label series directly")).toEqual({
    id,
    title: "Label series directly",
    url,
    imageURL: `${url}/og.png`,
  });
});

it.each(["", ".", ".."])("rejects an ID that cannot identify a guideline: %s", (id) => {
  expect(guidelinePreview(id, "Label series directly")).toBeUndefined();
});

it("uses the deployment templates for citation links and preview images", () => {
  const links = {
    urlTemplate: "https://guidance.example/entries/{id}",
    imageURLTemplate: "https://images.example/{id}.png",
  };

  expect(guidelinePreview("direct labels", "Direct labels", links)).toEqual({
    id: "direct labels",
    title: "Direct labels",
    url: "https://guidance.example/entries/direct%20labels",
    imageURL: "https://images.example/direct%20labels.png",
  });
});
