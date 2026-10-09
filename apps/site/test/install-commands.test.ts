import { execFileSync } from "node:child_process";
import { describe, expect, it } from "vite-plus/test";

import {
  createAgentCommand,
  USE_CASES,
  type AgentId,
} from "../src/components/install-copy/commands";

const agents: AgentId[] = [
  "claude",
  "codex",
  "opencode",
  "antigravity",
  "cursor",
  "gemini-cli",
  "github-copilot",
];

// Execute only a local shell function so the test exercises quoting without launching an agent.
function readPrompt(command: string) {
  const executable = command.split(" ")[0];

  return execFileSync(
    "sh",
    ["-c", `${executable}() { for arg do printf '%s\\n' "$arg"; done; }; ${command}`],
    { encoding: "utf8", env: { chartcoach: "must not expand" } },
  )
    .trim()
    .split("\n")
    .at(-1);
}

describe("installer commands", () => {
  it.each(agents)("preserves the literal skill prompt for %s", (agent) => {
    for (const useCase of USE_CASES) {
      expect(readPrompt(createAgentCommand(agent, useCase.instruction))).toBe(
        `hey $chartcoach, ${useCase.instruction}`,
      );
    }
  });

  it.each(agents)("preserves shell metacharacters for %s", (agent) => {
    const instruction = 'review "sales" with $revenue, `units`, and the team\'s \\notes.';

    expect(readPrompt(createAgentCommand(agent, instruction))).toBe(
      `hey $chartcoach, ${instruction}`,
    );
  });
});
