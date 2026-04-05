import { createReadStream, existsSync, statSync } from "node:fs";
import { dirname, extname, normalize, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

const __dirname = dirname(fileURLToPath(import.meta.url));
const chartsDirectory = resolve(__dirname, "../visground/data/artifacts/charts");

function mimeTypeFor(pathname) {
  switch (extname(pathname).toLowerCase()) {
    case ".png":
      return "image/png";
    case ".jpg":
    case ".jpeg":
      return "image/jpeg";
    case ".webp":
      return "image/webp";
    case ".svg":
      return "image/svg+xml";
    default:
      return "application/octet-stream";
  }
}

function serveChartsPlugin() {
  const handleChartsRequest = (req, res, next) => {
    if (!req.url || !req.url.startsWith("/charts/")) {
      next();
      return;
    }

    const relativePath = normalize(decodeURIComponent(req.url.replace(/^\/charts\//, "")));
    const targetPath = resolve(chartsDirectory, relativePath);
    if (
      !targetPath.startsWith(chartsDirectory) ||
      !existsSync(targetPath) ||
      !statSync(targetPath).isFile()
    ) {
      res.statusCode = 404;
      res.end("Not found");
      return;
    }

    res.setHeader("Content-Type", mimeTypeFor(targetPath));
    createReadStream(targetPath).pipe(res);
  };

  return {
    name: "chartcoach-viewer-serve-charts",
    configureServer(server) {
      server.middlewares.use(handleChartsRequest);
    },
    configurePreviewServer(server) {
      server.middlewares.use(handleChartsRequest);
    },
  };
}

export default defineConfig({
  plugins: [react(), tailwindcss(), serveChartsPlugin()],
  resolve: {
    conditions: ["chartcoach-source", "module", "browser", "development|production"],
  },
  server: {
    host: "127.0.0.1",
    port: 4174,
    strictPort: true,
  },
  preview: {
    host: "127.0.0.1",
    port: 4174,
    strictPort: true,
  },
});
