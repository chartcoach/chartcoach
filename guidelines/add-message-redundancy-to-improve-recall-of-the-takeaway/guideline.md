---
id: add-message-redundancy-to-improve-recall-of-the-takeaway
title: Add message redundancy so the main takeaway is stated in multiple ways
bibliography: references.bib
description: Explicitly restating the conclusion via annotations or text is associated
  with higher-quality recall.
labels:
- chart:general
- task:communicate
- visual:annotation
- impact:comprehension
- data:general
- audience:general
- strategy:redundancy
---

## State the message more than once using text and annotations <!-- role: advice -->

Express the visualization’s main conclusion redundantly using text, annotations, or labels in addition to the primary data encoding.

## Why message redundancy improves recall <!-- role: reason -->

When the conclusion is explicitly encoded in more than one form, viewers have multiple retrieval routes for the same takeaway, which improves what they can later describe.

**Mechanism:** Redundant qualitative cues reduce the chance that viewers miss the intended message and increase the likelihood the takeaway is encoded into memory.

**Evidence:** Visualizations with message redundancy had higher average recall-description quality than those without; the top third of best-described visualizations contained message redundancy much more often than the bottom third [@borkinMemorabilityVisualizationRecognition2016].

**Notes:** Message redundancy was common in venues emphasizing clear communication (infographics, news).

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Understand and later restate the main point correctly.
- **Task:** Summarize the conclusion; remember key trend/relationship.
- **Data:** Any data where a “so what” conclusion exists.
- **Chart Setting:** Explanatory communication where misinterpretation is costly.
- **Audience:** Broad audiences, including non-experts.
- **Success Criterion:** High-quality recall descriptions that include the message.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The goal is open-ended exploration without a single intended takeaway. **Why:** Forcing a single message can bias interpretation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Space and visual minimalism. **Risk:** Over-annotation can clutter the view and distract from data reading. **Mitigation:** Keep redundant message statements short and targeted.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding extra text that repeats context but not the conclusion. **Why it fails:** It increases reading time without reinforcing the intended takeaway.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers describe chart parts but cannot articulate the main conclusion. **Quick Check:** Ask a viewer for the “one-sentence takeaway” after a short view. **Stronger Test:** Compare recall-description quality between a version with and without explicit takeaway annotations.

## What to do instead <!-- role: fix -->

- Add a concise takeaway sentence near the data region summarizing the trend.
- Annotate key points or outliers with short labels that encode the conclusion.
- Use a title that states the conclusion if there is no room for additional annotations.
- Remove non-essential decorative elements to make room for message cues.
