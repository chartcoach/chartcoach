import { useEffect, useState } from "react";

export function useViewportHeight() {
  const [height, setHeight] = useState<number>();
  useEffect(() => {
    const viewport = window.visualViewport;

    if (!viewport) return;
    // Safari keeps the layout viewport tall when its software keyboard opens.
    const resize = () => setHeight(viewport.height + viewport.offsetTop);
    resize();
    viewport.addEventListener("resize", resize);
    viewport.addEventListener("scroll", resize);

    return () => {
      viewport.removeEventListener("resize", resize);
      viewport.removeEventListener("scroll", resize);
    };
  }, []);

  return height;
}
