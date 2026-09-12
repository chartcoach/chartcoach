import { defineConfig } from "vite-plus";

import {
  antiSlopIgnorePatterns,
  antiSlopRules,
  antiSlopEffectRules,
} from "./tools/oxlint/anti-slop/preset.ts";

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
      { name: "anti-slop-effect", specifier: "./tools/oxlint/anti-slop/effect/index.ts" },
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
      "oxc/no-accumulating-spread": "error",
      "vite-plus/prefer-vite-plus-imports": "error",
    },
    overrides: [
      { files: ["apps/chat/**"], rules: antiSlopEffectRules },
      {
        files: ["apps/chat/components/**"],
        rules: {
          "no-restricted-imports": [
            "error",
            {
              patterns: [
                {
                  group: [
                    "node:*",
                    "eve",
                    "eve/channels*",
                    "../**/browser/**",
                    "../**/lib/**",
                    "../**/agent/**",
                  ],
                  message:
                    "Components render UI and dispatch hook commands. Keep transport and server code in their owning layers.",
                },
              ],
            },
          ],
          "no-restricted-globals": [
            "error",
            {
              name: "fetch",
              message: "Keep request lifecycles in a hook and transport calls in browser/.",
            },
          ],
        },
      },
      {
        files: ["packages/catalog/src/catalog/**", "packages/catalog/src/index.ts"],
        rules: {
          "no-restricted-imports": [
            "error",
            {
              patterns: [
                "node:*",
                "@chartcoach/*",
                "../node/**",
                "./node/**",
                "../**/apps/**",
                "../**/brand/**",
              ],
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
