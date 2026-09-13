import { useEffect, useRef, useState } from "react";
import { removeConnection, saveConnection } from "../browser/workspace-client";
import type { Connection, ConnectionInput } from "../shared/preferences";
import type { useWorkspace } from "./use-workspace";
import { emptyConnection } from "./use-connection-form";

export function useModelSettings(workspace: ReturnType<typeof useWorkspace>) {
  const [open, setOpen] = useState(false);
  const [draft, setDraft] = useState<ConnectionInput>();
  const [removing, setRemoving] = useState<Connection>();
  const [pending, setPending] = useState(false);
  const [error, setError] = useState<string>();
  const controller = useRef<AbortController>(undefined);
  useEffect(() => () => controller.current?.abort(), []);

  async function run(operation: (signal: AbortSignal) => Promise<void>) {
    if (controller.current) return;
    const request = new AbortController();
    controller.current = request;
    setPending(true);
    setError(undefined);

    try {
      await operation(request.signal);
    } catch (cause) {
      if (!request.signal.aborted)
        setError(
          cause instanceof Error ? cause.message : "Could not update the connection. Try again.",
        );
    } finally {
      if (!request.signal.aborted) setPending(false);
      controller.current = undefined;
    }
  }

  const close = () => {
    setOpen(false);
    setDraft(undefined);
    setError(undefined);
  };

  return {
    open,
    draft,
    removing,
    pending,
    error,
    setOpen: (value: boolean) => {
      if (controller.current) return;

      if (!value) close();
      else {
        setOpen(true);
        setError(undefined);
      }
    },
    add: () => setDraft(emptyConnection("openai")),
    edit: ({ id, provider, name, model, baseURL, contextWindow, auth }: Connection) =>
      setDraft({ id, provider, name, model, baseURL, contextWindow, auth }),
    cancelEdit: () => (workspace.connections.length ? setDraft(undefined) : close()),
    select: (id: string) => {
      workspace.selectConnection(id);
      close();
    },
    save: (value: ConnectionInput) =>
      run(async (signal) => {
        const connection = await saveConnection(value, signal);
        await workspace.refreshConnections(signal);

        if (signal.aborted) return;
        workspace.selectConnection(connection.id);
        close();
      }),
    requestRemoval: setRemoving,
    cancelRemoval: () => {
      if (!controller.current) setRemoving(undefined);
    },
    remove: () =>
      run(async (signal) => {
        if (!removing) return;
        await removeConnection(removing.id, signal);
        const preferences = await workspace.refreshConnections(signal);

        if (signal.aborted) return;

        if (workspace.connectionId === removing.id)
          workspace.selectConnection(preferences.connections[0]?.id);
        setRemoving(undefined);
      }),
  };
}
