import { stripVTControlCharacters } from "node:util";
import { Chalk } from "chalk";
import { expect, it } from "vite-plus/test";
import { renderLoading, renderReady } from "../cli/output";

const details = {
  url: "http://127.0.0.1:4273/",
  catalog: { guidelines: 781, digest: "abc123" },
  dataDir: "/tmp/chartcoach",
};

it("renders a readable startup summary with optional terminal color", () => {
  const plain = new Chalk({ level: 0 });
  const color = new Chalk({ level: 1 });
  const output = renderReady(details, plain);

  expect(renderLoading(plain)).toBe("◌ Loading catalog…\n");
  expect(output).toBe(`
✓ ChartCoach is ready
  ➜ http://127.0.0.1:4273/

  Catalog  781 guidelines
  Release  abc123
  Model    Choose a connection in the browser
  Data     /tmp/chartcoach

  Press Ctrl+C to stop.
`);
  expect(renderReady(details, color)).toContain("\u001B[");
  expect(stripVTControlCharacters(renderReady(details, color))).toBe(output);
});
