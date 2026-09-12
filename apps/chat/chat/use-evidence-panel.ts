import { useEffect, useMemo, useRef, useState } from "react";
import type { EvidenceItem } from "./evidence";

export function useEvidencePanel(items: readonly EvidenceItem[], busy: boolean) {
  const [expanded, setExpanded] = useState(true);
  const [sheetOpen, setSheetOpen] = useState(false);
  const mobileTrigger = useRef<HTMLButtonElement>(null);
  const desktopTrigger = useRef<HTMLButtonElement>(null);

  const groups = useMemo(() => {
    const primary: EvidenceItem[] = [];
    const supporting: EvidenceItem[] = [];
    const read: EvidenceItem[] = [];
    const matched: EvidenceItem[] = [];

    for (const item of items) {
      switch (item.stage) {
        case "primary":
          primary.push(item);
          break;
        case "supporting":
          supporting.push(item);
          break;
        case "read":
          read.push(item);
          break;
        case "matched":
          matched.push(item);
          break;
      }
    }

    return {
      primary,
      supporting,
      candidates: [...read, ...matched],
      readCount: items.length - matched.length,
      total: items.length,
    };
  }, [items]);

  const primaryCount = groups.primary.length;

  const summary = primaryCount
    ? `${primaryCount} primary · ${items.length} found`
    : items.length
      ? `${items.length} found · ${groups.readCount} read`
      : busy
        ? "Finding relevant guidance…"
        : "No guidelines retrieved yet";

  useEffect(() => {
    const trigger = mobileTrigger.current;

    if (!sheetOpen || !trigger) return;

    const observer = new ResizeObserver(() => {
      if (!trigger.getClientRects().length) setSheetOpen(false);
    });

    observer.observe(trigger);

    return () => observer.disconnect();
  }, [sheetOpen]);

  return {
    groups,
    primaryCount,
    summary,
    expanded,
    setExpanded,
    sheetOpen,
    setSheetOpen,
    mobileTrigger,
    desktopTrigger,
    restoreFocus: (event: Event) => {
      if (!mobileTrigger.current?.getClientRects().length) {
        event.preventDefault();
        desktopTrigger.current?.focus();
      }
    },
  };
}
