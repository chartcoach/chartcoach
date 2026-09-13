import { renderToStaticMarkup } from "react-dom/server";
import type { EveDynamicToolPart, EveMessage } from "eve/react";
import { expect, it, vi } from "vite-plus/test";
import { Transcript } from "./transcript";

const read: EveMessage = {
  id: "read",
  role: "assistant",
  parts: [
    {
      type: "dynamic-tool",
      toolCallId: "read-labels",
      toolName: "read_guidelines",
      state: "output-available",
      input: { ids: ["direct-labels"] },
      output: {
        guidelines: [
          {
            id: "direct-labels",
            title: "Label series directly",
            description: "Place the name by its series.",
          },
        ],
        citations: [
          {
            id: "direct-labels",
            url: "https://chartcoach.dev/guidelines/direct-labels",
            sources: [],
          },
        ],
      },
    },
  ],
};

const feedback = {
  workflow: "visfeedback",
  status: "answer",
  points: [
    {
      primary_guideline_id: "direct-labels",
      supporting_guideline_ids: [],
      assessment: "violated",
      context: "The legend is far from the lines.",
      recommendation: "Place each series name beside its line.",
    },
  ],
  question: null,
};

function answer(
  output: Extract<EveDynamicToolPart, { state: "output-available" }>["output"] = feedback,
  metadata: EveMessage["metadata"] = { status: "complete" },
  parts: EveMessage["parts"] = [],
): EveMessage {
  return {
    id: "answer",
    role: "assistant",
    metadata: { status: "complete", ...metadata },
    parts: [
      ...parts,
      {
        type: "dynamic-tool",
        toolCallId: "present",
        toolName: "present_answer",
        state: "output-available",
        input: output,
        output,
      },
    ],
  };
}

function render(messages: EveMessage[]) {
  return renderToStaticMarkup(
    <Transcript messages={messages} attachments={new Map()} stoppedTurnIds={new Set()} />,
  );
}

it("offers another evidence check when a completed turn has no presentation", () => {
  const html = render([
    { id: "empty", role: "assistant", metadata: { status: "complete" }, parts: [] },
  ]);

  expect(html).toContain("The answer needs another evidence check.");
  expect(html).toContain("Try again");
});

it.each([
  { workflow: "discuss", label: "Your question" },
  { workflow: "visrec", label: "Your brief" },
])("renders grounded $workflow advice with its decision context", ({ workflow, label }) => {
  const html = render([
    read,
    answer(
      {
        ...feedback,
        workflow,
        points: [{ ...feedback.points[0], assessment: null }],
      },
      { status: "complete" },
    ),
  ]);

  expect(html).toContain("Place each series name beside its line.");
  expect(html).toContain(label);
  expect(html).toContain('aria-label="Primary: Label series directly"');
  expect(html).not.toContain(">Improve</h3>");
});

it("renders an action with a verified citation and its context on demand", () => {
  const html = render([answer(feedback, {}, read.parts)]);
  expect(html).toContain("The legend is far from the lines.");
  expect(html).toMatch(
    /<dt[^>]*>Guideline guidance<\/dt><dd[^>]*>Place the name by its series\.<\/dd>/,
  );
  expect(html).toContain("Place each series name beside its line.");
  expect(html).toContain("Label series directly");
  expect(html).toContain('href="https://chartcoach.dev/guidelines/direct-labels"');
  expect(html).toContain('aria-label="Primary: Label series directly"');
  expect(html).toMatch(/<details[^>]*><summary[^>]*>Why this applies/);
});

it("can cite a guideline read in an earlier turn", () => {
  const html = render([
    read,
    {
      id: "follow-up",
      role: "user",
      parts: [{ type: "text", text: "Where should I put the labels?" }],
    },
    answer(),
  ]);

  expect(html).toContain("Place each series name beside its line.");
  expect(html).toContain('aria-label="Primary: Label series directly"');
});

const searchPart: EveMessage["parts"][number] = {
  type: "dynamic-tool",
  toolCallId: "search-labels",
  toolName: "search_guidelines",
  state: "output-available",
  input: { query: "line labels", method: "keyword" },
  output: {
    method: "keyword",
    matches: [
      {
        id: "direct-labels",
        title: "Label series directly",
        description: "Place the name by its series.",
        url: "https://chartcoach.dev/guidelines/direct-labels",
      },
      {
        id: "clear-legend",
        title: "Keep legends readable",
        description: "Make the legend easy to follow.",
        url: "https://chartcoach.dev/guidelines/clear-legend",
      },
    ],
  },
};

it("shows a retry notice when a response cites an unread search match", () => {
  const html = render([answer(feedback, {}, [searchPart])]);
  expect(html).toContain("The answer needs another evidence check.");
  expect(html).not.toContain("Place each series name beside its line.");
});

it("withholds an answer when its read citation points outside the catalog", () => {
  const html = render([
    {
      ...read,
      parts: [
        {
          type: "dynamic-tool",
          toolCallId: "read-unsafe",
          toolName: "read_guidelines",
          state: "output-available",
          input: { ids: ["direct-labels"] },
          output: {
            guidelines: [
              {
                id: "direct-labels",
                title: "Label series directly",
                description: "Place the name by its series.",
              },
            ],
            citations: [
              {
                id: "direct-labels",
                url: "https://example.com/guidelines/direct-labels",
                sources: [],
              },
            ],
          },
        },
      ],
    },
    answer(),
  ]);

  expect(html).toContain("The answer needs another evidence check.");
  expect(html).not.toContain("Place each series name beside its line.");
});

function additionalRead(ids: string[]): EveMessage["parts"][number] {
  return {
    type: "dynamic-tool",
    toolCallId: "support-read",
    toolName: "read_guidelines",
    state: "output-available",
    input: { ids },
    output: {
      guidelines: ids.map((id) => ({
        id,
        title: `Guidance for ${id}`,
        description: `Design guidance for ${id}.`,
      })),
      citations: ids.map((id) => ({
        id,
        url: `https://chartcoach.dev/guidelines/${id}`,
        sources: [],
      })),
    },
  };
}

it("distinguishes explicit supporting evidence from other search candidates", () => {
  const html = render([
    answer(
      {
        ...feedback,
        points: [{ ...feedback.points[0], supporting_guideline_ids: ["readability"] }],
      },
      { status: "complete" },
      [searchPart, ...read.parts, additionalRead(["readability"])],
    ),
  ]);

  expect(html).toContain('aria-label="Primary: Label series directly"');
  expect(html).toContain('aria-label="Supporting: Guidance for readability"');
  expect(html).toMatch(/Supporting <span[^>]*>1<\/span>/);
  expect(html).toMatch(/Explored <span[^>]*>1<\/span>/);
  expect(html).not.toMatch(/<details[^>]* open[=> ]/);
  expect(html).toMatch(/<details[^>]*><summary[^>]*>Why this applies/);
  expect(html).toMatch(
    /<dt[^>]*>Guideline guidance<\/dt><dd[^>]*>Place the name by its series\.<\/dd>/,
  );
});

it("communicates respected, violated, and uncertain findings with distinct next actions", () => {
  const errors = vi.spyOn(console, "error");

  const result = {
    ...feedback,
    points: [
      { ...feedback.points[0], assessment: "violated" },
      {
        primary_guideline_id: "contrast",
        supporting_guideline_ids: [],
        assessment: "respected",
        context: "Labels contrast clearly with the background.",
        recommendation: "Keep this contrast.",
      },
      {
        primary_guideline_id: "ordering",
        supporting_guideline_ids: [],
        assessment: "uncertain",
        context: "The intended category order is unclear.",
        recommendation: "Check whether category order has domain meaning.",
      },
    ],
  };

  const html = render([
    answer(result, { status: "complete" }, [
      ...read.parts,
      additionalRead(["contrast", "ordering"]),
    ]),
  ]);

  expect(html).toContain("Improve");
  expect(html).toContain("Working well");
  expect(html).toContain(">Check</h3>");
  expect(html).toContain("Place each series name beside its line.");
  expect(html).toContain("Keep this contrast.");
  expect(html).toContain("Check whether category order has domain meaning.");
  expect(errors).not.toHaveBeenCalled();
  errors.mockRestore();
});

it("uses verified SQL matches for previews and treats arbitrary SQL cells as data", () => {
  const html = render([
    answer(
      { workflow: "visfeedback", status: "no_match", points: [], question: null },
      { status: "complete" },
      [
        {
          type: "dynamic-tool",
          toolCallId: "sql",
          toolName: "query_catalog",
          state: "output-available",
          input: { sql: "SELECT id, title FROM guidelines" },
          output: {
            method: "sql",
            columns: [
              { name: "id", type: "VARCHAR" },
              { name: "title", type: "VARCHAR" },
            ],
            rows: [["direct-labels", "A made-up recommendation"]],
            row_count: 1,
            limit: 20,
            truncated: false,
            matches: [
              {
                id: "direct-labels",
                title: "Label series directly",
                description: "Place the name by its series.",
                url: "https://chartcoach.dev/guidelines/direct-labels",
              },
            ],
          },
        },
      ],
    ),
  ]);

  expect(html).toContain("I could not find an applicable guideline");
  expect(html).toContain('aria-label="Search results"');
  expect(html).toContain('aria-label="Read guideline: Label series directly"');
});

it("renders recommendation emphasis while keeping authored links and images inert", () => {
  const html = render([
    read,
    answer(
      {
        ...feedback,
        points: [
          {
            ...feedback.points[0],
            recommendation:
              "Use **direct labels**. [Reference](https://example.com/track) ![image](https://example.com/image.png) <iframe src='https://example.com/frame'></iframe>",
          },
        ],
      },
      { status: "complete" },
    ),
  ]);

  expect(html).toMatch(/<strong\b[^>]*>direct labels<\/strong>/);
  expect(html).not.toContain('href="https://example.com');
  expect(html).not.toContain('src="https://example.com');
  expect(html).not.toContain("<iframe");
});

it("keeps an accepted answer visible when its turn is cancelled", () => {
  const html = renderToStaticMarkup(
    <Transcript
      messages={[read, answer(feedback, { status: "complete", turnId: "cancelled" })]}
      attachments={new Map()}
      stoppedTurnIds={new Set(["cancelled"])}
    />,
  );

  expect(html).toContain("Response stopped.");
  expect(html).toContain("Place each series name beside its line.");
});

it("requires a successful read result before accepting a citation", () => {
  const html = render([
    {
      ...read,
      parts: [
        {
          type: "dynamic-tool",
          toolCallId: "failed-read",
          toolName: "read_guidelines",
          input: { ids: ["direct-labels"] },
          state: "output-error",
          errorText: "Catalog unavailable.",
        },
      ],
    },
    answer(),
  ]);

  expect(html).toContain("The answer needs another evidence check.");
  expect(html).not.toContain("Place each series name beside its line.");
});

it("waits for the final read result before accepting a citation", () => {
  const parts = read.parts.map((part) =>
    part.type === "dynamic-tool" && part.state === "output-available"
      ? { ...part, partial: true as const }
      : part,
  );

  const html = render([{ ...read, parts }, answer()]);
  expect(html).toContain("The answer needs another evidence check.");
  expect(html).not.toContain("Place each series name beside its line.");
});

it.each([
  {
    workflow: "visfeedback",
    status: "needs_context",
    question: "What should the reader compare?",
    expected: "What should the reader compare?",
  },
  {
    workflow: "visfeedback",
    status: "no_match",
    question: null,
    expected: "I could not find an applicable guideline",
  },
  {
    workflow: "visfeedback",
    status: "out_of_scope",
    question: null,
    expected: "I can review a chart, recommend a design, or discuss visualization choices",
  },
])("renders the $status response", ({ status, question, expected }) => {
  const html = render([
    answer({ workflow: "visfeedback", status, points: [], question }, { status: "complete" }),
  ]);

  expect(html).toContain(expected);
  expect(html).not.toContain("<img");
});
