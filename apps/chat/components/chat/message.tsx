import { Answer } from "./answer";
import { Activity } from "./activity";
import type { ChartAttachment } from "../../chat/attachment";
import type { MessageView } from "../../chat/evidence";
import * as stylex from "@stylexjs/stylex";
import { colors } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";
import { workflows } from "../../shared/workflow";

export function Message({
  view,
  attachments,
}: {
  view: MessageView;
  attachments: ReadonlyMap<string, ChartAttachment>;
}) {
  const { message, guidelines, answer, drafting, complete, stopped, failed } = view;

  return (
    <article {...stylex.props(styles.message, message.role === "user" && styles.user)}>
      <header {...stylex.props(styles.header)}>
        <h2 {...stylex.props(styles.author)}>{message.role === "user" ? "You" : "ChartCoach"}</h2>
        {view.workflow ? (
          <span
            {...stylex.props(styles.workflow, ui.appear)}
            role="status"
            aria-label={`Active mode: ${workflows[view.workflow].label}`}
            title={workflows[view.workflow].description}
          >
            {workflows[view.workflow].label}
          </span>
        ) : null}
      </header>
      {message.role === "assistant" ? <Activity view={view} /> : null}
      {message.parts.map((part, index) => {
        const key = `${message.id}:${index.toString()}`;

        if (part.type === "text") {
          return message.role === "user" ? (
            <p key={key} {...stylex.props(styles.text)}>
              {part.text}
            </p>
          ) : null;
        }

        if (part.type === "file" && message.role === "user") {
          const attachment = part.filename ? attachments.get(part.filename) : undefined;
          const name = attachment?.name ?? part.filename ?? "Uploaded chart";
          const url = attachment?.data ?? part.url;

          return (
            <figure key={key} {...stylex.props(styles.attachment)}>
              {url ? <img {...stylex.props(styles.image)} src={url} alt={name} /> : null}
              <figcaption {...stylex.props(styles.caption)}>{name}</figcaption>
            </figure>
          );
        }

        return null;
      })}
      {answer || complete ? (
        <Answer answer={answer} guidelines={guidelines} streaming={drafting} />
      ) : null}
      {failed && !answer ? (
        <p {...stylex.props(ui.error)} role="alert">
          {view.failureReason ??
            `${message.role === "assistant" ? "Response interrupted." : "Message failed."} You can edit and send your message again.`}
        </p>
      ) : null}
      {message.role === "assistant" && stopped ? (
        <p {...stylex.props(ui.activity)}>Response stopped.</p>
      ) : null}
    </article>
  );
}

const styles = stylex.create({
  header: { display: "flex", alignItems: "center", gap: 10, minHeight: 24, marginBottom: 12 },
  workflow: {
    color: colors.accentText,
    fontSize: 11,
    fontWeight: 500,
    lineHeight: "18px",
    paddingInline: 8,
    borderRadius: 12,
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: colors.border,
  },
  message: {
    fontSize: 16,
    lineHeight: 1.75,
    marginBottom: 36,
    overflowWrap: "anywhere",
    minWidth: 0,
  },
  author: {
    fontSize: 12,
    fontWeight: 500,
    lineHeight: 1.5,
    marginTop: 0,
    marginBottom: 0,
    color: colors.muted,
  },
  user: {
    borderBottomWidth: 1,
    borderBottomStyle: "solid",
    borderBottomColor: colors.border,
    paddingBottom: 26,
  },
  text: { whiteSpace: "pre-wrap", margin: 0 },
  attachment: { marginBlock: 12, marginInline: 0 },
  image: {
    maxWidth: "100%",
    maxHeight: 340,
    display: "block",
    objectFit: "contain",
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: colors.border,
    borderRadius: 6,
  },
  caption: { color: colors.muted, fontSize: 13, marginTop: 6 },
});
