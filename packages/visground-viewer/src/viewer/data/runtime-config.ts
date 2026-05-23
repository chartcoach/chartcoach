import type {
  ViewerDimensionSpec,
  ViewerLayoutSelection,
  ViewerRuntimeConfig,
} from "../contract/types";

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function ensureString(value: unknown, label: string): string {
  if (typeof value !== "string" || value.length === 0) {
    throw new Error(`${label} must be a non-empty string.`);
  }
  return value;
}

function normalizeAliases(value: unknown, label: string): Record<string, string> | undefined {
  if (value === undefined) {
    return undefined;
  }
  if (!isRecord(value)) {
    throw new Error(`${label} must be an object.`);
  }
  return Object.fromEntries(
    Object.entries(value).map(([key, aliasValue]) => [
      key,
      ensureString(aliasValue, `${label}.${key}`),
    ]),
  );
}

function normalizeOrder(value: unknown, label: string): Record<string, number> | undefined {
  if (value === undefined) {
    return undefined;
  }
  if (!isRecord(value)) {
    throw new Error(`${label} must be an object.`);
  }
  return Object.fromEntries(
    Object.entries(value).map(([key, orderValue]) => {
      if (typeof orderValue !== "number" || !Number.isFinite(orderValue)) {
        throw new Error(`${label}.${key} must be a finite number.`);
      }
      return [key, orderValue];
    }),
  );
}

function normalizeDimensions(value: unknown): ViewerDimensionSpec[] {
  if (!Array.isArray(value) || value.length === 0) {
    throw new Error("Viewer runtime config requires at least one dimension.");
  }

  const seen = new Set<string>();
  return value.map((entry, index) => {
    if (!isRecord(entry)) {
      throw new Error(`dimensions[${index}] must be an object.`);
    }

    const id = ensureString(entry.id, `dimensions[${index}].id`);
    if (seen.has(id)) {
      throw new Error(`Viewer runtime config dimension '${id}' is duplicated.`);
    }
    seen.add(id);

    const rawNullLabel = entry.nullLabel;
    const nullLabel =
      rawNullLabel === undefined
        ? undefined
        : ensureString(rawNullLabel, `dimensions[${index}].nullLabel`);
    let noneValueMode: ViewerDimensionSpec["noneValueMode"];
    const rawNoneValueMode = entry.noneValueMode;
    if (rawNoneValueMode !== undefined) {
      if (rawNoneValueMode !== "null" && rawNoneValueMode !== "all") {
        throw new Error(`dimensions[${index}].noneValueMode must be 'null' or 'all'.`);
      }
      noneValueMode = rawNoneValueMode;
    }
    const aliases = normalizeAliases(entry.aliases, `dimensions[${index}].aliases`);
    const order = normalizeOrder(entry.order, `dimensions[${index}].order`);

    return {
      id,
      label: ensureString(entry.label, `dimensions[${index}].label`),
      ...(nullLabel ? { nullLabel } : {}),
      ...(noneValueMode ? { noneValueMode } : {}),
      ...(aliases ? { aliases } : {}),
      ...(order ? { order } : {}),
    };
  });
}

function normalizeDimensionList(
  value: unknown,
  label: string,
  knownDimensionIds: Set<string>,
  options?: { allowEmpty?: boolean },
): string[] {
  if (!Array.isArray(value)) {
    throw new Error(`${label} must be an array.`);
  }
  if (!options?.allowEmpty && value.length === 0) {
    throw new Error(`${label} must be a non-empty array.`);
  }

  const seen = new Set<string>();
  return value.map((entry, index) => {
    const dimensionId = ensureString(entry, `${label}[${index}]`);
    if (!knownDimensionIds.has(dimensionId)) {
      throw new Error(`${label}[${index}] references unknown dimension '${dimensionId}'.`);
    }
    if (seen.has(dimensionId)) {
      throw new Error(`${label} cannot contain duplicate dimension '${dimensionId}'.`);
    }
    seen.add(dimensionId);
    return dimensionId;
  });
}

function normalizeDefaultFilters(
  value: unknown,
  filterDimensions: readonly string[],
): Record<string, string | null> {
  if (!isRecord(value)) {
    throw new Error("default_filters must be an object.");
  }

  return Object.fromEntries(
    filterDimensions.map((dimensionId) => {
      const candidate = value[dimensionId];
      if (candidate === undefined) {
        return [dimensionId, null];
      }
      if (typeof candidate !== "string" && candidate !== null) {
        throw new Error(`default_filters.${dimensionId} must be a string or null.`);
      }
      return [dimensionId, candidate];
    }),
  );
}

function normalizeDefaultLayout(
  value: unknown,
  axisDimensions: readonly string[],
): ViewerLayoutSelection {
  if (!isRecord(value)) {
    throw new Error("default_layout must be an object.");
  }

  const axisDimensionSet = new Set(axisDimensions);
  const row_dimension = ensureString(value.row_dimension, "default_layout.row_dimension");
  const column_dimension = ensureString(value.column_dimension, "default_layout.column_dimension");
  const group_dimension =
    value.group_dimension === undefined || value.group_dimension === null
      ? null
      : ensureString(value.group_dimension, "default_layout.group_dimension");

  if (!axisDimensionSet.has(row_dimension)) {
    throw new Error("default_layout.row_dimension must be listed in axis_dimensions.");
  }
  if (!axisDimensionSet.has(column_dimension)) {
    throw new Error("default_layout.column_dimension must be listed in axis_dimensions.");
  }
  if (row_dimension === column_dimension) {
    throw new Error("default_layout row and column dimensions must differ.");
  }
  if (group_dimension !== null && !axisDimensionSet.has(group_dimension)) {
    throw new Error("default_layout.group_dimension must be null or listed in axis_dimensions.");
  }
  if (group_dimension !== null && [row_dimension, column_dimension].includes(group_dimension)) {
    throw new Error("default_layout.group_dimension must differ from row and column dimensions.");
  }

  return {
    row_dimension,
    column_dimension,
    group_dimension,
  };
}

export function parseViewerRuntimeConfig(value: unknown): ViewerRuntimeConfig {
  if (!isRecord(value)) {
    throw new Error("Viewer runtime config must be an object.");
  }

  const dimensions = normalizeDimensions(value.dimensions);
  const knownDimensionIds = new Set(dimensions.map((dimension) => dimension.id));
  const filter_dimensions = normalizeDimensionList(
    value.filter_dimensions,
    "filter_dimensions",
    knownDimensionIds,
    { allowEmpty: true },
  );
  const axis_dimensions = normalizeDimensionList(
    value.axis_dimensions,
    "axis_dimensions",
    knownDimensionIds,
  );

  if (axis_dimensions.length < 2) {
    throw new Error("Viewer runtime config requires at least two axis_dimensions.");
  }

  const default_filters = normalizeDefaultFilters(value.default_filters, filter_dimensions);
  const default_layout = normalizeDefaultLayout(value.default_layout, axis_dimensions);

  return {
    dimensions,
    filter_dimensions,
    axis_dimensions,
    default_filters,
    default_layout,
  };
}

export function dimensionMap(config: ViewerRuntimeConfig): Record<string, ViewerDimensionSpec> {
  return Object.fromEntries(config.dimensions.map((dimension) => [dimension.id, dimension]));
}

export function displayLabel(
  config: ViewerRuntimeConfig,
  dimensionId: string | null,
  value: string | null,
): string {
  if (dimensionId === null) {
    return String(value ?? "");
  }

  const spec = dimensionMap(config)[dimensionId];
  if (!spec) {
    return String(value ?? "");
  }
  if (value === null) {
    return spec.nullLabel ?? "None";
  }
  return spec.aliases?.[value] ?? value;
}

export function labelForDimension(config: ViewerRuntimeConfig, dimensionId: string | null): string {
  if (dimensionId === null) {
    return "";
  }
  return dimensionMap(config)[dimensionId]?.label ?? dimensionId;
}
