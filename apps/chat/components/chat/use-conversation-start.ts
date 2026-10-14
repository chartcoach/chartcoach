import { useLayoutEffect, useRef, useState } from "react";
import { motion } from "../ui/tokens.stylex";

const reducedMotion = () => matchMedia("(prefers-reduced-motion: reduce)").matches;

/** Layout position, unaffected by a glide that is still running. */
const center = (node: HTMLElement | null) =>
  node ? node.offsetLeft + node.offsetWidth / 2 : undefined;

/**
 * Layout offset inside the column. A gliding column is transformed, which makes
 * it the composer's offset parent until the glide finishes.
 */
const offset = (node: HTMLElement | null, column: HTMLElement | null) =>
  node && column
    ? node.offsetTop - (node.offsetParent === column ? 0 : column.offsetTop)
    : undefined;

type Origin = { center?: number; top?: number };

/**
 * Moves between the welcome and a conversation. The welcome recedes before the
 * first turn's layout commits, then the thread column glides aside for the
 * guidelines panel and the composer glides from the centered welcome to the
 * bottom. A new chat glides both back as the welcome returns. A saved
 * conversation skips the welcome and fades in once its history loads.
 */
export function useConversationStart(empty: boolean, restoring: boolean) {
  const [welcome, setWelcome] = useState(empty && !restoring);
  const [restored, setRestored] = useState(!restoring);
  const origin = useRef<Origin>(undefined);
  const welcomeRef = useRef<HTMLElement>(null);
  const startersRef = useRef<HTMLElement>(null);
  const columnRef = useRef<HTMLDivElement>(null);
  const composerRef = useRef<HTMLDivElement>(null);
  const messagesRef = useRef<HTMLDivElement>(null);
  const panelRef = useRef<HTMLElement>(null);
  const leaving = welcome && !empty;

  if (empty && !restoring && !welcome) setWelcome(true);

  if (!restoring && !restored) setRestored(true);

  const measure = (): Origin => ({
    center: center(columnRef.current),
    top: offset(composerRef.current, columnRef.current),
  });

  useLayoutEffect(() => {
    if (!leaving) return;
    const nodes = [welcomeRef.current, startersRef.current];
    // Browsers without Web Animations hand over immediately.
    const duration = nodes[0]?.animate && !reducedMotion() ? parseFloat(motion.exit) : 0;

    const exits = nodes.map((node) =>
      node?.animate?.([{ opacity: 1 }, { opacity: 0, transform: "scale(0.985)" }], {
        duration,
        easing: motion.easeOutCubic,
        fill: "forwards",
      }),
    );

    // The welcome is nearly transparent two thirds of the way through its exit.
    const handoff = setTimeout(() => {
      origin.current = measure();
      setWelcome(false);
    }, duration * 0.65);

    return () => {
      clearTimeout(handoff);

      for (const exit of exits) exit?.cancel();
    };
  }, [leaving]);

  useLayoutEffect(() => {
    const from = origin.current;
    const column = columnRef.current;
    const composer = composerRef.current;
    origin.current = undefined;

    if (!from || !column?.animate) return;
    const reduce = reducedMotion();
    const glide = { duration: parseFloat(motion.move), easing: motion.easeInOut };
    const enter = { duration: parseFloat(motion.enter), easing: motion.easeOut };
    const rise = from.top === undefined ? 0 : from.top - (offset(composer, column) ?? from.top);

    column.animate(
      [
        { transform: `translateX(${reduce ? 0 : from.center! - center(column)!}px)` },
        { transform: "none" },
      ],
      glide,
    );

    // The composer moves between the centered welcome and the bottom of the column.
    if (!reduce && Math.abs(rise) >= 1)
      composer?.animate([{ transform: `translateY(${rise}px)` }, { transform: "none" }], glide);

    if (welcome)
      for (const node of [welcomeRef.current, startersRef.current])
        node?.animate(
          [
            { opacity: 0, transform: reduce ? "none" : "scale(0.985)" },
            { opacity: 1, transform: "none" },
          ],
          enter,
        );
    else
      panelRef.current?.animate(
        [
          { opacity: 0, transform: `translateX(${reduce ? 0 : 16}px)` },
          { opacity: 1, transform: "none" },
        ],
        { ...enter, delay: 120, fill: "backwards" },
      );
  }, [welcome]);

  // Restored history fades in on the render that first shows it.
  useLayoutEffect(() => {
    if (!restored || welcome) return;
    const fade = { duration: parseFloat(motion.enter), easing: motion.easeOut };

    for (const node of [messagesRef.current, panelRef.current])
      node?.animate?.([{ opacity: 0 }, { opacity: 1 }], fade);
  }, [restored]);

  // Remember where the conversation column and composer sit, so a new chat glides from there.
  useLayoutEffect(() => {
    const column = columnRef.current;

    if (welcome || !column) return;

    const observer = new ResizeObserver(() => {
      origin.current = measure();
    });

    observer.observe(column);

    if (composerRef.current) observer.observe(composerRef.current);

    return () => observer.disconnect();
  }, [welcome]);

  return {
    welcome,
    welcomeRef,
    startersRef,
    columnRef,
    composerRef,
    messagesRef,
    panelRef,
  };
}
