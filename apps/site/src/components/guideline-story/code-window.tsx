import { Fragment } from "react";
import type { CodeLine, CodeToken } from "./types";

type CodeWindowProps = {
  title: string;
  language: string;
  lines: readonly CodeLine[];
};

export function CodeWindow(props: CodeWindowProps) {
  return (
    <CodeWindowFrame
      {...props}
      preClassName="px-5 py-5 text-[0.8125rem] leading-[1.7] sm:px-6 sm:pb-6 sm:text-[0.875rem]"
    />
  );
}

export function DenseCodeWindow(props: CodeWindowProps) {
  return (
    <CodeWindowFrame
      {...props}
      preClassName="px-4 py-4 text-[0.75rem] leading-[1.7] sm:px-5 sm:pb-5 sm:text-[0.8125rem]"
    />
  );
}

function CodeWindowFrame({
  title,
  language,
  lines,
  preClassName,
}: CodeWindowProps & {
  preClassName: string;
}) {
  const languageLabel = getLanguageLabel(language);

  return (
    <div
      className="relative min-w-0 overflow-hidden bg-code-bg"
      aria-label={`${title} ${language} code example`}
    >
      <div className="flex flex-wrap items-center justify-between gap-3 px-4 pt-4 sm:px-5">
        <span className="min-w-0 break-words font-mono text-xs text-muted">{title}</span>
        <span className="rounded-full border border-border bg-bg px-2.5 py-1 font-mono text-xs text-muted">
          {languageLabel}
        </span>
      </div>
      <pre
        tabIndex={0}
        role="region"
        aria-label={`${title} code`}
        className={[
          "m-0 overflow-x-auto bg-code-bg font-mono text-code-fg focus-visible:outline-2 focus-visible:outline-offset-[-2px]",
          language === "json" ? "whitespace-pre" : "whitespace-pre-wrap [overflow-wrap:anywhere]",
          preClassName,
        ].join(" ")}
      >
        <code>
          {lines.map((parts, lineIndex) => (
            <Fragment key={lineIndex}>
              {parts.length === 0
                ? "\u00a0"
                : parts.map((part, partIndex) => (
                    <CodeTokenView key={`${lineIndex}-${partIndex}`} token={part} />
                  ))}
              {lineIndex < lines.length - 1 ? "\n" : null}
            </Fragment>
          ))}
        </code>
      </pre>
    </div>
  );
}

function getLanguageLabel(language: string) {
  switch (language) {
    case "ts":
      return "TYPESCRIPT";
    case "py":
      return "PYTHON";
    case "sh":
      return "SHELL";
    case "json":
      return "JSON";
    case "markdown":
      return "MARKDOWN";
    default:
      return language.toUpperCase();
  }
}

function CodeTokenView({ token }: { token: CodeToken }) {
  return (
    <span className={`cc-code-token cc-code-token--${token.kind ?? "plain"}`}>{token.text}</span>
  );
}
