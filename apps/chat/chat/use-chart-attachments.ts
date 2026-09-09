import { useRef, useState, type RefObject } from "react";
import type { AssistantRuntime, AttachmentAdapter } from "@assistant-ui/react";
import { readAttachment } from "./attachment";

export function useChartAttachments(
  runtimeRef: RefObject<AssistantRuntime | undefined>,
  blocked: boolean,
  onError: (message: string | undefined) => void,
) {
  const [reading, setReading] = useState(false);
  const uploading = useRef(false);
  const messageInput = useRef<HTMLTextAreaElement>(null);
  const adapter: AttachmentAdapter = {
    accept: "image/png,image/jpeg,image/webp",
    async add({ file }) {
      if (blocked || uploading.current)
        throw new Error("Wait for the current task to finish before attaching a chart.");
      uploading.current = true;
      setReading(true);
      onError(undefined);
      try {
        const attachment = await readAttachment(file);
        const composer = runtimeRef.current!.thread.composer;
        // Validate the replacement before releasing the selected draft attachment.
        for (let index = composer.getState().attachments.length - 1; index >= 0; index--) {
          await composer.getAttachmentByIndex(index).remove();
        }
        return {
          id: attachment.filename,
          type: "image",
          name: attachment.name,
          contentType: attachment.mediaType,
          file,
          status: { type: "requires-action", reason: "composer-send" },
          content: [
            {
              type: "file",
              data: attachment.data,
              mimeType: attachment.mediaType,
              filename: attachment.filename,
            },
          ],
        };
      } finally {
        uploading.current = false;
        setReading(false);
        messageInput.current?.focus();
      }
    },
    async send(attachment) {
      if (!attachment.content?.length) throw new Error("Choose the chart image again.");
      return { ...attachment, status: { type: "complete" }, content: attachment.content };
    },
    async remove() {},
  };
  async function upload(files: File[]) {
    if (blocked || uploading.current) {
      onError("Wait for the current task to finish before attaching a chart.");
      return;
    }
    if (files.length !== 1 || !files[0]) {
      onError("Choose one chart image at a time.");
      return;
    }
    try {
      await runtimeRef.current!.thread.composer.addAttachment(files[0]);
    } catch (cause) {
      onError(
        cause instanceof Error ? cause.message : "Could not read the image. Choose it again.",
      );
    }
  }

  return { adapter, reading, messageInput, upload };
}
