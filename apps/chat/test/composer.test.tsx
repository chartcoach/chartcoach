import {
  AssistantRuntimeProvider,
  useExternalStoreRuntime,
  type ThreadMessage,
} from "@assistant-ui/react";
import { useRef } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { expect, it } from "vite-plus/test";
import { Composer } from "../components/chat/composer";

function NativeComposer({ running }: { running: boolean }) {
  const runtime = useExternalStoreRuntime<ThreadMessage>({
    messages: [],
    isRunning: running,
    onNew: async () => {},
    onCancel: async () => {},
  });
  const input = useRef<HTMLTextAreaElement>(null);
  return (
    <AssistantRuntimeProvider runtime={runtime}>
      <Composer
        onUpload={() => {}}
        messageInput={input}
        busy={running}
        disabled={running}
        reading={false}
      />
    </AssistantRuntimeProvider>
  );
}

it("uses the native composer send gate for an empty draft", () => {
  const html = renderToStaticMarkup(<NativeComposer running={false} />);
  expect(html).toContain('aria-label="Message composer"');
  expect(html).toMatch(/<button[^>]*aria-label="Send message"[^>]*disabled=""/);
  expect(html).toContain('aria-describedby="upload-hint message-privacy"');
});

it("exposes cancellation while the runtime is running", () => {
  const html = renderToStaticMarkup(<NativeComposer running />);
  expect(html).toContain('aria-label="Stop response"');
  expect(html).not.toMatch(/<button[^>]*aria-label="Stop response"[^>]*disabled=""/);
  expect(html).toMatch(/<textarea[^>]*disabled=""/);
});
