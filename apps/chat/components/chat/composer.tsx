import { AttachmentPrimitive, ComposerPrimitive, useAuiState } from "@assistant-ui/react";
import * as Match from "effect/Match";
import { ArrowUp, ImagePlus, Info, X } from "lucide-react";
import { Popover } from "radix-ui";
import { useState, type ReactNode, type RefObject } from "react";
import * as stylex from "@stylexjs/stylex";
import { colors, media, motion } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

const swap = stylex.keyframes({
  from: { opacity: 0, transform: "scale(0.9)" },
  to: { opacity: 1, transform: "scale(1)" },
});

const styles = stylex.create({
  area: {
    width: "min(100%, 720px)",
    flexShrink: 0,
    marginInline: "auto",
    paddingTop: 12,
    paddingInline: { default: 24, [media.mobile]: 12 },
    paddingBottom: "max(8px, env(safe-area-inset-bottom))",
  },
  root: {
    backgroundColor: colors.surface,
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: { default: colors.border, ":focus-within": colors.muted },
    borderRadius: { default: 16, [media.mobile]: 26 },
    boxShadow: "0 2px 12px #00000006",
    padding: { default: 16, [media.mobile]: 12 },
  },
  collapsedRoot: {
    display: { default: null, [media.mobile]: "grid" },
    gridTemplateColumns: { default: null, [media.mobile]: "auto minmax(0, 1fr) auto" },
    gridTemplateAreas: { default: null, [media.mobile]: '"attachment input send"' },
    alignItems: { default: null, [media.mobile]: "center" },
    columnGap: { default: null, [media.mobile]: 2 },
    padding: { default: 16, [media.mobile]: 3 },
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
    minHeight: { default: 48, [media.short]: 32, [media.mobile]: 0 },
    maxHeight: 180,
    paddingBlock: 0,
    paddingInline: 2,
    fontSize: 16,
    WebkitTapHighlightColor: "transparent",
    "::placeholder": { color: colors.muted },
  },
  collapsedInput: { gridArea: "input" },
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
  collapsedControls: { display: { default: "grid", [media.mobile]: "contents" } },
  model: { display: "contents" },
  collapsedModel: { display: { default: "contents", [media.mobile]: "none" } },
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
  swap: {
    animationName: swap,
    animationDuration: { default: motion.control, [media.reducedMotion]: "0ms" },
    animationTimingFunction: motion.easeOut,
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
    display: "flex",
    justifyContent: "center",
    textAlign: "center",
    color: colors.muted,
    fontSize: 12,
    lineHeight: 1.5,
    marginTop: 4,
  },
  privacyTrigger: {
    fontSize: 11,
    gap: 6,
    minHeight: 32,
    paddingBlock: 4,
    paddingInline: 8,
  },
  privacyContent: {
    zIndex: 50,
    width: "min(340px, calc(100vw - 32px))",
    padding: 18,
    backgroundColor: colors.surface,
    color: colors.foreground,
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: colors.border,
    borderRadius: 12,
    boxShadow: "0 8px 32px #00000020",
    fontSize: 13,
    lineHeight: 1.6,
  },
  privacyHeading: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    gap: 8,
    marginBottom: 8,
  },
  privacyTitle: { fontWeight: 550 },
  privacyText: { color: colors.muted, marginTop: 8 },
  tracingLink: {
    color: colors.accentText,
    fontWeight: 500,
    textUnderlineOffset: 2,
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
  keepExpanded = false,
  tracing = false,
}: {
  onUpload: (files: File[]) => void;
  messageInput: RefObject<HTMLTextAreaElement | null>;
  busy: boolean;
  disabled: boolean;
  reading: boolean;
  error?: string;
  onRecover?: () => Promise<void>;
  modelControl?: ReactNode;
  keepExpanded?: boolean;
  tracing?: boolean;
}) {
  const [editing, setEditing] = useState(false);

  const draft = useAuiState(
    (state) => state.composer.text !== "" || state.composer.attachments.length > 0,
  );

  const collapsed = !keepExpanded && !editing && !draft;

  return (
    <div {...stylex.props(styles.area)}>
      <ComposerPrimitive.Root
        {...stylex.props(styles.root, collapsed && styles.collapsedRoot)}
        aria-label="Message composer"
        data-state={collapsed ? "collapsed" : "expanded"}
        // React delivers focus from portaled children, such as the model dialog, through
        // this root. Their DOM nodes sit outside it, and they keep the composer expanded.
        onFocus={(event) => {
          if (!event.currentTarget.contains(event.target)) setEditing(true);
        }}
        onBlur={(event) => {
          if (!event.currentTarget.contains(event.relatedTarget)) setEditing(false);
        }}
      >
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
              <AttachmentPrimitive.Root {...stylex.props(styles.attachment, ui.appear)}>
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
          {...stylex.props(styles.input, collapsed && styles.collapsedInput)}
          id="message"
          ref={messageInput}
          placeholder="Ask about your chart…"
          minRows={1}
          maxRows={6}
          disabled={disabled}
          submitMode="enter"
          cancelOnEscape={false}
          addAttachmentOnPaste={false}
          aria-describedby="upload-hint message-privacy"
          onFocus={() => setEditing(true)}
          onPaste={(event) => {
            const files = Array.from(event.clipboardData.files);

            if (files.length) {
              event.preventDefault();
              onUpload(files);
            }
          }}
        />
        <div
          {...stylex.props(styles.controls, collapsed && styles.collapsedControls)}
          // WebKit blurs the input when a button is pressed without focusing the button. The
          // composer would collapse under the pointer and the button would miss its click.
          onMouseDown={(event) => {
            if (document.activeElement === messageInput.current) event.preventDefault();
          }}
        >
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
          <div {...stylex.props(styles.model, collapsed && styles.collapsedModel)}>
            {modelControl}
          </div>
          {busy ? (
            <ComposerPrimitive.Cancel
              {...stylex.props(ui.button, ui.focus, styles.send, styles.stop, styles.swap)}
              aria-label="Stop response"
              title="Stop response"
            >
              <span {...stylex.props(styles.stopFace)} aria-hidden="true">
                <span {...stylex.props(styles.stopGlyph)} />
              </span>
            </ComposerPrimitive.Cancel>
          ) : (
            <ComposerPrimitive.Send
              {...stylex.props(ui.button, ui.focus, styles.send, styles.swap)}
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
      <div {...stylex.props(styles.note)}>
        <Popover.Root>
          <Popover.Trigger
            {...stylex.props(ui.button, ui.quietButton, ui.focus, styles.privacyTrigger)}
            title="Privacy and tracing"
          >
            <span id="message-privacy">
              Sent to your AI provider{tracing ? " · Tracing on" : ""}
            </span>
            <Info size={12} {...stylex.props(ui.icon)} aria-hidden="true" />
          </Popover.Trigger>
          <Popover.Portal>
            <Popover.Content
              {...stylex.props(styles.privacyContent)}
              side="top"
              sideOffset={8}
              collisionPadding={16}
              aria-label="Privacy and tracing details"
            >
              <div {...stylex.props(styles.privacyHeading)}>
                <h2 {...stylex.props(styles.privacyTitle)}>Your conversation</h2>
                <Popover.Close
                  {...stylex.props(ui.button, ui.quietButton, ui.focus)}
                  aria-label="Close privacy details"
                >
                  <X size={16} aria-hidden="true" />
                </Popover.Close>
              </div>
              <p {...stylex.props(styles.privacyText)}>
                Messages and images are sent to the configured AI provider.
              </p>
              {tracing ? (
                <p {...stylex.props(styles.privacyText)}>
                  Conversation tracing is enabled to improve chartcoach and may include messages,
                  images, and responses. You can opt out by{" "}
                  <a
                    {...stylex.props(styles.tracingLink, ui.focus)}
                    href="https://docs.chartcoach.dev/"
                    target="_blank"
                    rel="noreferrer"
                  >
                    self-hosting chartcoach with tracing disabled
                  </a>
                  .
                </p>
              ) : null}
            </Popover.Content>
          </Popover.Portal>
        </Popover.Root>
      </div>
    </div>
  );
}
