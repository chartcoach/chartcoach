import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { test } from "node:test";

import { parse } from "yaml";
import picomatch from "picomatch";

const root = fileURLToPath(new URL("../../", import.meta.url));

type Pattern = string | Pattern[];

const filters: Record<string, Pattern[]> = parse(
  readFileSync(join(root, ".github/filters.yml"), "utf8"),
);

function flatten(pattern: Pattern): string[] {
  return Array.isArray(pattern) ? pattern.flatMap(flatten) : [pattern];
}

function selection(paths: string[], event = "pull_request") {
  const matched = Object.fromEntries(
    Object.entries(filters).map(([name, patterns]) => [
      name,
      String(
        paths.some((path) =>
          patterns.flatMap(flatten).some((pattern) => picomatch(pattern, { dot: true })(path)),
        ),
      ),
    ]),
  );

  const directory = mkdtempSync(join(tmpdir(), "chartcoach-ci-"));
  const output = join(directory, "output");

  try {
    const result = spawnSync(process.execPath, [join(root, "tools/ci/select.ts")], {
      encoding: "utf8",
      env: {
        ...process.env,
        GITHUB_EVENT_NAME: event,
        GITHUB_OUTPUT: output,
        FILTERS: JSON.stringify(matched),
      },
    });

    assert.equal(result.status, 0, result.stderr);

    return Object.fromEntries(
      readFileSync(output, "utf8")
        .trim()
        .split("\n")
        .map((line) => {
          const separator = line.indexOf("=");

          return [line.slice(0, separator), JSON.parse(line.slice(separator + 1))];
        }),
    );
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
}

void test("site changes select the site workspace and quality checks", () => {
  assert.deepEqual(selection(["apps/site/src/pages/index.astro"]), {
    quality: true,
    anti_slop: false,
    python: false,
    npm: false,
    javascript: true,
    packages: ["@chartcoach/site"],
  });
});

void test("docs changes select the docs workspace", () => {
  assert.deepEqual(selection(["apps/docs/content/docs/index.mdx"]).packages, ["@chartcoach/docs"]);
  assert.equal(selection(["apps/docs/content/docs/index.mdx"]).python, false);
  assert.equal(selection(["apps/docs/content/docs/index.mdx"]).npm, false);
});

void test("hidden package inputs select their owning checks", () => {
  assert.deepEqual(selection(["apps/docs/.node-version"]).packages, ["@chartcoach/docs"]);
  assert.deepEqual(selection(["apps/site/.gitignore"]).packages, ["@chartcoach/site"]);
  assert.equal(selection(["packages/catalog/.npmignore"]).npm, true);
});

void test("Python tests select Python checks", () => {
  assert.deepEqual(selection(["packages/chartcoach/tests/test_catalog_runtime.py"]), {
    quality: false,
    anti_slop: false,
    python: true,
    npm: false,
    javascript: false,
    packages: [],
  });
});

void test("Python implementation changes also verify JavaScript table parity", () => {
  const result = selection(["packages/chartcoach/src/chartcoach/_catalog/models.py"]);
  assert.equal(result.python, true);
  assert.equal(result.npm, false);
  assert.deepEqual(result.packages, ["@chartcoach/catalog"]);
});

void test("shared catalog fixtures select both languages and their consumers", () => {
  const result = selection(["fixtures/catalog-release/entries.parquet"]);
  assert.equal(result.python, true);
  assert.equal(result.npm, true);
  assert.deepEqual(result.packages, [
    "@chartcoach/catalog",
    "@chartcoach/site",
    "chartcoach",
    "@chartcoach/release",
  ]);
});

void test("brand changes rebuild the web apps and verify the packed chat", () => {
  assert.deepEqual(selection(["packages/brand/tokens.css"]).packages, [
    "@chartcoach/catalog",
    "@chartcoach/site",
    "@chartcoach/docs",
    "chartcoach",
    "@chartcoach/release",
  ]);
});

void test("chat, skills, and consumer tooling changes verify packed applications", () => {
  for (const path of [
    "apps/chat/cli/index.ts",
    "skills/chartcoach/SKILL.md",
    "tools/release/verify-chat.ts",
    "infra/Dockerfile",
  ]) {
    const result = selection([path]);
    assert.equal(result.npm, true, path);
    assert.deepEqual(result.packages, ["@chartcoach/catalog", "chartcoach", "@chartcoach/release"]);
  }
});

void test("repository prose runs quality checks", () => {
  assert.deepEqual(selection(["README.md"]), {
    quality: true,
    anti_slop: false,
    python: false,
    npm: false,
    javascript: false,
    packages: [],
  });
});

void test("CI controls select the complete validation graph", () => {
  for (const path of [
    ".github/filters.yml",
    ".github/actions/setup-js/action.yml",
    "tools/ci/select.ts",
    "Makefile",
  ]) {
    const result = selection([path]);
    assert.equal(result.python, true, path);
    assert.equal(result.npm, true, path);
    assert.equal(result.quality, true, path);
    assert.equal(result.anti_slop, true, path);
    assert.deepEqual(result.packages, [
      "@chartcoach/catalog",
      "@chartcoach/site",
      "@chartcoach/docs",
      "chartcoach",
      "@chartcoach/release",
    ]);
  }
});

void test("main pushes select complete checks and release artifacts even for prose changes", () => {
  const result = selection(["README.md"], "push");
  assert.equal(result.python, true);
  assert.equal(result.npm, true);
  assert.equal(result.anti_slop, true);
  assert.deepEqual(result.packages, [
    "@chartcoach/catalog",
    "@chartcoach/site",
    "@chartcoach/docs",
    "chartcoach",
    "@chartcoach/release",
  ]);
});

void test("selection rejects incomplete PR classification", () => {
  const result = spawnSync(process.execPath, [join(root, "tools/ci/select.ts")], {
    encoding: "utf8",
    env: { ...process.env, GITHUB_EVENT_NAME: "pull_request", FILTERS: "{}" },
  });

  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /Missing or invalid path filter/);
});

function gate(overrides = {}, selected = {}) {
  const needs = {
    changes: {
      result: "success",
      outputs: {
        quality: "false",
        javascript: "false",
        npm: "false",
        python: "false",
        ...selected,
      },
    },
    quality: { result: "skipped" },
    javascript: { result: "skipped" },
    "npm-consumers": { result: "skipped" },
    python: { result: "skipped" },
    "python-minimum": { result: "skipped" },
    ...overrides,
  };

  return spawnSync(process.execPath, [join(root, "tools/ci/gate.ts")], {
    encoding: "utf8",
    env: { ...process.env, NEEDS: JSON.stringify(needs) },
  });
}

void test("the gate accepts skipped checks for unchanged inputs", () => {
  assert.equal(gate().status, 0);
});

void test("the gate requires selected jobs to succeed", () => {
  for (const [job, flag] of [
    ["quality", "quality"],
    ["javascript", "javascript"],
    ["npm-consumers", "npm"],
    ["python", "python"],
    ["python-minimum", "python"],
  ] as const) {
    for (const result of ["failure", "cancelled", "skipped"]) {
      const check = gate(
        {
          python: { result: "success" },
          "python-minimum": { result: "success" },
          [job]: { result },
        },
        { [flag]: "true" },
      );

      assert.notEqual(check.status, 0, `${job}: ${result}`);
      assert.match(check.stderr, new RegExp(`${job}:`));
    }
  }
});

void test("the gate rejects failed classification and unexpected job failures", () => {
  assert.notEqual(gate({ changes: { result: "failure", outputs: {} } }).status, 0);
  assert.notEqual(gate({ quality: { result: "failure" } }).status, 0);
});

void test("the gate rejects incomplete check selection", () => {
  const result = gate({ changes: { result: "success", outputs: {} } });

  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /Missing or invalid check selection/);
});
