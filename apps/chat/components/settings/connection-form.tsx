import { ConnectionCredentials } from "./connection-credentials";
import { useId } from "react";
import * as stylex from "@stylexjs/stylex";
import { providerNames, providerSchema } from "../../shared/model";
import { type ConnectionInput } from "../../shared/preferences";
import { useConnectionForm } from "../../chat/use-connection-form";
import { ProviderIcon } from "./provider-icon";
import { styles } from "./styles";
import { ui } from "../ui/ui";

export function ConnectionForm({
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
  const form = useConnectionForm(initial, onSave);

  const {
    draft,
    contextWindow,
    setContextWindow,
    models,
    loading,
    error,
    invalidField,
    setField,
    changeProvider,
    discover,
    submit,
  } = form;

  const id = useId();

  return (
    <form onSubmit={submit}>
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
              aria-label={providerNames[provider]}
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
            name="name"
            autoComplete="off"
            aria-invalid={invalidField === "name"}
            aria-describedby={invalidField === "name" ? `${id}-error` : undefined}
            value={draft.name}
            onChange={(event) => setField("name", event.target.value)}
            required
            maxLength={80}
          />
        </label>
        <ConnectionCredentials form={form} id={id} origins={origins} />
        <div {...stylex.props(styles.field)}>
          <label {...stylex.props(styles.label)} htmlFor={`${id}-model`}>
            Model
          </label>
          <span {...stylex.props(styles.inputRow)}>
            <input
              {...stylex.props(styles.input, ui.focus)}
              value={draft.model}
              id={`${id}-model`}
              name="model"
              autoComplete="off"
              spellCheck={false}
              aria-invalid={invalidField === "model"}
              aria-describedby={invalidField === "model" ? `${id}-error` : undefined}
              aria-label="Model"
              list={`${id}-models`}
              placeholder="Enter a vision-capable model ID"
              onChange={(event) => setField("model", event.target.value)}
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
              name="contextWindow"
              aria-invalid={invalidField === "contextWindow"}
              aria-describedby={invalidField === "contextWindow" ? `${id}-error` : undefined}
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
          <p id={`${id}-error`} role="alert" {...stylex.props(ui.error)}>
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
