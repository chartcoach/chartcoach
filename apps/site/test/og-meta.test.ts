import { expect, it } from "vite-plus/test";

import { buildOgImageProps } from "../src/og/meta";

it("normalizes OG lists before applying their display limits", () => {
  const props = buildOgImageProps({
    title: "  Chart title ",
    description: "Chart description",
    labels: [" ", " a ", "b", "c", "d", "e", "f", "g", "h"],
    metaItems: ["", " source ", "source", "year", "extra", "hidden"],
    roles: ["", " advice  role "],
    verbs: ["", " compare ", "choose", "read", "revise", "apply", "hidden"],
    references: [
      { title: " ", meta: " ignored " },
      { title: " First source ", meta: "  A   B  " },
      { title: "Second source" },
      { title: "Third source" },
    ],
  });

  expect(props.labels).toEqual(["a", "b", "c", "d", "e", "f", "g"]);
  expect(props.metaItems).toEqual(["source", "source", "year", "extra"]);
  expect(props.roles).toEqual(["advice role"]);
  expect(props.verbs).toEqual(["compare", "choose", "read", "revise", "apply"]);
  expect(props.references).toEqual([
    { title: "First source", meta: "A B" },
    { title: "Second source", meta: undefined },
  ]);
});
