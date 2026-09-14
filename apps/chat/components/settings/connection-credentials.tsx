import { Eye, EyeOff } from "lucide-react";
import * as stylex from "@stylexjs/stylex";
import type { useConnectionForm } from "../../chat/use-connection-form";
import { styles } from "./styles";
import { ui } from "../ui/ui";

function CompatibleCredentials({
  form,
  id,
  origins,
}: {
  form: ReturnType<typeof useConnectionForm>;
  id: string;
  origins: string[];
}) {
  const { draft, invalidField, setField } = form;

  return (
    <>
      <label {...stylex.props(styles.field)}>
        <span {...stylex.props(styles.label)}>API base URL</span>
        <input
          {...stylex.props(styles.input, ui.focus)}
          type="url"
          name="baseURL"
          autoComplete="off"
          spellCheck={false}
          aria-invalid={invalidField === "baseURL"}
          aria-describedby={invalidField === "baseURL" ? `${id}-error` : undefined}
          aria-label="API base URL"
          value={draft.baseURL ?? ""}
          onChange={(event) => setField("baseURL", event.target.value)}
          placeholder="https://your-provider.example/v1"
          required
        />
        {origins.length ? (
          <details {...stylex.props(styles.originDetails)}>
            <summary>View {origins.length.toLocaleString()} allowed origins</summary>
            <span {...stylex.props(styles.hint)}>{origins.join(", ")}</span>
          </details>
        ) : (
          <span {...stylex.props(styles.hint)}>
            Configure CHARTCOACH_MODEL_ORIGINS on the server.
          </span>
        )}
      </label>
      <label {...stylex.props(styles.field)}>
        <span {...stylex.props(styles.label)}>Authentication</span>
        <select
          {...stylex.props(styles.input, styles.compactSelect, ui.focus)}
          aria-label="Authentication"
          value={draft.auth ?? "api-key"}
          onChange={(event) => setField("auth", event.target.value === "none" ? "none" : "api-key")}
        >
          <option value="api-key">API key</option>
          <option value="none">No authentication (local endpoint)</option>
        </select>
      </label>
    </>
  );
}

export function ConnectionCredentials({
  form,
  id,
  origins,
}: {
  form: ReturnType<typeof useConnectionForm>;
  id: string;
  origins: string[];
}) {
  const { draft, invalidField, reveal, toggleReveal, setField } = form;

  return (
    <>
      {draft.provider === "compatible" ? (
        <CompatibleCredentials form={form} id={id} origins={origins} />
      ) : null}
      <div {...stylex.props(styles.field)}>
        <label {...stylex.props(styles.label)} htmlFor={`${id}-key`}>
          API key
        </label>
        <span {...stylex.props(styles.inputRow)}>
          <input
            {...stylex.props(styles.input, ui.focus)}
            disabled={draft.auth === "none"}
            type={reveal ? "text" : "password"}
            id={`${id}-key`}
            name="apiKey"
            aria-invalid={invalidField === "apiKey"}
            aria-describedby={invalidField === "apiKey" ? `${id}-error` : undefined}
            value={draft.apiKey ?? ""}
            aria-label="API key"
            autoComplete="off"
            spellCheck={false}
            placeholder={
              draft.id ? "Saved key, leave blank to keep it" : "Enter your provider API key"
            }
            onChange={(event) => setField("apiKey", event.target.value)}
            required={!draft.id && draft.auth !== "none"}
          />
          <button
            type="button"
            {...stylex.props(ui.button, ui.quietButton, ui.focus)}
            aria-label={reveal ? "Hide API key" : "Show API key"}
            onClick={toggleReveal}
          >
            {reveal ? (
              <EyeOff size={17} aria-hidden="true" />
            ) : (
              <Eye size={17} aria-hidden="true" />
            )}
          </button>
        </span>
      </div>
    </>
  );
}
