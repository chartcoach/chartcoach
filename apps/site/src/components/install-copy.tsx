import { Check, ChevronDown, Copy } from "lucide-react";
import { useEffect, useRef, useState } from "react";

import { writeClipboard } from "@/components/clipboard";
import { AGENTS, AgentLogo } from "./install-copy/agents";
import {
  createAgentCommand,
  USE_CASES,
  type AgentId,
  type UseCaseId,
} from "./install-copy/commands";
import { ShellLine } from "./install-copy/shell-line";
import "@/styles/install-copy.css";

const INSTALL_COMMAND = "npx skills add chartcoach/skills";

type CopyState = "idle" | "copied" | "failed";

function AgentSelect({ value, onChange }: { value: AgentId; onChange: (id: AgentId) => void }) {
  const agent = AGENTS.find((candidate) => candidate.id === value) ?? AGENTS[0];

  return (
    <div className="install-select install-agent">
      <AgentLogo agent={agent} className="size-5 shrink-0" />
      <select
        aria-label="Agent"
        value={value}
        onChange={(event) => {
          const selected = AGENTS.find((candidate) => candidate.id === event.currentTarget.value);

          if (selected) onChange(selected.id);
        }}
      >
        {AGENTS.map((candidate) => (
          <option key={candidate.id} value={candidate.id}>
            {candidate.label}
          </option>
        ))}
      </select>
      <ChevronDown className="install-select-chevron size-4" aria-hidden="true" />
    </div>
  );
}

function UseCaseSelect({
  value,
  onChange,
}: {
  value: UseCaseId;
  onChange: (id: UseCaseId) => void;
}) {
  return (
    <div className="install-select install-use-case-select">
      <select
        aria-label="Chart task"
        value={value}
        onChange={(event) => {
          const selected = USE_CASES.find(
            (candidate) => candidate.id === event.currentTarget.value,
          );

          if (selected) onChange(selected.id);
        }}
      >
        {USE_CASES.map((useCase) => (
          <option key={useCase.id} value={useCase.id}>
            {useCase.label}
          </option>
        ))}
      </select>
      <ChevronDown className="install-select-chevron size-4" aria-hidden="true" />
    </div>
  );
}

function UseCaseButtons({
  value,
  onChange,
}: {
  value: UseCaseId;
  onChange: (id: UseCaseId) => void;
}) {
  return (
    <div className="install-use-case-buttons" role="group" aria-label="Chart task">
      {USE_CASES.map((useCase) => (
        <button
          key={useCase.id}
          type="button"
          aria-pressed={value === useCase.id}
          onClick={() => onChange(useCase.id)}
        >
          {useCase.label}
        </button>
      ))}
    </div>
  );
}

function CopyButton({ state, onCopy }: { state: CopyState; onCopy: () => void }) {
  const Icon = state === "copied" ? Check : Copy;

  return (
    <button
      type="button"
      className="install-copy-button"
      aria-label={state === "copied" ? "Agent commands copied" : "Copy agent commands"}
      onClick={onCopy}
    >
      <Icon className="size-5" aria-hidden="true" />
    </button>
  );
}

export function InstallCopy() {
  const [activeAgentId, setActiveAgentId] = useState<AgentId>("claude");
  const [activeUseCaseId, setActiveUseCaseId] = useState<UseCaseId>("evaluate");
  const [copyState, setCopyState] = useState<CopyState>("idle");
  const resetTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const copyVersion = useRef(0);

  const activeAgent = AGENTS.find((agent) => agent.id === activeAgentId) ?? AGENTS[0];
  const activeUseCase = USE_CASES.find((useCase) => useCase.id === activeUseCaseId) ?? USE_CASES[0];

  const snippetLines = [
    INSTALL_COMMAND,
    createAgentCommand(activeAgent.id, activeUseCase.instruction),
  ];

  function resetCopyState() {
    copyVersion.current += 1;

    if (resetTimer.current) clearTimeout(resetTimer.current);
    resetTimer.current = null;
    setCopyState("idle");
  }

  useEffect(() => {
    return () => {
      copyVersion.current += 1;

      if (resetTimer.current) clearTimeout(resetTimer.current);
    };
  }, []);

  async function handleCopy() {
    const version = ++copyVersion.current;

    if (resetTimer.current) clearTimeout(resetTimer.current);
    let nextState: CopyState;

    try {
      await writeClipboard(snippetLines.join("\n"));
      nextState = "copied";
    } catch {
      nextState = "failed";
    }

    if (version !== copyVersion.current) return;
    setCopyState(nextState);
    resetTimer.current = setTimeout(() => setCopyState("idle"), 1400);
  }

  function selectAgent(id: AgentId) {
    setActiveAgentId(id);
    resetCopyState();
  }

  function selectUseCase(id: UseCaseId) {
    setActiveUseCaseId(id);
    resetCopyState();
  }

  return (
    <div className="home-install-copy">
      <div className="install-window">
        <div className="install-toolbar">
          <AgentSelect value={activeAgentId} onChange={selectAgent} />
          <UseCaseSelect value={activeUseCaseId} onChange={selectUseCase} />
          <UseCaseButtons value={activeUseCaseId} onChange={selectUseCase} />
          <CopyButton state={copyState} onCopy={handleCopy} />
        </div>
        <pre className="install-code">
          <code>
            {snippetLines.map((line) => (
              <span key={line} className="home-install-line">
                <span className="select-none text-muted" aria-hidden="true">
                  ${" "}
                </span>
                <ShellLine line={line} />
              </span>
            ))}
          </code>
        </pre>
      </div>
      <span className="sr-only" role="status">
        {copyState === "copied"
          ? "Copied"
          : copyState === "failed"
            ? "Copy failed. Select the commands to copy manually."
            : ""}
      </span>
    </div>
  );
}
