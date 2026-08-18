/** @vitest-environment jsdom */

import { act, createElement } from "react";
import { createRoot } from "react-dom/client";
import { afterEach, beforeEach, describe, expect, test, vi } from "vite-plus/test";

import { CatalogNotebookRuntime } from "../components/notebook-runtime";

const probeElement = "catalog-sdk-probe";

declare global {
  var IS_REACT_ACT_ENVIRONMENT: boolean | undefined;
}

class CatalogSdkProbe extends HTMLElement {
  connectedCallback() {
    this.dataset.sdkReady = String(Boolean(globalThis.ChartCoachCatalog?.openCatalog));
  }
}

if (!customElements.get(probeElement)) {
  customElements.define(probeElement, CatalogSdkProbe);
}

beforeEach(() => {
  globalThis.IS_REACT_ACT_ENVIRONMENT = true;
});

afterEach(() => {
  delete globalThis.IS_REACT_ACT_ENVIRONMENT;
  document.body.replaceChildren();
  vi.unstubAllGlobals();
});

describe("catalog notebook runtime", () => {
  test("binds the SDK before a registered element connects", async () => {
    vi.stubGlobal("requestAnimationFrame", () => 1);
    vi.stubGlobal("cancelAnimationFrame", () => undefined);
    const container = document.createElement("div");
    document.body.append(container);
    const root = createRoot(container);

    await act(async () => {
      root.render(
        createElement(
          "div",
          null,
          createElement(CatalogNotebookRuntime),
          createElement(probeElement),
        ),
      );
    });

    expect(container.querySelector(probeElement)?.getAttribute("data-sdk-ready")).toBe("true");
    await act(async () => root.unmount());
  });
});
