import type { EveMessage } from "eve/react";
import { convertEveMessage } from "@assistant-ui/eve";
import {
  AssistantRuntimeProvider,
  getExternalStoreMessages,
  MessagePrimitive,
  ThreadPrimitive,
  useExternalStoreRuntime,
} from "@assistant-ui/react";
import type { ChartAttachment } from "../chat/attachment";
import { deriveConversation, type ConversationOptions, type MessageView } from "../chat/evidence";
import { EvidencePanel } from "../components/chat/evidence-panel";
import { Message } from "../components/chat/message";

export function Transcript({
  messages,
  attachments,
  ...options
}: ConversationOptions & {
  messages: readonly EveMessage[];
  attachments: ReadonlyMap<string, ChartAttachment>;
}) {
  const conversation = deriveConversation(messages, options);

  const runtime = useExternalStoreRuntime<MessageView>({
    messages: conversation.messages,
    convertMessage: (view, index) =>
      convertEveMessage(view.message, index, messages, { isRunning: false }),
    onNew: async () => {},
  });

  return (
    <AssistantRuntimeProvider runtime={runtime}>
      <ThreadPrimitive.Viewport>
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
      </ThreadPrimitive.Viewport>
      <EvidencePanel items={conversation.evidence} />
    </AssistantRuntimeProvider>
  );
}
