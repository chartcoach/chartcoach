"use client";

import { useEffect, useLayoutEffect, useMemo, useRef, useState } from "react";
import { useEveAgent } from "eve/react";
import { convertEveMessage, getEveMessageContent } from "@assistant-ui/eve";
import { useExternalStoreRuntime, type AssistantRuntime } from "@assistant-ui/react";
import { readAttachment, type ChartAttachment } from "./attachment";
import { useChartAttachments } from "./use-chart-attachments";
import { deriveConversation, type MessageView } from "./evidence";
import type { CatalogFilterSelection } from "./use-catalog-filters";
import { type Mode } from "../shared/workflow";
import { starters } from "../shared/starters";
import { useAnswerDraft } from "./use-answer-draft";
import type { useWorkspace } from "./use-workspace";
import {
  chartImageURL,
  createThread,
  loadChartImage,
  saveChartImage,
  updateThread,
} from "../browser/workspace-client";

const statusLabels: Readonly<Partial<Record<ReturnType<typeof useEveAgent>["status"], string>>> = {
  submitted: "Starting your conversation",
  streaming: "Finding grounded advice",
  resuming: "Reconnecting to your conversation",
  error: "Response interrupted. You can send your message again.",
};

type ChatHeaders = {
  "x-chartcoach-mode": Mode;
  "x-chartcoach-thread"?: string;
  "x-chartcoach-connection"?: string;
};

export function useChatRuntime(
  selection: CatalogFilterSelection | undefined,
  workspace: ReturnType<typeof useWorkspace>,
) {
  const [threadId, setThreadId] = useState(workspace.active?.id);
  const threadRef = useRef(workspace.active?.id);
  const connectionRef = useRef(workspace.connectionId);
  const [mode, setMode] = useState<Mode>("auto");
  const modeRef = useRef<Mode>(mode);
  const [attachments, setAttachments] = useState(new Map<string, ChartAttachment>());
  const sentChart = useRef<ChartAttachment>(undefined);
  const [error, setError] = useState<string>();
  const [interruptedTurns, setInterruptedTurns] = useState<ReadonlySet<string>>(new Set());
  const sendError = useRef<Error>(undefined);
  const runtimeRef = useRef<AssistantRuntime>(undefined);
  const selectionRef = useRef(selection);
  const registeredSession = useRef(workspace.active?.sessionId);
  const pendingSend = useRef<AbortController>(undefined);
  const [preparing, setPreparing] = useState(false);
  useLayoutEffect(() => {
    selectionRef.current = selection;
    modeRef.current = mode;
    connectionRef.current = workspace.connectionId;
  }, [selection, mode, workspace.connectionId]);
  const agent = useEveAgent({
    // Eve's optimistic projection flattens images into literal [file: ...] text.
    // Render accepted messages instead; the composer retains any failed draft.
    optimistic: false,
    initialSession: workspace.active?.sessionId
      ? { sessionId: workspace.active.sessionId, streamIndex: 0 }
      : undefined,
    resume: !!workspace.active?.sessionId,
    headers: () => {
      const headers: ChatHeaders = { "x-chartcoach-mode": modeRef.current };
      if (threadRef.current) headers["x-chartcoach-thread"] = threadRef.current;
      if (connectionRef.current) headers["x-chartcoach-connection"] = connectionRef.current;
      return headers;
    },
    onSessionChange: (session) => {
      if (session?.sessionId && session.sessionId !== registeredSession.current) {
        registeredSession.current = session.sessionId;
        if (threadRef.current) workspace.rememberThread(threadRef.current);
      }
    },
    onError: (error) => {
      sendError.current = error;
      setError(error.message);
    },
    onFinish: (snapshot) => {
      if (threadRef.current) workspace.rememberThread(threadRef.current);
      if (snapshot.status !== "error") return;
      const message = snapshot.data.messages.findLast((item) => item.role === "assistant");
      const turnId = message?.metadata?.turnId;
      if (turnId && message.metadata?.status !== "complete") {
        setInterruptedTurns((current) => new Set(current).add(turnId));
      }
    },
  });
  const busy = preparing || agent.status === "submitted" || agent.status === "streaming";
  const needsNewSession =
    agent.events.some(
      (event) => event.type === "session.failed" || event.type === "session.completed",
    ) ||
    (agent.error && "code" in agent.error && agent.error.code === "session_not_active");
  const { adapter, reading, messageInput, upload, uploadExample } = useChartAttachments(
    runtimeRef,
    busy || agent.status === "resuming",
    setError,
  );
  const disabled = busy || reading || agent.status === "resuming" || workspace.loading;
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
  const statusText =
    (preparing ? "Preparing your catalog selection" : statusLabels[agent.status]) ??
    (conversation.messages.at(-1)?.stopped
      ? "Response stopped."
      : conversation.messages.length
        ? "Response complete."
        : "");

  const runtime = useExternalStoreRuntime<MessageView>({
    suggestions: starters.map(({ prompt, title, description }) => ({
      prompt,
      title,
      label: description,
    })),
    messages: conversation.messages,
    isRunning: busy,
    isDisabled: reading || agent.status === "resuming",
    isSendDisabled:
      !!needsNewSession ||
      !selection ||
      selection.matchedGuidelines === 0 ||
      !workspace.ready ||
      !workspace.connection,
    adapters: {
      attachments: adapter,
      threadList: {
        threadId,
        isLoading: !workspace.ready || workspace.loading,
        threads: workspace.threads
          .filter((thread) => !thread.archived)
          .map((thread) => ({ id: thread.id, title: thread.title, status: "regular" as const })),
        archivedThreads: workspace.threads
          .filter((thread) => thread.archived)
          .map((thread) => ({ id: thread.id, title: thread.title, status: "archived" as const })),
        onSwitchToNewThread: newChat,
        onSwitchToThread: async (id) => {
          if (!disabled) await workspace.openThread(id);
        },
        onRename: async (id, title) => {
          await editHistory(id, { title });
        },
        onArchive: async (id) => {
          await editHistory(id, { archived: true });
        },
        onUnarchive: async (id) => {
          await editHistory(id, { archived: false });
        },
      },
    },
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
              text: "Help me with this image using the selected workflow and cite the relevant guidelines.",
            },
          ];
      try {
        const current = selectionRef.current;
        if (!current)
          throw new Error("Wait for the catalog to load before starting a conversation.");
        if (current.matchedGuidelines === 0)
          throw new Error("Broaden your knowledge selection before starting a conversation.");
        const connectionId = connectionRef.current;
        if (!connectionId) throw new Error("Choose a model connection before sending.");
        if (!threadRef.current) {
          setPreparing(true);
          const title =
            content
              .flatMap((part) => (part.type === "text" ? [part.text] : []))
              .join(" ")
              .trim()
              .slice(0, 160) || "Chart discussion";
          const thread = await createThread(
            { title, connectionId, knowledge: current },
            controller.signal,
          );
          threadRef.current = thread.id;
          setThreadId(thread.id);
          workspace.rememberThread(thread.id);
        }
        if (chart) await saveChartImage(threadRef.current, chart, controller.signal);
        controller.signal.throwIfAborted();
        setPreparing(false);
        await agent.send(getEveMessageContent({ ...message, content }));
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
    registeredSession.current = undefined;
    threadRef.current = undefined;
    setThreadId(undefined);
    history.replaceState(null, "", location.pathname);
    setAttachments(new Map());
    sentChart.current = undefined;
    setInterruptedTurns(new Set());
    setError(undefined);
    messageInput.current?.focus();
  }
  async function editHistory(id: string, value: Parameters<typeof updateThread>[1]) {
    try {
      await updateThread(id, value);
      await workspace.refreshThreads();
    } catch {
      setError("Could not update your history. Try again.");
    }
  }
  async function restartKeepingChart() {
    if (disabled) throw new Error("Wait for this answer to finish before changing its knowledge.");
    const composer = runtime.thread.composer;
    const draft = composer.getState();
    let chart = sentChart.current;
    if (!chart && !draft.attachments.length && threadRef.current) {
      const file = conversation.messages
        .flatMap(({ message }) => (message.role === "user" ? message.parts : []))
        .findLast((part) => part.type === "file");
      if (file?.type === "file" && file.filename) {
        setPreparing(true);
        try {
          chart = await readAttachment(await loadChartImage(threadRef.current, file.filename));
        } finally {
          setPreparing(false);
        }
      }
    }
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
  const currentError = error ?? agent.error?.message ?? workspace.error;
  return {
    mode,
    setMode,
    runtime,
    conversation,
    attachments,
    busy,
    disabled,
    reading,
    error: conversation.messages.at(-1)?.failureReason === currentError ? undefined : currentError,
    recover: needsNewSession
      ? async () => {
          try {
            await restartKeepingChart();
          } catch (cause) {
            setError(
              cause instanceof Error ? cause.message : "Could not restore your chart. Try again.",
            );
          }
        }
      : undefined,
    upload,
    uploadExample,
    newChat,
    restartKeepingChart,
    statusText,
    messageInput,
  };
}
