import type { ReactNode, RefObject } from "react";
import * as stylex from "@stylexjs/stylex";
import { getExternalStoreMessages, MessagePrimitive, ThreadPrimitive } from "@assistant-ui/react";
import type { MessageView, deriveConversation } from "../../chat/evidence";
import type { ChartAttachment } from "../../chat/attachment";
import { useConversationStart } from "./use-conversation-start";
import { Message } from "./message";
import { EvidencePanel } from "./evidence-panel";
import { Conversation } from "./conversation";
import { Starters } from "./starters";
import { ProgressLabel, ProgressMark } from "./progress";
import { ui } from "../ui/ui";
import { styles } from "./chat.styles";

export function ConversationPanel({
  heading,
  conversation,
  attachments,
  empty,
  restoring,
  showStatus,
  busy,
  disabled,
  statusText,
  matchedGuidelines,
  sendExample,
  example,
  composer,
}: {
  heading: RefObject<HTMLHeadingElement | null>;
  conversation: ReturnType<typeof deriveConversation>;
  attachments: ReadonlyMap<string, ChartAttachment>;
  empty: boolean;
  restoring: boolean;
  showStatus: boolean;
  busy: boolean;
  disabled: boolean;
  statusText: string;
  matchedGuidelines?: number;
  sendExample: (path: string, prompt: string) => Promise<void>;
  example?: string;
  composer: ReactNode;
}) {
  const { welcome, welcomeRef, columnRef, messagesRef, panelRef } = useConversationStart(
    empty,
    restoring,
  );

  return (
    <main {...stylex.props(styles.main)} data-empty={welcome}>
      <h1 ref={heading} tabIndex={-1} {...stylex.props(ui.srOnly)}>
        chartcoach conversation
      </h1>
      <ThreadPrimitive.Root
        {...stylex.props(
          styles.workspace,
          welcome && styles.emptyWorkspace,
          !welcome && styles.withEvidence,
        )}
      >
        <div ref={columnRef} {...stylex.props(styles.thread, welcome && styles.emptyThread)}>
          <Conversation empty={welcome || restoring}>
            {welcome ? (
              <section ref={welcomeRef} {...stylex.props(styles.welcome)} inert={!empty}>
                <h2 {...stylex.props(styles.title)}>
                  Design with <span {...stylex.props(styles.accent)}>guidance.</span>
                </h2>
                <p {...stylex.props(styles.intro)}>
                  Review a chart, plan a design, or explore a tradeoff.
                </p>
                <Starters disabled={disabled} pending={example} onExample={sendExample} />
              </section>
            ) : (
              <div ref={messagesRef} {...stylex.props(styles.messages)}>
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
              {showStatus ? (
                <>
                  <ProgressMark running />
                  <ProgressLabel phase="preparing" />
                </>
              ) : (
                statusText
              )}
            </p>
            {matchedGuidelines === 0 ? (
              <p {...stylex.props(ui.activity, styles.status)} role="status">
                No guidelines selected. Open Guidelines to broaden your selection.
              </p>
            ) : null}
          </Conversation>
          {composer}
        </div>
        <EvidencePanel
          ref={panelRef}
          items={conversation.evidence}
          active={!welcome && !restoring}
          busy={busy}
        />
      </ThreadPrimitive.Root>
    </main>
  );
}
