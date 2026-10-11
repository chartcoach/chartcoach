import { defaultGuidelineLinks } from "../shared/guideline-links";
import { useCallback, useEffect, useRef, useState } from "react";
import { useParams, usePathname, useRouter } from "next/navigation";
import { loadPreferences, loadThread, loadThreads } from "../browser/workspace-client";
import { chatPath } from "../shared/routes";
import type { Connection } from "../shared/preferences";
import type { SavedThread, ThreadDetail } from "../shared/threads";

export function useWorkspace() {
  const router = useRouter();
  const pathname = usePathname();
  const { threadId: requestedId } = useParams<{ threadId?: string }>();
  const [connections, setConnections] = useState<Connection[]>([]);
  const [connectionId, setConnectionId] = useState<string>();
  const [allowedOrigins, setAllowedOrigins] = useState<string[]>([]);
  const [guidelineLinks, setGuidelineLinks] = useState(defaultGuidelineLinks);
  const [tracing, setTracing] = useState(false);
  const [threads, setThreads] = useState<SavedThread[]>([]);
  const [active, setActive] = useState<ThreadDetail>();
  const currentThread = useRef<ThreadDetail>(undefined);
  const [key, setKey] = useState("new");
  const [ready, setReady] = useState(false);
  const [error, setError] = useState<string>();
  const [threadError, setThreadError] = useState<string>();
  const [attempt, setAttempt] = useState(0);
  const [threadAttempt, setThreadAttempt] = useState(0);

  const historyRequest = useRef(0);

  async function refreshThreads(signal?: AbortSignal) {
    const request = ++historyRequest.current;
    let savedThreads: SavedThread[];

    try {
      savedThreads = await loadThreads(signal);
      signal?.throwIfAborted();
    } catch (cause) {
      if (request !== historyRequest.current) return;
      throw cause;
    }

    if (request !== historyRequest.current) return;
    setThreads(savedThreads);
    setError(undefined);
    const metadata = savedThreads.find((thread) => thread.id === currentThread.current?.id);

    if (metadata && currentThread.current) {
      currentThread.current = { ...currentThread.current, ...metadata };
      setActive(currentThread.current);
    }
  }

  async function refreshConnections(signal?: AbortSignal) {
    const preferences = await loadPreferences(signal);
    signal?.throwIfAborted();
    setConnections(preferences.connections);
    setAllowedOrigins(preferences.allowedOrigins);
    setTracing(preferences.tracing);
    setGuidelineLinks(preferences.guidelines);

    return preferences;
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

  useEffect(() => {
    const controller = new AbortController();
    void (async () => {
      try {
        const preferences = await loadPreferences(controller.signal);
        controller.signal.throwIfAborted();
        setConnections(preferences.connections);
        setAllowedOrigins(preferences.allowedOrigins);
        setTracing(preferences.tracing);
        setGuidelineLinks(preferences.guidelines);
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
        // Establish the owner cookie before protected reads. History and the
        // route's conversation then load independently.
        setReady(true);
        setError(undefined);
        await refreshThreads(controller.signal);
      } catch (cause) {
        if (!controller.signal.aborted)
          setError(cause instanceof Error ? cause.message : "Could not load your workspace.");
      }
    })();

    return () => controller.abort();
  }, [attempt]);

  useEffect(() => {
    setThreadError(undefined);

    if (!ready) return;

    if (!requestedId) {
      if (currentThread.current) {
        currentThread.current = undefined;
        setActive(undefined);
        setKey(`new:${crypto.randomUUID()}`);
      }

      return;
    }

    if (currentThread.current?.id === requestedId) return;
    const controller = new AbortController();
    void loadThread(requestedId, controller.signal)
      .then((thread) => {
        if (controller.signal.aborted) return;
        currentThread.current = thread;
        setActive(thread);
        setKey(`${thread.id}:${crypto.randomUUID()}`);
        setConnectionId(thread.connectionId);
      })
      .catch((cause) => {
        if (!controller.signal.aborted)
          setThreadError(
            cause instanceof Error ? cause.message : "Could not open the conversation.",
          );
      });

    return () => controller.abort();
  }, [requestedId, ready, threadAttempt]);

  const openThread = useCallback(
    (id: string) =>
      router.push(chatPath(id), { scroll: false, transitionTypes: ["workspace-navigation"] }),
    [router],
  );

  function rememberThread() {
    void refreshThreads().catch(() =>
      setError("History could not refresh. Your conversation is saved."),
    );
  }

  function adoptThread(thread: ThreadDetail) {
    currentThread.current = thread;
    setActive(thread);
    // Keep the initiating runtime mounted while its first message is accepted.
    router.replace(chatPath(thread.id), { scroll: false });
    rememberThread();
  }

  function clearThread() {
    currentThread.current = undefined;
    setActive(undefined);
  }

  function attachSession(sessionId: string) {
    if (currentThread.current) {
      currentThread.current = { ...currentThread.current, sessionId };
      setActive(currentThread.current);
    }
  }

  const loading = !ready || (requestedId ? active?.id !== requestedId : !!active);

  return {
    connections,
    connectionId,
    connection: connections.find((item) => item.id === connectionId),
    selectConnection,
    allowedOrigins,
    tracing,
    guidelineLinks,
    threads,
    active,
    key,
    ready,
    loading,
    error,
    threadError,
    requestedId,
    pathname,
    openThread,
    adoptThread,
    attachSession,
    clearThread,
    newChat: () => router.push("/", { scroll: false, transitionTypes: ["workspace-navigation"] }),
    chatHref: () => (currentThread.current ? chatPath(currentThread.current.id) : "/"),
    retry: () => {
      if (!ready) setAttempt((value) => value + 1);
      else if (threadError) setThreadAttempt((value) => value + 1);
      else rememberThread();
    },
    rememberThread,
    refreshThreads,
    refreshConnections,
  };
}
