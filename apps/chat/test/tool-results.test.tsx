import { renderToStaticMarkup } from "react-dom/server";
import { expect, it, vi } from "vite-plus/test";
import { ToolActivity } from "../components/chat/tool-activity";

it("renders SQL text, numbers, nested JSON, and null distinctly", () => {
  const html = renderToStaticMarkup(
    <ToolActivity
      part={{
        type: "dynamic-tool",
        toolCallId: "values",
        toolName: "query_catalog",
        state: "output-available",
        input: { sql: "SELECT 'labels', 3, {'author': 'Ada'}, NULL" },
        output: {
          method: "sql",
          columns: [
            { name: "text", type: "VARCHAR" },
            { name: "count", type: "INTEGER" },
            { name: "source", type: "STRUCT(author VARCHAR)" },
            { name: "year", type: "INTEGER" },
          ],
          rows: [["labels", 3, { author: "Ada" }, null]],
          row_count: 1,
          limit: 20,
          truncated: false,
        },
      }}
      stopped={false}
      failed={false}
    />,
  );
  expect(html).toMatch(/<td\b[^>]*>labels<\/td>/);
  expect(html).toMatch(/<td\b[^>]*>3<\/td>/);
  expect(html).toContain("{&quot;author&quot;:&quot;Ada&quot;}");
  expect(html).toMatch(/<td\b[^>]*><span[^>]*>NULL<\/span><\/td>/);
});

it.each([
  {
    name: "catalog schema columns",
    tool: "describe_catalog",
    input: {},
    output: {
      tables: [
        {
          name: "guidelines",
          rows: 2,
          columns: [
            { name: "id", type: "VARCHAR" },
            { name: "title", type: "VARCHAR" },
          ],
        },
      ],
      profiles: [],
      label_families: [],
      section_roles: [],
      limits: { default_rows: 20, max_rows: 50, max_response_bytes: 65536, timeout_ms: 5000 },
    },
    expected: "Catalog tables · DuckDB",
  },
  {
    name: "duplicate SQL headings and rows",
    tool: "query_catalog",
    input: { sql: "SELECT id AS value, id AS value FROM guidelines" },
    output: {
      method: "sql",
      columns: [
        { name: "value", type: "VARCHAR" },
        { name: "value", type: "VARCHAR" },
      ],
      rows: [
        ["labels", "labels"],
        ["labels", "labels"],
      ],
      row_count: 2,
      limit: 20,
      truncated: false,
    },
    expected: "2 rows",
  },
])("renders $name with stable child identity", ({ tool, input, output, expected }) => {
  const errors = vi.spyOn(console, "error").mockImplementation(() => {});
  try {
    const html = renderToStaticMarkup(
      <ToolActivity
        part={{
          type: "dynamic-tool",
          toolCallId: "inspect",
          toolName: tool,
          state: "output-available",
          input,
          output,
        }}
        stopped={false}
        failed={false}
      />,
    );
    expect(html).toContain(expected);
    if (tool === "query_catalog") expect(html.match(/<td\b[^>]*>labels<\/td>/g)).toHaveLength(4);
    expect(errors).not.toHaveBeenCalled();
  } finally {
    errors.mockRestore();
  }
});
