---
id: respect-graph-schemas-and-conventions
title: Match chart type to the message implied by common graph conventions
bibliography: references.bib
description: Choose formats that align with learned graph schemas so viewers infer
  the intended relationships.
labels:
- chart:bar
- task:interpret
- visual:position
- impact:trust
- data:categorical
- audience:novice
- complexity:foundational
---

## Choose a format whose conventional meaning matches your intended takeaway <!-- role: advice -->

Use common chart types in ways that align with what viewers typically expect them to communicate, such as using bar charts for discrete comparisons and line charts for continuous trends. Avoid repurposing a familiar format in a way that invites a different inference than you intend.

## Viewers apply learned schemas when reading graphs <!-- role: reason -->

Graph comprehension relies on schemas: learned expectations about how visual elements map to variables and what relationships the format emphasizes. When a design violates these expectations, viewers may extract unintended messages even if the plotted values are correct.

**Mechanism:** A schema guides attention and interpretation by suggesting what relations are meaningful (comparisons vs trends) and how to map marks and axes to real-world referents.

**Evidence:** Viewers’ descriptions of the same data differ depending on whether it is shown as bars or lines, reflecting expectations that bar graphs emphasize comparisons and line graphs emphasize trends, and mismatches can prompt incorrect inferences [@zacksDesigningGraphsDecisionMakers2020].

**Notes:** Conventions are a form of shared prior knowledge; breaking them increases the burden on explanation and attention guidance.

## Apply when communicating to broad audiences <!-- role: context -->

- **User Goal:** Quickly grasp what the data mean and what relationships to extract.
- **Task:** Interpret the message, summarize the pattern, make a decision based on the display.
- **Data:** Discrete categories vs continuous sequences (especially time).
- **Chart Setting:** Public reports, media, policy briefs, regulated disclosures.
- **Audience:** Non-specialists who rely heavily on familiar formats.
- **Success Criterion:** Viewers produce the intended qualitative interpretation without coaching.

## When you must break convention to show a rare structure <!-- role: exceptions -->

**Break it when:** The data structure cannot be represented with common formats without hiding critical relationships. **Why:** Forcing a conventional format can obscure the message more than it helps.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Conventional formats may limit novelty or compactness. **Risk:** Over-reliance on convention can produce generic charts that fail to emphasize the decision-relevant message. **Mitigation:** Use conventional structure plus selective highlighting and annotation to emphasize the point.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a line chart to connect categories where continuity is not meaningful. **Why it fails:** Viewers may infer a continuous trend or intermediate values that do not exist [@zacksDesigningGraphsDecisionMakers2020].
- **Mistake:** Using a bar chart when the main message is about smooth change over a sequence. **Why it fails:** The format encourages discrete comparisons rather than perceiving an overall trend [@zacksDesigningGraphsDecisionMakers2020].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers describe a different relationship than intended (e.g., a “trend” when you meant a “group difference”). **Quick Check:** Ask a reader to describe the pattern in one sentence; if they emphasize the wrong relationship, the schema is mismatched. **Stronger Test:** Show two candidate chart types and compare which yields the intended description more often.

## What to do instead <!-- role: fix -->

- Switch to a chart type whose conventional schema matches the intended relationship (comparison vs trend).
- If you must keep the format, add explicit labeling of what the axes and marks represent and what comparison to make.
- Separate discrete and continuous aspects into separate views rather than forcing one ambiguous form.
- Use layout and grouping to reinforce the intended interpretation of the structure.
