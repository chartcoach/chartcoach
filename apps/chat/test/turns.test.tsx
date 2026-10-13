import { expect, it } from "vite-plus/test";
import type { EveMessage } from "eve/react";
import { deriveConversation } from "../chat/evidence";
import { progressPhase } from "../chat/progress";
import { projectTurns, type SentTurn } from "../chat/turns";

const earlier: EveMessage[] = [
  { id: "1:user", role: "user", parts: [{ type: "text", text: "Review this chart." }] },
  { id: "1:assistant", role: "assistant", parts: [], metadata: { status: "complete" } },
];

const sent: SentTurn = {
  id: "follow-up",
  start: earlier.length,
  parts: [
    { type: "text", text: "Which palette prints well?" },
    {
      type: "file",
      mediaType: "image/png",
      filename: "chart.png",
      url: "data:image/png;base64,AQID",
    },
  ],
};

const accepted: EveMessage = { id: "2:user", role: "user", parts: sent.parts };

const reply: EveMessage = {
  id: "2:assistant",
  role: "assistant",
  parts: [],
  metadata: { status: "streaming" },
};

it("shows a sent message and a starting reply before the runtime accepts them", () => {
  const { messages } = projectTurns(earlier, [sent], true);

  expect(messages.slice(earlier.length)).toEqual([
    {
      id: "follow-up:user",
      role: "user",
      parts: sent.parts,
      metadata: { optimistic: true, status: "submitted" },
    },
    {
      id: "follow-up:assistant",
      role: "assistant",
      parts: [],
      metadata: { optimistic: true, status: "streaming" },
    },
  ]);
  expect(progressPhase(deriveConversation(messages).messages.at(-1)!)).toBe("preparing");
});

it("gives accepted messages the ids their turn was shown with", () => {
  const userOnly = projectTurns([...earlier, accepted], [sent], true);

  expect(userOnly.messages.map(({ id }) => id)).toEqual([
    "1:user",
    "1:assistant",
    "follow-up:user",
    "follow-up:assistant",
  ]);

  const answered = projectTurns([...earlier, accepted, reply], [sent], true);

  expect(answered.messages.map(({ id }) => id)).toEqual([
    "1:user",
    "1:assistant",
    "follow-up:user",
    "follow-up:assistant",
  ]);
  expect(answered.messages.some(({ metadata }) => metadata?.optimistic)).toBe(false);
  expect(answered.id("2:assistant")).toBe("follow-up:assistant");
});

it("keeps earlier turns identified after the next message is sent", () => {
  const next: SentTurn = { id: "next", start: 4, parts: [{ type: "text", text: "Thanks." }] };
  const { messages } = projectTurns([...earlier, accepted, reply], [sent, next], true);

  expect(messages.map(({ id }) => id)).toEqual([
    "1:user",
    "1:assistant",
    "follow-up:user",
    "follow-up:assistant",
    "next:user",
    "next:assistant",
  ]);
});

it("drops the starting reply when an accepted turn stops before replying", () => {
  const { messages } = projectTurns([...earlier, accepted], [sent], false);

  expect(messages.at(-1)?.id).toBe("follow-up:user");
});

it("keeps an interruption on the reply it ended while a retry starts", () => {
  const interrupted: EveMessage = {
    id: "1:assistant",
    role: "assistant",
    parts: [],
    metadata: { status: "streaming", turnId: "1" },
  };

  const { messages } = projectTurns([earlier[0]!, interrupted], [sent], true);

  const views = deriveConversation(messages, {
    interrupted: true,
    error: "The connection closed.",
  }).messages;

  expect(views[1]).toMatchObject({ failed: true, failureReason: "The connection closed." });
  expect(views.at(-1)).toMatchObject({ failed: false });
  expect(progressPhase(views.at(-1)!)).toBe("preparing");
});

it("keeps the ids of accepted messages when their send is withdrawn", () => {
  const withdrawn = { ...sent, withdrawn: true };

  expect(projectTurns(earlier, [withdrawn], false).messages).toEqual(earlier);
  expect(
    projectTurns([...earlier, accepted, reply], [withdrawn], false).messages.map(({ id }) => id),
  ).toEqual(["1:user", "1:assistant", "follow-up:user", "follow-up:assistant"]);
});
