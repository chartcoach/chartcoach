import type { ReactNode } from "react";
import { renderToStaticMarkup } from "react-dom/server";

/** Parse server output for semantic assertions in jsdom tests, without mounting effects. */
export function renderDocument(element: ReactNode): Document {
  return new DOMParser().parseFromString(renderToStaticMarkup(element), "text/html");
}
