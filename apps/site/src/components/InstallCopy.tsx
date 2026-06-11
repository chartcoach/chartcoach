import { Check, Copy } from "lucide-react";
import { useEffect, useRef, useState } from "react";
import type { SVGProps } from "react";

import { writeClipboard } from "@/components/clipboard";

const INSTALL_COMMAND = "npx skills add chartcoach/chartcoach";

type CopyState = "idle" | "copied" | "failed";
type IconProps = SVGProps<SVGSVGElement> & {
  active: boolean;
};

function ClaudeCodeIcon({ active, ...props }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true" {...props}>
      <path
        fillRule="evenodd"
        clipRule="evenodd"
        fill={active ? "#D97757" : "currentColor"}
        d="M20.998 10.949H24v3.102h-3v3.028h-1.487V20H18v-2.921h-1.487V20H15v-2.921H9V20H7.488v-2.921H6V20H4.487v-2.921H3V14.05H0V10.95h3V5h17.998v5.949zM6 10.949h1.488V8.102H6v2.847zm10.51 0H18V8.102h-1.49v2.847z"
      />
    </svg>
  );
}

function OpenAIIcon({ active: _active, ...props }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" {...props}>
      <path d="M9.205 8.658v-2.26c0-.19.072-.333.238-.428l4.543-2.616c.619-.357 1.356-.523 2.117-.523 2.854 0 4.662 2.212 4.662 4.566 0 .167 0 .357-.024.547l-4.71-2.759a.797.797 0 00-.856 0l-5.97 3.473zm10.609 8.8V12.06c0-.333-.143-.57-.429-.737l-5.97-3.473 1.95-1.118a.433.433 0 01.476 0l4.543 2.617c1.309.76 2.189 2.378 2.189 3.948 0 1.808-1.07 3.473-2.76 4.163zM7.802 12.703l-1.95-1.142c-.167-.095-.239-.238-.239-.428V5.899c0-2.545 1.95-4.472 4.591-4.472 1 0 1.927.333 2.712.928L8.23 5.067c-.285.166-.428.404-.428.737v6.898zM12 15.128l-2.795-1.57v-3.33L12 8.658l2.795 1.57v3.33L12 15.128zm1.796 7.23c-1 0-1.927-.332-2.712-.927l4.686-2.712c.285-.166.428-.404.428-.737v-6.898l1.974 1.142c.167.095.238.238.238.428v5.233c0 2.545-1.974 4.472-4.614 4.472zm-5.637-5.303l-4.544-2.617c-1.308-.761-2.188-2.378-2.188-3.948A4.482 4.482 0 014.21 6.327v5.423c0 .333.143.571.428.738l5.947 3.449-1.95 1.118a.432.432 0 01-.476 0zm-.262 3.9c-2.688 0-4.662-2.021-4.662-4.519 0-.19.024-.38.047-.57l4.686 2.71c.286.167.571.167.856 0l5.97-3.448v2.26c0 .19-.07.333-.237.428l-4.543 2.616c-.619.357-1.356.523-2.117.523zm5.899 2.83a5.947 5.947 0 005.827-4.756C22.287 18.339 24 15.84 24 13.296c0-1.665-.713-3.282-1.998-4.448.119-.5.19-.999.19-1.498 0-3.401-2.759-5.947-5.946-5.947-.642 0-1.26.095-1.88.31A5.962 5.962 0 0010.205 0a5.947 5.947 0 00-5.827 4.757C1.713 5.447 0 7.945 0 10.49c0 1.666.713 3.283 1.998 4.448-.119.5-.19 1-.19 1.499 0 3.401 2.759 5.946 5.946 5.946.642 0 1.26-.095 1.88-.309a5.96 5.96 0 004.162 1.713z" />
    </svg>
  );
}

function OpenCodeIcon({ active: _active, ...props }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" {...props}>
      <path fillRule="evenodd" clipRule="evenodd" d="M16 6H8v12h8V6zm4 16H4V2h16v20z" />
    </svg>
  );
}

const AGENTS = [
  {
    id: "claude",
    label: "Claude",
    command: "claude 'hey $chartcoach, review a crowded pie chart.'",
    Icon: ClaudeCodeIcon,
  },
  {
    id: "codex",
    label: "Codex",
    command: "codex 'hey $chartcoach, review a crowded pie chart.'",
    Icon: OpenAIIcon,
  },
  {
    id: "opencode",
    label: "OpenCode",
    command: "opencode run 'hey $chartcoach, review a crowded pie chart.'",
    Icon: OpenCodeIcon,
  },
] as const;

type AgentId = (typeof AGENTS)[number]["id"];

export function InstallCopy() {
  const [activeId, setActiveId] = useState<AgentId>("codex");
  const [state, setState] = useState<CopyState>("idle");
  const resetTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const activeAgent = AGENTS.find((agent) => agent.id === activeId) ?? AGENTS[1];
  const snippetLines = [INSTALL_COMMAND, activeAgent.command];
  const clipboardText = `${INSTALL_COMMAND}\n${activeAgent.command}`;

  useEffect(() => {
    return () => {
      if (resetTimer.current) clearTimeout(resetTimer.current);
    };
  }, []);

  async function handleCopy() {
    try {
      await writeClipboard(clipboardText);
      setState("copied");
    } catch {
      setState("failed");
    }

    if (resetTimer.current) clearTimeout(resetTimer.current);
    resetTimer.current = setTimeout(() => setState("idle"), 1400);
  }

  const copied = state === "copied";

  return (
    <div className="mt-10 flex w-full max-w-[46rem] flex-col items-center gap-4 xl:mt-12 xl:max-w-[52rem]">
      <div
        className="flex flex-wrap items-center justify-center gap-4 text-[1rem] sm:text-[1.0625rem] xl:text-[1.1875rem]"
        role="tablist"
        aria-label="Agent command"
      >
        {AGENTS.map((agent, index) => {
          const selected = activeId === agent.id;
          return (
            <div key={agent.id} className="flex items-center gap-4">
              {index > 0 && <span className="h-4 w-px bg-border" aria-hidden="true" />}
              <button
                type="button"
                role="tab"
                aria-selected={selected}
                onClick={() => {
                  setActiveId(agent.id);
                  setState("idle");
                  if (resetTimer.current) clearTimeout(resetTimer.current);
                }}
                className={[
                  "cursor-pointer border-0 bg-transparent p-0 font-medium transition-colors",
                  selected ? "text-fg" : "text-muted hover:text-fg",
                ].join(" ")}
              >
                <span className="inline-flex items-center gap-2.5">
                  <agent.Icon
                    active={selected}
                    className="h-[1.125rem] w-[1.125rem] shrink-0 xl:h-5 xl:w-5"
                  />
                  <span>{agent.label}</span>
                </span>
              </button>
            </div>
          );
        })}
      </div>
      <div className="relative w-full overflow-hidden rounded-md border border-border bg-surface text-left">
        <pre className="m-0 whitespace-pre-wrap break-words py-3 pl-4 pr-16 font-mono text-[0.8125rem] leading-[1.55] tracking-tight text-fg/75 sm:pr-20 xl:py-4 xl:pl-5 xl:pr-24 xl:text-[0.9375rem] xl:leading-[1.65]">
          <code className="block">
            {snippetLines.map((line, index) => (
              <span key={line} className={index === 0 ? "block" : "mt-2 block"}>
                <span className="text-muted/55">$ </span>
                {line}
              </span>
            ))}
          </code>
        </pre>
        <button
          type="button"
          aria-label={copied ? "Agent commands copied" : "Copy agent commands"}
          onClick={handleCopy}
          className="absolute right-0 top-0 flex h-12 w-12 cursor-pointer items-center justify-center border-b border-l border-border bg-surface text-muted transition-colors hover:bg-surface-muted hover:text-fg xl:h-14 xl:w-14"
        >
          {copied ? (
            <Check className="h-4 w-4 text-fg" aria-hidden="true" />
          ) : (
            <Copy className="h-4 w-4" aria-hidden="true" />
          )}
        </button>
      </div>
      <p
        className="m-0 h-4 font-mono text-[0.6875rem] font-medium uppercase tracking-[0.16em] text-muted xl:text-[0.75rem]"
        aria-live="polite"
      >
        {state === "copied" ? "Copied" : state === "failed" ? "Copy failed" : ""}
      </p>
    </div>
  );
}
