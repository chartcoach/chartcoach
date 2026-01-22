---
id: design-graphs-to-support-a-task-relevant-anchor-point
title: Design graphs so a task-relevant anchor point is visually and conceptually
  unambiguous
bibliography: references.bib
description: Make the intended comparison dimension and its natural anchor feature
  easy to pick as the first attended element.
labels:
- chart:bar
- task:compare
- visual:attention
- impact:clarity
- data:categorical
- audience:novice
- concept:visual-routines
---

## Make the task-relevant comparison dimension yield a clear anchor point <!-- role: advice -->

Make the task-relevant dimension in a graph produce an obvious “anchor” element that a viewer can attend to first. Avoid designs where multiple dimensions offer competing anchors for the same items.

## Task-relevant anchor points steer what relation gets extracted <!-- role: reason -->

Between-value comparisons are carried out as ordered attentional routines: viewers first select an “anchor” object defined by a feature in the task-relevant dimension and then use that selection to extract the relation (for example, extracting a size relation by first attending to the taller bar). When multiple dimensions vary, the visual system must still choose a first attended object, and that choice is tied to which relation is computed.

**Mechanism:** A clear anchor point reduces ambiguity about which object is treated as the target in the comparison, making the intended relation easier to compute and less likely to be derailed by other potential relations.

**Evidence:** In two-bar graphs, first saccades clustered on the taller bar for size judgments and on the darker bar for contrast judgments, indicating systematic anchor-based routines for each comparison type [@michalVisualRoutinesAre2017]. When both size and contrast varied but only one dimension was relevant, first-saccade preferences followed the anchor point for the task-relevant dimension rather than the irrelevant one [@michalVisualRoutinesAre2017].

**Notes:** Anchor preferences were idiosyncratic across individuals (some preferred the opposite feature), but were consistent within an individual and tracked the relevant dimension during the task [@michalVisualRoutinesAre2017].

## When graphs invite multiple competing comparisons <!-- role: context -->

- **User Goal:** Determine which of two values is larger along a specified dimension (e.g., size-based quantity or color-based category).
- **Task:** Classify a two-item configuration (e.g., which value is larger, which feature comes first).
- **Data:** Two categories/conditions with one intended comparison dimension; other visual dimensions may vary incidentally.
- **Chart Setting:** Simple bar charts or other two-object comparisons where items can vary in multiple features.
- **Audience:** Learners or general audiences performing quick relational judgments.
- **Success Criterion:** Fast, accurate extraction of the intended relation with minimal distraction.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The goal is to encourage noticing multiple different relations in the same display (e.g., exploration rather than a single specified comparison). **Why:** A single dominant anchor supports one relation and can deprioritize other potentially relevant relations [@michalVisualRoutinesAre2017].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Emphasizing a single anchor can reduce visual parity between items and may make secondary dimensions feel less available. **Risk:** If the viewer’s preferred anchor differs from the designer’s assumption, emphasis may not align with their routine. **Mitigation:** Keep the intended task explicit so the relevant dimension governs the routine.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding multiple varying dimensions on the same two bars without clarifying which dimension is meant to be compared. **Why it fails:** Viewers can be pulled toward different anchor points (e.g., “tall” vs “dark”), increasing competition during relation extraction [@michalVisualRoutinesAre2017].

## Quick tests <!-- role: check -->

**Failure Sign:** People hesitate or look back and forth before committing to a comparison, especially when features disagree across dimensions. **Quick Check:** Identify whether the intended comparison dimension has a natural “extreme” (e.g., tallest/darkest) that stands out as the first attended item. **Stronger Test:** Run a small eye-tracking or click-first pilot to see whether first selections cluster on the intended anchor when irrelevant features vary.

## What to do instead <!-- role: fix -->

- Make irrelevant dimensions constant when the task is a single-dimension comparison.
- Separate dimensions into different panels if both must vary and both matter.
- Add explicit task framing in nearby text that names the dimension to compare.
- Redesign encodings so the irrelevant dimension does not create an equally strong competing anchor on a different object.
