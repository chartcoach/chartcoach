"use client";

import * as stylex from "@stylexjs/stylex";
import { Activity } from "react";
import { AssistantRuntimeProvider } from "@assistant-ui/react";
import { Composer } from "./composer";
import { Dropzone } from "./dropzone";
import { ConversationPanel } from "./conversation-panel";
import { WorkspaceView } from "./workspace-view";
import { useChat } from "../../chat/use-chat";
import { useChatPresentation } from "../../chat/use-chat-presentation";
import { useModelContext } from "../../chat/use-model-context";
import { useWorkspace } from "../../chat/use-workspace";
import { useNavigation } from "../../chat/use-navigation";
import { ModelSettings } from "../settings/model-settings";
import { GuidelinesPage } from "../catalog/filters";
import { HistoryPanel } from "./history";
import { NavigationHeader } from "./navigation-header";
import { ui } from "../ui/ui";
import { styles } from "./chat.styles";

function ChatLayout({
  state,
  navigation,
}: {
  state: ReturnType<typeof useChat>;
  navigation: ReturnType<typeof useNavigation>;
}) {
  const {
    conversation,
    attachments,
    busy,
    disabled,
    reading,
    error,
    recover,
    statusText,
    messageInput,
    catalog,
    onFiltersChange,
    onCatalogReload,
    uploadExample,
    workspace,
  } = state;

  useModelContext(workspace.connection?.model);

  const { hasAttachment, heading, empty, showStatus, sentMessageId, dropDisabled, onUpload } =
    useChatPresentation(state, navigation);

  const composer = (
    <Composer
      embedded={empty}
      onUpload={onUpload}
      messageInput={messageInput}
      busy={busy}
      disabled={disabled}
      reading={reading}
      error={error ?? catalog.error}
      onRecover={recover}
      modelControl={<ModelSettings workspace={workspace} disabled={disabled || !workspace.ready} />}
    />
  );

  return (
    <Dropzone disabled={dropDisabled} hasAttachment={hasAttachment} onFiles={onUpload}>
      <a {...stylex.props(styles.skip, ui.focus)} href="#message">
        Skip to message
      </a>
      <header
        {...stylex.props(
          styles.header,
          navigation.desktopOpen ? styles.headerWithSidebar : styles.headerWithRail,
        )}
      >
        <NavigationHeader navigation={navigation} disabled={disabled} />
      </header>
      <div {...stylex.props(styles.body)}>
        <HistoryPanel
          navigation={navigation}
          disabled={disabled}
          guidelineCount={catalog.selection?.matchedGuidelines}
        />
        <WorkspaceView>
          <div {...stylex.props(styles.canvas)}>
            {catalog.metadata && catalog.selection ? (
              <GuidelinesPage
                key={catalog.metadata.catalogId}
                open={navigation.view === "guidelines"}
                onClose={navigation.showChat}
                metadata={catalog.metadata}
                value={catalog.selection.filters}
                matchedGuidelines={catalog.selection.matchedGuidelines}
                disabled={disabled}
                onApply={onFiltersChange}
                onReload={onCatalogReload}
              />
            ) : navigation.view === "guidelines" ? (
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
            ) : null}
            <Activity mode={navigation.view === "chat" ? "visible" : "hidden"}>
              <ConversationPanel
                heading={heading}
                conversation={conversation}
                attachments={attachments}
                empty={empty}
                showStatus={showStatus}
                busy={busy}
                disabled={disabled}
                statusText={statusText}
                sentMessageId={sentMessageId}
                matchedGuidelines={catalog.selection?.matchedGuidelines}
                uploadExample={uploadExample}
                composer={composer}
              />
            </Activity>
          </div>
        </WorkspaceView>
      </div>
    </Dropzone>
  );
}

export function Chat() {
  const workspace = useWorkspace();
  const navigation = useNavigation();

  return <ChatSession key={workspace.key} workspace={workspace} navigation={navigation} />;
}

function ChatSession({
  workspace,
  navigation,
}: {
  workspace: ReturnType<typeof useWorkspace>;
  navigation: ReturnType<typeof useNavigation>;
}) {
  const state = useChat(workspace);

  return (
    <AssistantRuntimeProvider runtime={state.runtime}>
      <ChatLayout state={state} navigation={navigation} />
    </AssistantRuntimeProvider>
  );
}
