"use client";

import * as stylex from "@stylexjs/stylex";
import { GuidelinesPage } from "./filters";
import { useChatWorkspace, WorkspacePending } from "../chat/chat";
import { WorkspaceView } from "../chat/workspace-view";
import { styles } from "../chat/chat.styles";
import { ui } from "../ui/ui";

export function GuidelineSelection() {
  const { state, navigation } = useChatWorkspace();
  const { catalog, disabled, onFiltersChange, onCatalogReload } = state;

  if (state.workspace.loading) return <WorkspacePending />;

  return (
    <WorkspaceView>
      {catalog.metadata && catalog.selection ? (
        <GuidelinesPage
          key={catalog.metadata.catalogId}
          onClose={navigation.showChat}
          metadata={catalog.metadata}
          value={catalog.selection.filters}
          matchedGuidelines={catalog.selection.matchedGuidelines}
          disabled={disabled}
          onApply={onFiltersChange}
          onReload={onCatalogReload}
        />
      ) : (
        <main {...stylex.props(styles.settingsFallback)}>
          <h1>Guidelines</h1>
          <p role="status">{catalog.error ?? "Loading guidelines…"}</p>
          {catalog.error ? (
            <button
              {...stylex.props(ui.button, ui.outlineButton, ui.focus)}
              disabled={disabled}
              onClick={onCatalogReload}
            >
              Reload catalog
            </button>
          ) : null}
          <button
            {...stylex.props(ui.button, ui.quietButton, ui.focus)}
            onClick={navigation.showChat}
          >
            Back to chat
          </button>
        </main>
      )}
    </WorkspaceView>
  );
}
