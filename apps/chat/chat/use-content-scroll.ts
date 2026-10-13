import { useCallback, useLayoutEffect, useRef, useState } from "react";

export function useContentScroll(initial: "top" | "bottom" = "top", enabled = true) {
  const [atLatest, setAtLatest] = useState(true);
  const [viewport, setViewport] = useState<HTMLDivElement | null>(null);
  const scroll = useRef<() => void>(() => {});
  const viewportRef = useCallback((node: HTMLDivElement | null) => setViewport(node), []);

  useLayoutEffect(() => {
    if (!enabled || !viewport) return;
    const content = viewport.firstElementChild;

    if (!content) return;

    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    let following = initial === "bottom";
    let reveal: HTMLElement | null = null;
    let destination: number | null = null;
    let frame = 0;
    let revealFrame = 0;
    let lastTime = 0;
    let lastTop = viewport.scrollTop;
    let lastMaximum = 0;
    let touchY: number | null = null;

    const maximum = () => Math.max(0, viewport.scrollHeight - viewport.clientHeight);
    const nearBottom = () => maximum() - viewport.scrollTop < 4;

    const stop = () => {
      cancelAnimationFrame(frame);
      cancelAnimationFrame(revealFrame);
      frame = 0;
      revealFrame = 0;
      destination = null;
      reveal = null;
    };

    const updateState = () => setAtLatest(following || nearBottom());

    const animate = (time: number) => {
      frame = 0;

      if (destination === null) return;
      const target = Math.min(destination, maximum());
      const distance = target - viewport.scrollTop;
      const elapsed = Math.min(64, time - lastTime);
      lastTime = time;
      const previousTop = viewport.scrollTop;
      viewport.scrollTop =
        reducedMotion.matches || Math.abs(distance) < 1
          ? target
          : viewport.scrollTop + distance * (1 - Math.exp(-elapsed / 65));

      if (viewport.scrollTop === previousTop && Math.abs(distance) >= 1) {
        viewport.scrollTop = target;
      }

      lastTop = viewport.scrollTop;

      if (Math.abs(target - viewport.scrollTop) >= 1) {
        frame = requestAnimationFrame(animate);
      } else {
        viewport.scrollTop = target;
        lastTop = viewport.scrollTop;
        destination = null;
      }

      updateState();
    };

    const moveTo = (top: number) => {
      destination = Math.max(0, Math.min(top, maximum()));

      if (!frame) {
        lastTime = performance.now();
        frame = requestAnimationFrame(animate);
      }
    };

    const scrollToLatest = () => {
      stop();
      following = true;
      moveTo(maximum());
      updateState();
    };

    scroll.current = scrollToLatest;

    const resize = () => {
      const nextMaximum = maximum();

      if (following && nextMaximum < lastMaximum && viewport.scrollTop >= nextMaximum - 1) {
        lastTop = viewport.scrollTop;
      }

      lastMaximum = nextMaximum;

      // Measure the disclosure on every animation frame reported by ResizeObserver.
      if (reveal && viewport.contains(reveal)) {
        const revealRect = reveal.getBoundingClientRect();
        const viewportRect = viewport.getBoundingClientRect();
        const bottom = revealRect.bottom - viewportRect.bottom;

        if (revealRect.height > viewport.clientHeight - 24) {
          moveTo(viewport.scrollTop + revealRect.top - viewportRect.top - 12);
        } else if (bottom > 0) {
          moveTo(viewport.scrollTop + bottom + 12);
        }
      } else if (following) {
        moveTo(maximum());
      }

      updateState();
    };

    const onScroll = () => {
      const nextMaximum = maximum();

      const layoutClamp =
        following && nextMaximum < lastMaximum && viewport.scrollTop >= nextMaximum - 1;

      if (viewport.scrollTop < lastTop - 1 && !layoutClamp) {
        following = false;
        stop();
      } else if (!frame && nearBottom()) {
        following = true;
      }

      lastMaximum = nextMaximum;
      lastTop = viewport.scrollTop;
      updateState();
    };

    const pause = () => {
      following = false;
      stop();
      updateState();
    };

    const onWheel = (event: WheelEvent) => {
      if (event.deltaY < 0) pause();
    };

    const onTouchStart = (event: TouchEvent) => {
      touchY = event.touches[0]?.clientY ?? null;
    };

    const onTouchMove = (event: TouchEvent) => {
      const nextY = event.touches[0]?.clientY;

      if (touchY !== null && nextY !== undefined && nextY > touchY + 2) pause();
      touchY = nextY ?? null;
    };

    const onKey = (event: KeyboardEvent) => {
      if (["ArrowUp", "PageUp", "Home"].includes(event.key)) pause();
    };

    const onClick = (event: MouseEvent) => {
      if (!(event.target instanceof Element)) return;
      const trigger = event.target.closest("summary, button[aria-expanded]");

      if (!trigger) return;

      if (trigger.matches(":disabled, [aria-disabled='true']")) return;

      const details = trigger.closest("details");

      const controlled = document.getElementById(trigger.getAttribute("aria-controls") ?? "");
      const target = details ?? controlled ?? trigger.parentElement;

      if (!(target instanceof HTMLElement) || !viewport.contains(target)) return;
      stop();
      revealFrame = requestAnimationFrame(() => {
        revealFrame = 0;
        const open = details ? details.open : trigger.getAttribute("aria-expanded") === "true";

        if (!open || !viewport.contains(target)) return;
        reveal = target;
        following = false;
        resize();
      });
    };

    const observer = new ResizeObserver(resize);
    observer.observe(viewport);
    observer.observe(content);
    viewport.addEventListener("scroll", onScroll, { passive: true });
    viewport.addEventListener("wheel", onWheel, { passive: true });
    viewport.addEventListener("touchstart", onTouchStart, { passive: true });
    viewport.addEventListener("touchmove", onTouchMove, { passive: true });
    viewport.addEventListener("keydown", onKey);
    viewport.addEventListener("click", onClick, true);

    if (initial === "bottom") viewport.scrollTop = maximum();
    lastTop = viewport.scrollTop;
    lastMaximum = maximum();
    following ||= nearBottom();
    updateState();

    return () => {
      stop();
      observer.disconnect();
      scroll.current = () => {};

      viewport.removeEventListener("scroll", onScroll);
      viewport.removeEventListener("wheel", onWheel);
      viewport.removeEventListener("touchstart", onTouchStart);
      viewport.removeEventListener("touchmove", onTouchMove);
      viewport.removeEventListener("keydown", onKey);
      viewport.removeEventListener("click", onClick, true);
    };
  }, [enabled, initial, viewport]);

  return { viewportRef, atLatest, scrollToLatest: useCallback(() => scroll.current(), []) };
}
