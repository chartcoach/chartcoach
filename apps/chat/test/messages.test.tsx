// @vitest-environment jsdom
import { renderToStaticMarkup } from "react-dom/server";
import type { EveMessage } from "eve/react";
import { expect, it } from "vite-plus/test";
import { Transcript } from "./transcript";
import { renderDocument } from "./render-document";

it.each([
  ["visfeedback", "Review"],
  ["visrec", "Recommend"],
  ["discuss", "Discuss"],
])("identifies the active %s workflow beside the response", (skill, label) => {
  const page = renderDocument(
    <Transcript
      messages={[
        {
          id: "reply",
          role: "assistant",
          parts: [
            {
              type: "dynamic-tool",
              toolCallId: "workflow",
              toolName: "load_skill",
              state: "output-available",
              input: { skill },
              output: "Loaded guidance",
            },
          ],
        },
      ]}
      attachments={new Map()}
    />,
  );

  const header = page.querySelector("header")!;
  expect(header.textContent).toContain("ChartCoach");
  expect(header.querySelector('[role="status"]')?.getAttribute("aria-label")).toBe(
    `Active mode: ${label}`,
  );
});

it("groups completed tool calls behind one collapsed activity control", () => {
  const page = renderDocument(
    <Transcript
      messages={[
        {
          id: "completed",
          role: "assistant",
          metadata: { status: "complete" },
          parts: ["labels", "axis"].flatMap((query) => [
            {
              type: "reasoning" as const,
              text: "Private provider reasoning",
            },
            {
              type: "dynamic-tool" as const,
              toolCallId: query,
              toolName: "search_guidelines",
              state: "output-available" as const,
              input: { query, method: "keyword" },
              output: { method: "keyword", matches: [] },
            },
          ]),
        },
      ]}
      attachments={new Map()}
    />,
  );

  const summaries = page.querySelectorAll('button[aria-label="Activity, 2 actions"]');
  expect(summaries).toHaveLength(1);
  const summary = summaries[0]!;
  expect(summary.getAttribute("aria-expanded")).toBe("false");
  const visibleText = page.createElement("div");
  visibleText.append(summary.cloneNode(true));
  visibleText.querySelectorAll('[aria-hidden="true"]').forEach((element) => element.remove());
  expect(visibleText.textContent).toBe("Activity2 actions");
  const disclosure = page.getElementById(summary.getAttribute("aria-controls")!)!;
  expect(disclosure.hasAttribute("inert")).toBe(true);
  expect(disclosure.textContent).toContain("Search matches (0)");
  expect(page.body.textContent).not.toContain("Private provider reasoning");
});

it("shows the active read action while partial results remain in progress", () => {
  const page = renderDocument(
    <Transcript
      messages={[
        {
          id: "reading",
          role: "assistant",
          metadata: { status: "streaming" },
          parts: [
            {
              type: "dynamic-tool",
              toolCallId: "read",
              toolName: "read_guidelines",
              state: "output-available",
              partial: true,
              input: { ids: ["labels"] },
              output: { guidelines: [], citations: [] },
            },
          ],
        },
      ]}
      attachments={new Map()}
    />,
  );

  const summary = page.querySelector("button[aria-expanded]")!;
  expect(summary.getAttribute("aria-label")).toBe(
    "Exploring guidelines, 1 action. Current: Read guidelines and sources · labels",
  );
  expect(summary.getAttribute("aria-expanded")).toBe("false");
  expect(summary.querySelector('[role="status"] [aria-hidden="false"]')?.textContent).toBe(
    "Exploring guidelines",
  );
  expect(page.getElementById(summary.getAttribute("aria-controls")!)?.textContent).toContain(
    "Working",
  );
});

it.each([
  ["vector", "Vector search"],
  ["keyword", "Keyword search"],
  ["hybrid", "Hybrid search"],
])(
  "identifies the current %s search even when a later parallel call has finished",
  (method, label) => {
    const page = renderDocument(
      <Transcript
        messages={[
          {
            id: "searching",
            role: "assistant",
            parts: [
              {
                type: "dynamic-tool",
                toolCallId: "search",
                toolName: "search_guidelines",
                state: "input-available",
                input: { query: "axis labels", method },
              },
              {
                type: "dynamic-tool",
                toolCallId: "schema",
                toolName: "describe_catalog",
                state: "output-available",
                input: {},
                output: {},
              },
            ],
          },
        ]}
        attachments={new Map()}
      />,
    );

    const summary = page.querySelector("button[aria-expanded]")!;
    expect(summary.getAttribute("aria-label")).toBe(
      `Exploring guidelines, 2 actions. Current: ${label} · axis labels`,
    );
    expect(summary.textContent).toContain(`${label} · axis labels`);
  },
);

it.each([
  {
    method: "vector",
    label: "Vector search",
    ranking: "cosine",
    embedding: { model: "all-MiniLM-L6-v2", metric: "cosine", dimensions: 384 },
  },
  { method: "keyword", label: "Keyword search", ranking: "BM25", embedding: {} },
  {
    method: "hybrid",
    label: "Hybrid search",
    ranking: "RRF",
    embedding: { model: "all-MiniLM-L6-v2", metric: "cosine", dimensions: 384 },
  },
])(
  "shows the query, matches and method from a $method search result",
  ({ method, label, ranking, embedding }) => {
    const html = renderToStaticMarkup(
      <Transcript
        messages={[
          {
            id: "search-reply",
            role: "assistant",
            parts: [
              {
                type: "dynamic-tool",
                toolCallId: "search",
                toolName: "search_guidelines",
                state: "output-available",
                input: { query: "long category labels" },
                output: {
                  method,
                  ranking,
                  ...embedding,
                  matches: [
                    {
                      id: "horizontal-bars",
                      title: "Use horizontal bars for long labels",
                      description: "Keep category labels readable.",
                      url: "https://chartcoach.dev/guidelines/horizontal-bars",
                    },
                  ],
                },
              },
            ],
          },
        ]}
        attachments={new Map()}
        stoppedTurnIds={new Set()}
      />,
    );

    expect(html).toContain("<details");
    expect(html).toContain("long category labels");
    expect(html).toContain("Search matches (1)");
    expect(html).toContain(label);
    expect(html).toContain(ranking);

    if (embedding.model) expect(html).toContain(embedding.model);
    expect(html).toContain("Use horizontal bars for long labels");
    expect(html).toContain("Keep category labels readable.");
  },
);

it.each([
  { kind: "URL", url: "https://example.com/paper", doi: null, href: "https://example.com/paper" },
  {
    kind: "DOI",
    url: null,
    doi: "10.1109/TVCG.2020.3030376",
    href: "https://doi.org/10.1109%2FTVCG.2020.3030376",
  },
])("shows guidelines with their $kind source links", ({ url, doi, href }) => {
  const html = renderToStaticMarkup(
    <Transcript
      messages={[
        {
          id: "read-reply",
          role: "assistant",
          parts: [
            {
              type: "dynamic-tool",
              toolCallId: "read",
              toolName: "read_guidelines",
              state: "output-available",
              input: { ids: ["horizontal-bars"] },
              output: {
                guidelines: [
                  {
                    id: "horizontal-bars",
                    title: "Use horizontal bars",
                    description: "Give long labels room.",
                  },
                ],
                citations: [
                  {
                    id: "horizontal-bars",
                    url: "https://chartcoach.dev/guidelines/horizontal-bars",
                    sources: [
                      {
                        reference_id: "paper",
                        citation: "Example Author (2020). Chart labels.",
                        url,
                        doi,
                      },
                    ],
                  },
                ],
              },
            },
          ],
        },
      ]}
      attachments={new Map()}
      stoppedTurnIds={new Set()}
    />,
  );

  expect(html).toContain("Use horizontal bars");
  expect(html).toContain("Give long labels room.");
  expect(html).toContain('href="https://chartcoach.dev/guidelines/horizontal-bars"');
  expect(html).toContain(`href="${href}"`);
  expect(html).toContain("Example Author (2020). Chart labels.");
});

it("withholds unverified assistant prose", () => {
  const html = renderToStaticMarkup(
    <Transcript
      messages={[
        {
          id: "reply",
          role: "assistant",
          parts: [
            {
              type: "text",
              state: "done",
              text: "Unverified advice ![remote](https://example.com/chart.png)",
            },
          ],
        },
      ]}
      attachments={new Map()}
      stoppedTurnIds={new Set()}
    />,
  );

  expect(html).not.toContain("<img");
  expect(html).not.toContain("Unverified advice");
});

it("shows a SQL query with typed columns and bounded results", () => {
  const html = renderToStaticMarkup(
    <Transcript
      messages={[
        {
          id: "sql",
          role: "assistant",
          parts: [
            {
              type: "dynamic-tool",
              toolName: "query_catalog",
              toolCallId: "sql",
              state: "output-available",
              input: { sql: "SELECT title, optional FROM guidelines" },
              output: {
                method: "sql",
                columns: [
                  { name: "title", type: "VARCHAR" },
                  { name: "optional", type: "VARCHAR" },
                ],
                rows: [["<script>alert(1)</script>", null]],
                row_count: 1,
                limit: 1,
                truncated: true,
                matches: [],
              },
            },
          ],
        },
      ]}
      attachments={new Map()}
      stoppedTurnIds={new Set()}
    />,
  );

  expect(html).toContain("SELECT title, optional FROM guidelines");
  expect(html).toContain("SQL · DuckDB");
  expect(html).toContain('scope="col">title');
  expect(html).toContain("VARCHAR");
  expect(html).toContain("NULL");
  expect(html).toContain("Results are limited to 1 rows");
  expect(html).toContain("&lt;script&gt;alert(1)&lt;/script&gt;");
});

it("shows catalog table schemas, vocabulary, and query limits", () => {
  const html = renderToStaticMarkup(
    <Transcript
      messages={[
        {
          id: "schema",
          role: "assistant",
          parts: [
            {
              type: "dynamic-tool",
              toolName: "describe_catalog",
              toolCallId: "schema",
              state: "output-available",
              input: {},
              output: {
                tables: [
                  {
                    name: "guidelines",
                    rows: 781,
                    columns: [{ name: "id", type: "VARCHAR" }],
                  },
                ],
                profiles: ["minilm"],
                label_families: [{ name: "chart", description: "Chart types" }],
                section_roles: [{ name: "recommendation", description: "Recommended action" }],
                limits: {
                  default_rows: 20,
                  max_rows: 50,
                  max_response_bytes: 65536,
                  timeout_ms: 5000,
                },
              },
            },
          ],
        },
      ]}
      attachments={new Map()}
      stoppedTurnIds={new Set()}
    />,
  );

  expect(html).toContain("Explore catalog structure");
  expect(html).toContain("781");
  expect(html).toContain("VARCHAR");
  expect(html).toContain("recommendation");
  expect(html).toContain("minilm");
  expect(html).toContain("20");
  expect(html).toContain("50");
});

it("shows an unfinished tool as stopped when its turn was cancelled", () => {
  const message: EveMessage = {
    id: "reply",
    role: "assistant",
    metadata: { turnId: "turn" },
    parts: [
      {
        type: "dynamic-tool",
        toolCallId: "search",
        toolName: "search_guidelines",
        state: "input-available",
        input: { query: "labels" },
      },
    ],
  };

  const html = renderToStaticMarkup(
    <Transcript messages={[message]} attachments={new Map()} stoppedTurnIds={new Set(["turn"])} />,
  );

  expect(html).toContain("Stopped");
  expect(html).toContain("Response stopped.");
});

const recoveryHint = "Gemini rejected the model. Choose an available model in Model settings.";

it.each([
  {
    failure: "replayed turn failure",
    options: {
      failedTurnIds: new Set(["turn"]),
      failureReasons: new Map([["turn", recoveryHint]]),
    },
  },
  { failure: "stream interruption", options: { interrupted: true, error: recoveryHint } },
])("settles response activity after $failure", (failure) => {
  const message: EveMessage = {
    id: "reply",
    role: "assistant",
    metadata: { turnId: "turn" },
    parts: [
      {
        type: "dynamic-tool",
        toolCallId: "search",
        toolName: "search_guidelines",
        state: "input-available",
        input: { query: "labels" },
      },
    ],
  };

  const html = renderToStaticMarkup(
    <Transcript messages={[message]} attachments={new Map()} {...failure.options} />,
  );

  expect(html).toContain("Failed");
  expect(html).toContain(recoveryHint);
  expect(html.match(/role="alert"/g)).toHaveLength(1);
});

it("keeps a completed response intact when a later message cannot be sent", () => {
  const messages: EveMessage[] = [
    {
      id: "reply",
      role: "assistant",
      metadata: {
        turnId: "turn",
        status: "complete",
      },
      parts: [
        {
          type: "dynamic-tool",
          toolCallId: "present-question",
          toolName: "present_answer",
          state: "output-available",
          input: {},
          output: {
            workflow: "visfeedback",
            status: "needs_context",
            points: [],
            question: "Where will this chart be displayed?",
          },
        },
      ],
    },
    {
      id: "follow-up",
      role: "user",
      metadata: { status: "failed" },
      parts: [{ type: "text", text: "Where should they go?", state: "done" }],
    },
  ];

  const html = renderToStaticMarkup(
    <Transcript
      messages={messages}
      attachments={new Map()}
      stoppedTurnIds={new Set()}
      failedTurnIds={new Set(["turn"])}
      interrupted
    />,
  );

  expect(html).toContain("Where will this chart be displayed?");
  expect(html).toContain("Message failed.");
  expect(html.match(/role="alert"/g)).toHaveLength(1);
});
