import test from "node:test";
import assert from "node:assert/strict";
import {
  createViewerRuntime,
  deriveViewerState,
  loadViewerArtifactRowsFromParquetUrl,
  parseViewerRuntimeConfig,
} from "../distlib/testing.js";

function makeCandidate(id) {
  return {
    visgen_id: id,
    dimension_values: {},
    guideline_count: 0,
    guideline_details: [],
    score_breakdown: [],
    image_url: null,
  };
}

function makeRow(overrides) {
  return {
    visgen_id: overrides.visgen_id,
    vis_id: overrides.vis_id ?? "case-1",
    query: overrides.query ?? "How do sales compare?",
    search_text: overrides.search_text ?? "case-1 How do sales compare?",
    objective: overrides.objective ?? null,
    request_chart: overrides.request_chart ?? null,
    audience: overrides.audience ?? null,
    grammar: overrides.grammar ?? null,
    grounding_mode: overrides.grounding_mode ?? null,
    model: overrides.model ?? null,
    overall_score: overrides.overall_score ?? null,
    candidate: overrides.candidate ?? makeCandidate(overrides.visgen_id),
  };
}

test("deriveViewerState uses transported runtime config instead of hardcoded defaults", () => {
  const runtimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      {
        id: "grammar",
        label: "Renderer",
        aliases: {
          altair: "Alt",
          plotly: "Plot",
        },
      },
      { id: "grounding_mode", label: "Grounding" },
      { id: "model", label: "Model" },
    ],
    filter_dimensions: ["grammar"],
    axis_dimensions: ["model", "grounding_mode"],
    default_filters: {
      grammar: "plotly",
    },
    default_layout: {
      row_dimension: "model",
      column_dimension: "grounding_mode",
      group_dimension: null,
    },
  });

  const runtime = createViewerRuntime(
    [
      makeRow({ visgen_id: "a", grammar: "altair", grounding_mode: "none", model: "gpt" }),
      makeRow({ visgen_id: "b", grammar: "plotly", grounding_mode: "hybrid", model: "claude" }),
    ],
    runtimeConfig,
  );

  const derived = deriveViewerState(runtime, {});
  assert.equal(derived.selection.filters.grammar, "plotly");
  assert.equal(derived.state.overview.ui_schema.filters[0].label, "Renderer");
  assert.deepEqual(
    derived.state.overview.ui_schema.filters[0].options.map((option) => option.label),
    ["Alt", "Plot"],
  );
  assert.equal(derived.state.overview.ui_schema.layout_controls.length, 0);
});

test("deriveViewerState preserves explicit null grouping selections", () => {
  const runtimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      { id: "model", label: "Model" },
      { id: "grounding_mode", label: "Grounding" },
      { id: "grammar", label: "Grammar" },
    ],
    filter_dimensions: [],
    axis_dimensions: ["model", "grounding_mode", "grammar"],
    default_filters: {},
    default_layout: {
      row_dimension: "model",
      column_dimension: "grounding_mode",
      group_dimension: "grammar",
    },
  });

  const runtime = createViewerRuntime(
    [
      makeRow({ visgen_id: "a", grammar: "altair", grounding_mode: "none", model: "gpt" }),
      makeRow({ visgen_id: "b", grammar: "plotly", grounding_mode: "none", model: "gpt" }),
    ],
    runtimeConfig,
  );

  const derived = deriveViewerState(runtime, {
    layout: {
      group_dimension: null,
    },
  });

  assert.equal(derived.selection.layout.group_dimension, null);
  assert.equal(derived.state.overview.matrix.kind, "flat");
  assert.equal(derived.state.overview.ui_schema.matrix_axes.group_label, null);
  const groupControl = derived.state.overview.ui_schema.layout_controls.find(
    (control) => control.id === "group_dimension",
  );
  assert.equal(groupControl?.value, null);
});

test("deriveViewerState applies default grouping when no explicit group selection is requested", () => {
  const runtimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      { id: "model", label: "Model" },
      { id: "grounding_mode", label: "Grounding" },
      { id: "grammar", label: "Grammar" },
    ],
    filter_dimensions: [],
    axis_dimensions: ["model", "grounding_mode", "grammar"],
    default_filters: {},
    default_layout: {
      row_dimension: "model",
      column_dimension: "grounding_mode",
      group_dimension: "grammar",
    },
  });

  const runtime = createViewerRuntime(
    [
      makeRow({ visgen_id: "a", grammar: "altair", grounding_mode: "none", model: "gpt" }),
      makeRow({ visgen_id: "b", grammar: "plotly", grounding_mode: "none", model: "gpt" }),
    ],
    runtimeConfig,
  );

  const derived = deriveViewerState(runtime, {});

  assert.equal(derived.selection.layout.group_dimension, "grammar");
  assert.equal(derived.state.overview.matrix.kind, "grouped");
  assert.equal(derived.state.overview.ui_schema.matrix_axes.group_label, "Grammar");
});

test("deriveViewerState hides inert filter and layout controls and suppresses toolbar pills", () => {
  const runtimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      { id: "model", label: "Model" },
      { id: "grounding_mode", label: "Grounding" },
      { id: "audience", label: "Audience", nullLabel: "Everyone" },
    ],
    filter_dimensions: ["audience"],
    axis_dimensions: ["model", "grounding_mode"],
    default_filters: {
      audience: null,
    },
    default_layout: {
      row_dimension: "model",
      column_dimension: "grounding_mode",
      group_dimension: null,
    },
  });

  const runtime = createViewerRuntime(
    [
      makeRow({ visgen_id: "a", audience: null, grounding_mode: "none", model: "gpt" }),
      makeRow({ visgen_id: "b", audience: null, grounding_mode: "hybrid", model: "claude" }),
    ],
    runtimeConfig,
  );

  const derived = deriveViewerState(runtime, {});
  assert.deepEqual(derived.state.overview.ui_schema.filters, []);
  assert.deepEqual(derived.state.overview.ui_schema.layout_controls, []);
  assert.deepEqual(derived.state.overview.ui_schema.toolbar?.pills ?? [], []);
});

test("parquet loading falls back to buffered fetch when URL-backed parsing fails", async () => {
  const calls = [];
  const rows = await loadViewerArtifactRowsFromParquetUrl(
    "https://example.test/viewer.parquet",
    undefined,
    {
      async openUrlBuffer({ url }) {
        calls.push(["open", url]);
        return { kind: "url-buffer" };
      },
      async readObjects({ file }) {
        calls.push(["read", file instanceof ArrayBuffer ? "array-buffer" : file.kind]);
        if (!(file instanceof ArrayBuffer)) {
          throw new Error("Offset is outside the bounds of the DataView");
        }
        return [
          {
            visgen_id: "a",
            vis_id: "case-1",
            query: "How do sales compare?",
            search_text: "case-1 How do sales compare?",
            objective: null,
            request_chart: null,
            audience: null,
            grammar: null,
            grounding_mode: null,
            model: null,
            overall_score: null,
            candidate_json: JSON.stringify(makeCandidate("a")),
          },
        ];
      },
      async fetch(url) {
        calls.push(["fetch", url]);
        return {
          ok: true,
          async arrayBuffer() {
            return new Uint8Array([1, 2, 3]).buffer;
          },
        };
      },
    },
  );

  assert.equal(rows.length, 1);
  assert.deepEqual(calls, [
    ["open", "https://example.test/viewer.parquet"],
    ["read", "url-buffer"],
    ["fetch", "https://example.test/viewer.parquet"],
    ["read", "array-buffer"],
  ]);
});
