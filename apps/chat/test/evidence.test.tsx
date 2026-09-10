import type { EveDynamicToolPart, EveMessage } from "eve/react";
import { expect, it } from "vite-plus/test";
import { deriveConversation } from "../chat/evidence";
import type { Answer } from "../shared/answer";

const user: EveMessage = {
  id: "question",
  role: "user",
  parts: [{ type: "text", text: "Answer my chart." }],
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
  workflow: "visfeedback",
  status: "answer",
  question: null,
  points: [
    {
      primary_guideline_id: "labels",
      supporting_guideline_ids: ["contrast"],
      assessment: "violated",
      context: "Labels sit in a separate legend.",
      recommendation: "Place each label by its series.",
    },
  ],
} satisfies Answer;
function presentation(
  output: Extract<EveDynamicToolPart, { state: "output-available" }>["output"],
): EveMessage["parts"][number] {
  return {
    type: "dynamic-tool",
    toolCallId: "present",
    toolName: "present_answer",
    state: "output-available",
    input: output,
    output,
  };
}
const answer: EveMessage = {
  id: "answer",
  role: "assistant",
  metadata: { status: "complete", turnId: "turn" },
  parts: [presentation(result)],
};

it("keeps primary prominence when a guideline supports another decision", () => {
  const guidelines = [
    ...matches,
    {
      id: "spacing",
      title: "Keep labels separated",
      description: "Leave room between labels.",
      url: "https://chartcoach.dev/guidelines/spacing",
    },
  ];
  const conversation = deriveConversation([
    {
      ...read,
      parts: [
        {
          type: "dynamic-tool",
          toolCallId: "read-three",
          toolName: "read_guidelines",
          state: "output-available",
          input: { ids: guidelines.map((item) => item.id) },
          output: {
            guidelines,
            citations: guidelines.map((item) => ({ id: item.id, url: item.url, sources: [] })),
          },
        },
      ],
    },
    {
      ...answer,
      metadata: { status: "complete" },
      parts: [
        presentation({
          ...result,
          workflow: "discuss",
          points: [
            { ...result.points[0], supporting_guideline_ids: ["spacing"], assessment: null },
            {
              ...result.points[0],
              primary_guideline_id: "contrast",
              supporting_guideline_ids: ["labels"],
              assessment: null,
            },
            {
              ...result.points[0],
              primary_guideline_id: "spacing",
              supporting_guideline_ids: ["labels"],
              assessment: null,
            },
          ],
        }),
      ],
    },
  ]);
  expect(conversation.messages.at(-1)?.answer?.status).toBe("answer");
  expect(
    conversation.evidence.map((item) => ({ id: item.guideline.id, stage: item.stage })),
  ).toEqual([
    { id: "labels", stage: "primary" },
    { id: "contrast", stage: "primary" },
    { id: "spacing", stage: "primary" },
  ]);
});

it("orders primary evidence by the findings rather than retrieval rank", () => {
  const review: EveMessage = {
    ...answer,
    metadata: { status: "complete" },
    parts: [
      presentation({
        ...result,
        points: [
          { ...result.points[0], primary_guideline_id: "contrast", supporting_guideline_ids: [] },
          { ...result.points[0], primary_guideline_id: "labels", supporting_guideline_ids: [] },
        ],
      }),
    ],
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
  expect(conversation.messages[2]?.answer).toBeUndefined();
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
    lifecycle: "submitted",
    message: { ...answer, metadata: { ...answer.metadata, status: "submitted" as const } },
    options: {},
  },
])("keeps accepted evidence through $lifecycle orchestration", ({ message, options }) => {
  const conversation = deriveConversation([user, search, read, message], options);
  expect(conversation.evidence.map((item) => item.stage)).toEqual(["primary", "supporting"]);
  expect(conversation.messages.at(-1)?.answer).toEqual(result);
  expect(conversation.messages.at(-1)?.drafting).toBe(false);
});

it("streams complete grounded points before the presentation finishes", () => {
  const message: EveMessage = {
    id: "draft",
    role: "assistant",
    metadata: { status: "streaming" },
    parts: [
      {
        type: "dynamic-tool",
        toolName: "present_answer",
        toolCallId: "draft-call",
        state: "input-streaming",
        input: undefined,
        inputText: '{"workflow":"visfeedback"',
      },
    ],
  };
  const conversation = deriveConversation([read, message], {
    draft: {
      messageId: "draft",
      toolCallId: "draft-call",
      value: { ...result, points: [result.points[0], { primary_guideline_id: "contrast" }] },
    },
  });
  expect(conversation.messages.at(-1)?.answer).toEqual(result);
  expect(conversation.messages.at(-1)?.drafting).toBe(true);
  expect(conversation.evidence.map((item) => item.stage)).toEqual(["primary", "supporting"]);
});

it.each([
  {
    reason: "unread citation",
    messageId: "draft",
    toolCallId: "draft-call",
    value: { ...result, points: [{ ...result.points[0], primary_guideline_id: "unread" }] },
  },
  {
    reason: "incomplete first point",
    messageId: "draft",
    toolCallId: "draft-call",
    value: { ...result, points: [{ primary_guideline_id: "labels" }] },
  },
  { reason: "another message", messageId: "previous", toolCallId: "draft-call", value: result },
  { reason: "another tool call", messageId: "draft", toolCallId: "previous-call", value: result },
])("withholds a draft with $reason", ({ reason: _reason, ...draft }) => {
  const conversation = deriveConversation(
    [
      read,
      {
        id: "draft",
        role: "assistant",
        metadata: { status: "streaming" },
        parts: [
          {
            type: "dynamic-tool",
            toolName: "present_answer",
            toolCallId: "draft-call",
            state: "input-streaming",
            input: undefined,
            inputText: "{",
          },
        ],
      },
    ],
    { draft },
  );
  expect(conversation.messages.at(-1)?.answer).toBeUndefined();
  expect(conversation.evidence.map((item) => item.stage)).toEqual(["read", "read"]);
});

it("promotes a corrected presentation after an evidence error", () => {
  const rejected: EveMessage = {
    id: "repair",
    role: "assistant",
    metadata: { status: "streaming" },
    parts: [
      {
        type: "dynamic-tool",
        toolName: "present_answer",
        toolCallId: "rejected",
        state: "output-error",
        input: { ...result, points: [{ ...result.points[0], primary_guideline_id: "unread" }] },
        errorText: "Read this guideline before citing it.",
      },
    ],
  };
  expect(deriveConversation([read, rejected]).messages.at(-1)?.answer).toBeUndefined();
  const repaired = deriveConversation([
    read,
    { ...rejected, parts: [...rejected.parts, presentation(result)] },
  ]);
  expect(repaired.messages.at(-1)?.answer).toEqual(result);
  expect(repaired.messages.at(-1)?.complete).toBe(false);
  expect(repaired.evidence.map((item) => item.stage)).toEqual(["primary", "supporting"]);
});

it("withholds an unverified presentation output", () => {
  const conversation = deriveConversation([
    read,
    {
      ...answer,
      parts: [
        presentation({
          ...result,
          points: [{ ...result.points[0], primary_guideline_id: "unread" }],
        }),
      ],
    },
  ]);
  expect(conversation.messages.at(-1)?.answer).toBeUndefined();
  expect(conversation.evidence.map((item) => item.stage)).toEqual(["read", "read"]);
});

it("keeps a draft within the three-point answer contract", () => {
  const ids = ["labels", "contrast", "spacing", "ordering"];
  const guidelines = ids.map((id) => ({ id, title: id, description: `Guidance for ${id}` }));
  const conversation = deriveConversation([
    {
      ...read,
      parts: [
        {
          type: "dynamic-tool",
          toolCallId: "read-four",
          toolName: "read_guidelines",
          state: "output-available",
          input: { ids },
          output: {
            guidelines,
            citations: ids.map((id) => ({
              id,
              url: `https://chartcoach.dev/guidelines/${id}`,
              sources: [],
            })),
          },
        },
      ],
    },
    {
      id: "draft",
      role: "assistant",
      parts: [
        {
          type: "dynamic-tool",
          toolCallId: "draft-call",
          toolName: "present_answer",
          state: "input-available",
          input: {
            ...result,
            points: ids.map((id) => ({
              ...result.points[0],
              primary_guideline_id: id,
              supporting_guideline_ids: [],
            })),
          },
        },
      ],
    },
  ]);
  expect(
    conversation.messages.at(-1)?.answer?.points.map((point) => point.primary_guideline_id),
  ).toEqual(["labels", "contrast", "spacing"]);
});
