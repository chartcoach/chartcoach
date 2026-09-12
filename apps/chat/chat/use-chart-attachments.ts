import { useEffect, useRef, useState, type RefObject } from "react";
import type { AssistantRuntime, AttachmentAdapter } from "@assistant-ui/react";
import { readAttachment } from "./attachment";

export function useChartAttachments(
  runtimeRef: RefObject<AssistantRuntime | undefined>,
  blocked: boolean,
  onError: (message: string | undefined) => void,
) {
  const [reading, setReading] = useState(false);
  const uploading = useRef(false);
  const exampleRequest = useRef<AbortController>(undefined);
  useEffect(() => () => exampleRequest.current?.abort(), []);
  const messageInput = useRef<HTMLTextAreaElement>(null);

  const adapter: AttachmentAdapter = {
    accept: "image/png,image/jpeg,image/webp",
    async add({ file }) {
      if (blocked || uploading.current || exampleRequest.current)
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
    if (blocked || uploading.current || exampleRequest.current) {
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

  async function uploadExample(path: string) {
    if (blocked || uploading.current || exampleRequest.current) return false;
    const controller = new AbortController();
    exampleRequest.current = controller;
    setReading(true);
    onError(undefined);

    try {
      const response = await fetch(path, {
        signal: AbortSignal.any([controller.signal, AbortSignal.timeout(15_000)]),
      });

      if (!response.ok) throw new Error("Could not load the example chart. Try again.");
      const blob = await response.blob();
      controller.signal.throwIfAborted();
      exampleRequest.current = undefined;
      await runtimeRef.current!.thread.composer.addAttachment(
        new File([blob], path.split("/").at(-1)!, { type: "image/png" }),
      );

      return true;
    } catch {
      if (!controller.signal.aborted)
        onError("Could not load the example chart. Try again or upload your own.");

      return false;
    } finally {
      exampleRequest.current = undefined;
      setReading(false);
    }
  }

  return { adapter, reading, messageInput, upload, uploadExample };
}
