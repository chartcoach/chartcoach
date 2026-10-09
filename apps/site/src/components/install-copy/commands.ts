function prompt(instruction: string) {
  return `hey $chartcoach, ${instruction}`;
}

function singleQuote(value: string) {
  return `'${value.replace(/'/g, "'\\''")}'`;
}

function doubleQuote(value: string) {
  return `"${value.replace(/(["\\$`])/g, "\\$1")}"`;
}

const agentCommands = {
  claude: (instruction: string) => `claude ${singleQuote(prompt(instruction))}`,
  codex: (instruction: string) => `codex ${singleQuote(prompt(instruction))}`,
  opencode: (instruction: string) => `opencode run ${singleQuote(prompt(instruction))}`,
  antigravity: (instruction: string) => `agy -i ${doubleQuote(prompt(instruction))}`,
  cursor: (instruction: string) => `agent ${doubleQuote(prompt(instruction))}`,
  "gemini-cli": (instruction: string) => `gemini ${doubleQuote(prompt(instruction))}`,
  "github-copilot": (instruction: string) => `copilot --prompt ${doubleQuote(prompt(instruction))}`,
};

export type AgentId = keyof typeof agentCommands;

export function createAgentCommand(agent: AgentId, instruction: string) {
  return agentCommands[agent](instruction);
}

export const USE_CASES = [
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
] as const;

export type UseCaseId = (typeof USE_CASES)[number]["id"];
