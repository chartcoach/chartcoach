import { AlertDialog, Dialog } from "radix-ui";
import { Check, ChevronDown, KeyRound, LockKeyhole, Pencil, Plus, Trash2, X } from "lucide-react";
import { memo, ViewTransition } from "react";
import dynamic from "next/dynamic";
import * as stylex from "@stylexjs/stylex";
import type { Connection } from "../../shared/preferences";
import type { useWorkspace } from "../../chat/use-workspace";
import { useModelSettings } from "../../chat/use-model-settings";
import { emptyConnection } from "../../chat/use-connection-form";
import { ProviderIcon } from "./provider-icon";
import { styles } from "./styles";
import { ui } from "../ui/ui";

type ModelSettingsState = ReturnType<typeof useModelSettings>;

const ConnectionForm = dynamic(
  () => import("./connection-form").then((module) => module.ConnectionForm),
  {
    loading: () => (
      <p {...stylex.props(styles.hint)} role="status">
        Loading connection settings…
      </p>
    ),
  },
);

export const ModelSettings = memo(function ModelSettings({
  workspace,
  disabled,
}: {
  workspace: ReturnType<typeof useWorkspace>;
  disabled: boolean;
}) {
  const state = useModelSettings(workspace);

  return (
    <Dialog.Root open={state.open} onOpenChange={state.setOpen}>
      <Dialog.Trigger
        {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.trigger)}
        disabled={disabled}
        aria-label="Model settings"
      >
        {workspace.connection ? (
          <ProviderIcon
            provider={workspace.connection.provider}
            baseURL={workspace.connection.baseURL}
            size={16}
          />
        ) : (
          <KeyRound size={16} aria-hidden="true" />
        )}
        <span {...stylex.props(styles.triggerText)}>
          {workspace.connection?.model ?? "Bring your own key"}
        </span>
        <ChevronDown {...stylex.props(ui.icon)} size={13} aria-hidden="true" />
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
              disabled={state.pending}
              aria-label="Close model settings"
            >
              <X size={18} aria-hidden="true" />
            </Dialog.Close>
          </div>
          <div {...stylex.props(styles.body)}>
            {workspace.connections.length > 0 && !state.draft ? (
              <>
                <p {...stylex.props(styles.sectionTitle)}>Available connections</p>
                {workspace.connections.map((connection) => (
                  <div key={connection.id} {...stylex.props(styles.saved)}>
                    <button
                      {...stylex.props(styles.savedChoice, ui.focus)}
                      disabled={state.pending}
                      onClick={() => state.select(connection.id)}
                    >
                      <ProviderIcon provider={connection.provider} baseURL={connection.baseURL} />
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
                          disabled={state.pending}
                          onClick={() => state.edit(connection)}
                        >
                          <Pencil size={15} aria-hidden="true" />
                        </button>
                        <RemoveConnection connection={connection} state={state} />
                      </>
                    ) : null}
                  </div>
                ))}
                <button {...stylex.props(ui.button, ui.quietButton, ui.focus)} onClick={state.add}>
                  <Plus size={16} aria-hidden="true" /> Add a connection
                </button>
              </>
            ) : (
              <ViewTransition default="none" update="content-crossfade">
                <ConnectionForm
                  key={state.draft?.id ?? "new"}
                  initial={state.draft ?? emptyConnection("openai")}
                  pending={state.pending}
                  origins={workspace.allowedOrigins}
                  onSave={state.save}
                  onCancel={state.cancelEdit}
                />
              </ViewTransition>
            )}
            {state.error && !state.removing ? (
              <p role="alert" {...stylex.props(ui.error)}>
                {state.error}
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
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
});

function RemoveConnection({
  connection,
  state,
}: {
  connection: Connection;
  state: ModelSettingsState;
}) {
  return (
    <AlertDialog.Root
      open={state.removing?.id === connection.id}
      onOpenChange={(open) => (open ? state.requestRemoval(connection) : state.cancelRemoval())}
    >
      <AlertDialog.Trigger asChild>
        <button
          {...stylex.props(ui.button, ui.quietButton, ui.focus)}
          aria-label={`Remove ${connection.name}`}
          disabled={state.pending}
        >
          <Trash2 size={15} aria-hidden="true" />
        </button>
      </AlertDialog.Trigger>
      <AlertDialog.Portal>
        <AlertDialog.Overlay {...stylex.props(styles.overlay)} />
        <AlertDialog.Content {...stylex.props(styles.modal)}>
          <div {...stylex.props(styles.header)}>
            <div>
              <AlertDialog.Title {...stylex.props(styles.title)}>
                Remove {connection.name}?
              </AlertDialog.Title>
              <AlertDialog.Description {...stylex.props(styles.subtitle)}>
                This removes its saved API key. Existing conversations stay in your history. Choose
                another connection to continue them.
              </AlertDialog.Description>
            </div>
          </div>
          <div {...stylex.props(styles.body)}>
            {state.error ? (
              <p role="alert" {...stylex.props(ui.error)}>
                {state.error}
              </p>
            ) : null}
            <div {...stylex.props(styles.actions)}>
              <AlertDialog.Cancel
                {...stylex.props(ui.button, ui.outlineButton, ui.focus)}
                disabled={state.pending}
              >
                Keep connection
              </AlertDialog.Cancel>
              <AlertDialog.Action
                {...stylex.props(ui.button, ui.primaryButton, ui.focus)}
                disabled={state.pending}
                onClick={(event) => {
                  event.preventDefault();
                  void state.remove();
                }}
              >
                {state.pending ? "Removing…" : "Remove connection"}
              </AlertDialog.Action>
            </div>
          </div>
        </AlertDialog.Content>
      </AlertDialog.Portal>
    </AlertDialog.Root>
  );
}
