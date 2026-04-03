import { createElement } from "react";
import { createRoot } from "react-dom/client";
import ToolbarProvider from "./ToolbarProvider";

const mount = document.getElementById("cc-agentation-root");

if (mount && !mount.dataset.agentationMounted) {
  mount.dataset.agentationMounted = "true";
  createRoot(mount).render(createElement(ToolbarProvider));
}
