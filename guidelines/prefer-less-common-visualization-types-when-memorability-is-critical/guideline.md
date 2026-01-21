---
id: prefer-less-common-visualization-types-when-memorability-is-critical
title: Prefer Less-Common Visualization Types When Memorability Is Critical
bibliography: references.bib
description: Unique visualization types (e.g., diagrams, grids/matrices, trees/networks)
  are more memorable than common charts like bars and lines.
labels:
- chart:diagram
- task:recall
- visual:layout
- impact:memorability
- data:any
- audience:general
- complexity:advanced
- evidence:empirical
---

## The Rule <!-- role: advice -->

When you need a visualization to be remembered, consider using a more unique visualization type (e.g., diagrams, grid/matrix, trees/networks) instead of defaulting to bars/lines/tables.

## The Logic <!-- role: reason -->

Common chart types are visually uniform and easier to confuse with one another, while distinctive layouts provide stronger item-specific cues in memory.

- **The Principle:** Distinctiveness reduces interference among similar visuals
- **The Evidence:** Diagrams (and other less-common types like grids/matrices and trees/networks) scored higher on memorability than bars, lines, points, and tables; this trend remained after removing pictorial visualizations [@borkinWhatMakesVisualization2013a].

## Where to Apply <!-- role: context -->

- **User Goal:** Remembering and recognizing a visualization among many
- **Data Type:** Any where multiple encodings are plausible
- **Audience:** Viewers exposed to many charts (reports, media feeds, presentations)

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is explicitly to use “familiar” chart forms.
- **Reason:** The paper’s findings contradict the idea that familiarity improves memorability; choosing a common form may be intentional for reasons other than memorability [@borkinWhatMakesVisualization2013a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Familiarity and standardization.
- **The Risk:** A more unique type may be remembered without necessarily being better understood, since the study does not evaluate comprehension [@borkinWhatMakesVisualization2013a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using bars/lines by default for every dataset and trying to “differentiate” only with minor styling.
- **Why it fails:** The study suggests that within-category similarity contributes to confusion (higher false alarms) for common forms [@borkinWhatMakesVisualization2013a].

## How to Check <!-- role: check -->

- **Visual Sign:** Your chart looks like many other standard charts in the same report/site.
- **The Test:** Place it among 10 similar charts; if it is hard to pick out at a glance as “different,” it likely lacks type-level distinctiveness tied to memorability [@borkinWhatMakesVisualization2013a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Explore an alternative layout (diagrammatic structure, matrix-like encoding, network/tree form) that fits the same message.
- **Best Fix:** Choose a visualization type whose overall structure is intrinsically distinctive while still representing the data faithfully [@borkinWhatMakesVisualization2013a].
