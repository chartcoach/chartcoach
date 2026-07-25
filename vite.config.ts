import { defineConfig } from "vite-plus";

export default defineConfig({
  fmt: {
    printWidth: 100,
  },
  lint: {
    categories: {
      correctness: "error",
    },
    jsPlugins: [{ name: "vite-plus", specifier: "vite-plus/oxlint-plugin" }],
    options: {
      denyWarnings: true,
      typeAware: true,
    },
    plugins: ["typescript", "unicorn", "import"],
    rules: {
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
