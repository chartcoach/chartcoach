---
id: use-more-distinct-colors-to-improve-visualization-memorability
title: Use More Distinct Colors to Improve Memorability
bibliography: references.bib
description: Visualizations with more distinct colors are more memorable than monochrome
  or low-color charts.
labels:
- chart:any
- task:recall
- visual:color
- impact:memorability
- data:any
- audience:general
- evidence:empirical
---

## The Rule <!-- role: advice -->

Use multiple distinct colors (especially 7+ distinct colors when appropriate) if memorability is a priority.

## The Logic <!-- role: reason -->

More distinct colors increase visual distinctiveness, which improves recognition in a rapid image-memory setting.

- **The Principle:** Distinctiveness through color variation
- **The Evidence:** Visualizations with ≥7 colors were more memorable than those with 2–6 colors, and both outperformed 1-color/black-and-white; the ≥7 vs 1-color difference remained significant even after removing pictorial visualizations [@borkinWhatMakesVisualization2013a].

## Where to Apply <!-- role: context -->

- **User Goal:** Recognize the visualization later after brief exposure
- **Data Type:** Any; especially when many charts in a set might otherwise look similar
- **Audience:** Broad audiences in fast-scrolling environments

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are intentionally controlling for pictograms and other strong cues and want to isolate non-color effects.
- **Reason:** Color is one of the attributes with a measurable relationship to memorability and may confound an experiment/design comparison [@borkinWhatMakesVisualization2013a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual simplicity and a minimalist aesthetic.
- **The Risk:** More colors can make a design feel busy; memorability gains do not imply improved comprehension [@borkinWhatMakesVisualization2013a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding many colors without a rationale, assuming it automatically improves understanding.
- **Why it fails:** The paper measures memorability of the visualization as an image, not comprehension of the data [@borkinWhatMakesVisualization2013a].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart is monochrome or uses only one hue/gradient.
- **The Test:** Count distinct colors used for marks/regions; if it’s effectively 1 (or very few), you’re likely missing a memorability cue identified in the study [@borkinWhatMakesVisualization2013a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Introduce additional distinct colors in key elements so the chart is less visually confusable with similar charts.
- **Best Fix:** Apply a multi-color scheme that creates clear categorical/structural variation across the visualization (not just a single gradient) [@borkinWhatMakesVisualization2013a].
