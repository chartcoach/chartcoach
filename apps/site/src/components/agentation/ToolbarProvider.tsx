import { useEffect, useState } from "react";
import { Agentation } from "agentation";

const MIN_DESKTOP_WIDTH = 768;

function supportsAgentationViewport() {
  if (typeof window === "undefined") return false;
  return window.innerWidth >= MIN_DESKTOP_WIDTH && window.matchMedia("(pointer: fine)").matches;
}

export default function ToolbarProvider() {
  const [isSupportedViewport, setIsSupportedViewport] = useState(() =>
    supportsAgentationViewport(),
  );

  useEffect(() => {
    const updateViewportSupport = () => {
      setIsSupportedViewport(supportsAgentationViewport());
    };

    updateViewportSupport();

    const mediaQuery = window.matchMedia("(pointer: fine)");
    window.addEventListener("resize", updateViewportSupport);
    mediaQuery.addEventListener("change", updateViewportSupport);

    return () => {
      window.removeEventListener("resize", updateViewportSupport);
      mediaQuery.removeEventListener("change", updateViewportSupport);
    };
  }, []);

  const endpoint = import.meta.env.PUBLIC_AGENTATION_ENDPOINT?.trim() || undefined;

  if (!isSupportedViewport) return null;

  return <Agentation className="cc-agentation-toolbar" endpoint={endpoint} />;
}
