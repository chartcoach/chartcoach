import { useCallback, useEffect, useRef, useState } from "react";
import { loadPreferences, loadThread, loadThreads } from "../browser/workspace-client";
import type { Connection, SavedThread, ThreadDetail } from "../shared/preferences";

export function useWorkspace() {
  const [connections, setConnections] = useState<Connection[]>([]);
  const [connectionId, setConnectionId] = useState<string>();
  const [allowedOrigins, setAllowedOrigins] = useState<string[]>([]);
  const [threads, setThreads] = useState<SavedThread[]>([]);
  const [active, setActive] = useState<ThreadDetail>();
  const [key, setKey] = useState("new");
  const [ready, setReady] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string>();
  const opening = useRef<AbortController>(undefined);
  async function refreshThreads() {
    setThreads(await loadThreads());
  }
  async function refreshConnections() {
    const preferences = await loadPreferences();
    setConnections(preferences.connections);
    setAllowedOrigins(preferences.allowedOrigins);
  }
  function selectConnection(id: string | undefined) {
    setConnectionId(id);
    try {
      if (id) localStorage.setItem("chartcoach.connection", id);
      else localStorage.removeItem("chartcoach.connection");
    } catch {
      /* Storage can be disabled by the browser. */
    }
  }
  const openThread = useCallback(async (id: string) => {
    opening.current?.abort();
    const controller = new AbortController();
    opening.current = controller;
    setLoading(true);
    try {
      const thread = await loadThread(id, controller.signal);
      if (controller.signal.aborted) return;
      setActive(thread);
      setKey(`${id}:${crypto.randomUUID()}`);
      setConnectionId(thread.connectionId);
      setError(undefined);
      history.replaceState(null, "", `?thread=${encodeURIComponent(id)}`);
    } catch (cause) {
      if (!controller.signal.aborted)
        setError(cause instanceof Error ? cause.message : "Could not open the conversation.");
    } finally {
      if (!controller.signal.aborted) setLoading(false);
    }
  }, []);
  useEffect(() => {
    const controller = new AbortController();
    void (async () => {
      try {
        const preferences = await loadPreferences(controller.signal);
        if (controller.signal.aborted) return;
        setConnections(preferences.connections);
        setAllowedOrigins(preferences.allowedOrigins);
        let remembered: string | null = null;
        try {
          remembered = localStorage.getItem("chartcoach.connection");
        } catch {
          /* Browser storage is optional. */
        }
        setConnectionId(
          preferences.connections.find((item) => item.id === remembered)?.id ??
            preferences.connections[0]?.id,
        );
        const savedThreads = await loadThreads(controller.signal);
        if (controller.signal.aborted) return;
        setThreads(savedThreads);
        const id = new URLSearchParams(location.search).get("thread");
        if (id) await openThread(id);
      } catch (cause) {
        if (!controller.signal.aborted)
          setError(cause instanceof Error ? cause.message : "Could not load your workspace.");
      } finally {
        if (!controller.signal.aborted) setReady(true);
      }
    })();
    return () => {
      controller.abort();
      opening.current?.abort();
    };
  }, [openThread]);
  function rememberThread(id: string) {
    history.replaceState(null, "", `?thread=${encodeURIComponent(id)}`);
    void refreshThreads().catch(() =>
      setError("History could not refresh. Your conversation is saved."),
    );
  }
  return {
    connections,
    connectionId,
    connection: connections.find((item) => item.id === connectionId),
    selectConnection,
    allowedOrigins,
    threads,
    active,
    key,
    ready,
    loading,
    error,
    openThread,
    rememberThread,
    refreshThreads,
    refreshConnections,
  };
}
