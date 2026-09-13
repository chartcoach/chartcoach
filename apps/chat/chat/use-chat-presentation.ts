import { useEffect, useRef } from "react";
import { useAuiState } from "@assistant-ui/react";
import type { useChat } from "./use-chat";
import type { useNavigation } from "./use-navigation";

export function useChatPresentation(
  state: ReturnType<typeof useChat>,
  navigation: ReturnType<typeof useNavigation>,
) {
  const hasAttachment = useAuiState((value) => value.composer.attachments.length > 0);
  const { messageInput, conversation, busy } = state;
  const heading = useRef<HTMLHeadingElement>(null);
  useEffect(() => {
    if (navigation.view !== "chat") return;

    const desktop = window.matchMedia(
      "(min-width: 720px) and (hover: hover) and (pointer: fine)",
    ).matches;

    // A heading restores navigation focus without opening a mobile software keyboard.
    (desktop ? messageInput.current : heading.current)?.focus({ preventScroll: true });
  }, [navigation.view, messageInput]);
  const latest = conversation.messages.at(-1);

  return {
    hasAttachment,
    heading,
    empty: conversation.messages.length === 0,
    showStatus:
      busy &&
      (!latest ||
        latest.message.role !== "assistant" ||
        latest.complete ||
        latest.failed ||
        latest.stopped),
    sentMessageId: conversation.messages.findLast(({ message }) => message.role === "user")?.message
      .id,
    dropDisabled: state.disabled || navigation.view === "guidelines",
    onUpload: (files: File[]) => {
      if (navigation.view === "chat") void state.upload(files);
    },
  };
}
