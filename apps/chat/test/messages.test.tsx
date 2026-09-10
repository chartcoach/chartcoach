import { renderToStaticMarkup } from "react-dom/server";
import type { EveMessage } from "eve/react";
import { expect, it } from "vite-plus/test";
import { Transcript } from "./transcript";

it("groups completed tool calls behind one collapsed activity control", () => {
  const html = renderToStaticMarkup(
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
  expect(html.match(/>Activity</g)).toHaveLength(1);
  expect(html).toContain("2 actions");
  expect(html).toMatch(/<button[^>]*aria-expanded="false"/);
  expect(html).toContain('inert=""');
  expect(html).toContain("Search matches (0)");
  expect(html.match(/Search guidelines/g)).toHaveLength(2);
  expect(html).not.toContain("Private provider reasoning");
});

it("shows the active read action while partial results remain in progress", () => {
  const html = renderToStaticMarkup(
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
  expect(html).toContain("Reading guidelines and sources");
  expect(html).toContain("Working");
  expect(html).not.toContain("Done");
  expect(html).toMatch(/<button[^>]*aria-expanded="false"/);
  expect(html).toContain('inert=""');
});

it("shows the search query and returned matches in a collapsed disclosure", () => {
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
                method: "vector",
                model: "all-MiniLM-L6-v2",
                metric: "cosine",
                dimensions: 384,
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
  expect(html).toContain("Vector search");
  expect(html).toContain("all-MiniLM-L6-v2");
  expect(html).toContain("cosine");
  expect(html).toContain("Use horizontal bars for long labels");
  expect(html).toContain("Keep category labels readable.");
});

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

it.each([
  { method: "keyword", label: "Keyword search" },
  { method: "hybrid", label: "Hybrid search" },
])("labels $method searches from the tool result", ({ method, label }) => {
  const html = renderToStaticMarkup(
    <Transcript
      messages={[
        {
          id: "reply",
          role: "assistant",
          parts: [
            {
              type: "dynamic-tool",
              toolCallId: "search",
              toolName: "search_guidelines",
              state: "output-available",
              input: { query: "category labels" },
              output: { method, matches: [] },
            },
          ],
        },
      ]}
      attachments={new Map()}
      stoppedTurnIds={new Set()}
    />,
  );
  expect(html).toContain(label);
  expect(html).toContain("Search matches (0)");
  expect(html).not.toContain("Embedding model");
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
  expect(html).not.toContain("<script>");
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
  expect(html).not.toContain("Working");
});

it.each([
  { failure: "turn failure", failedTurnIds: new Set(["turn"]), interrupted: false },
  { failure: "stream interruption", failedTurnIds: new Set<string>(), interrupted: true },
])("settles response activity after $failure", (failure) => {
  const message: EveMessage = {
    id: "reply",
    role: "assistant",
    metadata: { turnId: "turn" },
    parts: [
      { type: "text", text: "The chart compares fruit harvests.", state: "streaming" },
      { type: "reasoning", text: "Inspecting the chart", state: "streaming" },
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
    <Transcript
      messages={[message]}
      attachments={new Map()}
      stoppedTurnIds={new Set()}
      failedTurnIds={failure.failedTurnIds}
      interrupted={failure.interrupted}
    />,
  );
  expect(html).not.toContain("The chart compares fruit harvests.");
  expect(html).toContain("Failed");
  expect(html).toContain("Response interrupted.");
  expect(html).not.toContain("Working");
  expect(html).not.toContain("Thinking");
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
  expect(html).not.toContain("Response interrupted.");
});
