import { createRoot, type Root } from "react-dom/client";
import type { AnywidgetModelLike } from "@/viewer/contract/types";
import { ViewerRoot } from "@/viewer/render/viewer-root";
import styleText from "@/viewer/styles/viewer.css?inline";

interface ViewerMount {
  update(next: { model?: AnywidgetModelLike }): void;
  destroy(): void;
}

function createStyledHost(target: HTMLElement): HTMLElement {
  target.replaceChildren();
  const container = document.createElement("div");
  container.style.width = "100%";
  container.style.display = "block";
  const style = document.createElement("style");
  style.textContent = styleText;
  container.appendChild(style);
  const renderHost = document.createElement("div");
  container.appendChild(renderHost);
  target.appendChild(container);
  return renderHost;
}

function renderMountError(host: HTMLElement, error: unknown) {
  console.error("[visground-viewer] mount failed", error);
  host.replaceChildren();

  const panel = document.createElement("div");
  panel.className = "vg-root";

  const banner = document.createElement("div");
  banner.className = "vg-shell";
  banner.innerHTML = `
    <div class="vg-error-banner">
      <strong>Viewer error</strong>
      <p class="vg-copy">${
        error instanceof Error ? error.message : String(error || "Unknown viewer error.")
      }</p>
    </div>
  `;

  panel.appendChild(banner);
  host.appendChild(panel);
}

export function mountVisgroundViewer(
  target: HTMLElement,
  options: { model: AnywidgetModelLike },
): ViewerMount {
  let current = { ...options };
  const host = createStyledHost(target);
  const root: Root = createRoot(host, {
    onCaughtError: (error) => {
      renderMountError(host, error);
    },
    onRecoverableError: (error) => {
      console.error("[visground-viewer] recoverable error", error);
    },
    onUncaughtError: (error) => {
      renderMountError(host, error);
    },
  });

  function render() {
    root.render(<ViewerRoot model={current.model} />);
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
      root.unmount();
      target.replaceChildren();
    },
  };
}
