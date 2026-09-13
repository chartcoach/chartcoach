import { useEffect, useState } from "react";
import { parsePartialJson } from "ai";
import type { EveMessage } from "eve/react";
import { answerDraftSchema, type AnswerDraftValue } from "../shared/answer";

export interface AnswerDraft {
  messageId: string;
  toolCallId: string;
  value: AnswerDraftValue;
}

export function useAnswerDraft(messages: readonly EveMessage[]) {
  const message = messages.findLast((item) => item.role === "assistant");

  const part = message?.parts.findLast(
    (item) => item.type === "dynamic-tool" && item.toolName === "present_answer",
  );

  const text =
    part?.type === "dynamic-tool" && part.state === "input-streaming" ? part.inputText : undefined;

  const toolCallId = part?.type === "dynamic-tool" ? part.toolCallId : undefined;
  const messageId = message?.id;
  const [draft, setDraft] = useState<AnswerDraft>();
  useEffect(() => {
    if (!text || !messageId || !toolCallId) return;
    let current = true;
    void parsePartialJson(text).then(({ value }) => {
      const parsed = answerDraftSchema.safeParse(value);

      if (current)
        setDraft(parsed.success ? { messageId, toolCallId, value: parsed.data } : undefined);
    });

    return () => {
      current = false;
    };
  }, [text, messageId, toolCallId]);

  return text && draft && draft.messageId === messageId && draft.toolCallId === toolCallId
    ? draft
    : undefined;
}
