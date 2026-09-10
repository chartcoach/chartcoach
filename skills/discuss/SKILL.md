---
name: discuss
description: Compare visualization choices with chartcoach guidelines and their source citations.
---

# chartcoach Discuss

Use guideline entry records to compare visualization choices or explain a
tradeoff. Read `core` for catalog selection, retrieval, and citation.

## Describe the decision

Record the facts that can change the answer:

| Field         | Record                                                            |
| ------------- | ----------------------------------------------------------------- |
| Decision      | What the user is choosing or trying to understand                 |
| Data and task | Variables, scales, units, number of categories, and reader task   |
| Audience      | Knowledge, accessibility needs, and decision context              |
| Medium        | Static, interactive, dashboard, paper, slide, or mobile           |
| Constraints   | Space, color, print, interaction, uncertainty, and target library |

Ask for a missing fact when it could change the recommendation. Otherwise
state the assumption beside the affected claim.

## Find records

Follow `core` to search each competing option and its constraints separately.
Use a short term or phrase with `contains`. Records matching both options can
explain when to choose one over the other. Use full-text search for combined
concepts when a profile exists, or SQL for section content and relationships.

## Check the records

Read selected records together using the host's tools or the access recipes in
`core`, then focus on the sections relevant to the decision.

Discard a record when its chart family, task, audience, data type, or
interaction state differs from the user's case. Check its applicable
situations and exceptions before using it to settle the comparison. Retrieval
rank describes the search result, not the strength of the evidence.

The entry's citations identify the published sources attached to the guideline.
Inspect a source before attributing an explanation or claim to it. Keep limits
on its applicability beside the affected recommendation.

## Write the answer

Choose the primary guideline for the claim being made, not merely for mentioning
the same chart element. Guidance on how to implement an option does not by itself
establish when to choose that option. Use the relevant conditions and exceptions
to ground the choice. When one guideline supports both alternatives, explain
their tradeoff together as one comparison point rather than assigning an
indirect primary source to each side.

For each recommendation or comparison, connect:

```text
decision
  -> fact from the user's case
  -> guideline entry ID, title, and applicable section
  -> tradeoff or remaining uncertainty
  -> source citation
```

Compare alternatives against the same task and constraints. Explain when the
recommendation changes, rather than declaring a universal winner. A discussion
can establish a tradeoff without an image. Use chart-compliance assessments
when the task actually asks to review a chart, following `visfeedback`.

Include an exact-read command or guideline link when another reviewer needs to
inspect the full record.
