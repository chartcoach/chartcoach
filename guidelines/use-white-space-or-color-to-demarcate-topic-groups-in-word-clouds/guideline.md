---
id: use-white-space-or-color-to-demarcate-topic-groups-in-word-clouds
title: Demarcate topic groups with white space separators or consistent per-group
  color
bibliography: references.bib
description: Make semantic group boundaries legible by adding clear separations using
  whitespace and/or consistent colors per group.
labels:
- chart:word-cloud
- task:infer
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- domain:text
---

## Add clear group boundaries using whitespace and/or one color per group <!-- role: advice -->

Demarcate each semantic topic group with visible separation, using whitespace gaps, a consistent color per group, or both. Do not rely on arbitrary coloring to signal grouping.

## Boundary cues help viewers assign words to the right topic <!-- role: reason -->

Clear boundaries reduce ambiguity about which words belong together, which supports integrating multiple words into one inferred topic. Color can improve performance even when spatial layout is mixed, and spatial grouping can approach the performance of whitespace-separated columns when grouping is preserved.

**Mechanism:** Boundary cues (gap or shared color) reduce grouping uncertainty, helping viewers bind words into a topic set before inferring the underlying concept.

**Evidence:** Semantically mapped color improved topic/category identification in Wordle-style layouts compared to monochrome Wordle baselines under time limits [@hearstEvaluationSemanticallyGrouped2020]. Spatially grouped semantic layouts performed better than semantically colored-but-ungrouped layouts, and were close to column layouts in accuracy even when explicit whitespace separation was reduced [@hearstEvaluationSemanticallyGrouped2020].

**Notes:** In the evaluations, colors were arbitrarily assigned per category but consistently applied within each group.

## When this boundary rule applies <!-- role: context -->

- **User Goal:** Recognize and name underlying topics from displayed keywords.
- **Task:** Category/topic identification from multiple cues.
- **Data:** Words partitioned into discrete topic groups (e.g., topics, categories).
- **Chart Setting:** Word cloud or word-cloud-like layout where group membership is not otherwise explicit.
- **Audience:** Viewers who may misinterpret arbitrary word-cloud styling as meaningful encodings.
- **Success Criterion:** Better accuracy and confidence in identifying topics, with fewer grouping errors.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot keep color assignments consistent within a group across updates or views. **Why:** Inconsistent color breaks the grouping signal and can mislead viewers about topic membership [@hearstEvaluationSemanticallyGrouped2020].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** White space separators reduce packing density, and multi-color designs can complicate visual balance. **Risk:** Overusing many saturated colors can make the display feel busy while still failing if groups are not coherent. **Mitigation:** Limit the design to group-level color consistency and ensure grouping coherence upstream.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Assigning colors arbitrarily per word rather than per semantic group. **Why it fails:** Viewers may treat color as meaningful; random color does not reliably encode group structure [@hearstEvaluationSemanticallyGrouped2020].
- **Mistake:** Using group colors without any consistent mapping of words to groups (i.e., words from a group appear in multiple colors). **Why it fails:** The viewer cannot reliably bind words into a topic, undermining topic inference [@hearstEvaluationSemanticallyGrouped2020].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers report that they “can’t tell what goes together” or produce mixed-topic guesses. **Quick Check:** Ask viewers to circle/mark which words belong to one inferred topic; frequent cross-group selection indicates weak demarcation. **Stronger Test:** A/B test semantically colored vs monochrome (or grouped vs ungrouped) under a short exposure and compare correct topic counts.

## What to do instead <!-- role: fix -->

- Assign exactly one color per semantic group and apply it to all words in that group.
- Add whitespace gaps between groups when the layout is otherwise dense or when groups are numerous.
- If whitespace must be minimized, enforce tight spatial proximity within each group and preserve group color consistency.
- If neither whitespace nor reliable color grouping is feasible, use a structured grouped list instead of a word cloud.
