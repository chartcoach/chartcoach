import { useEffect, useRef, useState, type FormEvent } from "react";
import { loadModels } from "../browser/workspace-client";
import { providerNames, type Provider } from "../shared/model";
import {
  connectionInputSchema,
  type ConnectionInput,
  type ModelChoice,
} from "../shared/preferences";

export const emptyConnection = (provider: Provider): ConnectionInput => ({
  provider,
  name: providerNames[provider],
  model: "",
  contextWindow: 128_000,
});

export function useConnectionForm(
  initial: ConnectionInput,
  onSave: (value: ConnectionInput) => Promise<void>,
) {
  const [draft, setDraft] = useState(initial);
  const [contextWindow, setContextWindow] = useState(String(initial.contextWindow));
  const [reveal, setReveal] = useState(false);
  const [models, setModels] = useState<ModelChoice[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string>();
  const [invalidField, setInvalidField] = useState<string>();
  const request = useRef<AbortController>(undefined);
  useEffect(() => () => request.current?.abort(), []);

  function resetDiscovery() {
    request.current?.abort();
    setLoading(false);
    setModels([]);
    setError(undefined);
    setInvalidField(undefined);
  }

  function changeProvider(provider: Provider) {
    resetDiscovery();
    const next = { ...emptyConnection(provider), id: initial.id };
    setDraft(next);
    setContextWindow(String(next.contextWindow));
    setReveal(false);
  }

  function setField<K extends keyof ConnectionInput>(field: K, value: ConnectionInput[K]) {
    if (field === "baseURL" || field === "apiKey" || field === "auth") resetDiscovery();
    setDraft((current) => {
      const next = { ...current, [field]: value };

      if (field === "baseURL" || (field === "auth" && value === "none")) next.apiKey = "";

      return next;
    });
  }

  async function discover() {
    request.current?.abort();
    const controller = new AbortController();
    request.current = controller;
    setLoading(true);
    setError(undefined);

    try {
      const found = await loadModels(
        { ...draft, model: draft.model || "model", apiKey: draft.apiKey || undefined },
        controller.signal,
      );

      if (!controller.signal.aborted) setModels(found);
    } catch (cause) {
      if (!controller.signal.aborted)
        setError(cause instanceof Error ? cause.message : "Could not load models.");
    } finally {
      if (!controller.signal.aborted) setLoading(false);
    }
  }

  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const result = connectionInputSchema.safeParse({
      ...draft,
      apiKey: draft.apiKey || undefined,
      contextWindow: Number(contextWindow),
    });

    if (!result.success) {
      const field = String(result.error.issues[0]?.path[0] ?? "name");
      setInvalidField(field);
      setError(
        field === "apiKey"
          ? "Enter one API key with no spaces or line breaks."
          : "Complete the connection name, model ID, and valid context window.",
      );
      const input = event.currentTarget.elements.namedItem(field);

      if (input instanceof HTMLElement) input.focus();

      return;
    }

    setError(undefined);
    setInvalidField(undefined);
    void onSave(result.data);
  }

  return {
    draft,
    contextWindow,
    setContextWindow,
    reveal,
    toggleReveal: () => setReveal((value) => !value),
    models,
    loading,
    error,
    invalidField,
    setField,
    changeProvider,
    discover,
    submit,
  };
}
