"use client";

import * as stylex from "@stylexjs/stylex";
import {
  AssistantRuntimeProvider,
  getExternalStoreMessages,
  MessagePrimitive,
  ThreadPrimitive,
  useAuiState,
} from "@assistant-ui/react";
import { Plus } from "lucide-react";
import Image from "next/image";
import logo from "@chartcoach/brand/assets/brand/chartcoach-horizontal.svg";
import logoWhite from "@chartcoach/brand/assets/brand/chartcoach-horizontal-white.svg";
import { Message } from "./message";
import type { MessageView } from "../../chat/evidence";
import { EvidencePanel } from "./evidence-panel";
import { Composer } from "./composer";
import { Dropzone } from "./dropzone";
import { Conversation } from "./conversation";
import { useChat } from "../../chat/use-chat";
import { colors, media, emptyThreadScope } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";
import { LoadingMark } from "../ui/loading-mark";
import { CatalogFiltersPanel } from "../catalog/filters";
import { Starters } from "./starters";
import { useWorkspace } from "../../chat/use-workspace";
import { ModelSettings } from "../settings/model-settings";
import { HistoryPanel } from "./history";

const styles = stylex.create({
  skip: {
    position: "fixed",
    top: 8,
    left: 8,
    zIndex: 10,
    padding: 12,
    backgroundColor: colors.surface,
    color: colors.foreground,
    transform: { default: "translateY(-160%)", ":focus": "translateY(0)" },
  },
  header: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    paddingBlock: {
      default: 20,
      [media.short]: 8,
      [media.mobile]: { default: 12, [media.short]: 8 },
    },
    paddingInline: { default: "max(24px, env(safe-area-inset-left))", [media.mobile]: 16 },
    flexShrink: 0,
  },
  headerControls: { display: "flex", alignItems: "center", gap: 8 },
  newChatLabel: { display: { default: "inline", [media.mobile]: "none" } },
  wordmark: {
    flexShrink: 0,
    display: "inline-flex",
    alignItems: "center",
    textDecoration: "none",
    color: "inherit",
  },
  logoLight: {
    display: { default: "block", [media.dark]: "none" },
    width: { default: 140, [media.mobile]: 124 },
    height: "auto",
  },
  logoDark: {
    display: { default: "none", [media.dark]: "block" },
    width: { default: 140, [media.mobile]: 124 },
    height: "auto",
  },
  main: { flexGrow: 1, minHeight: 0, display: "flex", flexDirection: "column", minWidth: 0 },
  empty: {
    justifyContent: "safe center",
    overflowY: "hidden",
    paddingBottom: 0,
  },
  workspace: {
    display: "grid",
    gridTemplateRows: { default: "auto minmax(0, 1fr)", [media.desktop]: "minmax(0, 1fr)" },
    flexGrow: 1,
    minHeight: 0,
    minWidth: 0,
  },
  withEvidence: {
    gridTemplateColumns: {
      default: null,
      [media.desktop]: "minmax(0, 1fr) clamp(320px, 30vw, 460px)",
    },
  },
  thread: {
    display: "flex",
    flexDirection: "column",
    minHeight: 0,
    minWidth: 0,
    gridRow: { default: "2", [media.desktop]: "1" },
    gridColumn: { default: null, [media.desktop]: "1" },
  },
  emptyThread: { justifyContent: "flex-start" },
  emptyWorkspace: {
    flexGrow: 0,
    flexShrink: 1,
    gridTemplateRows: "minmax(0, 1fr)",
    minHeight: 0,
    maxHeight: "100%",
  },
  welcome: { maxWidth: 672, marginInline: "auto" },
  title: {
    maxWidth: 600,
    fontSize: "clamp(32px, 4vw, 48px)",
    fontWeight: 500,
    lineHeight: 1.12,
    letterSpacing: "-0.045em",
    textWrap: "balance",
    marginBottom: 16,
  },
  accent: { color: colors.accent },
  intro: { maxWidth: 540, color: colors.muted, lineHeight: 1.65, fontSize: 16, margin: 0 },
  messages: { maxWidth: 672, marginInline: "auto" },
  status: { maxWidth: 672, marginBlock: 12, marginInline: "auto" },
});

function ChatLayout({
  conversation,
  attachments,
  busy,
  disabled,
  reading,
  error,
  recover,
  upload,
  newChat,
  statusText,
  messageInput,
  catalog,
  onFiltersChange,
  onCatalogReload,
  mode,
  setMode,
  uploadExample,
  workspace,
}: ReturnType<typeof useChat>) {
  const hasAttachment = useAuiState((state) => state.composer.attachments.length > 0);
  const empty = conversation.messages.length === 0;
  const showStatus =
    busy &&
    !conversation.messages.at(-1)?.message.parts.some((part) => part.type === "dynamic-tool");
  const sentMessageId = conversation.messages.findLast(({ message }) => message.role === "user")
    ?.message.id;
  return (
    <Dropzone
      disabled={disabled}
      hasAttachment={hasAttachment}
      onFiles={(files) => void upload(files)}
    >
      <a {...stylex.props(styles.skip, ui.focus)} href="#message">
        Skip to message
      </a>
      <header {...stylex.props(styles.header)}>
        <a
          {...stylex.props(styles.wordmark, ui.focus)}
          href="https://chartcoach.dev"
          target="_blank"
          rel="noreferrer"
        >
          <Image
            src={logo}
            alt="chartcoach"
            width={140}
            height={35}
            {...stylex.props(styles.logoLight)}
            unoptimized
          />
          <Image
            src={logoWhite}
            alt="chartcoach"
            width={140}
            height={35}
            {...stylex.props(styles.logoDark)}
            unoptimized
          />
        </a>
        <div {...stylex.props(styles.headerControls)}>
          <HistoryPanel disabled={disabled} />
          {catalog.metadata && catalog.selection ? (
            <CatalogFiltersPanel
              key={catalog.metadata.catalogId}
              metadata={catalog.metadata}
              value={catalog.selection.filters}
              matchedGuidelines={catalog.selection.matchedGuidelines}
              disabled={disabled}
              onApply={onFiltersChange}
              onReload={onCatalogReload}
            />
          ) : (
            <button
              {...stylex.props(ui.button, ui.quietButton, ui.focus)}
              type="button"
              disabled={!catalog.error || disabled}
              onClick={onCatalogReload}
            >
              {catalog.error ? "Retry loading" : "Loading knowledge…"}
            </button>
          )}
          <button
            {...stylex.props(ui.button, ui.quietButton, ui.focus)}
            type="button"
            onClick={newChat}
            disabled={disabled}
            aria-label="New chat"
          >
            <Plus {...stylex.props(ui.icon)} size={16} />
            <span {...stylex.props(styles.newChatLabel)}>New chat</span>
          </button>
        </div>
      </header>
      <main
        {...stylex.props(styles.main, empty && styles.empty, emptyThreadScope)}
        data-empty={empty}
      >
        <h1 {...stylex.props(ui.srOnly)}>ChartCoach conversation</h1>
        <ThreadPrimitive.Root
          {...stylex.props(
            styles.workspace,
            empty && styles.emptyWorkspace,
            !empty && styles.withEvidence,
          )}
        >
          <div {...stylex.props(styles.thread, empty && styles.emptyThread)}>
            <Conversation>
              {empty ? (
                <section {...stylex.props(styles.welcome)}>
                  <h2 {...stylex.props(styles.title)}>
                    Design with <span {...stylex.props(styles.accent)}>guidance.</span>
                  </h2>
                  <p {...stylex.props(styles.intro)}>
                    Review a chart, plan a design, or explore a tradeoff. Start with your question
                    or try an example, with guideline sources behind the advice.
                  </p>
                  <Starters disabled={disabled} onImage={uploadExample} onWorkflow={setMode} />
                </section>
              ) : (
                <div {...stylex.props(styles.messages)}>
                  <ThreadPrimitive.Messages>
                    {({ message }) => {
                      const view = getExternalStoreMessages<MessageView>(message)[0];
                      return view ? (
                        <MessagePrimitive.Root>
                          <Message view={view} attachments={attachments} />
                        </MessagePrimitive.Root>
                      ) : null;
                    }}
                  </ThreadPrimitive.Messages>
                </div>
              )}
              <p
                {...stylex.props(showStatus ? [ui.activity, styles.status] : ui.srOnly)}
                role="status"
              >
                {showStatus ? <LoadingMark /> : null}
                {statusText}
              </p>
              {catalog.selection?.matchedGuidelines === 0 ? (
                <p {...stylex.props(ui.activity, styles.status)} role="status">
                  No guidelines selected. Open Knowledge to broaden your selection.
                </p>
              ) : null}
            </Conversation>
            <Composer
              mode={mode}
              onModeChange={setMode}
              onUpload={(files) => void upload(files)}
              messageInput={messageInput}
              busy={busy}
              disabled={disabled}
              reading={reading}
              error={error ?? catalog.error}
              onRecover={recover}
              modelControl={
                <ModelSettings workspace={workspace} disabled={disabled || !workspace.ready} />
              }
            />
          </div>
          <EvidencePanel
            key={sentMessageId ?? "empty"}
            items={conversation.evidence}
            active={!empty}
            busy={busy}
          />
        </ThreadPrimitive.Root>
      </main>
    </Dropzone>
  );
}

export function Chat() {
  const workspace = useWorkspace();
  return <ChatSession key={workspace.key} workspace={workspace} />;
}

function ChatSession({ workspace }: { workspace: ReturnType<typeof useWorkspace> }) {
  const state = useChat(workspace);
  return (
    <AssistantRuntimeProvider runtime={state.runtime}>
      <ChatLayout {...state} />
    </AssistantRuntimeProvider>
  );
}
