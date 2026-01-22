---
id: avoid-legends-that-force-color-memory
title: Label marks directly instead of using a separate color legend when identification
  matters
bibliography: references.bib
description: Reduce working-memory load by eliminating lookups between a legend and
  the data marks.
labels:
- chart:pie
- task:lookup
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- accessibility:cognition
---

## Put labels next to the data marks they describe <!-- role: advice -->

Label categories directly on or near the corresponding marks when viewers must identify items by color. Avoid designs that require repeated glances between marks and a distant legend.

## Legends create unnecessary working-memory demands <!-- role: reason -->

Graph reading is constrained by limited short-term memory, so forcing viewers to remember a color and search for it elsewhere slows comprehension and increases errors. Keeping text close to the relevant marks reduces the need for back-and-forth eye movements and memory maintenance.

**Mechanism:** Separating identifiers (legend) from data marks forces a hold-and-match process in working memory while attention shifts across the display.

**Evidence:** Graph designs that require glancing around the visualization and relying on short-term memory (such as distant legends) impose avoidable cognitive load and make comparisons harder [@zacksDesigningGraphsDecisionMakers2020].

**Notes:** This issue compounds when the viewer must integrate multiple lookups to answer higher-level questions.

## Use this when identity-by-color is part of the task <!-- role: context -->

- **User Goal:** Identify which category corresponds to which mark and make comparisons by category.
- **Task:** Lookup, match, summarize by group (e.g., “which region is larger overall?”).
- **Data:** Multiple categorical series encoded by color.
- **Chart Setting:** Static figures, print, slides, or small screens where scanning is costly.
- **Audience:** Non-experts or anyone under time pressure.
- **Success Criterion:** Fewer lookup errors; faster category-based comparisons.

## When space is too constrained for direct labels <!-- role: exceptions -->

**Break it when:** Marks are too dense or numerous to label without severe overlap. **Why:** Direct labels can create clutter that harms legibility.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Direct labeling uses space and may reduce room for data. **Risk:** Over-labeling can overwhelm the display. **Mitigation:** Label only the most decision-relevant series and simplify the rest.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a legend for a chart where viewers must repeatedly compare categories. **Why it fails:** Each comparison becomes a slow lookup that taxes working memory [@zacksDesigningGraphsDecisionMakers2020].
- **Mistake:** Placing the legend far from the marks or using many similar colors. **Why it fails:** Distance and similarity increase lookup difficulty and misidentification [@zacksDesigningGraphsDecisionMakers2020].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers point to the wrong category or hesitate while checking the legend repeatedly. **Quick Check:** Ask someone to identify two categories without tracing to the legend with their finger; if they can’t, labeling is too indirect. **Stronger Test:** Compare time-to-answer for two category questions with legend vs direct labels.

## What to do instead <!-- role: fix -->

- Place text labels adjacent to the marks (or slices) they identify.
- Use grouping and spatial proximity so categories are identifiable even with minimal labeling.
- Reduce the number of colored categories shown at once by filtering or aggregation.
- Use brief annotations for the few categories that matter most to the decision.
