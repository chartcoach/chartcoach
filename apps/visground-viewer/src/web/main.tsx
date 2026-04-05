import { createParquetViewerBridge } from "../viewer/bridge/parquet";
import { mountVisgroundViewer } from "../viewer/mount";

const DEFAULT_ARTIFACT_URL = `${window.location.origin}/data/viewer.parquet`;
const ARTIFACT_URL = import.meta.env.VITE_VISGROUND_VIEWER_PARQUET_URL ?? DEFAULT_ARTIFACT_URL;
const CHARTS_BASE_URL =
  import.meta.env.VITE_VISGROUND_VIEWER_CHARTS_BASE_URL ?? `${window.location.origin}/charts`;

function applyStandaloneTheme() {
  const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
  const readStoredTheme = () => {
    const storedTheme = window.localStorage.getItem("theme");
    return storedTheme === "dark" || storedTheme === "light" ? storedTheme : null;
  };

  const syncTheme = () => {
    const theme = readStoredTheme() ?? (mediaQuery.matches ? "dark" : "light");
    document.documentElement.dataset.theme = theme;
    document.documentElement.classList.toggle("dark", theme === "dark");
  };

  syncTheme();
  mediaQuery.addEventListener("change", syncTheme);
}

async function main() {
  const target = document.getElementById("root");
  if (!target) {
    throw new Error("Standalone viewer root not found.");
  }

  applyStandaloneTheme();

  const bridge = createParquetViewerBridge({
    artifactUrl: ARTIFACT_URL,
    resolveImageUrl(imageUrl) {
      if (!imageUrl) {
        return imageUrl;
      }
      try {
        const parsed = new URL(imageUrl, window.location.origin);
        if (
          (parsed.hostname === "localhost" || parsed.hostname === "127.0.0.1") &&
          parsed.port === "3434"
        ) {
          const filename = parsed.pathname.split("/").filter(Boolean).at(-1);
          if (filename) {
            return `${CHARTS_BASE_URL.replace(/\/$/, "")}/${filename}`;
          }
        }
      } catch {
        return imageUrl;
      }
      return imageUrl;
    },
  });
  mountVisgroundViewer(target, { bridge });
}

void main().catch((error) => {
  console.error("[visground-viewer:web] bootstrap failed", error);
  const target = document.getElementById("root");
  if (!target) {
    return;
  }
  target.innerHTML = `
    <main style="font-family: Inter, sans-serif; padding: 24px; color: #111;">
      <h1 style="margin: 0 0 12px; font-size: 20px;">Viewer bootstrap failed</h1>
      <p style="margin: 0 0 8px;">${error instanceof Error ? error.message : String(error)}</p>
      <p style="margin: 0;">Expected artifact: <code>${ARTIFACT_URL}</code></p>
    </main>
  `;
});
