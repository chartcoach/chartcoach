import { useEffect, useLayoutEffect, useRef, useState } from "react";
import { motion } from "./tokens.stylex";

const stagger = 40;

const maxStagger = 4;

const reducedMotion = () =>
  globalThis.matchMedia?.("(prefers-reduced-motion: reduce)").matches ?? false;

interface ListEntry<T> {
  key: string;
  item: T;
  leaving: boolean;
}

/** Keeps leaving entries beside the neighbors they had, so they collapse in place. */
function mergeEntries<T>(
  previous: readonly ListEntry<T>[],
  items: readonly T[],
  getKey: (item: T) => string,
) {
  const next = items.map((item) => ({ key: getKey(item), item, leaving: false }));
  const keys = new Map(next.map((entry, index) => [entry.key, index]));
  const merged: ListEntry<T>[] = [];
  let cursor = 0;

  for (const entry of previous) {
    const index = keys.get(entry.key);

    if (index === undefined) merged.push({ ...entry, leaving: true });
    else while (cursor <= index) merged.push(next[cursor++]!);
  }

  return [...merged, ...next.slice(cursor)];
}

/**
 * Keeps removed items rendered as leaving entries until `useListMotion` has
 * collapsed them. Render leaving entries with `data-motion-leaving`.
 */
export function useListPresence<T>(items: readonly T[], getKey: (item: T) => string) {
  const [state, setState] = useState(() => ({ items, entries: mergeEntries([], items, getKey) }));
  let { entries } = state;

  if (state.items !== items) {
    entries = mergeEntries(state.entries, items, getKey);
    setState({ items, entries });
  }

  const leaving = entries.flatMap((entry) => (entry.leaving ? [entry.key] : [])).join("\n");

  useEffect(() => {
    if (!leaving) return;

    const timer = setTimeout(
      () =>
        setState((current) => ({
          ...current,
          entries: current.entries.filter((entry) => !entry.leaving),
        })),
      reducedMotion() ? 0 : parseFloat(motion.move) + 40,
    );

    return () => clearTimeout(timer);
  }, [leaving]);

  return entries;
}

/**
 * Animates the keyed children of a list after each render. Children that join
 * after the first render expand into place, children marked as leaving collapse
 * where they are, and children that change order glide from where they were
 * drawn. Children opt in with `data-motion-key`; the list must be their offset
 * parent. A new `scope`, such as a changed filter, shows its children at once.
 */
export function useListMotion<E extends HTMLElement>(scope?: string) {
  const ref = useRef<E>(null);
  const baseline = useRef<{ scope?: string; tops: Map<string, number> }>(undefined);

  useLayoutEffect(() => {
    const list = ref.current;

    if (!list) return;

    const nodes = Array.from(list.children).filter(
      (node): node is HTMLElement => node instanceof HTMLElement && !!node.dataset.motionKey,
    );

    const present = nodes.filter((node) => node.dataset.motionLeaving === undefined);
    const keys = present.map((node) => node.dataset.motionKey!);
    const last = baseline.current;
    const previous = last && last.scope === scope ? last.tops : undefined;

    // A list that was empty appears with its section, so its first children skip
    // the entrance that later arrivals get.
    const animate = !!previous?.size && !!list.animate && !reducedMotion();

    const resize = { duration: parseFloat(motion.move), easing: motion.fluid };
    let joining = 0;

    if (animate)
      for (const node of nodes) {
        const running = node.getAnimations();
        const exiting = running.some((animation) => animation.id === "exit");
        const leaving = node.dataset.motionLeaving !== undefined;

        if (leaving ? exiting : previous.has(node.dataset.motionKey!)) continue;

        // Start from what is drawn, so an interrupted entrance or exit reverses in place.
        const shown = leaving || exiting;
        const height = shown ? node.offsetHeight : 0;
        const opacity = shown ? Number(getComputedStyle(node).opacity) : 0;

        for (const animation of running) animation.cancel();

        node.animate(
          [
            { height: `${height}px`, opacity },
            { height: `${leaving ? 0 : node.offsetHeight}px`, opacity: leaving ? 0 : 1 },
          ].map((frame) => ({ ...frame, overflow: "hidden" })),
          leaving
            ? { ...resize, id: "exit", fill: "forwards" }
            : {
                ...resize,
                id: "enter",
                delay: Math.min(joining++, maxStagger) * stagger,
                fill: "backwards",
              },
        );
      }

    baseline.current = {
      scope,
      tops: new Map(present.map((node, index) => [keys[index]!, node.offsetTop])),
    };

    if (!animate) return;
    // Joining and leaving children move their neighbors as they resize. Glide
    // only when children that stay change order.
    const before = [...previous.keys()].filter((key) => keys.includes(key));
    const after = keys.filter((key) => previous.has(key));

    if (before.every((key, index) => key === after[index])) return;

    for (const [index, node] of present.entries()) {
      const top = previous.get(keys[index]!);

      if (top === undefined) continue;
      // Continue from the drawn position when a previous glide is still running.
      const drawn = getComputedStyle(node).transform;
      const offset = drawn === "none" ? 0 : new DOMMatrixReadOnly(drawn).m42;
      const distance = top + offset - node.offsetTop;

      if (Math.abs(distance) < 1) continue;

      for (const running of node.getAnimations()) if (running.id === "glide") running.cancel();
      node.animate([{ transform: `translateY(${distance}px)` }, { transform: "none" }], {
        ...resize,
        id: "glide",
      });
    }
  });

  return ref;
}
