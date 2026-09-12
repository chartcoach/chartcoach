import * as stylex from "@stylexjs/stylex";
import { Popover } from "radix-ui";
import { ChevronDown, Search, X } from "lucide-react";
import { useId } from "react";
import { VList } from "virtua";
import type { CatalogFilters, CatalogMetadata } from "../../shared/catalog-filters";
import { useAuthorPicker } from "../../chat/use-author-picker";
import { ui } from "../ui/ui";
import { styles as facets } from "./filters.styles";
import { styles } from "./author-filters.styles";

export function AuthorFilters({
  metadata,
  draft,
  counts,
  onChange,
  disabled = false,
  pending = false,
}: {
  metadata: CatalogMetadata;
  draft: CatalogFilters;
  counts?: { id: number; count: number }[];
  onChange: (filters: CatalogFilters) => void;
  disabled?: boolean;
  pending?: boolean;
}) {
  const picker = useAuthorPicker(metadata, draft, counts, onChange);
  const id = useId();

  return (
    <fieldset {...stylex.props(facets.section)} disabled={disabled}>
      <legend {...stylex.props(facets.legend)}>Authors</legend>
      <p {...stylex.props(facets.note)}>Include or exclude an author.</p>
      <Popover.Root open={picker.open} onOpenChange={picker.setOpen}>
        <Popover.Trigger
          {...stylex.props(ui.button, ui.focus, styles.trigger)}
          disabled={disabled || !counts}
        >
          <span>Browse authors</span>
          <span {...stylex.props(styles.count)}>
            {counts ? picker.available.toLocaleString() : "…"}
          </span>
          <ChevronDown size={16} aria-hidden="true" />
        </Popover.Trigger>
        <Popover.Portal>
          <Popover.Content
            {...stylex.props(styles.popup)}
            aria-labelledby={`${id}-title`}
            sideOffset={8}
            collisionPadding={12}
            onOpenAutoFocus={(event) => {
              event.preventDefault();
              picker.search.current?.focus();
            }}
          >
            <header {...stylex.props(styles.header)}>
              <h2 id={`${id}-title`} {...stylex.props(styles.title)}>
                Choose authors
              </h2>
              <Popover.Close
                {...stylex.props(ui.button, ui.quietButton, ui.focus)}
                aria-label="Close author picker"
              >
                <X size={16} aria-hidden="true" />
              </Popover.Close>
            </header>
            <div {...stylex.props(styles.search)}>
              <Search size={16} aria-hidden="true" {...stylex.props(ui.icon)} />
              <input
                ref={picker.search}
                type="search"
                name="author"
                autoComplete="off"
                aria-label="Find an author"
                placeholder="Search authors…"
                value={picker.query}
                onChange={(event) => picker.setQuery(event.target.value)}
                {...stylex.props(ui.focus, styles.input)}
              />
            </div>
            <div {...stylex.props(styles.toolbar)}>
              <span role="status" aria-busy={pending}>
                {counts ? `${picker.available.toLocaleString()} available` : "Loading authors…"}
              </span>
              <button
                type="button"
                {...stylex.props(
                  ui.button,
                  ui.focus,
                  styles.selected,
                  picker.selectedOnly && styles.active,
                )}
                aria-pressed={picker.selectedOnly}
                onClick={picker.toggleSelected}
              >
                Selected ({picker.selected})
              </button>
            </div>
            <div {...stylex.props(styles.viewport)}>
              <VList
                ref={picker.list}
                data={picker.rows}
                keepMounted={picker.keepMounted}
                {...stylex.props(styles.list)}
                role="list"
                aria-label="Authors by matching guideline count"
                aria-busy={pending}
                tabIndex={0}
              >
                {(author, index) => (
                  <div
                    key={author.id}
                    role="listitem"
                    aria-posinset={index + 1}
                    aria-setsize={picker.rows.length}
                    {...stylex.props(styles.row)}
                  >
                    <label {...stylex.props(styles.author)}>
                      <span {...stylex.props(styles.name)}>
                        <span title={author.name} {...stylex.props(styles.authorName)}>
                          {author.name}
                        </span>
                        <span {...stylex.props(styles.detail)}>
                          {author.count
                            ? `${author.count.toLocaleString()} ${author.count === 1 ? "guideline" : "guidelines"}`
                            : "No matches in this selection"}
                        </span>
                        <span {...stylex.props(facets.barTrack)} aria-hidden="true">
                          <span
                            {...stylex.props(
                              facets.barFill,
                              facets.barScale(author.count / Math.max(1, picker.maxCount)),
                              author.choice !== "any" && styles.selectedBar,
                            )}
                          />
                        </span>
                      </span>
                      <select
                        {...stylex.props(
                          ui.focus,
                          facets.select,
                          author.choice !== "any" && facets.selected,
                        )}
                        aria-label={`Filter author ${author.name}`}
                        value={author.choice}
                        disabled={disabled || pending}
                        onFocus={() => picker.focus(author.id)}
                        onBlur={picker.blur}
                        onChange={(event) => picker.choose(author.id, event.target.value)}
                      >
                        <option value="any">Any</option>
                        <option value="include">Include</option>
                        <option value="exclude">Exclude</option>
                      </select>
                    </label>
                  </div>
                )}
              </VList>
              {!picker.rows.length ? (
                <p {...stylex.props(styles.empty)}>
                  {picker.query
                    ? "No authors match your search."
                    : picker.selectedOnly
                      ? "No authors selected."
                      : "No authors match these year and source choices."}
                </p>
              ) : null}
            </div>
            <p {...stylex.props(styles.footnote)}>
              Most matching guidelines first. Selected authors stay editable.
            </p>
          </Popover.Content>
        </Popover.Portal>
      </Popover.Root>
      <p {...stylex.props(styles.summary)} role="status" aria-busy={pending}>
        {picker.selected
          ? `${draft.includeAuthorIds.length} included · ${draft.excludeAuthorIds.length} excluded`
          : "All available authors"}
      </p>
      <p {...stylex.props(facets.description)}>
        Browse by guideline count or search by name. Counts follow the publication years and source
        types.
      </p>
    </fieldset>
  );
}
