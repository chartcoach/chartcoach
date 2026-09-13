import { useLayoutEffect, useRef, useState } from "react";
import { createThread, saveChartImage } from "../browser/workspace-client";
import type { ChartAttachment } from "./attachment";
import type { CatalogFilterSelection } from "./use-catalog-filters";
import type { useWorkspace } from "./use-workspace";

type ThreadHeaders = { "x-chartcoach-thread"?: string; "x-chartcoach-connection"?: string };

export function useThreadSession(
  workspace: ReturnType<typeof useWorkspace>,
  selection: CatalogFilterSelection | undefined,
) {
  const [threadId, setThreadId] = useState(workspace.active?.id);
  const thread = useRef(workspace.active?.id);
  const registeredSession = useRef(workspace.active?.sessionId);
  const current = useRef({ selection, connectionId: workspace.connectionId });
  useLayoutEffect(() => {
    current.current = { selection, connectionId: workspace.connectionId };
  }, [selection, workspace.connectionId]);

  function remember() {
    if (thread.current) workspace.rememberThread(thread.current);
  }

  return {
    threadId,
    id: () => thread.current,
    headers: () => {
      const headers: ThreadHeaders = {};

      if (thread.current) headers["x-chartcoach-thread"] = thread.current;

      if (current.current.connectionId)
        headers["x-chartcoach-connection"] = current.current.connectionId;

      return headers;
    },
    onSessionChange: (session: { sessionId: string } | undefined) => {
      if (session?.sessionId && session.sessionId !== registeredSession.current) {
        registeredSession.current = session.sessionId;
        remember();
      }
    },
    remember,
    prepare: async (title: string, chart: ChartAttachment | undefined, signal: AbortSignal) => {
      const { selection: selected, connectionId } = current.current;

      if (!selected)
        throw new Error("Wait for the catalog to load before starting a conversation.");

      if (selected.matchedGuidelines === 0)
        throw new Error("Broaden your guideline selection before starting a conversation.");

      if (!connectionId) throw new Error("Choose a model connection before sending.");

      if (!thread.current) {
        const created = await createThread({ title, connectionId, knowledge: selected }, signal);
        signal.throwIfAborted();
        thread.current = created.id;
        setThreadId(created.id);
        remember();
      }

      if (chart) await saveChartImage(thread.current, chart, signal);
      signal.throwIfAborted();
    },
    reset: () => {
      thread.current = undefined;
      registeredSession.current = undefined;
      setThreadId(undefined);
      history.replaceState(null, "", location.pathname);
    },
  };
}
