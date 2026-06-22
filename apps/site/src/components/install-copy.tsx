import { Check, ChevronDown, Copy } from "lucide-react";
import { useCallback, useEffect, useId, useRef, useState } from "react";
import type { CSSProperties, ReactNode, SVGProps } from "react";

import antigravityIconUrl from "@/assets/icons/antigravity.svg?url";
import cursorIconUrl from "@/assets/icons/cursor.svg?url";
import geminiCliIconUrl from "@/assets/icons/geminicli.svg?url";
import githubCopilotIconUrl from "@/assets/icons/githubcopilot.svg?url";
import { writeClipboard } from "@/components/clipboard";

const INSTALL_COMMAND = "npx skills add chartcoach/skills";

type CopyState = "idle" | "copied" | "failed";
type IconProps = SVGProps<SVGSVGElement>;
type UseCase = {
  id: string;
  label: string;
  instruction: string;
};
type ShellLineProps = {
  line: string;
};
type MenuChevronProps = {
  open: boolean;
};
type MenuPlacement = "above" | "below";
type AgentIcon =
  | {
      kind: "component";
      Component: (props: IconProps) => ReactNode;
    }
  | {
      kind: "asset";
      display: "image" | "mask";
      src: string;
    };
type Agent = {
  id: string;
  label: string;
  color: string;
  command: (instruction: string) => string;
  icon: AgentIcon;
};

function ClaudeCodeIcon(props: IconProps) {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true" {...props}>
      <path
        fillRule="evenodd"
        clipRule="evenodd"
        fill="currentColor"
        d="M20.998 10.949H24v3.102h-3v3.028h-1.487V20H18v-2.921h-1.487V20H15v-2.921H9V20H7.488v-2.921H6V20H4.487v-2.921H3V14.05H0V10.95h3V5h17.998v5.949zM6 10.949h1.488V8.102H6v2.847zm10.51 0H18V8.102h-1.49v2.847z"
      />
    </svg>
  );
}

function OpenAIIcon(props: IconProps) {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" {...props}>
      <path d="M9.205 8.658v-2.26c0-.19.072-.333.238-.428l4.543-2.616c.619-.357 1.356-.523 2.117-.523 2.854 0 4.662 2.212 4.662 4.566 0 .167 0 .357-.024.547l-4.71-2.759a.797.797 0 00-.856 0l-5.97 3.473zm10.609 8.8V12.06c0-.333-.143-.57-.429-.737l-5.97-3.473 1.95-1.118a.433.433 0 01.476 0l4.543 2.617c1.309.76 2.189 2.378 2.189 3.948 0 1.808-1.07 3.473-2.76 4.163zM7.802 12.703l-1.95-1.142c-.167-.095-.239-.238-.239-.428V5.899c0-2.545 1.95-4.472 4.591-4.472 1 0 1.927.333 2.712.928L8.23 5.067c-.285.166-.428.404-.428.737v6.898zM12 15.128l-2.795-1.57v-3.33L12 8.658l2.795 1.57v3.33L12 15.128zm1.796 7.23c-1 0-1.927-.332-2.712-.927l4.686-2.712c.285-.166.428-.404.428-.737v-6.898l1.974 1.142c.167.095.238.238.238.428v5.233c0 2.545-1.974 4.472-4.614 4.472zm-5.637-5.303l-4.544-2.617c-1.308-.761-2.188-2.378-2.188-3.948A4.482 4.482 0 014.21 6.327v5.423c0 .333.143.571.428.738l5.947 3.449-1.95 1.118a.432.432 0 01-.476 0zm-.262 3.9c-2.688 0-4.662-2.021-4.662-4.519 0-.19.024-.38.047-.57l4.686 2.71c.286.167.571.167.856 0l5.97-3.448v2.26c0 .19-.07.333-.237.428l-4.543 2.616c-.619.357-1.356.523-2.117.523zm5.899 2.83a5.947 5.947 0 005.827-4.756C22.287 18.339 24 15.84 24 13.296c0-1.665-.713-3.282-1.998-4.448.119-.5.19-.999.19-1.498 0-3.401-2.759-5.947-5.946-5.947-.642 0-1.26.095-1.88.31A5.962 5.962 0 0010.205 0a5.947 5.947 0 00-5.827 4.757C1.713 5.447 0 7.945 0 10.49c0 1.666.713 3.283 1.998 4.448-.119.5-.19 1-.19 1.499 0 3.401 2.759 5.946 5.946 5.946.642 0 1.26-.095 1.88-.309a5.96 5.96 0 004.162 1.713z" />
    </svg>
  );
}

function OpenCodeIcon(props: IconProps) {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" {...props}>
      <path fillRule="evenodd" clipRule="evenodd" d="M16 6H8v12h8V6zm4 16H4V2h16v20z" />
    </svg>
  );
}

function prompt(instruction: string) {
  return `hey $chartcoach, ${instruction}`;
}

function singleQuote(value: string) {
  return `'${value.replace(/'/g, "'\\''")}'`;
}

function doubleQuote(value: string) {
  return `"${value.replace(/(["\\])/g, "\\$1")}"`;
}

const AGENTS = [
  {
    id: "claude",
    label: "Claude",
    color: "#D97757",
    command: (instruction: string) => `claude ${singleQuote(prompt(instruction))}`,
    icon: { kind: "component", Component: ClaudeCodeIcon },
  },
  {
    id: "codex",
    label: "Codex",
    color: "var(--color-fg)",
    command: (instruction: string) => `codex ${singleQuote(prompt(instruction))}`,
    icon: { kind: "component", Component: OpenAIIcon },
  },
  {
    id: "opencode",
    label: "OpenCode",
    color: "var(--color-fg)",
    command: (instruction: string) => `opencode run ${singleQuote(prompt(instruction))}`,
    icon: { kind: "component", Component: OpenCodeIcon },
  },
  {
    id: "antigravity",
    label: "Antigravity",
    color: "var(--color-fg)",
    command: (instruction: string) => `agy -i ${doubleQuote(prompt(instruction))}`,
    icon: { kind: "asset", display: "image", src: antigravityIconUrl },
  },
  {
    id: "cursor",
    label: "Cursor",
    color: "var(--color-fg)",
    command: (instruction: string) => `agent ${doubleQuote(prompt(instruction))}`,
    icon: { kind: "asset", display: "mask", src: cursorIconUrl },
  },
  {
    id: "gemini-cli",
    label: "Gemini CLI",
    color: "#207CFE",
    command: (instruction: string) => `gemini ${doubleQuote(prompt(instruction))}`,
    icon: { kind: "asset", display: "image", src: geminiCliIconUrl },
  },
  {
    id: "github-copilot",
    label: "GitHub Copilot",
    color: "var(--color-fg)",
    command: (instruction: string) => `copilot --prompt ${doubleQuote(prompt(instruction))}`,
    icon: { kind: "asset", display: "mask", src: githubCopilotIconUrl },
  },
] as const satisfies readonly Agent[];

const AGENT_MENU_ITEM_HEIGHT = 40;
const AGENT_MENU_CHROME_HEIGHT = 10;
const AGENT_MENU_GAP = 8;
const AGENT_MENU_VIEWPORT_PADDING = 12;
const AGENT_MENU_HEIGHT = AGENTS.length * AGENT_MENU_ITEM_HEIGHT + AGENT_MENU_CHROME_HEIGHT;

const USE_CASES = [
  {
    id: "review",
    label: "Review",
    instruction: "review this chart.",
  },
  {
    id: "recommend",
    label: "Recommend",
    instruction: "suggest a clearer encoding.",
  },
  {
    id: "discuss",
    label: "Discuss",
    instruction: "discuss how I should show uncertainty.",
  },
  {
    id: "evaluate",
    label: "Evaluate",
    instruction: "evaluate this chart for mobile use.",
  },
  {
    id: "contribute",
    label: "Contribute",
    instruction: "draft a GitHub issue for missing guidance about log scales.",
  },
] as const satisfies readonly UseCase[];

type AgentId = (typeof AGENTS)[number]["id"];
type UseCaseId = (typeof USE_CASES)[number]["id"];

function AgentLogo({ agent, className }: { agent: (typeof AGENTS)[number]; className: string }) {
  if (agent.icon.kind === "asset") {
    if (agent.icon.display === "mask") {
      const maskStyle = {
        backgroundColor: agent.color,
        mask: `url("${agent.icon.src}") center / contain no-repeat`,
        WebkitMask: `url("${agent.icon.src}") center / contain no-repeat`,
      } as CSSProperties;

      return (
        <span
          aria-hidden="true"
          className={[className, "block"].join(" ")}
          data-agent-icon={agent.id}
          style={maskStyle}
        />
      );
    }

    const iconStyle = { backgroundImage: `url("${agent.icon.src}")` } as CSSProperties;

    return (
      <span
        aria-hidden="true"
        className={[className, "block bg-contain bg-center bg-no-repeat"].join(" ")}
        data-agent-icon={agent.id}
        style={iconStyle}
      />
    );
  }

  const Icon = agent.icon.Component;
  const style = { color: agent.color } as CSSProperties;
  return <Icon className={className} data-agent-icon={agent.id} style={style} />;
}

function ShellLine({ line }: ShellLineProps) {
  const match = line.match(/^(\S+)(\s+)(.*)$/);
  if (!match) return <span className="text-code-fg">{line}</span>;

  const [, command, spacing, rest] = match;
  const quoteStarts = [rest.indexOf("'"), rest.indexOf('"')].filter((index) => index >= 0);
  const quotedTextStart = quoteStarts.length > 0 ? Math.min(...quoteStarts) : -1;
  if (quotedTextStart === -1) {
    return (
      <>
        <span className="font-medium text-code-fg">{command}</span>
        {spacing}
        <span className="text-code-fg/75">{rest}</span>
      </>
    );
  }

  return (
    <>
      <span className="font-medium text-code-fg">{command}</span>
      {spacing}
      <span className="text-code-fg/75">{rest.slice(0, quotedTextStart)}</span>
      <span className="text-code-fg/90">{rest.slice(quotedTextStart)}</span>
    </>
  );
}

function MenuChevron({ open }: MenuChevronProps) {
  return (
    <span
      className="flex h-full w-9 shrink-0 items-center justify-center text-muted"
      aria-hidden="true"
    >
      <ChevronDown
        className={["h-4 w-4 transition-transform", open ? "rotate-180" : ""].join(" ")}
        strokeWidth={1.8}
      />
    </span>
  );
}

function useMenuDisclosure() {
  const [open, setOpen] = useState(false);
  const [placement, setPlacement] = useState<MenuPlacement>("below");
  const menuRef = useRef<HTMLDivElement | null>(null);
  const triggerRef = useRef<HTMLButtonElement | null>(null);

  const close = useCallback(() => setOpen(false), []);
  const updatePlacement = useCallback(() => {
    const trigger = triggerRef.current;
    if (!trigger) return;

    const rect = trigger.getBoundingClientRect();
    const spaceBelow = window.innerHeight - rect.bottom - AGENT_MENU_VIEWPORT_PADDING;
    const spaceAbove = rect.top - AGENT_MENU_VIEWPORT_PADDING;
    const needsAbove = spaceBelow < AGENT_MENU_HEIGHT + AGENT_MENU_GAP && spaceAbove > spaceBelow;
    setPlacement(needsAbove ? "above" : "below");
  }, []);
  const updatePlacementRef = useRef(updatePlacement);

  useEffect(() => {
    updatePlacementRef.current = updatePlacement;
  }, [updatePlacement]);

  const toggle = useCallback(() => {
    setOpen((current) => {
      if (!current) updatePlacement();
      return !current;
    });
  }, [updatePlacement]);

  useEffect(() => {
    if (!open) return;

    function handlePointerDown(event: PointerEvent) {
      const target = event.target;
      if (!(target instanceof Node)) return;
      if (!menuRef.current?.contains(target)) close();
    }

    function handleKeyDown(event: KeyboardEvent) {
      if (event.key !== "Escape") return;
      close();
      triggerRef.current?.focus();
    }

    function handleReposition() {
      updatePlacementRef.current();
    }

    document.addEventListener("pointerdown", handlePointerDown);
    document.addEventListener("keydown", handleKeyDown);
    window.addEventListener("resize", handleReposition);
    window.addEventListener("scroll", handleReposition, true);

    return () => {
      document.removeEventListener("pointerdown", handlePointerDown);
      document.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("resize", handleReposition);
      window.removeEventListener("scroll", handleReposition, true);
    };
  }, [close, open]);

  return { close, menuRef, open, placement, toggle, triggerRef };
}

export function InstallCopy() {
  const [activeAgentId, setActiveAgentId] = useState<AgentId>("claude");
  const [activeUseCaseId, setActiveUseCaseId] = useState<UseCaseId>("evaluate");
  const [state, setState] = useState<CopyState>("idle");
  const agentMenuId = useId();
  const resetTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const agentMenu = useMenuDisclosure();
  const agentMenuPlacementClass =
    agentMenu.placement === "above" ? "bottom-[calc(100%+0.45rem)]" : "top-[calc(100%+0.45rem)]";
  const activeAgent = AGENTS.find((agent) => agent.id === activeAgentId) ?? AGENTS[1];
  const activeUseCase = USE_CASES.find((useCase) => useCase.id === activeUseCaseId) ?? USE_CASES[0];
  const agentCommand = activeAgent.command(activeUseCase.instruction);
  const snippetLines = [INSTALL_COMMAND, agentCommand];
  const clipboardText = snippetLines.join("\n");
  const agentStyle = { "--agent-color": activeAgent.color } as CSSProperties;

  const clearResetTimer = useCallback(() => {
    if (!resetTimer.current) return;
    clearTimeout(resetTimer.current);
    resetTimer.current = null;
  }, []);

  useEffect(() => clearResetTimer, [clearResetTimer]);

  async function handleCopy() {
    try {
      await writeClipboard(clipboardText);
      setState("copied");
    } catch {
      setState("failed");
    }

    clearResetTimer();
    resetTimer.current = setTimeout(() => setState("idle"), 1400);
  }

  const copied = state === "copied";

  function resetSelectionState() {
    setState("idle");
    clearResetTimer();
  }

  return (
    <div className="home-install-copy mt-6 w-full min-w-0 max-w-[60rem] sm:mt-10 lg:mt-8 xl:mt-9 xl:max-w-[64rem]">
      <div
        className="min-w-0 overflow-visible rounded-xl border border-border bg-code-bg text-left shadow-[0_1px_2px_color-mix(in_srgb,var(--color-fg)_8%,transparent)]"
        style={agentStyle}
      >
        <div className="grid grid-cols-[minmax(0,1fr)_auto] gap-x-2 gap-y-3 rounded-t-[calc(0.75rem-1px)] border-b border-border bg-surface-muted px-3 py-3 sm:px-5 lg:flex lg:flex-row lg:items-center lg:gap-3 xl:gap-4 xl:px-6">
          <div
            ref={agentMenu.menuRef}
            className="relative min-w-0 lg:w-[14.5rem] lg:shrink-0 xl:w-[15.5rem]"
          >
            <button
              ref={agentMenu.triggerRef}
              type="button"
              aria-controls={agentMenu.open ? agentMenuId : undefined}
              aria-expanded={agentMenu.open}
              aria-haspopup="menu"
              onClick={() => {
                agentMenu.toggle();
              }}
              className="grid h-10 w-full cursor-pointer grid-cols-[auto_minmax(0,1fr)_2.25rem] items-center gap-2 rounded-md border border-transparent bg-transparent pl-2.5 pr-0 text-[0.9375rem] font-semibold text-fg transition-colors hover:bg-surface-muted focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-fg/20 sm:h-11 sm:text-[1rem] xl:text-[1.0625rem]"
            >
              <AgentLogo agent={activeAgent} className="h-5 w-5 shrink-0" />
              <span className="min-w-0 truncate text-left">{activeAgent.label}</span>
              <MenuChevron open={agentMenu.open} />
            </button>
            {agentMenu.open && (
              <div
                id={agentMenuId}
                role="menu"
                aria-label="Agent"
                className={[
                  "absolute left-0 z-50 w-full min-w-[13.5rem] overflow-hidden rounded-md border border-border bg-bg p-1 sm:min-w-[14.5rem]",
                  agentMenuPlacementClass,
                ].join(" ")}
              >
                {AGENTS.map((agent) => {
                  const selected = activeAgentId === agent.id;
                  return (
                    <button
                      key={agent.id}
                      type="button"
                      role="menuitemradio"
                      aria-checked={selected}
                      onClick={() => {
                        setActiveAgentId(agent.id);
                        agentMenu.close();
                        resetSelectionState();
                      }}
                      className={[
                        "flex h-10 w-full cursor-pointer items-center gap-2.5 rounded px-2.5 text-left text-sm font-medium transition-colors",
                        selected
                          ? "bg-surface-muted text-fg"
                          : "text-muted hover:bg-surface-muted hover:text-fg",
                      ].join(" ")}
                    >
                      <AgentLogo agent={agent} className="h-4 w-4 shrink-0" />
                      <span className="min-w-0 flex-1 truncate">{agent.label}</span>
                      {selected && (
                        <Check className="h-3.5 w-3.5 shrink-0 text-fg" aria-hidden="true" />
                      )}
                    </button>
                  );
                })}
              </div>
            )}
          </div>
          <div
            className="col-span-2 row-start-2 flex min-w-0 flex-1 flex-nowrap items-center justify-between lg:col-auto lg:row-auto lg:justify-start"
            aria-label="chartcoach use case"
          >
            {USE_CASES.map((useCase, index) => {
              const selected = activeUseCaseId === useCase.id;
              return (
                <button
                  key={useCase.id}
                  type="button"
                  aria-pressed={selected}
                  onClick={() => {
                    setActiveUseCaseId(useCase.id);
                    resetSelectionState();
                  }}
                  className={[
                    "relative h-8 shrink-0 cursor-pointer bg-transparent px-0.5 text-[0.5625rem] transition-colors after:absolute after:bottom-0 after:left-1/2 after:h-0.5 after:w-5 after:-translate-x-1/2 after:rounded-full after:transition-colors focus-visible:rounded-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-fg/20 min-[360px]:px-1 min-[360px]:text-[0.625rem] min-[390px]:text-[0.6875rem] sm:px-4 sm:text-[0.9375rem] xl:h-9 xl:px-5 xl:text-[1rem]",
                    index > 0
                      ? "before:absolute before:left-0 before:top-1/2 before:hidden before:h-4 before:-translate-y-1/2 before:border-l before:border-border sm:before:block"
                      : "",
                    selected
                      ? "font-semibold text-accent after:bg-accent hover:text-accent"
                      : "font-medium text-muted after:bg-transparent hover:text-fg",
                  ].join(" ")}
                >
                  {useCase.label}
                </button>
              );
            })}
          </div>
          <button
            type="button"
            aria-label={copied ? "Agent commands copied" : "Copy agent commands"}
            onClick={handleCopy}
            className="col-start-2 row-start-1 ml-auto flex h-10 w-10 shrink-0 cursor-pointer items-center justify-center rounded-md border border-transparent bg-transparent text-muted transition-colors hover:bg-surface-muted hover:text-fg focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-fg/20 lg:col-auto lg:row-auto lg:order-last"
          >
            {copied ? (
              <Check className="h-5 w-5 text-fg" aria-hidden="true" />
            ) : (
              <Copy className="h-5 w-5" aria-hidden="true" />
            )}
          </button>
        </div>
        <pre className="m-0 min-w-0 max-w-full overflow-x-auto px-4 py-3.5 font-mono text-[0.8125rem] leading-[1.65] tracking-normal text-code-fg sm:px-7 sm:py-5 sm:text-[0.9375rem] xl:text-[1rem]">
          <code className="block min-w-0 whitespace-pre-wrap break-words">
            {snippetLines.map((line, index) => (
              <span
                key={line}
                className={index === 0 ? "home-install-line block" : "home-install-line mt-3 block"}
              >
                <span className="select-none text-muted/55">$ </span>
                <ShellLine line={line} />
              </span>
            ))}
          </code>
        </pre>
      </div>
      <span className="sr-only" aria-live="polite">
        {state === "copied" ? "Copied" : state === "failed" ? "Copy failed" : ""}
      </span>
    </div>
  );
}
