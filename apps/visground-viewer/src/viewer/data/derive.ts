import type {
  MatrixAxisValue,
  MatrixCell,
  MatrixRow,
  ViewerLayoutControl,
  ViewerLayoutSelection,
  ViewerSelection,
  ViewerStatePayload,
  ViewerToolbarPill,
} from "../contract/types";
import {
  viewerAxisDimensions,
  viewerDefaultSelection,
  viewerDimensions,
  viewerFilterDimensions,
  type ViewerDimensionSpec,
} from "./runtime-config";
import type { ViewerArtifactRow } from "./parquet";

const MISSING = Symbol("missing");

type Registry = {
  visIds: string[];
  dimensionValues: Record<string, Array<string | null>>;
};

type RuntimeContext = {
  records: ViewerArtifactRow[];
  registry: Registry;
  catalog: ViewerStatePayload["catalog"];
};

function getRecordValue(record: ViewerArtifactRow, dimension: string): string | null {
  const candidate = record as Record<string, unknown>;
  const value = candidate[dimension];
  return typeof value === "string" || value === null ? value : null;
}

function dimensionMap(): Record<string, ViewerDimensionSpec> {
  return Object.fromEntries(viewerDimensions.map((dimension) => [dimension.id, dimension]));
}

function displayLabel(dimension: string | null, value: string | null) {
  if (dimension === null) {
    return String(value ?? "");
  }
  const spec = dimensionMap()[dimension];
  if (!spec) return String(value ?? "");
  if (value === null) {
    return spec.nullLabel ?? "None";
  }
  return spec.aliases?.[value] ?? value;
}

function labelForDimension(dimension: string | null) {
  if (dimension === null) return "";
  return dimensionMap()[dimension]?.label ?? dimension;
}

function values(records: ViewerArtifactRow[], dimension: string): Array<string | null> {
  const spec = dimensionMap()[dimension];
  const order = spec?.order ?? {};
  const seen = new Set<string>();
  const collected: Array<string | null> = [];

  for (const record of records) {
    const value = getRecordValue(record, dimension);
    const key = value === null ? "__none__" : value;
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

function nonNullValues(records: ViewerArtifactRow[], dimension: string): string[] {
  return values(records, dimension).filter((value): value is string => value !== null);
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

function discoverRegistry(records: ViewerArtifactRow[]): Registry {
  return {
    visIds: nonNullValues(records, "vis_id"),
    dimensionValues: Object.fromEntries(
      viewerDimensions.map((dimension) => [dimension.id, values(records, dimension.id)]),
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

function applyDimensionFilters(
  records: ViewerArtifactRow[],
  filters: Record<string, string | null>,
): ViewerArtifactRow[] {
  return records.filter((record) => {
    return Object.entries(filters).every(([dimension, value]) => {
      const spec = dimensionMap()[dimension];
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

function normalizeLayout(
  requested: Partial<ViewerLayoutSelection>,
  axisDimensions: readonly string[],
  preferred: ViewerLayoutSelection,
): ViewerLayoutSelection {
  const rowDimension = chooseRequestedValue<string>(
    requested.row_dimension ?? MISSING,
    axisDimensions,
    preferred.row_dimension,
  );
  const columnCandidates = axisDimensions.filter((dimension) => dimension !== rowDimension);
  const columnDimension = chooseRequestedValue<string>(
    requested.column_dimension ?? MISSING,
    columnCandidates,
    preferred.column_dimension,
  );
  const groupCandidates = [
    null,
    ...axisDimensions.filter((dimension) => ![rowDimension, columnDimension].includes(dimension)),
  ] as const;
  const groupDimension = chooseRequestedValue<string | null>(
    requested.group_dimension ?? MISSING,
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
  normalizedFilters: Record<string, string | null>,
) {
  return viewerFilterDimensions.flatMap((dimensionId) => {
    const options = values(caseRecords, dimensionId);
    if (options.length <= 1) return [];
    return [
      {
        id: dimensionId,
        label: labelForDimension(dimensionId),
        value: normalizedFilters[dimensionId] ?? null,
        options: options.map((option) => ({
          value: option,
          label: displayLabel(dimensionId, option),
        })),
      },
    ];
  });
}

function buildLayoutControls(layout: ViewerLayoutSelection): ViewerLayoutControl[] {
  const rowDimension = layout.row_dimension;
  const columnDimension = layout.column_dimension;
  const groupDimension = layout.group_dimension;
  const axisDimensions = [...viewerAxisDimensions];
  return [
    {
      id: "row_dimension",
      label: "Rows",
      value: rowDimension,
      options: axisDimensions
        .filter((dimension) => ![columnDimension, groupDimension].includes(dimension))
        .map((dimension) => ({ value: dimension, label: labelForDimension(dimension) })),
    },
    {
      id: "column_dimension",
      label: "Columns",
      value: columnDimension,
      options: axisDimensions
        .filter((dimension) => ![rowDimension, groupDimension].includes(dimension))
        .map((dimension) => ({ value: dimension, label: labelForDimension(dimension) })),
    },
    {
      id: "group_dimension",
      label: "Groups",
      value: groupDimension,
      options: [
        { value: null, label: "No grouping" },
        ...axisDimensions
          .filter((dimension) => ![rowDimension, columnDimension].includes(dimension))
          .map((dimension) => ({ value: dimension, label: labelForDimension(dimension) })),
      ],
    },
  ];
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
  return value === null ? "__none__" : value;
}

function cellKey(groupValue: string | null, rowValue: string | null, columnValue: string | null) {
  return `${schemaValueKey(groupValue)}::${schemaValueKey(rowValue)}::${schemaValueKey(columnValue)}`;
}

function dimensionSortKey(dimensionId: string, value: string | null) {
  const spec = dimensionMap()[dimensionId];
  if (value === null) {
    return [0, -1, ""] as const;
  }
  if (!spec) {
    return [1, 999, value] as const;
  }
  return [1, spec.order?.[value] ?? 999, displayLabel(dimensionId, value)] as const;
}

function variantLabel(record: ViewerArtifactRow, hiddenAxes: readonly string[]) {
  const parts = hiddenAxes.map(
    (dimensionId) =>
      `${labelForDimension(dimensionId)}: ${displayLabel(dimensionId, getRecordValue(record, dimensionId))}`,
  );
  return parts.length ? parts.join(" · ") : null;
}

function serializeCellVariants(records: ViewerArtifactRow[], hiddenAxes: readonly string[]) {
  const ordered = [...records].sort((left, right) => {
    const leftScore = left.overall_score ?? Number.NEGATIVE_INFINITY;
    const rightScore = right.overall_score ?? Number.NEGATIVE_INFINITY;
    if (leftScore !== rightScore) return rightScore - leftScore;
    for (const dimensionId of hiddenAxes) {
      const leftKey = dimensionSortKey(dimensionId, getRecordValue(left, dimensionId));
      const rightKey = dimensionSortKey(dimensionId, getRecordValue(right, dimensionId));
      if (leftKey[0] !== rightKey[0]) return leftKey[0] - rightKey[0];
      if (leftKey[1] !== rightKey[1]) return leftKey[1] - rightKey[1];
      if (leftKey[2] !== rightKey[2]) return leftKey[2].localeCompare(rightKey[2]);
    }
    return left.visgen_id.localeCompare(right.visgen_id);
  });

  const baseLabels = ordered.map((record) => variantLabel(record, hiddenAxes));
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
  records: ViewerArtifactRow[],
  groupDimension: string | null,
  groupValue: string | null,
  hiddenAxes: readonly string[],
  rowDimension: string,
  rowValue: string | null,
  columnDimension: string,
  columnValue: string | null,
): MatrixCell {
  const variants = serializeCellVariants(records, hiddenAxes);
  return {
    cell_key: cellKey(groupValue, rowValue, columnValue),
    group_value: groupValue,
    group_label: groupDimension ? displayLabel(groupDimension, groupValue) : null,
    row_value: rowValue,
    row_label: displayLabel(rowDimension, rowValue),
    column_value: columnValue,
    column_label: displayLabel(columnDimension, columnValue),
    hidden_axes: [...hiddenAxes],
    hidden_axis_labels: hiddenAxes.map((dimensionId) => labelForDimension(dimensionId)),
    variant_count: variants.length,
    missing: records.length === 0,
    placeholder_reason: records.length === 0 ? "missing candidate" : null,
    variants,
  };
}

function buildOverviewMatrix(scopedRecords: ViewerArtifactRow[], layout: ViewerLayoutSelection) {
  const groupDimension = layout.group_dimension;
  const rowDimension = layout.row_dimension;
  const columnDimension = layout.column_dimension;
  const hiddenAxes = viewerAxisDimensions.filter(
    (dimensionId) => ![rowDimension, columnDimension, groupDimension].includes(dimensionId),
  );

  const rowValues = values(scopedRecords, rowDimension);
  const columnValues = values(scopedRecords, columnDimension);

  if (groupDimension !== null) {
    const groupValues = values(scopedRecords, groupDimension);
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
          label: displayLabel(rowDimension, rowValue),
          ...axisValueMeta(scopedRecords, rowDimension, rowValue),
          cells,
        } satisfies MatrixRow;
      });

      return {
        value: groupValue,
        label: displayLabel(groupDimension, groupValue),
        ...axisValueMeta(scopedRecords, groupDimension, groupValue),
        columns: columnValues.map(
          (columnValue) =>
            ({
              value: columnValue,
              label: displayLabel(columnDimension, columnValue),
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
        label: displayLabel(rowDimension, rowValue),
        ...axisValueMeta(scopedRecords, rowDimension, rowValue),
        cells: columnValues.map((columnValue) => {
          const bucket = scopedRecords.filter(
            (record) =>
              getRecordValue(record, rowDimension) === rowValue &&
              getRecordValue(record, columnDimension) === columnValue,
          );
          return matrixCellPayload(
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
          label: displayLabel(columnDimension, columnValue),
          ...axisValueMeta(scopedRecords, columnDimension, columnValue),
        }) satisfies MatrixAxisValue,
    ),
    rows,
  };
}

export function createViewerRuntime(records: ViewerArtifactRow[]): RuntimeContext {
  const registry = discoverRegistry(records);
  return {
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
    requestedSelection.vis_id ?? MISSING,
    runtime.registry.visIds,
    runtime.records[0]?.vis_id ?? runtime.registry.visIds[0],
  );
  const caseRecords = runtime.records.filter((record) => record.vis_id === visId);

  const normalizedFilters = Object.fromEntries(
    viewerFilterDimensions.map((dimensionId) => {
      const options = values(caseRecords, dimensionId);
      return [
        dimensionId,
        chooseRequestedValue<string | null>(
          requestedSelection.filters?.[dimensionId] ?? MISSING,
          options,
          viewerDefaultSelection.filters[dimensionId],
        ),
      ];
    }),
  ) as Record<string, string | null>;

  const scopedRecords = applyDimensionFilters(caseRecords, normalizedFilters);
  const layout = normalizeLayout(
    requestedSelection.layout ?? {},
    viewerAxisDimensions,
    viewerDefaultSelection.layout,
  );
  const filterControls = buildFilterControls(caseRecords, normalizedFilters);
  const layoutControls = buildLayoutControls(layout);

  const selection: ViewerSelection = {
    vis_id: visId,
    filters: normalizedFilters,
    layout,
  };

  const hiddenLabels = viewerAxisDimensions
    .filter(
      (dimensionId) =>
        ![layout.row_dimension, layout.column_dimension, layout.group_dimension].includes(
          dimensionId,
        ),
    )
    .map((dimensionId) => labelForDimension(dimensionId));

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
        label: caseRecords.find((record) => record.query)?.query ?? visId,
        ui_schema: {
          toolbar: {
            pills: toolbarPills,
          },
          filters: filterControls,
          layout_controls: layoutControls,
          matrix_axes: {
            group_label: layout.group_dimension ? labelForDimension(layout.group_dimension) : null,
            row_label: labelForDimension(layout.row_dimension),
            column_label: labelForDimension(layout.column_dimension),
            hidden_labels: hiddenLabels,
          },
        },
        matrix: buildOverviewMatrix(scopedRecords, layout),
      },
      error: null,
    },
  };
}
