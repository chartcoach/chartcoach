import { useMemo } from "react";
import type { EveMessage, useEveAgent } from "eve/react";
import { chartImageURL } from "../browser/workspace-client";
import { deriveConversation } from "./evidence";
import { useAnswerDraft } from "./use-answer-draft";

export function useConversation(
  agent: Pick<ReturnType<typeof useEveAgent>, "events" | "status" | "error"> & {
    data: { messages: readonly EveMessage[] };
  },
  threadId: string | undefined,
  interruptedTurns: ReadonlySet<string>,
) {
  const draft = useAnswerDraft(agent.data.messages);

  const conversation = useMemo(
    () =>
      deriveConversation(
        agent.data.messages.map((message) =>
          threadId && message.role === "user"
            ? {
                ...message,
                parts: message.parts.map((part) =>
                  part.type === "file" && part.filename
                    ? { ...part, url: chartImageURL(threadId, part.filename) }
                    : part,
                ),
              }
            : message,
        ),
        {
          draft,
          stoppedTurnIds: new Set(
            agent.events.flatMap((event) =>
              event.type === "turn.cancelled" ? [event.data.turnId] : [],
            ),
          ),
          failedTurnIds: new Set([
            ...interruptedTurns,
            ...agent.events.flatMap((event) =>
              event.type === "turn.failed" ? [event.data.turnId] : [],
            ),
          ]),
          failureReasons: new Map(
            agent.events.flatMap((event) =>
              event.type === "turn.failed" ? [[event.data.turnId, event.data.message]] : [],
            ),
          ),
          interrupted: agent.status === "error",
          error: agent.error?.message,
        },
      ),
    [
      agent.data.messages,
      agent.events,
      agent.status,
      agent.error,
      interruptedTurns,
      draft,
      threadId,
    ],
  );

  return conversation;
}
