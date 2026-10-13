import type { GuidelineLinks } from "../shared/guideline-links";
import { useMemo } from "react";
import type { EveMessage, useEveAgent } from "eve/react";
import { chartImageURL } from "../browser/workspace-client";
import { deriveConversation } from "./evidence";
import { projectTurns, type SentTurn } from "./turns";
import { useAnswerDraft } from "./use-answer-draft";

export function useConversation(
  agent: Pick<ReturnType<typeof useEveAgent>, "events" | "status" | "error"> & {
    data: { messages: readonly EveMessage[] };
  },
  threadId: string | undefined,
  interruptedTurns: ReadonlySet<string>,
  guidelineLinks: GuidelineLinks,
  turns: readonly SentTurn[],
  running: boolean,
) {
  const draft = useAnswerDraft(agent.data.messages);

  const conversation = useMemo(() => {
    const projection = projectTurns(agent.data.messages, turns, running);

    return deriveConversation(
      projection.messages.map((message) =>
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
        guidelineLinks,
        draft: draft && { ...draft, messageId: projection.id(draft.messageId) },
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
    );
  }, [
    agent.data.messages,
    agent.events,
    agent.status,
    agent.error,
    interruptedTurns,
    draft,
    guidelineLinks,
    threadId,
    turns,
    running,
  ]);

  return conversation;
}
