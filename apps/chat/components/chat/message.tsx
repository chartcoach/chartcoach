import { Review } from "./review";
import { ReviewActivity } from "./review-activity";
import type { ChartAttachment } from "../../chat/attachment";
import type { MessageView } from "../../chat/evidence";
import * as stylex from "@stylexjs/stylex";
import { colors } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

export function Message({
  view,
  attachments,
}: {
  view: MessageView;
  attachments: ReadonlyMap<string, ChartAttachment>;
}) {
  const { message, guidelines, review, complete, stopped, failed } = view;
  return (
    <article {...stylex.props(styles.message, message.role === "user" && styles.user)}>
      <h2 {...stylex.props(styles.author)}>{message.role === "user" ? "You" : "Review"}</h2>
      {message.role === "assistant" ? <ReviewActivity view={view} /> : null}
      {message.parts.map((part, index) => {
        const key = `${message.id}:${index.toString()}`;
        if (part.type === "text") {
          return message.role === "user" ? (
            <p {...stylex.props(styles.text)} key={key}>
              {part.text}
            </p>
          ) : null;
        }
        if (part.type === "file" && message.role === "user") {
          const attachment = part.filename ? attachments.get(part.filename) : undefined;
          const name = attachment?.name ?? part.filename ?? "Uploaded chart";
          const url = attachment?.data ?? part.url;
          return (
            <figure {...stylex.props(styles.attachment)} key={key}>
              {url ? <img {...stylex.props(styles.image)} src={url} alt={name} /> : null}
              <figcaption {...stylex.props(styles.caption)}>{name}</figcaption>
            </figure>
          );
        }
        return null;
      })}
      {complete ? <Review review={review} guidelines={guidelines} /> : null}
      {failed ? (
        <p {...stylex.props(ui.error)}>
          {message.role === "assistant" ? "Response interrupted." : "Message failed."} You can edit
          and send your message again.
        </p>
      ) : null}
      {message.role === "assistant" && stopped ? (
        <p {...stylex.props(ui.activity)}>Response stopped.</p>
      ) : null}
    </article>
  );
}

const styles = stylex.create({
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
    marginBottom: 12,
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
