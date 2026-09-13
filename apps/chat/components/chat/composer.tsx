import { AttachmentPrimitive, ComposerPrimitive } from "@assistant-ui/react";
import * as Match from "effect/Match";
import { ArrowUp, ImagePlus, X } from "lucide-react";
import type { ReactNode, RefObject } from "react";
import * as stylex from "@stylexjs/stylex";
import { colors, media, motion } from "../ui/tokens.stylex";
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
    borderColor: { default: colors.border, ":focus-within": colors.muted },
    borderRadius: 16,
    boxShadow: "0 2px 12px #00000006",
    padding: 16,
  },
  embedded: { width: "100%", paddingInline: 0, paddingTop: 24, paddingBottom: 0 },
  input: {
    display: "block",
    width: "100%",
    borderWidth: 0,
    resize: "none",
    backgroundColor: "transparent",
    color: "inherit",
    outlineStyle: "none",
    lineHeight: 1.6,
    minHeight: { default: 64, [media.short]: 48 },
    maxHeight: 180,
    paddingBlock: 0,
    paddingInline: 2,
    fontSize: 16,
    WebkitTapHighlightColor: "transparent",
    "::placeholder": { color: colors.muted },
  },
  controls: {
    display: "grid",
    gridTemplateColumns: {
      default: "auto minmax(0, 1fr) auto",
    },
    gridTemplateAreas: {
      default: '"attachment model send"',
    },
    gap: 8,
    alignItems: "center",
    marginTop: 10,
  },
  attachmentControl: { gridArea: "attachment", minWidth: { default: 128, [media.mobile]: 44 } },
  attachmentLabel: { display: { default: "inline", [media.mobile]: "none" }, whiteSpace: "nowrap" },
  send: {
    gridArea: "send",
    marginLeft: "auto",
    flexShrink: 0,
    borderWidth: 0,
    borderRadius: 22,
    width: 44,
    height: 44,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    color: { default: "#fff", ":disabled": colors.muted },
    backgroundColor: { default: colors.accent, ":disabled": colors.navigation },
    opacity: {
      default: 1,
      ":disabled": 1,
      ":hover:enabled": { default: null, [media.hover]: 0.8 },
    },
  },
  stop: { backgroundColor: "transparent", padding: 4 },
  stopFace: {
    width: 36,
    height: 36,
    flexShrink: 0,
    borderRadius: "50%",
    display: "grid",
    placeItems: "center",
    backgroundColor: colors.foreground,
    color: colors.background,
    transform: { default: "scale(1)", ":active": "scale(0.94)" },
    transitionProperty: "transform",
    transitionDuration: { default: motion.control, [media.reducedMotion]: "0ms" },
    transitionTimingFunction: motion.easeOut,
  },
  stopGlyph: { width: 12, height: 12, borderRadius: 2, backgroundColor: "currentColor" },
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
  onRecover,
  modelControl,
  embedded = false,
}: {
  onUpload: (files: File[]) => void;
  messageInput: RefObject<HTMLTextAreaElement | null>;
  busy: boolean;
  disabled: boolean;
  reading: boolean;
  error?: string;
  onRecover?: () => Promise<void>;
  modelControl?: ReactNode;
  embedded?: boolean;
}) {
  return (
    <div {...stylex.props(styles.area, embedded && styles.embedded)}>
      <ComposerPrimitive.Root {...stylex.props(styles.root)} aria-label="Message composer">
        <ComposerPrimitive.Attachments>
          {({ attachment }) => {
            const content = attachment.content?.find(
              (part) =>
                part.type === "image" ||
                (part.type === "file" && part.mimeType.startsWith("image/")),
            );

            const src = Match.value(content).pipe(
              Match.when({ type: "image" }, (part) => part.image),
              Match.when({ type: "file" }, (part) => part.data),
              Match.orElse(() => undefined),
            );

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
                  {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.remove)}
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
          placeholder="Ask about your chart or a design choice…"
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
            {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.attachmentControl)}
            multiple={false}
            disabled={disabled}
            aria-label={reading ? "Reading image" : "Add chart"}
          >
            <ImagePlus {...stylex.props(ui.icon)} size={18} />
            <span {...stylex.props(styles.attachmentLabel)}>
              {reading ? "Reading image" : "Add chart"}
            </span>
          </ComposerPrimitive.AddAttachment>
          <span {...stylex.props(ui.srOnly)} id="upload-hint">
            PNG, JPEG, WebP · Up to 3 MiB
          </span>
          {modelControl}
          {busy ? (
            <ComposerPrimitive.Cancel
              {...stylex.props(ui.button, ui.focus, styles.send, styles.stop)}
              aria-label="Stop response"
              title="Stop response"
            >
              <span {...stylex.props(styles.stopFace)} aria-hidden="true">
                <span {...stylex.props(styles.stopGlyph)} />
              </span>
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
      {onRecover ? (
        <div>
          <p {...stylex.props(ui.activity)}>
            This conversation ended. Keep your chart and draft in a new chat.
          </p>
          <button
            type="button"
            {...stylex.props(ui.button, ui.outlineButton, ui.focus)}
            disabled={disabled}
            onClick={() => void onRecover()}
          >
            Continue in a new chat
          </button>
        </div>
      ) : null}
      <p {...stylex.props(styles.note)} id="message-privacy">
        Messages and images are sent to the configured AI provider.
      </p>
    </div>
  );
}
