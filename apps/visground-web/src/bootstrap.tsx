import {
  createParquetViewerBridge,
  mountVisgroundViewer,
  parseViewerRuntimeConfig,
  type ViewerRuntimeConfig,
} from "@chartcoach/visground-viewer";

const DEFAULT_IMAGE_BASE_URL = "";
const DEFAULT_ARTIFACT_URL = `${window.location.origin}/data/viewer.parquet`;
const ARTIFACT_URL = import.meta.env.VITE_VISGROUND_VIEWER_PARQUET_URL ?? DEFAULT_ARTIFACT_URL;
const RUNTIME_CONFIG_URL =
  import.meta.env.VITE_VISGROUND_VIEWER_CONFIG_URL ?? deriveRuntimeConfigUrl(ARTIFACT_URL);
const IMAGE_BASE_URL =
  import.meta.env.VITE_VISGROUND_VIEWER_IMAGE_BASE_URL ?? DEFAULT_IMAGE_BASE_URL;

function deriveRuntimeConfigUrl(artifactUrl: string) {
  const parsed = new URL(artifactUrl, window.location.origin);
  parsed.pathname = parsed.pathname.endsWith(".parquet")
    ? parsed.pathname.replace(/\.parquet$/, ".config.json")
    : `${parsed.pathname}.config.json`;
  return parsed.toString();
}

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

async function loadRuntimeConfig(url: string): Promise<ViewerRuntimeConfig> {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to load viewer runtime config from ${url} (${response.status}).`);
  }
  return parseViewerRuntimeConfig(await response.json());
}

export async function bootStandaloneViewer() {
  const target = document.getElementById("root");
  if (!target) {
    throw new Error("Standalone viewer root not found.");
  }

  applyStandaloneTheme();

  const runtimeConfig = await loadRuntimeConfig(RUNTIME_CONFIG_URL);
  const bridge = createParquetViewerBridge({
    artifactUrl: ARTIFACT_URL,
    runtimeConfig,
    resolveImageUrl: resolveViewerImageUrl,
  });
  mountVisgroundViewer(target, { bridge });
}

export function expectedStandaloneViewerAssets() {
  return {
    artifactUrl: ARTIFACT_URL,
    runtimeConfigUrl: RUNTIME_CONFIG_URL,
  };
}
