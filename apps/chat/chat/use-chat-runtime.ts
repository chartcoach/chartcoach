"use client";

import { useEffect, useLayoutEffect, useMemo, useRef, useState } from "react";
import { useEveAgent } from "eve/react";
import { convertEveMessage, getEveMessageContent } from "@assistant-ui/eve";
import { useExternalStoreRuntime, type AssistantRuntime } from "@assistant-ui/react";
import { reviewSchema } from "../shared/review";
import type { ChartAttachment } from "./attachment";
import { useChartAttachments } from "./use-chart-attachments";
import { deriveConversation, type MessageView } from "./evidence";
import type { CatalogFilterSelection } from "./use-catalog-filters";
import { encodeCatalogSelection } from "../lib/catalog-client";

const statusLabels: Readonly<Partial<Record<ReturnType<typeof useEveAgent>["status"], string>>> = {
  submitted: "Starting your review",
  streaming: "Reviewing your chart",
  resuming: "Reconnecting to your conversation",
  error: "Response interrupted. You can send your message again.",
};

export function useChatRuntime(selection: CatalogFilterSelection | undefined) {
  const [attachments, setAttachments] = useState(new Map<string, ChartAttachment>());
  const sentChart = useRef<ChartAttachment>(undefined);
  const [error, setError] = useState<string>();
  const [interruptedTurns, setInterruptedTurns] = useState<ReadonlySet<string>>(new Set());
  const sendError = useRef<Error>(undefined);
  const runtimeRef = useRef<AssistantRuntime>(undefined);
  const selectionRef = useRef(selection);
  const selectionHeader = useRef<string>(undefined);
  const hasSession = useRef(false);
  const pendingSend = useRef<AbortController>(undefined);
  const [preparing, setPreparing] = useState(false);
  useLayoutEffect(() => {
    selectionRef.current = selection;
  }, [selection]);
  const agent = useEveAgent({
    headers: () => {
      const headers: Record<string, string> = {};
      if (!hasSession.current && selectionHeader.current)
        headers["x-chartcoach-selection"] = selectionHeader.current;
      return headers;
    },
    onSessionChange: (session) => {
      hasSession.current = !!session?.sessionId;
      if (hasSession.current) selectionHeader.current = undefined;
    },
    onError: (error) => {
      sendError.current = error;
      setError(error.message);
    },
    onFinish: (snapshot) => {
      if (snapshot.status !== "error") return;
      const message = snapshot.data.messages.findLast((item) => item.role === "assistant");
      const turnId = message?.metadata?.turnId;
      if (turnId && message.metadata?.status !== "complete") {
        setInterruptedTurns((current) => new Set(current).add(turnId));
      }
    },
  });
  const busy = preparing || agent.status === "submitted" || agent.status === "streaming";
  const { adapter, reading, messageInput, upload } = useChartAttachments(
    runtimeRef,
    busy || agent.status === "resuming",
    setError,
  );
  const disabled = busy || reading || agent.status === "resuming";
  const conversation = useMemo(
    () =>
      deriveConversation(agent.data.messages, {
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
        interrupted: agent.status === "error",
      }),
    [agent.data.messages, agent.events, agent.status, interruptedTurns],
  );
  const statusText =
    (preparing ? "Preparing your catalog selection" : statusLabels[agent.status]) ??
    (conversation.messages.at(-1)?.stopped
      ? "Response stopped."
      : conversation.messages.length
        ? "Response complete."
        : "");

  const runtime = useExternalStoreRuntime<MessageView>({
    messages: conversation.messages,
    isRunning: busy,
    isDisabled: reading || agent.status === "resuming",
    isSendDisabled: !selection || selection.matchedGuidelines === 0,
    adapters: { attachments: adapter },
    convertMessage(view, index) {
      const converted = convertEveMessage(view.message, index, agent.data.messages, {
        isRunning: busy,
        error: agent.error,
      });
      if (converted.role !== "assistant") return converted;
      return {
        ...converted,
        content: converted.content.filter((part) => part.type !== "text"),
      };
    },
    async onNew(message) {
      if (pendingSend.current) throw new Error("Wait for the current message to finish.");
      const controller = new AbortController();
      pendingSend.current = controller;
      setError(undefined);
      sendError.current = undefined;
      let chart: ChartAttachment | undefined;
      for (const attachment of message.attachments ?? []) {
        const file = attachment.content.find((part) => part.type === "file");
        if (file?.filename) {
          chart = {
            data: file.data,
            mediaType: file.mimeType,
            name: attachment.name,
            filename: file.filename,
          };
          const preview = chart;
          setAttachments((current) => new Map(current).set(preview.filename, preview));
        }
      }
      const content = message.content.some((part) => part.type === "text" && part.text.trim())
        ? message.content
        : [
            {
              type: "text" as const,
              text: "Review this chart and suggest improvements with guideline citations.",
            },
          ];
      try {
        const current = selectionRef.current;
        if (!current) throw new Error("Wait for the catalog to load before starting a review.");
        if (current.matchedGuidelines === 0)
          throw new Error("Broaden your knowledge selection before starting a review.");
        if (!hasSession.current) {
          setPreparing(true);
          selectionHeader.current = await encodeCatalogSelection(
            current.selection,
            controller.signal,
          );
        }
        controller.signal.throwIfAborted();
        setPreparing(false);
        await agent.send(getEveMessageContent({ ...message, content }), {
          outputSchema: reviewSchema,
        });
        if (sendError.current) throw sendError.current;
        if (chart) sentChart.current = chart;
      } catch (cause) {
        const reason = controller.signal.aborted
          ? undefined
          : cause instanceof Error
            ? cause.message
            : "Could not send the message. Try again.";
        setError(reason);
        const composer = runtimeRef.current!.thread.composer;
        if (composer.getState().isEmpty) {
          composer.setText(
            message.content.flatMap((part) => (part.type === "text" ? [part.text] : [])).join("\n"),
          );
          for (const attachment of message.attachments ?? [])
            await composer.addAttachment(attachment);
        }
        if (!controller.signal.aborted) throw cause;
      } finally {
        selectionHeader.current = undefined;
        pendingSend.current = undefined;
        setPreparing(false);
      }
    },
    async onCancel() {
      if (preparing) {
        pendingSend.current?.abort();
        return;
      }
      try {
        await agent.cancel();
      } catch {
        setError("Could not stop the response. Try again.");
      }
    },
  });
  useLayoutEffect(() => {
    runtimeRef.current = runtime;
  }, [runtime]);
  useEffect(
    () =>
      runtime.thread.composer.unstable_on("attachmentAddError", (event) => setError(event.message)),
    [runtime],
  );
  useEffect(() => () => pendingSend.current?.abort(), []);

  async function newChat() {
    await runtime.thread.composer.reset();
    runtime.thread.unstable_notifySessionReset();
    agent.reset();
    selectionHeader.current = undefined;
    hasSession.current = false;
    setAttachments(new Map());
    sentChart.current = undefined;
    setInterruptedTurns(new Set());
    setError(undefined);
    messageInput.current?.focus();
  }
  async function restartKeepingChart() {
    if (disabled) throw new Error("Wait for this review to finish before changing its knowledge.");
    const composer = runtime.thread.composer;
    const draft = composer.getState();
    const chart = sentChart.current;
    await newChat();
    composer.setText(draft.text);
    if (draft.attachments.length) {
      for (const attachment of draft.attachments) {
        if (attachment.content)
          await composer.addAttachment({ ...attachment, content: attachment.content });
      }
    } else if (chart) {
      await composer.addAttachment({
        id: chart.filename,
        type: "image",
        name: chart.name,
        contentType: chart.mediaType,
        content: [
          { type: "file", data: chart.data, mimeType: chart.mediaType, filename: chart.filename },
        ],
      });
    }
  }
  return {
    runtime,
    conversation,
    attachments,
    busy,
    disabled,
    reading,
    error: error ?? agent.error?.message,
    upload,
    newChat,
    restartKeepingChart,
    statusText,
    messageInput,
  };
}
