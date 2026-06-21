import { Fragment } from "react";
import type { CodeLine, CodeToken } from "./types";

type CodeWindowProps = {
  title: string;
  language: string;
  lines: readonly CodeLine[];
  wrap?: boolean;
};

export function CodeWindow(props: CodeWindowProps) {
  return (
    <CodeWindowFrame
      {...props}
      preClassName="px-5 pb-5 pt-14 text-[0.8125rem] leading-[1.7] sm:px-6 sm:pb-6 sm:text-[0.875rem]"
    />
  );
}

export function DenseCodeWindow(props: CodeWindowProps) {
  return (
    <CodeWindowFrame
      {...props}
      preClassName="px-4 pb-4 pt-12 text-[0.75rem] leading-[1.7] sm:px-5 sm:pb-5 sm:text-[0.8125rem]"
    />
  );
}

function CodeWindowFrame({
  title,
  language,
  lines,
  wrap = false,
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
      <span className="absolute left-5 top-4 z-10 min-w-0 max-w-[calc(100%-8rem)] truncate font-mono text-[0.6875rem] leading-none text-muted sm:left-6">
        {title}
      </span>
      <span className="absolute right-4 top-3.5 z-10 rounded-full border border-border bg-bg/82 px-2.5 py-1 font-mono text-[0.625rem] font-semibold uppercase leading-none tracking-[0.12em] text-muted shadow-[0_1px_2px_color-mix(in_srgb,var(--color-fg)_5%,transparent)] sm:right-5">
        {languageLabel}
      </span>
      <pre
        className={[
          "m-0 min-h-full overflow-x-auto whitespace-pre-wrap break-words bg-code-bg font-mono text-code-fg",
          wrap ? "" : "md:whitespace-pre md:break-normal",
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
