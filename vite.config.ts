import { defineConfig } from "vite-plus";

const ignoredPaths = [
  ".agent/**",
  ".agents/**",
  ".claude/**",
  ".codex/**",
  ".continue/**",
  ".cursor/**",
  ".gemini/**",
  ".opencode/**",
  ".pi/**",
  ".roo/**",
  ".windsurf/**",
  "tools/oxlint/anti-slop/**",
];

export default defineConfig({
  fmt: {
    ignorePatterns: ignoredPaths,
    printWidth: 100,
  },
  lint: {
    categories: {
      correctness: "error",
    },
    ignorePatterns: ignoredPaths,
    jsPlugins: [
      { name: "vite-plus", specifier: "vite-plus/oxlint-plugin" },
      { name: "anti-slop", specifier: "./tools/oxlint/anti-slop/index.ts" },
    ],
    options: {
      denyWarnings: true,
      typeAware: true,
    },
    plugins: ["typescript", "unicorn", "import"],
    rules: {
      "anti-slop/no-chained-type-assertions": "error",
      "anti-slop/no-conditional-empty-object-spread": "error",
      "anti-slop/no-known-value-widening": "error",
      "anti-slop/no-module-mocking": "error",
      "anti-slop/no-object-parameters": "error",
      "anti-slop/no-reflect-apply": "error",
      "anti-slop/no-reflect-get": "error",
      "anti-slop/no-runtime-typeof": "error",
      "anti-slop/no-shape-in-symbol-names": "error",
      "anti-slop/no-unknown-parameters": "error",
      "anti-slop/no-unknown-returns": "error",
      "anti-slop/no-unknown-type-aliases": "error",
      "anti-slop/no-unsafe-dictionary-type": "error",
      "anti-slop/no-widen-then-assert": "error",
      "anti-slop/require-safety-comment-for-type-assertion": "error",
      "vite-plus/prefer-vite-plus-imports": "error",
    },
    overrides: [
      {
        files: ["packages/catalog/src/**"],
        rules: {
          "no-restricted-imports": [
            "error",
            {
              patterns: ["node:*", "@chartcoach/*"],
            },
          ],
        },
      },
      {
        files: ["apps/docs/**"],
        rules: {
          "no-restricted-imports": [
            "error",
            {
              patterns: [
                "@chartcoach/catalog",
                "@chartcoach/catalog/*",
                "@chartcoach/site",
                "@chartcoach/site/*",
              ],
            },
          ],
        },
      },
      {
        files: ["apps/site/**"],
        rules: {
          "no-restricted-imports": [
            "error",
            {
              patterns: ["@chartcoach/docs", "@chartcoach/docs/*"],
            },
          ],
        },
      },
    ],
  },
  run: {
    cache: true,
  },
});
