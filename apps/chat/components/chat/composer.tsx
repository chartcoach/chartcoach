import { AttachmentPrimitive, ComposerPrimitive } from "@assistant-ui/react";
import { ArrowUp, ImagePlus, Square, X } from "lucide-react";
import type { RefObject } from "react";
import * as stylex from "@stylexjs/stylex";
import { colors, media } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

const styles = stylex.create({
  area: {
    width: "min(100%, 720px)",
    flexShrink: 0,
    marginInline: "auto",
    paddingTop: 12,
    paddingInline: { default: 24, [media.mobile]: 18 },
    paddingBottom: "max(18px, env(safe-area-inset-bottom))",
  },
  root: {
    backgroundColor: colors.surface,
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: { default: colors.border, ":focus-within": colors.accent },
    borderRadius: 8,
    padding: 14,
  },
  input: {
    display: "block",
    width: "100%",
    borderWidth: 0,
    resize: "none",
    backgroundColor: "transparent",
    color: "inherit",
    outlineStyle: "none",
    lineHeight: 1.6,
    minHeight: { default: 78, [media.short]: 52 },
    maxHeight: 180,
    paddingBlock: 0,
    paddingInline: 2,
    fontSize: 16,
    WebkitTapHighlightColor: "transparent",
    "::placeholder": { color: colors.muted },
  },
  controls: { display: "flex", gap: 8, alignItems: "center", marginTop: 10 },
  hint: {
    color: colors.muted,
    fontSize: 12,
    position: { default: null, [media.mobile]: "absolute" },
    width: { default: null, [media.mobile]: 1 },
    height: { default: null, [media.mobile]: 1 },
    overflow: { default: null, [media.mobile]: "hidden" },
    clipPath: { default: null, [media.mobile]: "inset(50%)" },
    whiteSpace: { default: null, [media.mobile]: "nowrap" },
  },
  send: {
    marginLeft: "auto",
    flexShrink: 0,
    borderWidth: 0,
    borderRadius: 6,
    width: 44,
    height: 44,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    color: "#fff",
    backgroundColor: "var(--brand-crimson)",
    opacity: {
      default: 1,
      ":disabled": 0.45,
      ":hover:enabled": { default: null, [media.hover]: 0.8 },
    },
  },
  attachment: {
    display: "flex",
    alignItems: "center",
    gap: 10,
    marginBottom: 14,
    fontSize: 14,
    color: colors.muted,
  },
  thumbnail: {
    width: 48,
    height: 48,
    flexShrink: 0,
    objectFit: "contain",
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: colors.border,
    borderRadius: 4,
  },
  attachmentName: {
    overflow: "hidden",
    textOverflow: "ellipsis",
    whiteSpace: "nowrap",
    minWidth: 0,
  },
  remove: { marginLeft: "auto", flexShrink: 0 },
  note: {
    textAlign: "center",
    color: colors.muted,
    fontSize: 12,
    lineHeight: 1.5,
    marginTop: { default: 12, [media.mobile]: 9 },
  },
});

export function Composer({
  onUpload,
  messageInput,
  busy,
  disabled,
  reading,
  error,
}: {
  onUpload: (files: File[]) => void;
  messageInput: RefObject<HTMLTextAreaElement | null>;
  busy: boolean;
  disabled: boolean;
  reading: boolean;
  error?: string;
}) {
  return (
    <div {...stylex.props(styles.area)}>
      <ComposerPrimitive.Root {...stylex.props(styles.root)} aria-label="Message composer">
        <ComposerPrimitive.Attachments>
          {({ attachment }) => {
            const content = attachment.content?.find(
              (part) =>
                part.type === "image" ||
                (part.type === "file" && part.mimeType.startsWith("image/")),
            );
            const src =
              content?.type === "image"
                ? content.image
                : content?.type === "file"
                  ? content.data
                  : undefined;
            return (
              <AttachmentPrimitive.Root {...stylex.props(styles.attachment)}>
                {src ? (
                  <img
                    {...stylex.props(styles.thumbnail)}
                    src={src}
                    alt={`Selected chart: ${attachment.name}`}
                  />
                ) : null}
                <span {...stylex.props(styles.attachmentName)}>
                  <AttachmentPrimitive.Name />
                </span>
                <AttachmentPrimitive.Remove
                  {...stylex.props(ui.quietButton, ui.button, ui.focus, styles.remove)}
                  aria-label="Remove image"
                  disabled={disabled}
                  onClick={() => messageInput.current?.focus()}
                >
                  <X {...stylex.props(ui.icon)} size={16} />
                </AttachmentPrimitive.Remove>
              </AttachmentPrimitive.Root>
            );
          }}
        </ComposerPrimitive.Attachments>
        <label {...stylex.props(ui.srOnly)} htmlFor="message">
          Message
        </label>
        <ComposerPrimitive.Input
          {...stylex.props(styles.input)}
          id="message"
          ref={messageInput}
          placeholder="What would you like to improve?"
          minRows={1}
          maxRows={6}
          disabled={disabled}
          submitMode="enter"
          cancelOnEscape={false}
          addAttachmentOnPaste={false}
          aria-describedby="upload-hint message-privacy"
          onPaste={(event) => {
            const files = Array.from(event.clipboardData.files);
            if (files.length) {
              event.preventDefault();
              onUpload(files);
            }
          }}
        />
        <div {...stylex.props(styles.controls)}>
          <ComposerPrimitive.AddAttachment
            {...stylex.props(ui.quietButton, ui.button, ui.focus)}
            multiple={false}
            disabled={disabled}
          >
            <ImagePlus {...stylex.props(ui.icon)} size={18} />
            {reading ? "Reading image" : "Add chart"}
          </ComposerPrimitive.AddAttachment>
          <span {...stylex.props(styles.hint)} id="upload-hint">
            PNG, JPEG, WebP · Up to 3 MiB
          </span>
          {busy ? (
            <ComposerPrimitive.Cancel
              {...stylex.props(ui.button, ui.focus, styles.send)}
              aria-label="Stop response"
            >
              <Square {...stylex.props(ui.icon)} size={16} />
            </ComposerPrimitive.Cancel>
          ) : (
            <ComposerPrimitive.Send
              {...stylex.props(ui.button, ui.focus, styles.send)}
              aria-label="Send message"
              disabled={disabled}
            >
              <ArrowUp {...stylex.props(ui.icon)} size={20} />
            </ComposerPrimitive.Send>
          )}
        </div>
      </ComposerPrimitive.Root>
      {error ? (
        <p {...stylex.props(ui.error)} role="alert">
          {error}
        </p>
      ) : null}
      <p {...stylex.props(styles.note)} id="message-privacy">
        Messages and images are sent to the configured AI provider.
      </p>
    </div>
  );
}
