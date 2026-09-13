"use client";

import * as stylex from "@stylexjs/stylex";
import { Streamdown } from "streamdown";
import { useGuidelinePage } from "../chat/use-guideline-page";
import { ui } from "./ui/ui";
import { colors } from "./ui/tokens.stylex";

const styles = stylex.create({
  page: {
    maxWidth: 800,
    marginInline: "auto",
    padding: 24,
    lineHeight: 1.7,
    overflowWrap: "anywhere",
  },
  title: { fontSize: 32, lineHeight: 1.2, marginBlock: 24 },
  section: { marginBlock: 32 },
  muted: { color: colors.muted, fontSize: 13 },
});

export function GuidelinePage() {
  const { guideline, error } = useGuidelinePage();

  return (
    <main {...stylex.props(styles.page)}>
      <a {...stylex.props(ui.focus)} href="/">
        ChartCoach
      </a>
      {error ? (
        <p role="alert">{error}</p>
      ) : guideline ? (
        <article>
          <h1 {...stylex.props(styles.title)}>{guideline.title}</h1>
          <p>{guideline.description}</p>
          {guideline.sections.map((section, index) => (
            <section key={index} {...stylex.props(styles.section)}>
              <h2>{section.title}</h2>
              <Streamdown mode="static" skipHtml controls={false}>
                {section.content}
              </Streamdown>
            </section>
          ))}
          <section {...stylex.props(styles.section)}>
            <h2>Sources</h2>
            <ul>
              {guideline.sources.map((source) => (
                <li key={source.reference_id}>
                  {source.url && /^https?:\/\//.test(source.url) ? (
                    <a href={source.url} rel="noopener noreferrer" target="_blank">
                      {source.citation}
                    </a>
                  ) : (
                    source.citation
                  )}
                </li>
              ))}
            </ul>
          </section>
          {guideline.release ? (
            <p {...stylex.props(styles.muted)}>Catalog release: {guideline.release}</p>
          ) : null}
        </article>
      ) : (
        <p role="status">Loading guideline…</p>
      )}
    </main>
  );
}
