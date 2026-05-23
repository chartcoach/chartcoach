import assert from "node:assert/strict";
import { test } from "vitest";
import { createParquetViewerBridge } from "../src/viewer/bridge/parquet.ts";
import { createViewerRuntime, deriveViewerState } from "../src/viewer/data/derive.ts";
import {
  loadViewerArtifactFromParquetUrl,
  parseViewerArtifactRows,
} from "../src/viewer/data/parquet.ts";
import { parseViewerRuntimeConfig } from "../src/viewer/data/runtime-config.ts";
import { safeGuidelineHref } from "../src/viewer/render/detail-drawer.tsx";

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
  const dimensionValues = {
    ...(overrides.objective !== undefined ? { objective: overrides.objective } : {}),
    ...(overrides.request_chart !== undefined ? { request_chart: overrides.request_chart } : {}),
    ...(overrides.audience !== undefined ? { audience: overrides.audience } : {}),
    ...(overrides.grammar !== undefined ? { grammar: overrides.grammar } : {}),
    ...(overrides.grounding_mode !== undefined ? { grounding_mode: overrides.grounding_mode } : {}),
    ...(overrides.model !== undefined ? { model: overrides.model } : {}),
    ...overrides.dimension_values,
  };
  const candidate = overrides.candidate ?? makeCandidate(overrides.visgen_id);
  return {
    visgen_id: overrides.visgen_id,
    vis_id: overrides.vis_id ?? "case-1",
    query: overrides.query ?? "How do sales compare?",
    search_text: overrides.search_text ?? "case-1 How do sales compare?",
    overall_score: overrides.overall_score ?? null,
    dimension_values: dimensionValues,
    candidate: {
      ...candidate,
      dimension_values: dimensionValues,
    },
  };
}

function parquetDependencyRows(rows) {
  return {
    async openUrlBuffer() {
      return { kind: "url-buffer" };
    },
    async readObjects() {
      return rows;
    },
  };
}

async function waitFor(assertion) {
  const startedAt = Date.now();
  let lastError;
  while (Date.now() - startedAt < 1000) {
    try {
      assertion();
      return;
    } catch (error) {
      lastError = error;
      await new Promise((resolve) => setTimeout(resolve, 5));
    }
  }
  throw lastError;
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

test("deriveViewerState reads configured dimensions from canonical dimension values", () => {
  const runtimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      { id: "task_family", label: "Task family" },
      { id: "model", label: "Model" },
      { id: "grounding_mode", label: "Grounding" },
    ],
    filter_dimensions: ["task_family"],
    axis_dimensions: ["model", "grounding_mode"],
    default_filters: {
      task_family: "comparison",
    },
    default_layout: {
      row_dimension: "model",
      column_dimension: "grounding_mode",
      group_dimension: null,
    },
  });

  const runtime = createViewerRuntime(
    [
      makeRow({
        visgen_id: "a",
        model: "gpt",
        grounding_mode: "none",
        dimension_values: { task_family: "comparison" },
      }),
      makeRow({
        visgen_id: "b",
        model: "claude",
        grounding_mode: "hybrid",
        dimension_values: { task_family: "composition" },
      }),
    ],
    runtimeConfig,
  );

  const derived = deriveViewerState(runtime, {});
  assert.equal(derived.selection.filters.task_family, "comparison");
  assert.deepEqual(
    derived.state.overview.ui_schema.filters[0].options.map((option) => option.value),
    ["comparison", "composition"],
  );
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

test("parquet artifact loading uses configured dimensions as the canonical schema", async () => {
  const runtimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      { id: "objective", label: "Objective" },
      { id: "model", label: "Model" },
    ],
    filter_dimensions: ["objective"],
    axis_dimensions: ["model", "objective"],
    default_filters: {
      objective: "select",
    },
    default_layout: {
      row_dimension: "model",
      column_dimension: "objective",
      group_dimension: null,
    },
  });

  const rows = await loadViewerArtifactFromParquetUrl(
    "https://example.test/viewer.parquet",
    undefined,
    {
      runtimeConfig,
      dependencies: {
        async openUrlBuffer() {
          return { kind: "url-buffer" };
        },
        async readObjects() {
          return [
            {
              visgen_id: "a",
              vis_id: "case-1",
              query: "How do sales compare?",
              search_text: "case-1 How do sales compare?",
              objective: "select",
              model: "gpt",
              unconfigured_dimension: "ignored",
              overall_score: null,
              candidate_json: JSON.stringify(makeCandidate("a")),
            },
          ];
        },
      },
    },
  );

  assert.deepEqual(rows[0].dimension_values, {
    objective: "select",
    model: "gpt",
  });
  assert.deepEqual(rows[0].candidate.dimension_values, {
    objective: "select",
    model: "gpt",
  });
  assert.equal(rows[0].candidate.overall_score, null);
});

test("parquet artifact loading rejects row and candidate identity conflicts", async () => {
  const runtimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      { id: "objective", label: "Objective" },
      { id: "model", label: "Model" },
    ],
    filter_dimensions: ["objective"],
    axis_dimensions: ["model", "objective"],
    default_filters: {
      objective: "select",
    },
    default_layout: {
      row_dimension: "model",
      column_dimension: "objective",
      group_dimension: null,
    },
  });

  await assert.rejects(
    () =>
      loadViewerArtifactFromParquetUrl("https://example.test/viewer.parquet", undefined, {
        runtimeConfig,
        dependencies: parquetDependencyRows([
          {
            visgen_id: "a",
            vis_id: "case-1",
            query: "How do sales compare?",
            search_text: "case-1 How do sales compare?",
            objective: "select",
            model: "gpt",
            overall_score: null,
            candidate_json: JSON.stringify(makeCandidate("b")),
          },
        ]),
      }),
    /conflicting candidate_json\.visgen_id 'b'/,
  );
});

test("parquet artifact loading rejects row and candidate score conflicts", async () => {
  const runtimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      { id: "objective", label: "Objective" },
      { id: "model", label: "Model" },
    ],
    filter_dimensions: ["objective"],
    axis_dimensions: ["model", "objective"],
    default_filters: {
      objective: "select",
    },
    default_layout: {
      row_dimension: "model",
      column_dimension: "objective",
      group_dimension: null,
    },
  });

  await assert.rejects(
    () =>
      loadViewerArtifactFromParquetUrl("https://example.test/viewer.parquet", undefined, {
        runtimeConfig,
        dependencies: parquetDependencyRows([
          {
            visgen_id: "a",
            vis_id: "case-1",
            query: "How do sales compare?",
            search_text: "case-1 How do sales compare?",
            objective: "select",
            model: "gpt",
            overall_score: 0.7,
            candidate_json: JSON.stringify({
              ...makeCandidate("a"),
              overall_score: 0.9,
            }),
          },
        ]),
      }),
    /conflicting overall_score values/,
  );
});

test("parquet artifact loading rejects row and score breakdown conflicts", async () => {
  const runtimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      { id: "objective", label: "Objective" },
      { id: "model", label: "Model" },
    ],
    filter_dimensions: ["objective"],
    axis_dimensions: ["model", "objective"],
    default_filters: {
      objective: "select",
    },
    default_layout: {
      row_dimension: "model",
      column_dimension: "objective",
      group_dimension: null,
    },
  });

  await assert.rejects(
    () =>
      loadViewerArtifactFromParquetUrl("https://example.test/viewer.parquet", undefined, {
        runtimeConfig,
        dependencies: parquetDependencyRows([
          {
            visgen_id: "a",
            vis_id: "case-1",
            query: "How do sales compare?",
            search_text: "case-1 How do sales compare?",
            objective: "select",
            model: "gpt",
            overall_score: 0.7,
            candidate_json: JSON.stringify({
              ...makeCandidate("a"),
              overall_score: 0.7,
              score_breakdown: [
                {
                  id: "overall",
                  label: "Overall",
                  dimension: "overall",
                  score: 0.9,
                  reasoning: null,
                  runs: [],
                },
              ],
            }),
          },
        ]),
      }),
    /conflicting score_breakdown overall score/,
  );
});

test("parquet artifact loading rejects invalid row shapes before normalization", async () => {
  const runtimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      { id: "objective", label: "Objective" },
      { id: "model", label: "Model" },
    ],
    filter_dimensions: ["objective"],
    axis_dimensions: ["model", "objective"],
    default_filters: {
      objective: "select",
    },
    default_layout: {
      row_dimension: "model",
      column_dimension: "objective",
      group_dimension: null,
    },
  });

  await assert.rejects(
    () =>
      loadViewerArtifactFromParquetUrl("https://example.test/viewer.parquet", undefined, {
        runtimeConfig,
        dependencies: parquetDependencyRows([
          {
            vis_id: "case-1",
            query: "How do sales compare?",
            search_text: "case-1 How do sales compare?",
            objective: "select",
            model: "gpt",
            overall_score: Number.NaN,
            candidate_json: "{}",
          },
        ]),
      }),
    /rows\[0\]\.visgen_id must be a non-empty string/,
  );
});

test("parquet artifact row parser rejects malformed raw rows", () => {
  assert.throws(
    () =>
      parseViewerArtifactRows([
        {
          visgen_id: "a",
          objective: "select",
          model: "gpt",
          overall_score: "0.7",
          candidate_json: "{}",
        },
      ]),
    /rows\[0\]\.vis_id must be a non-empty string/,
  );
});

test("parquet bridge re-normalizes raw rows when runtime config changes", async () => {
  const initialRuntimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      { id: "objective", label: "Objective" },
      { id: "model", label: "Model" },
    ],
    filter_dimensions: ["objective"],
    axis_dimensions: ["model", "objective"],
    default_filters: {
      objective: "select",
    },
    default_layout: {
      row_dimension: "model",
      column_dimension: "objective",
      group_dimension: null,
    },
  });
  const nextRuntimeConfig = parseViewerRuntimeConfig({
    dimensions: [
      { id: "task_family", label: "Task family" },
      { id: "model", label: "Model" },
      { id: "objective", label: "Objective" },
    ],
    filter_dimensions: ["task_family"],
    axis_dimensions: ["model", "objective"],
    default_filters: {
      task_family: "comparison",
    },
    default_layout: {
      row_dimension: "model",
      column_dimension: "objective",
      group_dimension: null,
    },
  });
  let externalSnapshot = null;
  let externalListener = () => {};
  const bridge = createParquetViewerBridge({
    artifactUrl: "https://example.test/viewer.parquet",
    runtimeConfig: initialRuntimeConfig,
    getExternalSnapshot: () => externalSnapshot,
    onExternalChange(listener) {
      externalListener = listener;
      return () => {};
    },
    dependencies: parquetDependencyRows([
      {
        visgen_id: "a",
        vis_id: "case-1",
        query: "How do sales compare?",
        search_text: "case-1 How do sales compare?",
        objective: "select",
        model: "gpt",
        task_family: "comparison",
        overall_score: null,
        candidate_json: JSON.stringify(makeCandidate("a")),
      },
    ]),
  });

  await waitFor(() => {
    assert.equal(bridge.getSnapshot().state.error, null);
    assert.equal(bridge.getSnapshot().selection.filters.objective, "select");
    assert.notEqual(bridge.getSnapshot().state.overview, null);
  });

  externalSnapshot = { runtimeConfig: nextRuntimeConfig };
  externalListener();

  assert.equal(bridge.getSnapshot().state.error, null);
  assert.equal(bridge.getSnapshot().selection.filters.task_family, "comparison");
  assert.equal(bridge.getSnapshot().runtimeConfig?.dimensions[0]?.id, "task_family");
  bridge.destroy?.();
});

test("guideline cards only render safe link schemes", () => {
  assert.equal(
    safeGuidelineHref("https://example.test/guideline"),
    "https://example.test/guideline",
  );
  assert.equal(safeGuidelineHref("/guidelines/local"), "/guidelines/local");
  assert.equal(safeGuidelineHref("javascript:alert(1)"), null);
  assert.equal(safeGuidelineHref("data:text/html,<script></script>"), null);
});
