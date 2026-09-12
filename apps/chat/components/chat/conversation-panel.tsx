import type { ReactNode, RefObject } from "react";
import * as stylex from "@stylexjs/stylex";
import { getExternalStoreMessages, MessagePrimitive, ThreadPrimitive } from "@assistant-ui/react";
import type { MessageView, deriveConversation } from "../../chat/evidence";
import type { ChartAttachment } from "../../chat/attachment";
import { Message } from "./message";
import { EvidencePanel } from "./evidence-panel";
import { Conversation } from "./conversation";
import { Starters } from "./starters";
import { ProgressLabel, ProgressMark } from "./progress";
import { emptyThreadScope } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";
import { styles } from "./chat.styles";

export function ConversationPanel({
  heading,
  conversation,
  attachments,
  empty,
  showStatus,
  busy,
  disabled,
  statusText,
  sentMessageId,
  matchedGuidelines,
  uploadExample,
  composer,
}: {
  heading: RefObject<HTMLHeadingElement | null>;
  conversation: ReturnType<typeof deriveConversation>;
  attachments: ReadonlyMap<string, ChartAttachment>;
  empty: boolean;
  showStatus: boolean;
  busy: boolean;
  disabled: boolean;
  statusText: string;
  sentMessageId?: string;
  matchedGuidelines?: number;
  uploadExample: (path: string) => Promise<boolean>;
  composer: ReactNode;
}) {
  return (
    <main
      {...stylex.props(styles.main, empty && styles.empty, emptyThreadScope)}
      data-empty={empty}
    >
      <h1 ref={heading} tabIndex={-1} {...stylex.props(ui.srOnly)}>
        ChartCoach conversation
      </h1>
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
                  Review a chart, plan a design, or explore a tradeoff.
                </p>
                {composer}
                <Starters disabled={disabled} onImage={uploadExample} />
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
          {!empty ? composer : null}
        </div>
        <EvidencePanel
          key={sentMessageId ?? "empty"}
          items={conversation.evidence}
          active={!empty}
          busy={busy}
        />
      </ThreadPrimitive.Root>
    </main>
  );
}
