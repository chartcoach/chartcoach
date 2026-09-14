import * as stylex from "@stylexjs/stylex";
import type { CatalogFilters, CatalogMetadata } from "../../shared/catalog-filters";
import { ui } from "../ui/ui";
import { styles } from "./filters.styles";
import { YearRange } from "./year-range";

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

  const updateRange = (start: number, end: number) =>
    onChange({
      ...draft,
      yearFrom: start === min ? null : start,
      yearTo: end === max ? null : end,
    });

  return (
    <fieldset {...stylex.props(styles.section)}>
      <legend {...stylex.props(styles.legend)}>Publication year</legend>
      <p {...stylex.props(styles.note)}>Drag the range or its handles, or enter exact years.</p>
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
                styles.barScaleY(bin.count / maxCount),
                bin.to < from || bin.from > to ? styles.dimmedBar : styles.selectedBar,
              )}
            />
          </span>
        ))}
      </div>
      {min < max ? (
        <YearRange
          min={min}
          max={max}
          disabled={disabled}
          from={from}
          to={to}
          onChange={updateRange}
        />
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
              name={field}
              autoComplete="off"
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
