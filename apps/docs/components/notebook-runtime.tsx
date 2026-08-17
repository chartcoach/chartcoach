"use client";

import { useEffect } from "react";

import * as catalogSdk from "@chartcoach/catalog";
import { MarimoIslandRuntime } from "@marimo-team/mdx-marimo/react";

declare global {
  var ChartCoachCatalog: typeof catalogSdk | undefined;
}

export function PythonNotebookRuntime() {
  return <MarimoIslandRuntime />;
}

export function CatalogNotebookRuntime() {
  useEffect(() => {
    globalThis.ChartCoachCatalog = catalogSdk;
    return () => {
      delete globalThis.ChartCoachCatalog;
    };
  }, []);

  return <MarimoIslandRuntime />;
}
