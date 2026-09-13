import { expect, it } from "vite-plus/test";
import { answerSchema, validateAnswer, type Answer } from "../shared/answer";

const point = {
  primary_guideline_id: "labels",
  supporting_guideline_ids: [],
  assessment: "violated",
  context: "The legend is far from the lines.",
  recommendation: "Place each series name beside its line.",
} satisfies Answer["points"][number];

const answer = {
  workflow: "visfeedback",
  status: "answer",
  points: [point],
  question: null,
} satisfies Answer;

const readIds = new Set(["labels", "contrast", "readability"]);

it.each([
  { reason: "malformed output", value: null },
  {
    reason: "unknown primary guideline",
    value: { ...answer, points: [point, { ...point, primary_guideline_id: "unknown" }] },
  },
  { reason: "duplicate primary guideline", value: { ...answer, points: [point, point] } },
  { reason: "empty feedback", value: { ...answer, points: [] } },
  { reason: "feedback with question", value: { ...answer, question: "What is your goal?" } },
  { reason: "fallback with feedback", value: { ...answer, status: "no_match" } },
  { reason: "missing context question", value: { ...answer, status: "needs_context", points: [] } },
  { reason: "malformed point", value: { ...answer, points: [{ primary_guideline_id: "labels" }] } },
  { reason: "assessment on a design recommendation", value: { ...answer, workflow: "visrec" } },
  {
    reason: "unread support",
    value: { ...answer, points: [{ ...point, supporting_guideline_ids: ["unread"] }] },
  },
  {
    reason: "primary used as support",
    value: { ...answer, points: [{ ...point, supporting_guideline_ids: ["labels"] }] },
  },
  {
    reason: "duplicate support",
    value: {
      ...answer,
      points: [{ ...point, supporting_guideline_ids: ["readability", "readability"] }],
    },
  },
])("rejects $reason", ({ value }) => {
  expect(validateAnswer(answerSchema.safeParse(value).data, readIds)).toBeUndefined();
});

it("allows a read supporting guideline to support multiple distinct findings", () => {
  const value = {
    ...answer,
    points: [
      { ...point, supporting_guideline_ids: ["readability"] },
      { ...point, primary_guideline_id: "contrast", supporting_guideline_ids: ["readability"] },
    ],
  };

  expect(validateAnswer(value, readIds)).toEqual(value);
});
