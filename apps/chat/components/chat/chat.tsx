"use client";

import * as stylex from "@stylexjs/stylex";
import { createContext, use, type ReactNode } from "react";
import { AssistantRuntimeProvider, useAuiState } from "@assistant-ui/react";
import { Composer } from "./composer";
import { Dropzone } from "./dropzone";
import { ConversationPanel } from "./conversation-panel";
import { WorkspaceView } from "./workspace-view";
import { useChat } from "../../chat/use-chat";
import { useChatPresentation } from "../../chat/use-chat-presentation";
import { useModelContext } from "../../chat/use-model-context";
import { useWorkspace } from "../../chat/use-workspace";
import { useNavigation } from "../../chat/use-navigation";
import { threadIdSchema } from "../../shared/threads";
import { ModelSettings } from "../settings/model-settings";
import { HistoryPanel } from "./history";
import { NavigationHeader } from "./navigation-header";
import { ui } from "../ui/ui";
import { styles } from "./chat.styles";

const ChatContext = createContext<{
  state: ReturnType<typeof useChat>;
  navigation: ReturnType<typeof useNavigation>;
} | null>(null);

export function useChatWorkspace() {
  const context = use(ChatContext);

  if (!context) throw new Error("Chat pages require the workspace layout.");

  return context;
}

function ChatConversation() {
  const { state, navigation } = useChatWorkspace();

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
    sendExample,
    example,
    workspace,
  } = state;

  const { heading, empty, restoring, showStatus, onUpload } = useChatPresentation(
    state,
    navigation,
  );

  if (workspace.loading && (workspace.requestedId || workspace.error)) return <WorkspacePending />;

  return (
    <WorkspaceView>
      <ConversationPanel
        heading={heading}
        conversation={conversation}
        attachments={attachments}
        empty={empty}
        restoring={restoring}
        showStatus={showStatus}
        busy={busy}
        disabled={disabled}
        statusText={statusText}
        matchedGuidelines={catalog.selection?.matchedGuidelines}
        sendExample={sendExample}
        example={example}
        composer={
          <Composer
            onUpload={onUpload}
            messageInput={messageInput}
            busy={busy}
            disabled={disabled}
            reading={reading}
            error={error ?? catalog.error}
            onRecover={recover}
            modelControl={
              <ModelSettings workspace={workspace} disabled={disabled || !workspace.ready} />
            }
            keepExpanded={workspace.ready && !workspace.connection}
            tracing={workspace.tracing}
          />
        }
      />
    </WorkspaceView>
  );
}

export function WorkspacePending() {
  const { state, navigation } = useChatWorkspace();
  const { workspace } = state;

  return (
    <WorkspaceView>
      <main
        id={navigation.view === "guidelines" ? "guidelines" : "message"}
        tabIndex={-1}
        {...stylex.props(styles.settingsFallback)}
      >
        <h1>{workspace.requestedId ? "Conversation" : "chartcoach"}</h1>
        <p role={workspace.threadError || workspace.error ? "alert" : "status"}>
          {workspace.threadError ?? workspace.error ?? "Loading your workspace…"}
        </p>
        {workspace.threadError || workspace.error ? (
          <button
            {...stylex.props(ui.button, ui.outlineButton, ui.focus)}
            onClick={workspace.retry}
          >
            Try again
          </button>
        ) : null}
      </main>
    </WorkspaceView>
  );
}

function ChatLayout({ children }: { children: ReactNode }) {
  const { state, navigation } = useChatWorkspace();
  const { workspace, catalog, disabled } = state;

  const validChatRoute =
    !workspace.requestedId || threadIdSchema.safeParse(workspace.requestedId).success;

  const hasAttachment = useAuiState((value) => value.composer.attachments.length > 0);
  useModelContext(workspace.connection?.model);

  return (
    <Dropzone
      disabled={disabled || navigation.view === "guidelines"}
      hasAttachment={hasAttachment}
      onFiles={(files) => void state.upload(files)}
    >
      <a
        {...stylex.props(styles.skip, ui.focus)}
        href={navigation.view === "guidelines" ? "#guidelines" : "#message"}
      >
        {navigation.view === "guidelines" ? "Skip to guidelines" : "Skip to message"}
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
          disabled={state.busy || state.reading || !workspace.ready}
          guidelineCount={catalog.selection?.matchedGuidelines}
        />
        <div {...stylex.props(styles.canvas)}>
          {navigation.view === "chat" && validChatRoute ? <ChatConversation /> : children}
        </div>
      </div>
    </Dropzone>
  );
}

export function ChatWorkspace({ children }: { children: ReactNode }) {
  const workspace = useWorkspace();
  const navigation = useNavigation(workspace);

  return (
    <ChatSession key={workspace.key} workspace={workspace} navigation={navigation}>
      {children}
    </ChatSession>
  );
}

function ChatSession({
  workspace,
  navigation,
  children,
}: {
  workspace: ReturnType<typeof useWorkspace>;
  navigation: ReturnType<typeof useNavigation>;
  children: ReactNode;
}) {
  const state = useChat(workspace);

  return (
    <ChatContext value={{ state, navigation }}>
      <AssistantRuntimeProvider runtime={state.runtime}>
        <ChatLayout>{children}</ChatLayout>
      </AssistantRuntimeProvider>
    </ChatContext>
  );
}
