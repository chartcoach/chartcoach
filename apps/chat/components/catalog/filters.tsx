import * as stylex from "@stylexjs/stylex";
import { BookOpen, X } from "lucide-react";
import { Dialog } from "radix-ui";
import { useId, useState } from "react";
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

type PanelProps = {
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
  onClose,
}: {
  metadata: CatalogMetadata;
  disabled: boolean;
  state: ReturnType<typeof useFilterDraft>;
  onClose: () => void;
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
        <div {...stylex.props(styles.overview)} aria-busy={explorer.pending}>
          <p {...stylex.props(styles.overviewCount)}>
            {count.toLocaleString()}
            <span {...stylex.props(styles.overviewTotal)}>
              {" "}
              / {metadata.totalGuidelines.toLocaleString()}
            </span>
          </p>
          <p {...stylex.props(styles.overviewLabel)}>guidelines available to your agent</p>
          <p {...stylex.props(styles.description, styles.queryStatus)}>
            {explorer.error
              ? "Catalog exploration paused"
              : explorer.data
                ? "Counts update as you choose."
                : "Loading guidelines…"}
            <span
              {...stylex.props(
                styles.updating,
                explorer.pending && !!explorer.data && styles.pending,
              )}
              aria-hidden="true"
            >
              Updating…
            </span>
          </p>
        </div>
        <fieldset disabled={disabled || applying} {...stylex.props(styles.section, styles.fields)}>
          <legend {...stylex.props(ui.srOnly)}>Guideline selection</legend>
          <YearFilters {...facets} bins={explorer.data?.years} disabled={disabled || applying} />
          {metadata.sourceTypes.length ? (
            <SourceFilters {...facets} counts={explorer.data?.sourceTypes} />
          ) : null}
          {metadata.authors.length ? (
            <AuthorFilters {...facets} counts={explorer.data?.authors} />
          ) : null}
        </fieldset>
        <details {...stylex.props(styles.explanation)}>
          <summary {...stylex.props(ui.focus, styles.disclosure)}>How your selection works</summary>
          <p {...stylex.props(styles.description)}>
            Each chart and count reflects your other choices, so you can compare alternatives.
            Author, year and type must match the same cited source. An excluded author removes every
            guideline citing them.
          </p>
        </details>
        <details {...stylex.props(styles.explanation)}>
          <summary {...stylex.props(ui.focus, styles.disclosure)}>
            Preview matching guidelines
          </summary>
          <ul {...stylex.props(styles.matches)} aria-busy={explorer.pending}>
            {explorer.data?.matches.map((match) => (
              <li key={match.id} {...stylex.props(styles.match)}>
                {match.title}
              </li>
            ))}
          </ul>
          {explorer.data?.matches.length === 0 ? (
            <p {...stylex.props(styles.description)}>No guidelines match your selection.</p>
          ) : null}
          <p {...stylex.props(styles.description)}>
            A sample of matching guidelines. The agent searches the full selection.
          </p>
        </details>
      </div>
      <footer {...stylex.props(styles.footer)}>
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
            : "Starts a fresh review. Your chart and draft stay with you."}
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
              explorer.pending && styles.pendingApply,
            )}
            type="button"
            aria-describedby={id}
            disabled={disabled || applying || !!error || (changed && !ready)}
            onClick={() => {
              if (changed) void apply();
              else onClose();
            }}
          >
            {applying ? "Applying…" : changed ? "Use these guidelines" : "Close"}
          </button>
        </div>
      </footer>
    </>
  );
}

export function CatalogFiltersPanel(props: PanelProps) {
  const [open, setOpen] = useState(false);
  const state = useFilterDraft({ ...props, open, onClose: () => setOpen(false) });
  const filters = props.value;
  const active =
    filters.includeAuthorIds.length +
    filters.excludeAuthorIds.length +
    filters.sourceTypeIds.length +
    Number(filters.yearFrom !== null || filters.yearTo !== null);
  return (
    <Dialog.Root
      open={open}
      onOpenChange={(nextOpen) => {
        if (state.applying) return;
        if (nextOpen) state.begin();
        setOpen(nextOpen);
      }}
    >
      <Dialog.Trigger asChild>
        <button
          {...stylex.props(ui.button, ui.focus, ui.quietButton, active > 0 && styles.active)}
          type="button"
          disabled={props.disabled}
          aria-label={
            active > 0
              ? `Knowledge, ${props.matchedGuidelines.toLocaleString()} guidelines selected`
              : "Knowledge"
          }
        >
          <BookOpen size={16} aria-hidden="true" /> Knowledge
          {active > 0 ? (
            <span {...stylex.props(styles.selectionCount)} aria-hidden="true">
              {props.matchedGuidelines.toLocaleString()}
            </span>
          ) : null}
        </button>
      </Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay {...stylex.props(styles.overlay)} />
        <Dialog.Content {...stylex.props(styles.panel)}>
          <header {...stylex.props(styles.header)}>
            <div>
              <Dialog.Title {...stylex.props(styles.title)}>Your agent's knowledge</Dialog.Title>
              <Dialog.Description {...stylex.props(styles.description, styles.dialogDescription)}>
                Choose the guidelines your agent can use.
              </Dialog.Description>
            </div>
            <Dialog.Close asChild>
              <button
                {...stylex.props(ui.button, ui.focus, ui.quietButton)}
                type="button"
                aria-label="Close knowledge"
                disabled={state.applying}
              >
                <X size={18} aria-hidden="true" />
              </button>
            </Dialog.Close>
          </header>
          <FilterDraft
            metadata={props.metadata}
            disabled={props.disabled}
            state={state}
            onClose={() => setOpen(false)}
          />
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
