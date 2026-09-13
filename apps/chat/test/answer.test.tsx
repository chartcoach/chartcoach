// @vitest-environment jsdom
import { renderDocument } from "./render-document";
import type { EveDynamicToolPart, EveMessage } from "eve/react";
import { expect, it } from "vite-plus/test";
import { Transcript } from "./transcript";

const readPart = {
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
      { id: "direct-labels", url: "https://chartcoach.dev/guidelines/direct-labels", sources: [] },
    ],
  },
} satisfies EveDynamicToolPart;

const read: EveMessage = { id: "read", role: "assistant", parts: [readPart] };

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
  return renderDocument(
    <Transcript messages={messages} attachments={new Map()} stoppedTurnIds={new Set()} />,
  );
}

it("offers another evidence check when a completed turn has no presentation", () => {
  const page = render([
    { id: "empty", role: "assistant", metadata: { status: "complete" }, parts: [] },
  ]);

  expect(page.body.textContent).toContain("The answer needs another evidence check.");
  expect(page.body.textContent).toContain("Try again");
});

it.each([
  ["visfeedback", "In your chart", "violated"],
  ["discuss", "Your question", null],
  ["visrec", "Your brief", null],
] as const)(
  "renders grounded %s advice with a local citation and expandable context",
  (workflow, label, assessment) => {
    const page = render([
      answer(
        { ...feedback, workflow, points: [{ ...feedback.points[0], assessment }] },
        {},
        read.parts,
      ),
    ]);

    const article = page.querySelector("article")!;
    expect(article.textContent).toContain("Place each series name beside its line.");
    expect(
      article.querySelector('a[aria-label="Primary: Label series directly"]')?.getAttribute("href"),
    ).toBe("/guideline?id=direct-labels");

    const context = article.querySelector<HTMLDetailsElement>(
      'ol[aria-label="Guideline-backed advice"] details',
    )!;

    expect(context.open).toBe(false);
    expect(context.querySelector("summary")?.textContent).toBe("Why this applies");
    expect(Array.from(context.querySelectorAll("dt"), (term) => term.textContent)).toEqual([
      label,
      "Guideline guidance",
    ]);
    expect(
      Array.from(context.querySelectorAll("dd"), (definition) => definition.textContent),
    ).toEqual(["The legend is far from the lines.", "Place the name by its series."]);
    expect(
      Array.from(
        article.querySelectorAll('ol[aria-label="Guideline-backed advice"] h3'),
        (heading) => heading.textContent,
      ),
    ).toEqual(assessment ? ["Improve"] : []);
  },
);

it("can cite a guideline read in an earlier turn", () => {
  const page = render([
    read,
    {
      id: "follow-up",
      role: "user",
      parts: [{ type: "text", text: "Where should I put the labels?" }],
    },
    answer(),
  ]);

  expect(page.body.textContent).toContain("Place each series name beside its line.");
  expect(
    page.querySelector('article a[aria-label="Primary: Label series directly"]'),
  ).not.toBeNull();
});

const searchPart: EveDynamicToolPart = {
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

it.each([
  { evidence: "an unread search match", part: searchPart },
  {
    evidence: "a read citation outside the catalog",
    part: {
      ...readPart,
      output: {
        ...readPart.output,
        citations: [
          { ...readPart.output.citations[0], url: "https://example.com/guidelines/direct-labels" },
        ],
      },
    },
  },
  {
    evidence: "a failed read",
    part: {
      type: "dynamic-tool",
      toolCallId: "failed-read",
      toolName: "read_guidelines",
      input: { ids: ["direct-labels"] },
      state: "output-error",
      errorText: "Catalog unavailable.",
    },
  },
  { evidence: "a partial read", part: { ...readPart, partial: true } },
] satisfies { evidence: string; part: EveDynamicToolPart }[])(
  "withholds advice based on $evidence",
  ({ part }) => {
    const page = render([answer(feedback, {}, [part])]);
    expect(page.body.textContent).toContain("The answer needs another evidence check.");
    expect(page.body.textContent).not.toContain("Place each series name beside its line.");
  },
);

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
  const page = render([
    answer(
      {
        ...feedback,
        points: [{ ...feedback.points[0], supporting_guideline_ids: ["readability"] }],
      },
      { status: "complete" },
      [searchPart, ...read.parts, additionalRead(["readability"])],
    ),
  ]);

  const citations = page.querySelectorAll('ol[aria-label="Guideline-backed advice"] a');
  expect(Array.from(citations, (link) => link.getAttribute("aria-label"))).toEqual([
    "Primary: Label series directly",
    "Supporting: Guidance for readability",
  ]);

  const groups = Array.from(page.querySelectorAll("button"), (button) =>
    button.textContent?.trim(),
  );

  expect(groups).toEqual(expect.arrayContaining(["Supporting 1", "Explored 1"]));
});

it("communicates respected, violated, and uncertain findings with distinct next actions", () => {
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

  const page = render([
    answer(result, { status: "complete" }, [
      ...read.parts,
      additionalRead(["contrast", "ordering"]),
    ]),
  ]);

  expect(
    Array.from(
      page.querySelectorAll('ol[aria-label="Guideline-backed advice"] h3'),
      (heading) => heading.textContent,
    ),
  ).toEqual(["Improve", "Working well", "Check"]);
  expect(page.body.textContent).toContain("Place each series name beside its line.");
  expect(page.body.textContent).toContain("Keep this contrast.");
  expect(page.body.textContent).toContain("Check whether category order has domain meaning.");
});

it("uses verified SQL matches for evidence previews", () => {
  const page = render([
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

  expect(page.body.textContent).toContain("I could not find an applicable guideline");
  expect(
    page
      .querySelector(
        'section[aria-label="Search results"] a[aria-label="Read guideline: Label series directly"]',
      )
      ?.getAttribute("href"),
  ).toBe("/guideline?id=direct-labels");
});

it("renders recommendation emphasis while keeping authored links and images inert", () => {
  const page = render([
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

  const advice = page.querySelector('ol[aria-label="Guideline-backed advice"]')!;
  expect(advice.querySelector("strong")?.textContent).toBe("direct labels");
  expect(Array.from(advice.querySelectorAll("a"), (link) => link.getAttribute("href"))).toEqual([
    "/guideline?id=direct-labels",
  ]);
  expect(advice.querySelectorAll("img, iframe")).toHaveLength(0);
});

it("keeps an accepted answer visible when its turn is cancelled", () => {
  const page = renderDocument(
    <Transcript
      messages={[read, answer(feedback, { status: "complete", turnId: "cancelled" })]}
      attachments={new Map()}
      stoppedTurnIds={new Set(["cancelled"])}
    />,
  );

  expect(page.body.textContent).toContain("Response stopped.");
  expect(page.body.textContent).toContain("Place each series name beside its line.");
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
  const page = render([
    answer({ workflow: "visfeedback", status, points: [], question }, { status: "complete" }),
  ]);

  expect(page.body.textContent).toContain(expected);
});
