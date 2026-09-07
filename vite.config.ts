import { defineConfig } from "vite-plus";

import { antiSlopIgnorePatterns, antiSlopRules } from "./tools/oxlint/anti-slop/preset.ts";

const ignoredPaths = [...antiSlopIgnorePatterns];

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
      reportUnusedDisableDirectives: "error",
      typeAware: true,
      typeCheck: true,
    },
    plugins: ["typescript", "unicorn", "import"],
    rules: {
      ...antiSlopRules,
      "vite-plus/prefer-vite-plus-imports": "error",
    },
    overrides: [
      {
        files: ["packages/catalog/src/catalog/**", "packages/catalog/src/index.ts"],
        rules: {
          "no-restricted-imports": [
            "error",
            {
              patterns: ["node:*", "@chartcoach/*", "../**/apps/**", "../**/brand/**"],
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
                "@chartcoach/catalog/*",
                "@chartcoach/site",
                "@chartcoach/site/*",
                "../**/packages/**",
                "../**/site/**",
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
              patterns: [
                "@chartcoach/catalog/*",
                "@chartcoach/docs",
                "@chartcoach/docs/*",
                "../**/packages/**",
                "../**/docs/**",
              ],
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
