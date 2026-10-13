import { useEffect, useLayoutEffect, useRef, type RefObject } from "react";

export function useChatFocus(
  view: "chat" | "guidelines",
  loading: boolean,
  disabled: boolean,
  messageInput: RefObject<HTMLTextAreaElement | null>,
  heading: RefObject<HTMLHeadingElement | null>,
) {
  const pending = useRef(true);
  const previousInput = useRef<HTMLTextAreaElement | null>(null);
  useLayoutEffect(() => {
    pending.current = true;

    const preserveFocus = () => {
      pending.current = false;
    };

    document.addEventListener("focusin", preserveFocus);

    return () => document.removeEventListener("focusin", preserveFocus);
  }, [view]);
  useLayoutEffect(() => {
    if (loading) pending.current = true;
  }, [loading]);
  useEffect(() => {
    if (view !== "chat" || loading || disabled) return;

    const moved = !!previousInput.current && previousInput.current !== messageInput.current;
    previousInput.current = messageInput.current;

    // A route transition can replace the input after focus falls back to the document body.
    if (!pending.current && !(moved && document.activeElement === document.body)) return;

    const desktop = window.matchMedia(
      "(min-width: 720px) and (hover: hover) and (pointer: fine)",
    ).matches;

    // Navigation focus must not open a mobile software keyboard.
    const target = desktop ? messageInput.current : heading.current;

    if (target) {
      target.focus({ preventScroll: true });
      pending.current = false;
    }
  }, [view, loading, disabled, messageInput, heading]);
}
