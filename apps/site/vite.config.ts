import { defineConfig } from "vite-plus";

export default defineConfig({
  resolve: {
    conditions: ["source"],
  },
  test: {
    environment: "node",
    include: ["test/**/*.test.ts"],
  },
});
