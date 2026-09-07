import { Braces, Check, Copy, Pencil } from "lucide-react";
import { useCallback, useEffect, useRef, useState } from "react";

import { writeClipboard } from "@/components/clipboard";

type CopyId = "markdown" | "bibtex";
type CopyState = CopyId | "failed" | null;
type CopyMessageState = Exclude<CopyState, null>;

const COPY_STATE_MESSAGES = {
  markdown: "Markdown copied",
  bibtex: "BibTeX copied",
  failed: "Copy failed",
} satisfies Record<CopyMessageState, string>;

type GuidelineActionsProps = {
  markdown: string;
  bibtex?: string;
  editHref: string;
};

function Tooltip({ children }: { children: string }) {
  return (
    <span className="pointer-events-none absolute left-0 top-[calc(100%+0.45rem)] z-20 whitespace-nowrap rounded-md border border-border bg-bg px-2 py-1 text-[0.6875rem] font-medium text-fg opacity-0 shadow-sm transition-opacity group-hover:opacity-100 group-focus-visible:opacity-100 sm:left-auto sm:right-0">
      {children}
    </span>
  );
}

export function GuidelineActions({ markdown, bibtex, editHref }: GuidelineActionsProps) {
  const [state, setState] = useState<CopyState>(null);
  const resetTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const canCopyBibtex = Boolean(bibtex?.trim());
  const copyStateMessage = state ? COPY_STATE_MESSAGES[state] : "";

  const clearResetTimer = useCallback(() => {
    if (!resetTimer.current) return;
    clearTimeout(resetTimer.current);
    resetTimer.current = null;
  }, []);

  useEffect(() => clearResetTimer, [clearResetTimer]);

  async function copy(id: CopyId, text: string) {
    try {
      await writeClipboard(text);
      setState(id);
    } catch {
      setState("failed");
    }

    clearResetTimer();
    resetTimer.current = setTimeout(() => setState(null), 1400);
  }

  return (
    <div className="flex flex-wrap items-center gap-2" aria-label="Guideline actions">
      <button
        type="button"
        onClick={() => void copy("markdown", markdown)}
        className="group relative inline-flex h-11 w-11 cursor-pointer items-center justify-center rounded-md border border-border bg-bg text-muted transition-colors hover:bg-surface-muted hover:text-fg"
        aria-label="Copy Markdown"
      >
        {state === "markdown" ? (
          <Check className="h-4 w-4" aria-hidden="true" />
        ) : (
          <Copy className="h-4 w-4" aria-hidden="true" />
        )}
        <Tooltip>{state === "markdown" ? "Copied" : "Copy Markdown"}</Tooltip>
      </button>
      <button
        type="button"
        onClick={() => {
          if (bibtex) void copy("bibtex", bibtex);
        }}
        disabled={!canCopyBibtex}
        className="group relative inline-flex h-11 w-11 cursor-pointer items-center justify-center rounded-md border border-border bg-bg text-muted transition-colors hover:bg-surface-muted hover:text-fg disabled:cursor-not-allowed disabled:opacity-45"
        aria-label="Copy BibTeX"
      >
        {state === "bibtex" ? (
          <Check className="h-4 w-4" aria-hidden="true" />
        ) : (
          <Braces className="h-4 w-4" aria-hidden="true" />
        )}
        <Tooltip>
          {state === "bibtex" ? "Copied" : canCopyBibtex ? "Copy BibTeX" : "No BibTeX references"}
        </Tooltip>
      </button>
      <a
        href={editHref}
        target="_blank"
        rel="noreferrer"
        className="group relative inline-flex h-11 w-11 items-center justify-center rounded-md border border-border bg-bg text-muted no-underline transition-colors hover:bg-surface-muted hover:text-fg"
        aria-label="Suggest edit"
      >
        <Pencil className="h-4 w-4" aria-hidden="true" />
        <Tooltip>Suggest edit</Tooltip>
      </a>
      <span className="sr-only" aria-live="polite">
        {copyStateMessage}
      </span>
    </div>
  );
}
