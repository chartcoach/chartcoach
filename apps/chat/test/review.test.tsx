import { renderToStaticMarkup } from "react-dom/server";
import type { EveMessage } from "eve/react";
import { expect, it } from "vite-plus/test";
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
  status: "feedback",
  feedback: [
    {
      primary_guideline_id: "direct-labels",
      supporting_guideline_ids: [],
      assessment: "violated",
      observation: "The legend is far from the lines.",
      recommendation: "Place each series name beside its line.",
    },
  ],
  question: null,
};
function answer(
  metadata: EveMessage["metadata"] = { status: "complete", result: feedback },
): EveMessage {
  return { id: "answer", role: "assistant", metadata, parts: [] };
}
function render(messages: EveMessage[]) {
  return renderToStaticMarkup(
    <Transcript messages={messages} attachments={new Map()} stoppedTurnIds={new Set()} />,
  );
}

it("renders an action with a verified citation and its observation on demand", () => {
  const html = render([{ ...answer(), parts: read.parts }]);
  expect(html).toContain("The legend is far from the lines.");
  expect(html).toMatch(
    /<dt[^>]*>Guideline requires<\/dt><dd[^>]*>Place the name by its series\.<\/dd>/,
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

it("shows the primary guideline before a collapsed group of other retrieved candidates", () => {
  const html = render([{ ...answer(), parts: [searchPart, ...read.parts] }]);
  expect(html).not.toContain("<img ");
  expect(html).toContain('aria-label="Preview Label series directly"');
  expect(html.indexOf('aria-label="Primary guidelines"')).toBeGreaterThan(
    html.indexOf("Place each series name beside its line."),
  );
  expect(html).toMatch(/Explored <span[^>]*>1<\/span>/);
});

it("shows a retry notice when a response cites an unread search match", () => {
  const html = render([{ ...answer(), parts: [searchPart] }]);
  expect(html).toContain("The review could not be verified");
  expect(html).not.toContain("Place each series name beside its line.");
  expect(html).not.toContain("<img ");
  expect(html).not.toContain('aria-label="Primary guidelines"');
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
    {
      ...answer({
        status: "complete",
        result: {
          ...feedback,
          feedback: [{ ...feedback.feedback[0], supporting_guideline_ids: ["readability"] }],
        },
      }),
      parts: [searchPart, ...read.parts, additionalRead(["readability"])],
    },
  ]);
  expect(html).toContain('aria-label="Primary: Label series directly"');
  expect(html).toContain('aria-label="Supporting: Guidance for readability"');
  expect(html).toMatch(/Supporting <span[^>]*>1<\/span>/);
  expect(html).toMatch(/Explored <span[^>]*>1<\/span>/);
  expect(html).not.toMatch(/<details[^>]* open[=> ]/);
  expect(html).toMatch(/<details[^>]*><summary[^>]*>Why this applies/);
  expect(html).toMatch(
    /<dt[^>]*>Guideline requires<\/dt><dd[^>]*>Place the name by its series\.<\/dd>/,
  );
});

it("communicates respected, violated, and uncertain findings with distinct next actions", () => {
  const result = {
    ...feedback,
    feedback: [
      { ...feedback.feedback[0], assessment: "violated" },
      {
        primary_guideline_id: "contrast",
        supporting_guideline_ids: [],
        assessment: "respected",
        observation: "Labels contrast clearly with the background.",
        recommendation: "Keep this contrast.",
      },
      {
        primary_guideline_id: "ordering",
        supporting_guideline_ids: [],
        assessment: "uncertain",
        observation: "The intended category order is unclear.",
        recommendation: "Check whether category order has domain meaning.",
      },
    ],
  };
  const html = render([
    {
      ...answer({ status: "complete", result }),
      parts: [...read.parts, additionalRead(["contrast", "ordering"])],
    },
  ]);
  expect(html).toContain("Improve");
  expect(html).toContain("Working well");
  expect(html).toContain(">Check</h3>");
  expect(html).toContain("Place each series name beside its line.");
  expect(html).toContain("Keep this contrast.");
  expect(html).toContain("Check whether category order has domain meaning.");
});

it.each([
  { reason: "unread support", supporting: ["clear-legend"] },
  { reason: "primary used as support", supporting: ["direct-labels"] },
  { reason: "duplicate support", supporting: ["readability", "readability"] },
])("rejects $reason", ({ supporting }) => {
  const result = {
    ...feedback,
    feedback: [{ ...feedback.feedback[0], supporting_guideline_ids: supporting }],
  };
  const html = render([
    {
      ...answer({ status: "complete", result }),
      parts: [searchPart, ...read.parts, additionalRead(["readability"])],
    },
  ]);
  expect(html).toContain("The review could not be verified");
  expect(html).not.toContain("Place each series name beside its line.");
});

it("allows a read supporting guideline to support multiple findings", () => {
  const result = {
    ...feedback,
    feedback: [
      { ...feedback.feedback[0], supporting_guideline_ids: ["readability"] },
      {
        ...feedback.feedback[0],
        primary_guideline_id: "contrast",
        supporting_guideline_ids: ["readability"],
      },
    ],
  };
  const html = render([
    {
      ...answer({ status: "complete", result }),
      parts: [...read.parts, additionalRead(["readability", "contrast"])],
    },
  ]);
  expect(html).not.toContain("The review could not be verified");
  expect(html.match(/aria-label="Supporting: Guidance for readability"/g)).toHaveLength(2);
});

it("uses verified SQL matches for previews and treats arbitrary SQL cells as data", () => {
  const html = render([
    {
      ...answer({
        status: "complete",
        result: { status: "no_match", feedback: [], question: null },
      }),
      parts: [
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
    },
  ]);
  expect(html).toContain("I could not find an applicable guideline");
  expect(html).not.toContain("Place each series name beside its line.");
  expect(html).toMatch(/Explored <span[^>]*>1<\/span>/);
  expect(html).not.toContain('aria-label="A made-up recommendation');
});

it("renders recommendation emphasis while keeping authored links and images inert", () => {
  const html = render([
    read,
    answer({
      status: "complete",
      result: {
        ...feedback,
        feedback: [
          {
            ...feedback.feedback[0],
            recommendation:
              "Use **direct labels**. [Reference](https://example.com/track) ![image](https://example.com/image.png) <iframe src='https://example.com/frame'></iframe>",
          },
        ],
      },
    }),
  ]);
  expect(html).toContain("direct labels");
  expect(html).not.toContain("**direct labels**");
  expect(html).not.toContain('href="https://example.com');
  expect(html).not.toContain('src="https://example.com');
  expect(html).not.toContain("<iframe");
});

it("does not display a completed result from a cancelled turn", () => {
  const html = renderToStaticMarkup(
    <Transcript
      messages={[read, answer({ status: "complete", turnId: "cancelled", result: feedback })]}
      attachments={new Map()}
      stoppedTurnIds={new Set(["cancelled"])}
    />,
  );
  expect(html).toContain("Response stopped.");
  expect(html).not.toContain("Place each series name beside its line.");
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
  expect(html).toContain("The review could not be verified");
  expect(html).not.toContain("Place each series name beside its line.");
});

it("blocks a review until all cited guidelines have been read", () => {
  const html = render([answer(), read]);
  expect(html).toContain("The review could not be verified");
  expect(html).not.toContain("Place each series name beside its line.");
});

it("waits for the final read result before accepting a citation", () => {
  const parts = read.parts.map((part) =>
    part.type === "dynamic-tool" && part.state === "output-available"
      ? { ...part, partial: true as const }
      : part,
  );
  const html = render([{ ...read, parts }, answer()]);
  expect(html).toContain("The review could not be verified");
  expect(html).not.toContain("Place each series name beside its line.");
});

it.each([
  { reason: "missing result", result: undefined },
  {
    reason: "unknown guideline",
    result: {
      ...feedback,
      feedback: [
        ...feedback.feedback,
        { ...feedback.feedback[0], primary_guideline_id: "unknown" },
      ],
    },
  },
  {
    reason: "duplicate guideline",
    result: { ...feedback, feedback: [...feedback.feedback, ...feedback.feedback] },
  },
  { reason: "empty feedback", result: { ...feedback, feedback: [] } },
  { reason: "feedback with question", result: { ...feedback, question: "What is your goal?" } },
  { reason: "fallback with feedback", result: { ...feedback, status: "no_match" } },
  {
    reason: "missing context question",
    result: { status: "needs_context", feedback: [], question: null },
  },
  {
    reason: "malformed item",
    result: { ...feedback, feedback: [{ primary_guideline_id: "direct-labels" }] },
  },
])("fails closed for $reason", ({ result }) => {
  const html = render([read, { ...answer(), metadata: { status: "complete", result } }]);
  expect(html).toContain("The review could not be verified");
  expect(html).not.toContain("Place each series name beside its line.");
});

it.each([
  "https://example.com/guidelines/direct-labels",
  "https://chartcoach.dev/guidelines/other-id",
  "https://chartcoach.dev/guidelines/direct-labels?redirect=elsewhere",
  "https://chartcoach.dev/guidelines/direct-labels#details",
  "https://user:password@chartcoach.dev/guidelines/direct-labels",
  "javascript:alert(1)",
])("rejects a citation with an unrelated or unsafe URL: %s", (url) => {
  const tool = read.parts[0];
  if (tool.type !== "dynamic-tool" || tool.state !== "output-available")
    throw new Error("Expected a completed read tool");
  const html = render([
    {
      ...read,
      parts: [
        {
          ...tool,
          output: {
            guidelines: [
              {
                id: "direct-labels",
                title: "Label series directly",
                description: "Place the name by its series.",
              },
            ],
            citations: [{ id: "direct-labels", url, sources: [] }],
          },
        },
      ],
    },
    answer(),
  ]);
  expect(html).toContain("The review could not be verified");
  expect(html).not.toContain("Place each series name beside its line.");
});

it.each([
  { id: "Direct_Labels", url: "https://chartcoach.dev/guidelines/Direct_Labels/", accepted: true },
  { id: "direct labels", url: "https://chartcoach.dev/guidelines/direct%20labels", accepted: true },
  { id: "..", url: "https://chartcoach.dev/guidelines/..", accepted: false },
  { id: ".", url: "https://chartcoach.dev/guidelines/%2e/", accepted: false },
  {
    id: "direct-labels?redirect=elsewhere",
    url: "https://chartcoach.dev/guidelines/direct-labels?redirect=elsewhere",
    accepted: false,
  },
])("validates the encoded guideline path for $id", ({ id, url, accepted }) => {
  const html = render([
    {
      ...read,
      parts: [
        {
          type: "dynamic-tool",
          toolCallId: "read-path",
          toolName: "read_guidelines",
          state: "output-available",
          input: { ids: [id] },
          output: {
            guidelines: [
              { id, title: "Label series directly", description: "Place the name by its series." },
            ],
            citations: [{ id, url, sources: [] }],
          },
        },
      ],
    },
    answer({
      status: "complete",
      result: { ...feedback, feedback: [{ ...feedback.feedback[0], primary_guideline_id: id }] },
    }),
  ]);
  if (accepted) {
    expect(html).toContain("Place each series name beside its line.");
    expect(html).toContain(`href="https://chartcoach.dev/guidelines/${encodeURIComponent(id)}"`);
  } else {
    expect(html).toContain("The review could not be verified");
    expect(html).not.toContain("Place each series name beside its line.");
  }
});

it.each(["streaming", "failed", "submitted"] as const)(
  "waits for successful completion before displaying a %s review",
  (status) => {
    const message = answer({ result: feedback, status });
    const html = render([read, message]);
    expect(html).not.toContain("Place each series name beside its line.");
  },
);

it.each([
  {
    status: "needs_context",
    question: "What should the reader compare?",
    expected: "What should the reader compare?",
  },
  { status: "no_match", question: null, expected: "I could not find an applicable guideline" },
  {
    status: "out_of_scope",
    question: null,
    expected: "I can review chart design using the Guideline Catalog",
  },
])("renders the $status response", ({ status, question, expected }) => {
  const html = render([answer({ status: "complete", result: { status, feedback: [], question } })]);
  expect(html).toContain(expected);
  expect(html).not.toContain("<img");
});
