import { expect, it } from "vite-plus/test";
import type { EveDynamicToolPart, EveMessage } from "eve/react";
import { deriveConversation } from "../chat/evidence";
import { progressPhase } from "../chat/progress";

const part: EveDynamicToolPart = {
  type: "dynamic-tool",
  toolName: "search_guidelines",
  toolCallId: "search",
  state: "input-available",
  input: { query: "labels" },
};

function phase(parts: EveMessage["parts"], metadata: EveMessage["metadata"] = {}) {
  return progressPhase(
    deriveConversation([{ id: "reply", role: "assistant", parts, metadata }]).messages[0],
  );
}

it("keeps exploration steady across tool calls and the model's intervening reasoning", () => {
  expect(phase([])).toBe("starting");
  expect(phase([{ ...part, toolName: "load_skill" }])).toBe("choosing");
  const completed: EveDynamicToolPart = { ...part, state: "output-available", output: {} };
  expect(phase([part])).toBe("exploring");
  expect(phase([completed])).toBe("exploring");
  expect(phase([completed, { ...part, toolName: "read_guidelines", toolCallId: "read" }])).toBe(
    "exploring",
  );
  expect(
    phase([completed, { ...completed, toolName: "read_guidelines", toolCallId: "read" }]),
  ).toBe("exploring");
});

it("reflects presentation and repair while settling terminal states immediately", () => {
  const writing: EveDynamicToolPart = { ...part, toolName: "present_answer" };
  expect(phase([writing])).toBe("writing");
  expect(
    phase([{ ...writing, state: "output-error", errorText: "Read the cited guideline first." }]),
  ).toBe("refining");

  for (const status of ["complete", "failed"] as const)
    expect(phase([writing], { status })).toBe("complete");

  const stopped = deriveConversation(
    [{ id: "reply", role: "assistant", parts: [writing], metadata: { turnId: "turn" } }],
    { stoppedTurnIds: new Set(["turn"]) },
  );

  expect(progressPhase(stopped.messages[0])).toBe("complete");
});
