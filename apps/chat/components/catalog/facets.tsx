import * as stylex from "@stylexjs/stylex";
import { Slider } from "radix-ui";
import { useState } from "react";
import type { CatalogFilters, CatalogMetadata } from "../../shared/catalog-filters";
import { ui } from "../ui/ui";
import { styles } from "./filters.styles";

type FacetProps = {
  metadata: CatalogMetadata;
  draft: CatalogFilters;
  onChange: (filters: CatalogFilters) => void;
};

type Counts = { id: number; count: number }[];

function CountBar({ count, max }: { count: number | undefined; max: number }) {
  return (
    <span {...stylex.props(styles.barTrack)} aria-hidden="true">
      <span {...stylex.props(styles.barFill, styles.barScale((count ?? 0) / Math.max(1, max)))} />
    </span>
  );
}

export function AuthorFilters({
  metadata,
  draft,
  onChange,
  counts,
}: FacetProps & { counts?: Counts }) {
  const [query, setQuery] = useState("");
  const [touched, setTouched] = useState<number[]>([]);
  const selected = new Set([...draft.includeAuthorIds, ...draft.excludeAuthorIds]);
  const retained = new Set([...selected, ...touched]);
  const lookup = new Map(counts?.map(({ id, count }) => [id, count]));
  const candidates = metadata.authors
    .filter((author) => author.name.toLocaleLowerCase().includes(query.trim().toLocaleLowerCase()))
    .sort((a, b) => b.guidelineCount - a.guidelineCount || a.name.localeCompare(b.name));
  const visibleLimit = query.trim() ? 8 : 4;
  const suggestions = candidates.slice(0, visibleLimit);
  const visible = [
    ...suggestions,
    ...metadata.authors.filter(
      (author) => retained.has(author.id) && !suggestions.includes(author),
    ),
  ];
  const max = Math.max(1, ...Array.from(lookup.values()));
  return (
    <fieldset {...stylex.props(styles.section)}>
      <legend {...stylex.props(styles.legend)}>Authors</legend>
      <p {...stylex.props(styles.note)}>
        Include any selected author, or exclude every guideline citing them.
      </p>
      <input
        {...stylex.props(ui.focus, styles.input)}
        type="search"
        aria-label="Find an author"
        placeholder={`Search ${metadata.authors.length.toLocaleString()} authors`}
        value={query}
        onChange={(event) => setQuery(event.target.value)}
      />
      {visible.map((author) => (
        <label key={author.id} {...stylex.props(styles.author)}>
          <span {...stylex.props(styles.facetLabel)}>
            <span {...stylex.props(styles.name)}>
              {author.name}
              <span {...stylex.props(styles.count)}>
                {lookup.get(author.id)?.toLocaleString() ?? (counts ? "0" : "…")}
              </span>
            </span>
            <CountBar count={lookup.get(author.id)} max={max} />
          </span>
          <select
            {...stylex.props(ui.focus, styles.select, selected.has(author.id) && styles.selected)}
            aria-label={`Filter author ${author.name}`}
            value={
              draft.excludeAuthorIds.includes(author.id)
                ? "exclude"
                : draft.includeAuthorIds.includes(author.id)
                  ? "include"
                  : "any"
            }
            onChange={(event) => {
              setTouched((ids) => (ids.includes(author.id) ? ids : [...ids, author.id]));
              onChange({
                ...draft,
                includeAuthorIds: [
                  ...draft.includeAuthorIds.filter((id) => id !== author.id),
                  ...(event.target.value === "include" ? [author.id] : []),
                ],
                excludeAuthorIds: [
                  ...draft.excludeAuthorIds.filter((id) => id !== author.id),
                  ...(event.target.value === "exclude" ? [author.id] : []),
                ],
              });
            }}
          >
            <option value="any">Any</option>
            <option value="include">Include</option>
            <option value="exclude">Exclude</option>
          </select>
        </label>
      ))}
      {candidates.length > visibleLimit || !candidates.length ? (
        <p {...stylex.props(styles.description)}>
          {candidates.length > visibleLimit
            ? `${candidates.length - visibleLimit} more authors. Refine your search.`
            : "No further authors match your search."}
        </p>
      ) : null}
    </fieldset>
  );
}

export function YearFilters({
  metadata,
  draft,
  onChange,
  bins,
  disabled,
}: FacetProps & { bins?: { from: number; to: number; count: number }[]; disabled?: boolean }) {
  const { min, max, undatedGuidelines } = metadata.years;
  if (min === null || max === null) return null;
  const from = draft.yearFrom ?? min;
  const to = draft.yearTo ?? max;
  const maxCount = Math.max(1, ...(bins?.map((bin) => bin.count) ?? []));
  return (
    <fieldset {...stylex.props(styles.section)}>
      <legend {...stylex.props(styles.legend)}>Publication year</legend>
      <p {...stylex.props(styles.note)}>Drag the range handles or enter exact years.</p>
      <div
        {...stylex.props(styles.histogram)}
        role="img"
        aria-label="Guidelines by publication year, with the other filters applied"
      >
        {bins?.map((bin) => (
          <span
            key={bin.from}
            title={`${bin.from === bin.to ? bin.from : `${bin.from}–${bin.to}`}: ${bin.count} guidelines`}
            {...stylex.props(styles.histogramColumn)}
          >
            <span
              {...stylex.props(
                styles.histogramBar,
                styles.barHeight(bin.count / maxCount),
                bin.to < from || bin.from > to ? styles.dimmedBar : styles.selectedBar,
              )}
            />
          </span>
        ))}
      </div>
      {min < max ? (
        <Slider.Root
          {...stylex.props(styles.slider)}
          min={min}
          max={max}
          step={1}
          disabled={disabled}
          minStepsBetweenThumbs={0}
          value={[Math.max(min, Math.min(max, from)), Math.max(min, Math.min(max, to))].sort(
            (a, b) => a - b,
          )}
          onValueChange={([start, end]) =>
            onChange({
              ...draft,
              yearFrom: start === min ? null : start!,
              yearTo: end === max ? null : end!,
            })
          }
        >
          <Slider.Track {...stylex.props(styles.sliderTrack)}>
            <Slider.Range {...stylex.props(styles.sliderRange)} />
          </Slider.Track>
          <Slider.Thumb
            {...stylex.props(ui.focus, styles.sliderThumb)}
            aria-label="Earliest publication year"
          />
          <Slider.Thumb
            {...stylex.props(ui.focus, styles.sliderThumb)}
            aria-label="Latest publication year"
          />
        </Slider.Root>
      ) : null}
      <div {...stylex.props(styles.axis)} aria-hidden="true">
        <span>{min}</span>
        <span>{max}</span>
      </div>
      <div {...stylex.props(styles.years)}>
        {(["yearFrom", "yearTo"] as const).map((field) => (
          <label key={field} {...stylex.props(styles.yearLabel)}>
            {field === "yearFrom" ? "From" : "Through"}
            <input
              {...stylex.props(ui.focus, styles.input)}
              type="number"
              inputMode="numeric"
              step={1}
              min={min}
              max={max}
              placeholder={String(field === "yearFrom" ? min : max)}
              value={draft[field] ?? ""}
              onChange={(event) =>
                onChange({
                  ...draft,
                  [field]: event.target.value === "" ? null : Number(event.target.value),
                })
              }
            />
          </label>
        ))}
      </div>
      {undatedGuidelines > 0 ? (
        <p {...stylex.props(styles.description)}>
          {undatedGuidelines.toLocaleString()}{" "}
          {undatedGuidelines === 1 ? "guideline has" : "guidelines have"} no dated source. A year
          range requires a dated source.
        </p>
      ) : null}
    </fieldset>
  );
}

export function SourceFilters({
  metadata,
  draft,
  onChange,
  counts,
}: FacetProps & { counts?: Counts }) {
  const lookup = new Map(counts?.map(({ id, count }) => [id, count]));
  const max = Math.max(1, ...Array.from(lookup.values()));
  return (
    <fieldset {...stylex.props(styles.section)}>
      <legend {...stylex.props(styles.legend)}>Source type</legend>
      <p {...stylex.props(styles.note)}>Select any combination. Leave clear for every type.</p>
      <div {...stylex.props(styles.sourceGrid)}>
        {metadata.sourceTypes.map((type) => (
          <label key={type.id} {...stylex.props(styles.source)}>
            <input
              {...stylex.props(ui.focus, styles.checkbox)}
              type="checkbox"
              aria-label={`Source type ${type.name}`}
              checked={draft.sourceTypeIds.includes(type.id)}
              onChange={(event) =>
                onChange({
                  ...draft,
                  sourceTypeIds: event.target.checked
                    ? [...draft.sourceTypeIds, type.id]
                    : draft.sourceTypeIds.filter((id) => id !== type.id),
                })
              }
            />
            <span {...stylex.props(styles.facetLabel)}>
              <span {...stylex.props(styles.name)}>
                {type.name}
                <span {...stylex.props(styles.count)}>
                  {lookup.get(type.id)?.toLocaleString() ?? (counts ? "0" : "…")}
                </span>
              </span>
              <CountBar count={lookup.get(type.id)} max={max} />
            </span>
          </label>
        ))}
      </div>
    </fieldset>
  );
}
