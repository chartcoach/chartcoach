import { useEffect, useRef, useState, type RefObject } from "react";
import type { AssistantRuntime, AttachmentAdapter } from "@assistant-ui/react";
import { readAttachment } from "./attachment";
import { chartMediaTypes } from "../shared/attachment";

export function useChartAttachments(
  runtimeRef: RefObject<AssistantRuntime | undefined>,
  blocked: boolean,
  onError: (message: string | undefined) => void,
) {
  const [reading, setReading] = useState(false);
  const [example, setExample] = useState<string>();
  const uploading = useRef(false);
  const exampleRequest = useRef<AbortController>(undefined);
  useEffect(() => () => exampleRequest.current?.abort(), []);
  const messageInput = useRef<HTMLTextAreaElement>(null);
  const [completedReads, setCompletedReads] = useState(0);
  useEffect(() => {
    if (!reading && completedReads > 0) messageInput.current?.focus();
  }, [reading, completedReads]);

  const adapter: AttachmentAdapter = {
    accept: chartMediaTypes.join(","),
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
        setCompletedReads((value) => value + 1);
        setReading(false);
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

    if (!chartMediaTypes.some((type) => type === files[0]!.type)) {
      onError("Choose a PNG, JPEG, or WebP chart image.");
      messageInput.current?.focus();

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

  async function sendExample(path: string, prompt: string) {
    if (blocked || uploading.current || exampleRequest.current) return;
    const controller = new AbortController();
    exampleRequest.current = controller;
    setExample(path);
    onError(undefined);

    try {
      const response = await fetch(path, {
        signal: AbortSignal.any([controller.signal, AbortSignal.timeout(15_000)]),
      });

      if (!response.ok) throw new Error("Could not load the example chart. Try again.");
      const blob = await response.blob();

      const chart = await readAttachment(
        new File([blob], path.split("/").at(-1)!, { type: "image/png" }),
      );

      controller.signal.throwIfAborted();
      exampleRequest.current = undefined;
      // Send without staging the example in the composer, so the welcome hands
      // straight over to the conversation.
      runtimeRef.current!.thread.append({
        content: [{ type: "text", text: prompt }],
        attachments: [
          {
            id: chart.filename,
            type: "image",
            name: chart.name,
            contentType: chart.mediaType,
            status: { type: "complete" },
            content: [
              {
                type: "file",
                data: chart.data,
                mimeType: chart.mediaType,
                filename: chart.filename,
              },
            ],
          },
        ],
      });
    } catch {
      if (!controller.signal.aborted)
        onError("Could not load the example chart. Try again or upload your own.");
    } finally {
      exampleRequest.current = undefined;
      setExample(undefined);
    }
  }

  return { adapter, reading, example, messageInput, upload, sendExample };
}
