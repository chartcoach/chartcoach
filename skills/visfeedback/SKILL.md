---
name: visfeedback
description: Review a rendered visualization with chartcoach guidelines and source citations.
---

# chartcoach Visfeedback

Inspect the rendered chart, find relevant guideline entry records, and connect
each feedback claim to visible evidence. Read `core` for catalog selection,
retrieval, and citation. Use `visrec` when the task starts from a design brief.

## Inspect the chart

Record the state being reviewed:

| Field             | Record                                                                           |
| ----------------- | -------------------------------------------------------------------------------- |
| Chart             | Marks, encodings, variables, units, scales, and layout                           |
| Reader task       | Overview, lookup, comparison, trend, distribution, relation, or anomaly          |
| Supporting text   | Title, labels, legend, axes, annotations, tooltips, and source notes             |
| Interaction state | Default, hover, selected, toggled, animated, or keyboard state                   |
| Risk              | Ambiguity, overplotting, hidden identity, clipping, contrast, or missing context |
| Evidence          | Screenshot, rendered page, accessibility snapshot, data, or inference            |
| Uncertainty       | Unreadable values, ambiguous marks, missing context, and untested behavior       |

Inspect every state you discuss. Use the rendered chart for visual claims and
an accessibility snapshot for names and structure.

Separate what you can observe from what you infer. Confirm the marks and
encoding before retrieving chart-family advice. If an image is ambiguous,
qualify the interpretation or request the smallest missing evidence, such as a
larger image or the underlying chart. A retrieved guideline cannot confirm
what the image depicts.

## Find records

Follow `core` to query the observed chart, task, and risks. Search concepts such
as `labels`, `overlap`, and `contrast` separately with `contains`, or combine
them in full-text search when a profile is available. Base retrieval on
observed facts and keep uncertain interpretations explicit.

## Check each record

Read selected records together before citing them, using the host's tools or
the access recipes in `core`.

For each record, decide whether it:

- applies and the chart follows it
- applies and the chart violates it
- is related but outside this case
- cannot be judged from the available evidence

Discard records whose chart family, reader task, data type, or interaction
state differs from the observed case. A screenshot can support layout and
labeling claims. Hover, keyboard, and animation claims need evidence from
those states. Read the applicable situations and exceptions even when the
title appears to match. A citation establishes which source is attached to a
record. Inspect that source before attributing a specific claim to it.

When evidence is missing, state which conclusion cannot be made and the next
inspection needed. Continue with the feedback supported by the available
evidence.

## Assess the requirement

Identify each guideline's testable requirement from its description, advice,
and checks. Preserve its conditions and placement. A related good feature is
not a substitute for satisfying that requirement. Omit a guideline when the
situation it addresses is absent.

- `respected`: An observed or explicitly stated feature satisfies the actual
  requirement. Explain the feature and recommend retaining it.
- `violated`: An observed or explicitly stated feature conflicts with the
  requirement and its conditions apply. State the mismatch and supported change.
- `uncertain`: Evidence cannot establish compliance. Name the missing detail
  and the specific check needed.

A missing or cropped feature is not evidence of a violation. The absence of a
recommended feature alone cannot establish a violation of a conditional rule.
Apply the conditions to strengths as strictly as to problems. Before calling a
rule respected or violated, state which fact establishes its required reader
task, available space, or reading context. A compatible-looking arrangement
cannot establish an unstated task. When that condition is unknown, omit the
point if it adds no decision, or mark it uncertain and ask what would establish
applicability. Do not fill the answer with conditional rules presented as
confirmed strengths.

Before answering, compare the requirement, observation, assessment, and action.
If the action adds a required feature, the existing chart cannot be respected
for that requirement. Use violated when the absence is observable and the rule
applies, or uncertain when evidence is insufficient. Keep the requirement as
qualified in the entry rather than strengthening it into a stricter rule.

## Write the feedback

For each point, connect:

```text
suggested change or decision to preserve the design
  -> visible chart evidence
  -> guideline entry ID, title, and applicable section
  -> tradeoff or missing evidence
  -> source citation
```

Group overlapping rules into one design decision. Prioritize consequential
changes, then relevant strengths and unresolved checks. Consider strengths and
problems on their evidence. Avoid inventing either to balance the answer.
Keep each action within the primary and supporting entries' actual guidance.
