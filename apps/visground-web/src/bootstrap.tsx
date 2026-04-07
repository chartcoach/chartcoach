import { mountVisgroundViewer } from "@chartcoach/visground-viewer";
import { createParquetViewerBridge } from "@chartcoach/visground-viewer/parquet-bridge";

const DEFAULT_IMAGE_BASE_URL =
  "https://files.peter.gy/projects/cc/supplementary/05-empirical-study/03-pipeline/03_generated_charts/";
const DEFAULT_ARTIFACT_URL = `${window.location.origin}/data/viewer.parquet`;
const ARTIFACT_URL = import.meta.env.VITE_VISGROUND_VIEWER_PARQUET_URL ?? DEFAULT_ARTIFACT_URL;
const IMAGE_BASE_URL =
  import.meta.env.VITE_VISGROUND_VIEWER_IMAGE_BASE_URL ??
  import.meta.env.VITE_VISGROUND_VIEWER_CHARTS_BASE_URL ??
  DEFAULT_IMAGE_BASE_URL;

function resolveViewerImageUrl(imageUrl: string | null) {
  if (!imageUrl) {
    return imageUrl;
  }

  const normalizedBaseUrl = IMAGE_BASE_URL.trim().replace(/\/$/, "");
  if (!normalizedBaseUrl) {
    return imageUrl;
  }

  try {
    const parsed = new URL(imageUrl, window.location.origin);
    const filename = parsed.pathname.split("/").filter(Boolean).at(-1);
    if (!filename) {
      return imageUrl;
    }
    return `${normalizedBaseUrl}/${filename}`;
  } catch {
    return imageUrl;
  }
}

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

export function bootStandaloneViewer() {
  const target = document.getElementById("root");
  if (!target) {
    throw new Error("Standalone viewer root not found.");
  }

  applyStandaloneTheme();

  const bridge = createParquetViewerBridge({
    artifactUrl: ARTIFACT_URL,
    resolveImageUrl: resolveViewerImageUrl,
  });
  mountVisgroundViewer(target, { bridge });
}
