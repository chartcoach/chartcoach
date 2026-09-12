import * as stylex from "@stylexjs/stylex";
import { ArrowLeft, Info } from "lucide-react";
import { Popover } from "radix-ui";
import { Activity, useEffect, useId, useRef } from "react";
import {
  emptyCatalogFilters,
  type CatalogFilters,
  type CatalogMetadata,
} from "../../shared/catalog-filters";
import { useFilterDraft } from "../../chat/use-filter-draft";
import type { CatalogFilterSelection } from "../../chat/use-catalog-filters";
import { ui } from "../ui/ui";
import { AuthorFilters, SourceFilters, YearFilters } from "./facets";
import { styles } from "./filters.styles";
import { MatchedGuidelines } from "./matched-guidelines";

type GuidelinesProps = {
  open: boolean;
  onClose: () => void;
  metadata: CatalogMetadata;
  value: CatalogFilters;
  matchedGuidelines: number;
  disabled: boolean;
  onApply: (selection: CatalogFilterSelection) => Promise<void>;
  onReload: () => Promise<void>;
};

function FilterDraft({
  metadata,
  disabled,
  state,
}: {
  metadata: CatalogMetadata;
  disabled: boolean;
  state: ReturnType<typeof useFilterDraft>;
}) {
  const id = useId();

  const {
    draft,
    setDraft,
    count,
    ready,
    error,
    valid,
    changed,
    applying,
    applyError,
    apply,
    reload,
    retry,
    explorer,
  } = state;

  const facets = { metadata, draft, onChange: setDraft };

  return (
    <>
      <div {...stylex.props(styles.body)}>
        <fieldset disabled={disabled || applying} {...stylex.props(styles.fields)}>
          <legend {...stylex.props(ui.srOnly)}>Guideline selection</legend>
          <YearFilters {...facets} bins={explorer.data?.years} disabled={disabled || applying} />
          {metadata.authors.length ? (
            <AuthorFilters {...facets} counts={explorer.data?.authors} />
          ) : null}
          {metadata.sourceTypes.length ? (
            <SourceFilters {...facets} counts={explorer.data?.sourceTypes} />
          ) : null}
        </fieldset>
        <MatchedGuidelines explorer={explorer} disabled={disabled || applying} />
      </div>
      <footer {...stylex.props(styles.footer)}>
        <div {...stylex.props(styles.footerSummary)}>
          <p
            {...stylex.props(styles.result)}
            role="status"
            aria-live="polite"
            aria-busy={explorer.pending}
          >
            {error
              ? valid
                ? "Could not check selection"
                : "Selection needs attention"
              : `${count.toLocaleString()} guidelines selected`}
          </p>
          {error ? <p {...stylex.props(ui.error, styles.error)}>{error}</p> : null}
          <p
            {...stylex.props(
              styles.note,
              styles.footerNote,
              Boolean(error || applyError) && ui.srOnly,
            )}
            id={id}
          >
            {count === 0
              ? "No guidelines match. Broaden your selection to review a chart."
              : changed
                ? "Starts a new conversation. Your chart and draft stay with you."
                : "Your agent is using this selection."}
          </p>
          {applyError ? (
            <p {...stylex.props(ui.error)} role="alert">
              {applyError}
            </p>
          ) : null}
          {(valid && error) || applyError ? (
            <div {...stylex.props(styles.recovery)}>
              {valid && error ? (
                <button
                  {...stylex.props(ui.button, ui.focus, ui.quietButton)}
                  type="button"
                  disabled={disabled || applying}
                  onClick={retry}
                >
                  Retry
                </button>
              ) : null}
              <button
                {...stylex.props(ui.button, ui.focus, ui.quietButton)}
                type="button"
                disabled={disabled || applying}
                onClick={() => void reload()}
              >
                Reload catalog
              </button>
            </div>
          ) : null}
        </div>
        <div {...stylex.props(styles.actions)}>
          <button
            {...stylex.props(ui.button, ui.focus, ui.quietButton)}
            type="button"
            disabled={disabled || applying}
            onClick={() => setDraft(emptyCatalogFilters(metadata.catalogId))}
          >
            Select all
          </button>
          <button
            {...stylex.props(
              ui.button,
              ui.focus,
              styles.apply,
              explorer.pending &&
                changed &&
                valid &&
                !disabled &&
                !applying &&
                !error &&
                styles.pendingApply,
            )}
            type="button"
            aria-describedby={id}
            aria-busy={explorer.pending || applying}
            disabled={!changed || disabled || applying || !!error || !ready}
            onClick={() => void apply()}
          >
            {applying ? "Applying…" : "Use these guidelines"}
          </button>
        </div>
      </footer>
    </>
  );
}

export function GuidelinesPage(props: GuidelinesProps) {
  const state = useFilterDraft(props);
  const heading = useRef<HTMLHeadingElement>(null);
  useEffect(() => {
    if (props.open) heading.current?.focus({ preventScroll: true });
  }, [props.open]);

  return (
    <Activity mode={props.open ? "visible" : "hidden"}>
      <main {...stylex.props(styles.page)} aria-label="Guidelines settings">
        <header {...stylex.props(styles.header)}>
          <div>
            <h1 ref={heading} tabIndex={-1} {...stylex.props(styles.title)}>
              Guidelines
            </h1>
            <p {...stylex.props(styles.description)}>Choose the guidelines your agent can use.</p>
          </div>
          <div {...stylex.props(styles.headerActions)}>
            <Popover.Root>
              <Popover.Trigger
                {...stylex.props(ui.button, ui.quietButton, ui.focus)}
                aria-label="How your selection works"
              >
                <Info size={18} aria-hidden="true" />
              </Popover.Trigger>
              <Popover.Portal>
                <Popover.Content
                  {...stylex.props(styles.help)}
                  sideOffset={8}
                  collisionPadding={16}
                >
                  <h2 {...stylex.props(styles.legend)}>How your selection works</h2>
                  <p {...stylex.props(styles.description)}>
                    Counts reflect your other choices. Author, year and type must match the same
                    cited source. Excluding an author removes every guideline citing them.
                  </p>
                </Popover.Content>
              </Popover.Portal>
            </Popover.Root>
            <button
              type="button"
              {...stylex.props(ui.button, ui.quietButton, ui.focus)}
              disabled={state.applying}
              onClick={props.onClose}
            >
              <ArrowLeft size={16} aria-hidden="true" /> Back to chat
            </button>
          </div>
        </header>
        <FilterDraft metadata={props.metadata} disabled={props.disabled} state={state} />
      </main>
    </Activity>
  );
}
