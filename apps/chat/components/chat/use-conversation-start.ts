import { useLayoutEffect, useRef, useState } from "react";
import { motion } from "../ui/tokens.stylex";

const reducedMotion = () => matchMedia("(prefers-reduced-motion: reduce)").matches;

/** Layout position, unaffected by a glide that is still running. */
const center = (node: HTMLElement | null) =>
  node ? node.offsetLeft + node.offsetWidth / 2 : undefined;

/**
 * Moves between the welcome and a conversation. The welcome recedes before the
 * first turn's layout commits, then the thread column glides aside for the
 * guidelines panel. A new chat glides the column back as the welcome returns.
 * A saved conversation skips the welcome and fades in once its history loads.
 */
export function useConversationStart(empty: boolean, restoring: boolean) {
  const [welcome, setWelcome] = useState(empty && !restoring);
  const [restored, setRestored] = useState(!restoring);
  const origin = useRef<number>(undefined);
  const welcomeRef = useRef<HTMLElement>(null);
  const columnRef = useRef<HTMLDivElement>(null);
  const messagesRef = useRef<HTMLDivElement>(null);
  const panelRef = useRef<HTMLElement>(null);
  const leaving = welcome && !empty;

  if (empty && !restoring && !welcome) setWelcome(true);

  if (!restoring && !restored) setRestored(true);

  useLayoutEffect(() => {
    const node = welcomeRef.current;

    if (!leaving) return;
    // Browsers without Web Animations hand over immediately.
    const duration = node?.animate && !reducedMotion() ? parseFloat(motion.exit) : 0;

    const exit = node?.animate?.([{ opacity: 1 }, { opacity: 0, transform: "scale(0.985)" }], {
      duration,
      easing: motion.easeOutCubic,
      fill: "forwards",
    });

    // The welcome is nearly transparent two thirds of the way through its exit.
    const handoff = setTimeout(() => {
      origin.current = center(columnRef.current);
      setWelcome(false);
    }, duration * 0.65);

    return () => {
      clearTimeout(handoff);
      exit?.cancel();
    };
  }, [leaving]);

  useLayoutEffect(() => {
    const from = origin.current;
    const column = columnRef.current;
    origin.current = undefined;

    if (from === undefined || !column?.animate) return;
    const reduce = reducedMotion();
    const enter = { duration: parseFloat(motion.enter), easing: motion.easeOut };

    column.animate(
      [
        { transform: `translateX(${reduce ? 0 : from - center(column)!}px)` },
        { transform: "none" },
      ],
      { duration: parseFloat(motion.move), easing: motion.easeInOut },
    );

    if (welcome)
      welcomeRef.current?.animate(
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

  // Remember where the conversation column sits, so a new chat glides from there.
  useLayoutEffect(() => {
    const column = columnRef.current;

    if (welcome || !column) return;

    const observer = new ResizeObserver(() => {
      origin.current = center(column);
    });

    observer.observe(column);

    return () => observer.disconnect();
  }, [welcome]);

  return { welcome, welcomeRef, columnRef, messagesRef, panelRef };
}
