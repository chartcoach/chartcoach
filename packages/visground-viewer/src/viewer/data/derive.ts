import type {
  MatrixAxisValue,
  MatrixCell,
  MatrixRow,
  ViewerFilterControl,
  ViewerLayoutControl,
  ViewerLayoutSelection,
  ViewerRuntimeConfig,
  ViewerSelection,
  ViewerStatePayload,
  ViewerToolbarPill,
} from "../contract/types";
import { dimensionMap, displayLabel, labelForDimension } from "./runtime-config";
import type { ViewerArtifactRow } from "./parquet";

const MISSING = Symbol("missing");

type Registry = {
  visIds: string[];
  dimensionValues: Record<string, Array<string | null>>;
};

type RuntimeContext = {
  config: ViewerRuntimeConfig;
  records: ViewerArtifactRow[];
  registry: Registry;
  catalog: ViewerStatePayload["catalog"];
};

function hasOwn<K extends PropertyKey>(value: object, key: K): value is Record<K, unknown> {
  return Object.prototype.hasOwnProperty.call(value, key);
}

function getRecordValue(record: ViewerArtifactRow, dimension: string): string | null {
  if (dimension === "vis_id") {
    return record.vis_id;
  }
  if (!hasOwn(record.dimension_values, dimension)) {
    throw new Error(
      `Viewer artifact row ${record.visgen_id} is missing configured dimension '${dimension}'.`,
    );
  }
  const value = record.dimension_values[dimension];
  if (value !== null && typeof value !== "string") {
    throw new Error(
      `Viewer artifact row ${record.visgen_id} has invalid value for dimension '${dimension}'.`,
    );
  }
  return value;
}

function assertConfiguredDimensionsExist(
  records: ViewerArtifactRow[],
  config: ViewerRuntimeConfig,
) {
  for (const record of records) {
    const missing = config.dimensions
      .map((dimension) => dimension.id)
      .filter((dimensionId) => !hasOwn(record.dimension_values, dimensionId));
    if (missing.length) {
      throw new Error(
        `Viewer artifact row ${record.visgen_id} is missing configured dimensions: ${missing.join(", ")}.`,
      );
    }
  }
}

function values(
  records: ViewerArtifactRow[],
  config: ViewerRuntimeConfig,
  dimension: string,
): Array<string | null> {
  const spec = dimensionMap(config)[dimension];
  const order = spec?.order ?? {};
  const seen = new Set<string>();
  const collected: Array<string | null> = [];

  for (const record of records) {
    const value = getRecordValue(record, dimension);
    const key = JSON.stringify(value);
    if (seen.has(key)) continue;
    seen.add(key);
    collected.push(value);
  }

  if (!Object.keys(order).length) {
    return collected;
  }

  const nonNull = collected.filter((value): value is string => value !== null);
  nonNull.sort((left, right) => {
    const leftOrder = order[left] ?? 999;
    const rightOrder = order[right] ?? 999;
    if (leftOrder !== rightOrder) return leftOrder - rightOrder;
    return left.localeCompare(right);
  });
  return collected.includes(null) ? [null, ...nonNull] : nonNull;
}

function nonNullValues(
  records: ViewerArtifactRow[],
  config: ViewerRuntimeConfig,
  dimension: string,
): string[] {
  return values(records, config, dimension).filter((value): value is string => value !== null);
}

function chooseRequestedValue<T>(
  requested: T | typeof MISSING,
  options: readonly T[],
  preferred?: T,
) {
  if (!options.length) {
    throw new Error("Viewer selection has no valid options.");
  }
  if (requested === MISSING) {
    return preferred !== undefined && options.includes(preferred) ? preferred : options[0];
  }
  if (options.includes(requested as T)) {
    return requested as T;
  }
  if (preferred !== undefined && options.includes(preferred)) {
    return preferred;
  }
  return options[0];
}

function discoverRegistry(records: ViewerArtifactRow[], config: ViewerRuntimeConfig): Registry {
  return {
    visIds: nonNullValues(records, config, "vis_id"),
    dimensionValues: Object.fromEntries(
      config.dimensions.map((dimension) => [dimension.id, values(records, config, dimension.id)]),
    ),
  };
}

function buildCatalog(records: ViewerArtifactRow[], visIds: string[]) {
  return visIds.map((visId) => {
    const caseRecords = records.filter((record) => record.vis_id === visId);
    const label = caseRecords.find((record) => record.query)?.query ?? visId;
    const searchText = Array.from(
      new Set(caseRecords.flatMap((record) => [record.vis_id, record.search_text].filter(Boolean))),
    ).join(" ");
    return {
      vis_id: visId,
      label,
      search_text: searchText,
    };
  });
}

function firstQuery(records: ViewerArtifactRow[]): string | null {
  for (const record of records) {
    const query = record.query.trim();
    if (query) {
      return query;
    }
  }
  return null;
}

function applyDimensionFilters(
  records: ViewerArtifactRow[],
  config: ViewerRuntimeConfig,
  filters: Record<string, string | null>,
): ViewerArtifactRow[] {
  return records.filter((record) => {
    return Object.entries(filters).every(([dimension, value]) => {
      const spec = dimensionMap(config)[dimension];
      if (value === null) {
        if (spec?.noneValueMode === "all") {
          return true;
        }
        return getRecordValue(record, dimension) === null;
      }
      return getRecordValue(record, dimension) === value;
    });
  });
}

function requestedField<T extends object, K extends keyof T>(
  value: T | null | undefined,
  key: K,
): Exclude<T[K], undefined> | typeof MISSING {
  if (!value || !hasOwn(value, key)) {
    return MISSING;
  }
  const candidate = value[key];
  return candidate === undefined ? MISSING : (candidate as Exclude<T[K], undefined>);
}

function normalizeLayout(
  requested: Partial<ViewerLayoutSelection>,
  axisDimensions: readonly string[],
  preferred: ViewerLayoutSelection,
): ViewerLayoutSelection {
  const rowDimension = chooseRequestedValue<string>(
    requestedField(requested, "row_dimension"),
    axisDimensions,
    preferred.row_dimension,
  );
  const columnCandidates = axisDimensions.filter((dimension) => dimension !== rowDimension);
  const columnDimension = chooseRequestedValue<string>(
    requestedField(requested, "column_dimension"),
    columnCandidates,
    preferred.column_dimension,
  );
  const groupCandidates = [
    null,
    ...axisDimensions.filter((dimension) => ![rowDimension, columnDimension].includes(dimension)),
  ] as const;
  const groupDimension = chooseRequestedValue<string | null>(
    requestedField(requested, "group_dimension"),
    groupCandidates,
    preferred.group_dimension,
  );

  return {
    row_dimension: rowDimension,
    column_dimension: columnDimension,
    group_dimension: groupDimension,
  };
}

function buildFilterControls(
  caseRecords: ViewerArtifactRow[],
  config: ViewerRuntimeConfig,
  normalizedFilters: Record<string, string | null>,
): ViewerFilterControl[] {
  return config.filter_dimensions.flatMap((dimensionId) => {
    const peerFilters = Object.fromEntries(
      Object.entries(normalizedFilters).filter(([candidateId]) => candidateId !== dimensionId),
    );
    const options = values(
      applyDimensionFilters(caseRecords, config, peerFilters),
      config,
      dimensionId,
    );
    if (options.length <= 1) {
      return [];
    }
    return [
      {
        id: dimensionId,
        label: labelForDimension(config, dimensionId),
        value: normalizedFilters[dimensionId] ?? null,
        options: options.map((option) => ({
          value: option,
          label: displayLabel(config, dimensionId, option),
        })),
      },
    ];
  });
}

function buildLayoutControls(
  config: ViewerRuntimeConfig,
  layout: ViewerLayoutSelection,
): ViewerLayoutControl[] {
  const rowDimension = layout.row_dimension;
  const columnDimension = layout.column_dimension;
  const groupDimension = layout.group_dimension;
  const axisDimensions = [...config.axis_dimensions];
  const controls: ViewerLayoutControl[] = [
    {
      id: "row_dimension",
      label: "Rows",
      value: rowDimension,
      options: axisDimensions
        .filter((dimension) => ![columnDimension, groupDimension].includes(dimension))
        .map((dimension) => ({ value: dimension, label: labelForDimension(config, dimension) })),
    },
    {
      id: "column_dimension",
      label: "Columns",
      value: columnDimension,
      options: axisDimensions
        .filter((dimension) => ![rowDimension, groupDimension].includes(dimension))
        .map((dimension) => ({ value: dimension, label: labelForDimension(config, dimension) })),
    },
    {
      id: "group_dimension",
      label: "Groups",
      value: groupDimension,
      options: [
        { value: null, label: "No grouping" },
        ...axisDimensions
          .filter((dimension) => ![rowDimension, columnDimension].includes(dimension))
          .map((dimension) => ({ value: dimension, label: labelForDimension(config, dimension) })),
      ],
    },
  ];

  return controls.filter((control) => control.options.length > 1);
}

function axisValueMeta(records: ViewerArtifactRow[], dimensionId: string, value: string | null) {
  if (dimensionId !== "grounding_mode") {
    return { meta_label: null, meta_kind: null };
  }
  const scoped = records.filter((record) => getRecordValue(record, dimensionId) === value);
  const guidelineIds = new Set(
    scoped.flatMap((record) => record.candidate.guideline_details.map((detail) => detail.id)),
  );
  const count = guidelineIds.size;
  if (!count) {
    return { meta_label: null, meta_kind: null };
  }
  return {
    meta_label: `${count} guideline${count === 1 ? "" : "s"}`,
    meta_kind: "guidelines" as const,
  };
}

function schemaValueKey(value: string | null) {
  return value;
}

function cellKey(groupValue: string | null, rowValue: string | null, columnValue: string | null) {
  return JSON.stringify([
    schemaValueKey(groupValue),
    schemaValueKey(rowValue),
    schemaValueKey(columnValue),
  ]);
}

function dimensionSortKey(config: ViewerRuntimeConfig, dimensionId: string, value: string | null) {
  const spec = dimensionMap(config)[dimensionId];
  if (value === null) {
    return [0, -1, ""] as const;
  }
  if (!spec) {
    return [1, 999, value] as const;
  }
  return [1, spec.order?.[value] ?? 999, displayLabel(config, dimensionId, value)] as const;
}

function variantLabel(
  config: ViewerRuntimeConfig,
  record: ViewerArtifactRow,
  hiddenAxes: readonly string[],
) {
  const parts = hiddenAxes.map(
    (dimensionId) =>
      `${labelForDimension(config, dimensionId)}: ${displayLabel(config, dimensionId, getRecordValue(record, dimensionId))}`,
  );
  return parts.length ? parts.join(" · ") : null;
}

function serializeCellVariants(
  config: ViewerRuntimeConfig,
  records: ViewerArtifactRow[],
  hiddenAxes: readonly string[],
) {
  const ordered = [...records].sort((left, right) => {
    const leftScore = left.overall_score ?? Number.NEGATIVE_INFINITY;
    const rightScore = right.overall_score ?? Number.NEGATIVE_INFINITY;
    if (leftScore !== rightScore) return rightScore - leftScore;
    for (const dimensionId of hiddenAxes) {
      const leftKey = dimensionSortKey(config, dimensionId, getRecordValue(left, dimensionId));
      const rightKey = dimensionSortKey(config, dimensionId, getRecordValue(right, dimensionId));
      if (leftKey[0] !== rightKey[0]) return leftKey[0] - rightKey[0];
      if (leftKey[1] !== rightKey[1]) return leftKey[1] - rightKey[1];
      if (leftKey[2] !== rightKey[2]) return leftKey[2].localeCompare(rightKey[2]);
    }
    return left.visgen_id.localeCompare(right.visgen_id);
  });

  const baseLabels = ordered.map((record) => variantLabel(config, record, hiddenAxes));
  const counts = new Map<string | null, number>();
  for (const label of baseLabels) counts.set(label, (counts.get(label) ?? 0) + 1);
  const seen = new Map<string | null, number>();

  return ordered.map((record, index) => {
    const baseLabel = baseLabels[index];
    const nextCount = (seen.get(baseLabel) ?? 0) + 1;
    seen.set(baseLabel, nextCount);
    let label = baseLabel;
    if ((counts.get(baseLabel) ?? 0) > 1) {
      const suffix = `#${nextCount}`;
      label = baseLabel ? `${baseLabel} · ${suffix}` : suffix;
    }
    return {
      variant_key: record.visgen_id,
      variant_label: label,
      candidate: record.candidate,
    };
  });
}

function matrixCellPayload(
  config: ViewerRuntimeConfig,
  records: ViewerArtifactRow[],
  groupDimension: string | null,
  groupValue: string | null,
  hiddenAxes: readonly string[],
  rowDimension: string,
  rowValue: string | null,
  columnDimension: string,
  columnValue: string | null,
): MatrixCell {
  const variants = serializeCellVariants(config, records, hiddenAxes);
  return {
    cell_key: cellKey(groupValue, rowValue, columnValue),
    group_value: groupValue,
    group_label: groupDimension ? displayLabel(config, groupDimension, groupValue) : null,
    row_value: rowValue,
    row_label: displayLabel(config, rowDimension, rowValue),
    column_value: columnValue,
    column_label: displayLabel(config, columnDimension, columnValue),
    hidden_axes: [...hiddenAxes],
    hidden_axis_labels: hiddenAxes.map((dimensionId) => labelForDimension(config, dimensionId)),
    variant_count: variants.length,
    missing: records.length === 0,
    placeholder_reason: records.length === 0 ? "missing candidate" : null,
    variants,
  };
}

function buildOverviewMatrix(
  scopedRecords: ViewerArtifactRow[],
  config: ViewerRuntimeConfig,
  layout: ViewerLayoutSelection,
) {
  const groupDimension = layout.group_dimension;
  const rowDimension = layout.row_dimension;
  const columnDimension = layout.column_dimension;
  const hiddenAxes = config.axis_dimensions.filter(
    (dimensionId) => ![rowDimension, columnDimension, groupDimension].includes(dimensionId),
  );

  const rowValues = values(scopedRecords, config, rowDimension);
  const columnValues = values(scopedRecords, config, columnDimension);

  if (groupDimension !== null) {
    const groupValues = values(scopedRecords, config, groupDimension);
    const groups = groupValues.map((groupValue) => {
      const rows = rowValues.map((rowValue) => {
        const cells = columnValues.map((columnValue) => {
          const bucket = scopedRecords.filter(
            (record) =>
              getRecordValue(record, groupDimension) === groupValue &&
              getRecordValue(record, rowDimension) === rowValue &&
              getRecordValue(record, columnDimension) === columnValue,
          );
          return matrixCellPayload(
            config,
            bucket,
            groupDimension,
            groupValue,
            hiddenAxes,
            rowDimension,
            rowValue,
            columnDimension,
            columnValue,
          );
        });
        return {
          value: rowValue,
          label: displayLabel(config, rowDimension, rowValue),
          ...axisValueMeta(scopedRecords, rowDimension, rowValue),
          cells,
        } satisfies MatrixRow;
      });

      return {
        value: groupValue,
        label: displayLabel(config, groupDimension, groupValue),
        ...axisValueMeta(scopedRecords, groupDimension, groupValue),
        columns: columnValues.map(
          (columnValue) =>
            ({
              value: columnValue,
              label: displayLabel(config, columnDimension, columnValue),
              ...axisValueMeta(scopedRecords, columnDimension, columnValue),
            }) satisfies MatrixAxisValue,
        ),
        rows,
      };
    });

    return { kind: "grouped" as const, groups };
  }

  const rows = rowValues.map(
    (rowValue) =>
      ({
        value: rowValue,
        label: displayLabel(config, rowDimension, rowValue),
        ...axisValueMeta(scopedRecords, rowDimension, rowValue),
        cells: columnValues.map((columnValue) => {
          const bucket = scopedRecords.filter(
            (record) =>
              getRecordValue(record, rowDimension) === rowValue &&
              getRecordValue(record, columnDimension) === columnValue,
          );
          return matrixCellPayload(
            config,
            bucket,
            null,
            null,
            hiddenAxes,
            rowDimension,
            rowValue,
            columnDimension,
            columnValue,
          );
        }),
      }) satisfies MatrixRow,
  );

  return {
    kind: "flat" as const,
    columns: columnValues.map(
      (columnValue) =>
        ({
          value: columnValue,
          label: displayLabel(config, columnDimension, columnValue),
          ...axisValueMeta(scopedRecords, columnDimension, columnValue),
        }) satisfies MatrixAxisValue,
    ),
    rows,
  };
}

export function createViewerRuntime(
  records: ViewerArtifactRow[],
  config: ViewerRuntimeConfig,
): RuntimeContext {
  assertConfiguredDimensionsExist(records, config);
  const registry = discoverRegistry(records, config);
  return {
    config,
    records,
    registry,
    catalog: buildCatalog(records, registry.visIds),
  };
}

export function deriveViewerState(
  runtime: RuntimeContext,
  requested: Partial<ViewerSelection> | null | undefined,
): { selection: ViewerSelection; state: ViewerStatePayload } {
  const requestedSelection = requested ?? {};
  const visId = chooseRequestedValue(
    requestedField(requestedSelection, "vis_id"),
    runtime.registry.visIds,
    runtime.records[0]?.vis_id ?? runtime.registry.visIds[0],
  );
  const caseRecords = runtime.records.filter((record) => record.vis_id === visId);

  const normalizedFilters = Object.fromEntries(
    runtime.config.filter_dimensions.map((dimensionId) => {
      const options = values(caseRecords, runtime.config, dimensionId);
      return [
        dimensionId,
        chooseRequestedValue<string | null>(
          requestedField(requestedSelection.filters, dimensionId),
          options,
          runtime.config.default_filters[dimensionId],
        ),
      ];
    }),
  ) as Record<string, string | null>;

  const scopedRecords = applyDimensionFilters(caseRecords, runtime.config, normalizedFilters);
  const layout = normalizeLayout(
    requestedSelection.layout ?? {},
    runtime.config.axis_dimensions,
    runtime.config.default_layout,
  );
  const filterControls = buildFilterControls(caseRecords, runtime.config, normalizedFilters);
  const layoutControls = buildLayoutControls(runtime.config, layout);

  const selection: ViewerSelection = {
    vis_id: visId as string,
    filters: normalizedFilters,
    layout,
  };

  const hiddenLabels = runtime.config.axis_dimensions
    .filter(
      (dimensionId) =>
        ![layout.row_dimension, layout.column_dimension, layout.group_dimension].includes(
          dimensionId,
        ),
    )
    .map((dimensionId) => labelForDimension(runtime.config, dimensionId));

  const toolbarPills: ViewerToolbarPill[] = [];
  if (filterControls.length) {
    toolbarPills.push({ id: "filters", label: "Filters" });
  }
  if (layoutControls.length) {
    toolbarPills.push({ id: "layout", label: "Layout" });
  }

  return {
    selection,
    state: {
      catalog: runtime.catalog,
      overview: {
        label: (firstQuery(scopedRecords) ?? firstQuery(caseRecords) ?? visId) as string,
        ui_schema: {
          toolbar: {
            pills: toolbarPills,
          },
          filters: filterControls,
          layout_controls: layoutControls,
          matrix_axes: {
            group_label: layout.group_dimension
              ? labelForDimension(runtime.config, layout.group_dimension)
              : null,
            row_label: labelForDimension(runtime.config, layout.row_dimension),
            column_label: labelForDimension(runtime.config, layout.column_dimension),
            hidden_labels: hiddenLabels,
          },
        },
        matrix: buildOverviewMatrix(scopedRecords, runtime.config, layout),
      },
      error: null,
    },
  };
}
