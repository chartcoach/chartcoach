import * as stylex from "@stylexjs/stylex";
import { ArrowUpRight } from "lucide-react";
import { HoverCard } from "radix-ui";
import { VList } from "virtua";
import type { useCatalogExplorer } from "../../chat/use-catalog-explorer";
import { useMatchList } from "../../chat/use-match-list";
import { GuidelineCard } from "../guideline-card";
import { styles } from "./matched-guidelines.styles";
import { ui } from "../ui/ui";

export function MatchedGuidelines({
  explorer,
  disabled,
}: {
  explorer: ReturnType<typeof useCatalogExplorer>;
  disabled: boolean;
}) {
  const { data, list, pending, error, retry, total, keepMounted, focus, blur, scroll } =
    useMatchList(explorer, disabled);

  return (
    <section {...stylex.props(styles.section)} aria-label="Matching guidelines">
      <header {...stylex.props(styles.header)}>
        <h2 {...stylex.props(styles.title)}>Matching guidelines</h2>
        <span {...stylex.props(styles.updating, pending && styles.pending)} aria-hidden="true">
          Updating…
        </span>
      </header>
      <p {...stylex.props(styles.description)}>
        Open a guideline to read it. Hover or focus a title for a visual preview.
      </p>
      <div {...stylex.props(styles.viewport)}>
        <VList
          key={data?.key ?? "loading"}
          ref={list}
          data={data?.matches ?? []}
          keepMounted={keepMounted}
          {...stylex.props(styles.list)}
          role="list"
          aria-label="Matched guideline results"
          aria-busy={pending}
          tabIndex={0}
          onScroll={scroll}
        >
          {(match, index) => {
            const guideline = {
              ...match,
              url: `https://chartcoach.dev/guidelines/${encodeURIComponent(match.id)}`,
            };

            return (
              <div
                key={match.id}
                role="listitem"
                aria-posinset={index + 1}
                aria-setsize={total}
                {...stylex.props(styles.item)}
              >
                <HoverCard.Root openDelay={250} closeDelay={120}>
                  <HoverCard.Trigger asChild>
                    <a
                      {...stylex.props(ui.focus, styles.link)}
                      href={guideline.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      aria-label={`Read guideline: ${match.title} (opens in a new tab)`}
                      onFocus={() => focus(index)}
                      onBlur={blur}
                    >
                      <span {...stylex.props(styles.name)}>{match.title}</span>
                      <ArrowUpRight
                        size={15}
                        {...stylex.props(ui.icon, styles.arrow)}
                        aria-hidden="true"
                      />
                    </a>
                  </HoverCard.Trigger>
                  <HoverCard.Portal>
                    <HoverCard.Content
                      {...stylex.props(styles.preview)}
                      side="top"
                      align="start"
                      sideOffset={8}
                      collisionPadding={12}
                      hideWhenDetached
                    >
                      <GuidelineCard guideline={guideline} />
                    </HoverCard.Content>
                  </HoverCard.Portal>
                </HoverCard.Root>
              </div>
            );
          }}
        </VList>
        {!data?.matches.length ? (
          <p {...stylex.props(styles.empty)}>
            {error
              ? "Matching guidelines are unavailable."
              : pending || !data
                ? "Loading matching guidelines…"
                : "No guidelines match your selection."}
          </p>
        ) : null}
      </div>
      <footer {...stylex.props(styles.footer)}>
        <span {...stylex.props(styles.range)}>
          {data && data.matches.length < total ? "Scroll to explore more" : ""}
        </span>
      </footer>
      {error ? (
        <p {...stylex.props(ui.error)} role="alert">
          {error}
          {retry ? (
            <button
              {...stylex.props(ui.button, ui.quietButton, ui.focus)}
              type="button"
              onClick={retry}
            >
              Retry matches
            </button>
          ) : null}
        </p>
      ) : null}
    </section>
  );
}
