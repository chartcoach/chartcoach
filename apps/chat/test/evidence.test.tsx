import type { EveMessage } from "eve/react";
import { expect, it } from "vite-plus/test";
import { deriveConversation } from "../chat/evidence";

const user: EveMessage = {
  id: "question",
  role: "user",
  parts: [{ type: "text", text: "Review my chart." }],
};
const matches = [
  {
    id: "labels",
    title: "Label series directly",
    description: "Place each name by its series.",
    url: "https://chartcoach.dev/guidelines/labels",
  },
  {
    id: "contrast",
    title: "Ensure text contrast",
    description: "Keep text legible against its background.",
    url: "https://chartcoach.dev/guidelines/contrast",
  },
];
const search: EveMessage = {
  id: "search",
  role: "assistant",
  parts: [
    {
      type: "dynamic-tool",
      toolCallId: "search",
      toolName: "search_guidelines",
      state: "output-available",
      input: { query: "chart labels", method: "keyword" },
      output: { method: "keyword", matches },
    },
  ],
};
const read: EveMessage = {
  id: "read",
  role: "assistant",
  parts: [
    {
      type: "dynamic-tool",
      toolCallId: "read",
      toolName: "read_guidelines",
      state: "output-available",
      input: { ids: ["labels", "contrast"] },
      output: {
        guidelines: matches,
        citations: matches.map((item) => ({ id: item.id, url: item.url, sources: [] })),
      },
    },
  ],
};
const result = {
  status: "feedback",
  question: null,
  feedback: [
    {
      primary_guideline_id: "labels",
      supporting_guideline_ids: ["contrast"],
      assessment: "violated",
      observation: "Labels sit in a separate legend.",
      recommendation: "Place each label by its series.",
    },
  ],
};
const answer: EveMessage = {
  id: "answer",
  role: "assistant",
  parts: [],
  metadata: { status: "complete", turnId: "turn", result },
};

it("orders primary evidence by the findings rather than retrieval rank", () => {
  const review: EveMessage = {
    ...answer,
    metadata: {
      status: "complete",
      result: {
        ...result,
        feedback: [
          { ...result.feedback[0], primary_guideline_id: "contrast", supporting_guideline_ids: [] },
          { ...result.feedback[0], primary_guideline_id: "labels", supporting_guideline_ids: [] },
        ],
      },
    },
  };
  const { evidence } = deriveConversation([user, search, read, review]);
  expect(
    evidence.filter((item) => item.stage === "primary").map((item) => item.guideline.id),
  ).toEqual(["contrast", "labels"]);
});

it("publishes matches as they arrive and promotes them after reads and a verified answer", () => {
  const matched = deriveConversation([user, search]);
  expect(matched.evidence.map((item) => [item.guideline.id, item.stage])).toEqual([
    ["labels", "matched"],
    ["contrast", "matched"],
  ]);
  const inspected = deriveConversation([user, search, read]);
  expect(inspected.evidence.map((item) => [item.guideline.id, item.stage])).toEqual([
    ["labels", "read"],
    ["contrast", "read"],
  ]);
  const completed = deriveConversation([user, search, read, answer]);
  expect(completed.evidence.map((item) => [item.guideline.id, item.stage])).toEqual([
    ["labels", "primary"],
    ["contrast", "supporting"],
  ]);
});

it("retains earlier matches during a turn and resets the panel for a new request", () => {
  const emptySearch: EveMessage = {
    ...search,
    id: "empty",
    parts: [
      {
        type: "dynamic-tool",
        toolCallId: "retry",
        toolName: "search_guidelines",
        state: "output-available",
        input: { query: "axis" },
        output: { method: "vector", matches: [] },
      },
    ],
  };
  expect(
    deriveConversation([user, search, emptySearch]).evidence.map((item) => item.guideline.id),
  ).toEqual(["labels", "contrast"]);
  expect(
    deriveConversation([user, search, read, answer, { ...user, id: "follow-up" }]).evidence,
  ).toEqual([]);
  expect(deriveConversation([]).evidence).toEqual([]);
});

it("keeps future reads from verifying earlier answers", () => {
  const conversation = deriveConversation([user, search, answer, read]);
  expect(conversation.messages[2]?.review).toBeUndefined();
  expect(conversation.messages[2]?.guidelines.size).toBe(0);
  expect(conversation.evidence.every((item) => item.stage === "read")).toBe(true);
});

it.each([
  {
    lifecycle: "streaming",
    message: { ...answer, metadata: { ...answer.metadata, status: "streaming" as const } },
    options: {},
  },
  { lifecycle: "cancelled", message: answer, options: { stoppedTurnIds: new Set(["turn"]) } },
  {
    lifecycle: "failed",
    message: { ...answer, metadata: { ...answer.metadata, status: "failed" as const } },
    options: {},
  },
  {
    lifecycle: "invalid",
    message: {
      ...answer,
      metadata: {
        ...answer.metadata,
        result: {
          ...result,
          feedback: [{ ...result.feedback[0], primary_guideline_id: "unread" }],
        },
      },
    },
    options: {},
  },
])("preserves read evidence without promoting a $lifecycle answer", ({ message, options }) => {
  const conversation = deriveConversation([user, search, read, message], options);
  expect(conversation.evidence.map((item) => item.stage)).toEqual(["read", "read"]);
  expect(conversation.messages.at(-1)?.review).toBeUndefined();
});
