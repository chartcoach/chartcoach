"use client";

import { MarimoIslandRuntime } from "@marimo-team/mdx-marimo/react";

import * as catalogSdk from "@chartcoach/catalog";

type CatalogHost = {
  ChartCoachCatalog?: typeof catalogSdk;
};

declare global {
  var ChartCoachCatalog: typeof catalogSdk | undefined;
}

function bindCatalogSdk(host: CatalogHost): void {
  host.ChartCoachCatalog = catalogSdk;
}

if (globalThis.window) {
  bindCatalogSdk(globalThis);
}

export function PythonNotebookRuntime() {
  return <MarimoIslandRuntime />;
}

export function CatalogNotebookRuntime() {
  return <MarimoIslandRuntime />;
}
