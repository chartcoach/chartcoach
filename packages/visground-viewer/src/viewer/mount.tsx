import { createRoot, type Root } from "react-dom/client";
import type { AnywidgetModelLike } from "./contract/types";
import { createAnywidgetViewerBridge } from "./bridge/anywidget";
import type { ViewerBridge } from "./bridge/types";
import { ViewerRoot } from "./render/viewer-root";
import styleText from "./styles/viewer.css?inline";

interface ViewerMount {
  update(next: { bridge?: ViewerBridge; model?: AnywidgetModelLike }): void;
  destroy(): void;
}

function resolveTheme(target: HTMLElement): "light" | "dark" {
  const scopedTheme =
    target.closest<HTMLElement>("[data-theme]")?.dataset.theme ??
    document.documentElement.dataset.theme ??
    document.body.dataset.theme;
  if (scopedTheme === "dark" || scopedTheme === "light") {
    return scopedTheme;
  }

  if (
    document.documentElement.classList.contains("dark") ||
    document.body.classList.contains("dark")
  ) {
    return "dark";
  }

  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function bindTheme(target: HTMLElement, container: HTMLElement) {
  const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");

  const syncTheme = () => {
    const theme = resolveTheme(target);
    container.dataset.theme = theme;
    container.classList.toggle("dark", theme === "dark");
  };

  syncTheme();

  const observer = new MutationObserver(syncTheme);
  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["class", "data-theme"],
  });
  observer.observe(document.body, {
    attributes: true,
    attributeFilter: ["class", "data-theme"],
  });

  mediaQuery.addEventListener("change", syncTheme);

  return () => {
    observer.disconnect();
    mediaQuery.removeEventListener("change", syncTheme);
  };
}

function createStyledHost(target: HTMLElement): {
  cleanupTheme: () => void;
  renderHost: HTMLElement;
} {
  target.replaceChildren();
  const container = document.createElement("div");
  container.className = "bg-background text-foreground";
  container.style.width = "100%";
  container.style.display = "block";
  const style = document.createElement("style");
  style.textContent = styleText;
  container.appendChild(style);
  const renderHost = document.createElement("div");
  container.appendChild(renderHost);
  target.appendChild(container);
  return {
    cleanupTheme: bindTheme(target, container),
    renderHost,
  };
}

function renderMountError(host: HTMLElement, error: unknown) {
  console.error("[visground-viewer] mount failed", error);
  host.replaceChildren();

  const panel = document.createElement("div");
  panel.className = "vg-root bg-background text-foreground";

  const banner = document.createElement("div");
  banner.className =
    "mx-auto w-full max-w-[84rem] px-3 pb-3 pt-1 text-foreground md:px-4 lg:max-w-[74rem]";
  const body = document.createElement("div");
  body.className = "mt-4 grid gap-1 border border-border bg-card px-4 py-3 text-card-foreground";
  const title = document.createElement("strong");
  title.textContent = "Viewer error";
  const message = document.createElement("p");
  message.className = "m-0 leading-[1.48] text-muted-foreground";
  message.textContent =
    error instanceof Error ? error.message : String(error || "Unknown viewer error.");

  body.append(title, message);
  banner.appendChild(body);
  panel.appendChild(banner);
  host.appendChild(panel);
}

export function mountVisgroundViewer(
  target: HTMLElement,
  options: { bridge: ViewerBridge },
): ViewerMount {
  let current = { ...options };
  const { cleanupTheme, renderHost } = createStyledHost(target);
  const root: Root = createRoot(renderHost, {
    onCaughtError: (error) => {
      renderMountError(renderHost, error);
    },
    onRecoverableError: (error) => {
      console.error("[visground-viewer] recoverable error", error);
    },
    onUncaughtError: (error) => {
      renderMountError(renderHost, error);
    },
  });

  function render() {
    root.render(<ViewerRoot bridge={current.bridge} />);
  }

  render();

  return {
    update(next) {
      current = {
        ...current,
        ...next,
      };
      render();
    },
    destroy() {
      cleanupTheme();
      current.bridge.destroy?.();
      root.unmount();
      target.replaceChildren();
    },
  };
}

export function mountAnywidgetVisgroundViewer(
  target: HTMLElement,
  options: { model: AnywidgetModelLike; artifactUrl: string },
): ViewerMount {
  return mountVisgroundViewer(target, {
    bridge: createAnywidgetViewerBridge(options.model, options.artifactUrl),
  });
}
