import { Dialog } from "radix-ui";
import {
  Check,
  ChevronDown,
  Eye,
  EyeOff,
  KeyRound,
  LockKeyhole,
  Pencil,
  Plus,
  Trash2,
  X,
} from "lucide-react";
import { useEffect, useId, useRef, useState } from "react";
import { useAui } from "@assistant-ui/react";
import * as stylex from "@stylexjs/stylex";
import {
  connectionInputSchema,
  providerNames,
  providerSchema,
  type Connection,
  type ConnectionInput,
  type ModelChoice,
  type Provider,
} from "../../shared/preferences";
import { loadModels, removeConnection, saveConnection } from "../../browser/workspace-client";
import type { useWorkspace } from "../../chat/use-workspace";
import { ProviderIcon } from "./provider-icon";
import { styles } from "./styles";
import { ui } from "../ui/ui";

const empty = (provider: Provider): ConnectionInput => ({
  provider,
  name: providerNames[provider],
  model: "",
  contextWindow: 128_000,
});

export function ModelSettings({
  workspace,
  disabled,
}: {
  workspace: ReturnType<typeof useWorkspace>;
  disabled: boolean;
}) {
  const [open, setOpen] = useState(false);
  const aui = useAui();
  const modelName = workspace.connection?.model;
  useEffect(
    () => aui.modelContext.register({ getModelContext: () => ({ config: { modelName } }) }),
    [aui, modelName],
  );
  return (
    <Dialog.Root open={open} onOpenChange={setOpen}>
      <Dialog.Trigger
        {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.trigger)}
        disabled={disabled}
        aria-label="Model settings"
      >
        {workspace.connection ? (
          <ProviderIcon provider={workspace.connection.provider} size={16} />
        ) : (
          <KeyRound size={16} />
        )}
        <span {...stylex.props(styles.triggerText)}>
          {workspace.connection?.model ?? "Bring your own key"}
        </span>
        <ChevronDown {...stylex.props(ui.icon)} size={13} />
      </Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay {...stylex.props(styles.overlay)} />
        <Dialog.Content {...stylex.props(styles.modal)}>
          <div {...stylex.props(styles.header)}>
            <div>
              <Dialog.Title {...stylex.props(styles.title)}>Your model, your key</Dialog.Title>
              <Dialog.Description {...stylex.props(styles.subtitle)}>
                Choose the model that helps you think through your chart.
              </Dialog.Description>
            </div>
            <Dialog.Close
              {...stylex.props(ui.button, ui.quietButton, ui.focus)}
              aria-label="Close model settings"
            >
              <X size={18} />
            </Dialog.Close>
          </div>
          <SettingsContent workspace={workspace} onClose={() => setOpen(false)} />
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}

function SettingsContent({
  workspace,
  onClose,
}: {
  workspace: ReturnType<typeof useWorkspace>;
  onClose: () => void;
}) {
  const [draft, setDraft] = useState<ConnectionInput>();
  const [pending, setPending] = useState(false);
  const [error, setError] = useState<string>();
  const controller = useRef<AbortController>(undefined);
  useEffect(() => () => controller.current?.abort(), []);
  async function save(value: ConnectionInput) {
    setPending(true);
    setError(undefined);
    const abort = new AbortController();
    controller.current = abort;
    try {
      const connection = await saveConnection(value, abort.signal);
      await workspace.refreshConnections();
      if (abort.signal.aborted) return;
      workspace.selectConnection(connection.id);
      onClose();
    } catch (cause) {
      if (!abort.signal.aborted)
        setError(cause instanceof Error ? cause.message : "Could not save this connection.");
    } finally {
      if (!abort.signal.aborted) setPending(false);
    }
  }
  async function remove(connection: Connection) {
    setPending(true);
    setError(undefined);
    try {
      await removeConnection(connection.id);
      await workspace.refreshConnections();
      if (workspace.connectionId === connection.id) {
        const next = workspace.connections.find((item) => item.id !== connection.id);
        workspace.selectConnection(next?.id);
      }
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : "Could not remove this connection.");
    } finally {
      setPending(false);
    }
  }
  return (
    <>
      <div {...stylex.props(styles.body)}>
        {workspace.connections.length > 0 && !draft ? (
          <>
            <p {...stylex.props(styles.sectionTitle)}>Available connections</p>
            {workspace.connections.map((connection) => (
              <div key={connection.id} {...stylex.props(styles.saved)}>
                <button
                  {...stylex.props(styles.savedChoice, ui.focus)}
                  disabled={pending}
                  onClick={() => {
                    workspace.selectConnection(connection.id);
                    onClose();
                  }}
                >
                  <ProviderIcon provider={connection.provider} />
                  <span {...stylex.props(styles.savedText)}>
                    {connection.name}
                    <span {...stylex.props(styles.modelName)}>{connection.model}</span>
                  </span>
                  {workspace.connectionId === connection.id ? (
                    <Check size={16} aria-label="Selected" />
                  ) : null}
                </button>
                {!connection.managed ? (
                  <>
                    <button
                      {...stylex.props(ui.button, ui.quietButton, ui.focus)}
                      aria-label={`Edit ${connection.name}`}
                      disabled={pending}
                      onClick={() =>
                        setDraft({
                          id: connection.id,
                          provider: connection.provider,
                          name: connection.name,
                          model: connection.model,
                          baseURL: connection.baseURL,
                          contextWindow: connection.contextWindow,
                        })
                      }
                    >
                      <Pencil size={15} />
                    </button>
                    <button
                      {...stylex.props(ui.button, ui.quietButton, ui.focus)}
                      aria-label={`Remove ${connection.name}`}
                      disabled={pending}
                      onClick={() => void remove(connection)}
                    >
                      <Trash2 size={15} />
                    </button>
                  </>
                ) : null}
              </div>
            ))}
            <button
              {...stylex.props(ui.button, ui.quietButton, ui.focus)}
              onClick={() => setDraft(empty("openai"))}
            >
              <Plus size={16} /> Add a connection
            </button>
          </>
        ) : (
          <ConnectionForm
            key={draft?.id ?? "new"}
            initial={draft ?? empty("openai")}
            pending={pending}
            origins={workspace.allowedOrigins}
            onSave={save}
            onCancel={() => (workspace.connections.length ? setDraft(undefined) : onClose())}
          />
        )}
        {error ? (
          <p role="alert" {...stylex.props(ui.error)}>
            {error}
          </p>
        ) : null}
      </div>
      <div {...stylex.props(styles.footer)}>
        <LockKeyhole {...stylex.props(ui.icon)} size={16} aria-hidden="true" />
        <p {...stylex.props(styles.hint)}>
          Keys are encrypted on this server and scoped to this browser. They are sent to the
          provider, never to the model as chat content.
        </p>
      </div>
    </>
  );
}

function ConnectionForm({
  initial,
  pending,
  origins,
  onSave,
  onCancel,
}: {
  initial: ConnectionInput;
  pending: boolean;
  origins: string[];
  onSave: (value: ConnectionInput) => Promise<void>;
  onCancel: () => void;
}) {
  const [draft, setDraft] = useState(initial);
  const [contextWindow, setContextWindow] = useState(String(initial.contextWindow));
  const [reveal, setReveal] = useState(false);
  const [models, setModels] = useState<ModelChoice[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string>();
  const id = useId();
  const request = useRef<AbortController>(undefined);
  useEffect(() => () => request.current?.abort(), []);
  function changeProvider(provider: Provider) {
    request.current?.abort();
    setLoading(false);
    setModels([]);
    setError(undefined);
    setDraft({ ...empty(provider), id: initial.id });
    setContextWindow(String(empty(provider).contextWindow));
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
  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        const value = connectionInputSchema.safeParse({
          ...draft,
          apiKey: draft.apiKey || undefined,
          contextWindow: Number(contextWindow),
        });
        if (!value.success)
          setError(
            value.error.issues[0]?.path[0] === "apiKey"
              ? "Enter one API key with no spaces or line breaks."
              : "Complete the connection name, model ID, and valid context window.",
          );
        else void onSave(value.data);
      }}
    >
      <fieldset disabled={pending} {...stylex.props(styles.fieldset)}>
        <legend {...stylex.props(ui.srOnly)}>Provider connection</legend>
        <div {...stylex.props(styles.providers)}>
          {providerSchema.options.map((provider) => (
            <button
              type="button"
              key={provider}
              {...stylex.props(
                ui.button,
                ui.outlineButton,
                styles.provider,
                ui.focus,
                draft.provider === provider && styles.selected,
              )}
              aria-pressed={draft.provider === provider}
              onClick={() => changeProvider(provider)}
            >
              <ProviderIcon provider={provider} size={18} />
              {providerNames[provider]}
            </button>
          ))}
        </div>
        <label {...stylex.props(styles.field)}>
          <span {...stylex.props(styles.label)}>Connection name</span>
          <input
            {...stylex.props(styles.input, ui.focus)}
            value={draft.name}
            onChange={(event) => setDraft({ ...draft, name: event.target.value })}
            required
            maxLength={80}
          />
        </label>
        {draft.provider === "compatible" ? (
          <label {...stylex.props(styles.field)}>
            <span {...stylex.props(styles.label)}>API base URL</span>
            <input
              {...stylex.props(styles.input, ui.focus)}
              type="url"
              aria-label="API base URL"
              value={draft.baseURL ?? ""}
              onChange={(event) => {
                request.current?.abort();
                setLoading(false);
                setModels([]);
                setDraft({ ...draft, baseURL: event.target.value, apiKey: "" });
              }}
              placeholder="https://your-provider.example/v1"
              required
            />
            <span {...stylex.props(styles.hint)}>
              Allowed origins:{" "}
              {origins.length ? origins.join(", ") : "configure CHAT_MODEL_ORIGINS on the server"}
            </span>
          </label>
        ) : null}
        <div {...stylex.props(styles.field)}>
          <label {...stylex.props(styles.label)} htmlFor={`${id}-key`}>
            API key
          </label>
          <span {...stylex.props(styles.inputRow)}>
            <input
              {...stylex.props(styles.input, ui.focus)}
              type={reveal ? "text" : "password"}
              id={`${id}-key`}
              value={draft.apiKey ?? ""}
              aria-label="API key"
              autoComplete="off"
              spellCheck={false}
              placeholder={
                draft.id ? "Saved key, leave blank to keep it" : "Enter your provider API key"
              }
              onChange={(event) => {
                request.current?.abort();
                setLoading(false);
                setModels([]);
                setDraft({ ...draft, apiKey: event.target.value });
              }}
              required={!draft.id}
            />
            <button
              type="button"
              {...stylex.props(ui.button, ui.quietButton, ui.focus)}
              aria-label={reveal ? "Hide API key" : "Show API key"}
              onClick={() => setReveal(!reveal)}
            >
              {reveal ? <EyeOff size={17} /> : <Eye size={17} />}
            </button>
          </span>
        </div>
        <div {...stylex.props(styles.field)}>
          <label {...stylex.props(styles.label)} htmlFor={`${id}-model`}>
            Model
          </label>
          <span {...stylex.props(styles.inputRow)}>
            <input
              {...stylex.props(styles.input, ui.focus)}
              value={draft.model}
              id={`${id}-model`}
              aria-label="Model"
              list={`${id}-models`}
              placeholder="Enter a vision-capable model ID"
              onChange={(event) => setDraft({ ...draft, model: event.target.value })}
              required
            />
            <button
              type="button"
              disabled={loading}
              {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.modelAction)}
              onClick={() => void discover()}
            >
              {loading ? "Loading…" : "Load models"}
            </button>
          </span>
          <datalist id={`${id}-models`}>
            {models.map((model) => (
              <option key={model.id} value={model.id}>
                {model.name}
              </option>
            ))}
          </datalist>
          <span {...stylex.props(styles.hint)}>
            Choose a model that supports images and tool calls. You can enter its ID directly.
          </span>
        </div>
        <details {...stylex.props(styles.advanced)}>
          <summary {...stylex.props(styles.summary)}>Context window</summary>
          <label {...stylex.props(styles.field)}>
            <span>Maximum context tokens</span>
            <input
              {...stylex.props(styles.input, ui.focus)}
              type="number"
              min={4096}
              max={2_000_000}
              value={contextWindow}
              required
              onChange={(event) => setContextWindow(event.target.value)}
            />
            <span {...stylex.props(styles.hint)}>
              Use the limit published for your model. Eve uses it to compact long conversations.
            </span>
          </label>
        </details>
        {error ? (
          <p role="alert" {...stylex.props(ui.error)}>
            {error}
          </p>
        ) : null}
        <div {...stylex.props(styles.actions)}>
          <button type="submit" {...stylex.props(ui.button, ui.primaryButton, ui.focus)}>
            {pending ? "Saving…" : "Save and use"}
          </button>
          <button
            type="button"
            {...stylex.props(ui.button, ui.quietButton, ui.focus)}
            onClick={onCancel}
          >
            Cancel
          </button>
        </div>
      </fieldset>
    </form>
  );
}
