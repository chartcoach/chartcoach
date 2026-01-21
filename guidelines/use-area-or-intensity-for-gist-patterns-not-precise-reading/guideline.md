---
id: use-area-or-intensity-for-gist-patterns-not-precise-reading
title: Use Area or Intensity Only for Big-Picture Patterns
bibliography: references.bib
description: Reserve low-precision encodings like area and intensity for rapid overview
  patterns, not exact comparisons.
labels:
- chart:heatmap
- task:detect-pattern
- visual:intensity
- impact:clarity
- data:matrix
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->

Use **area** and **intensity** encodings to communicate broad patterns (clusters, hotspots, rough gradients), not fine-grained numeric comparisons.

## The Logic <!-- role: reason -->

- **The Principle:** Some channels are excellent for parallel “gist” extraction but poor for exact magnitude estimation.
- **The Evidence:** The paper contrasts how color-coded grids make patterns trivial while noting intensity/area are far less precise than position/length for reading values [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Rapidly spotting structure (e.g., where values are high/low; whether groups separate).
- **Data Type:** Large arrays/matrices where overview matters.
- **Audience:** Viewers scanning for patterns before drilling down.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users must make close calls (e.g., rank near-ties, compute ratios).
- **Reason:** Area/intensity will introduce large estimation error for those tasks [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up numerical precision.
- **The Risk:** Viewers may over-interpret intensity differences as precise differences.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more color steps or saturating the palette to “make it clearer.”
- **Why it fails:** More steps do not change the underlying low precision of intensity judgments [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** People argue about which of two similarly colored regions is higher.
- **The Test:** Ask viewers to rank 5 nearby cells/areas; if they can’t reliably, the display is being used for the wrong task.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add numeric readouts for exact values on demand (or annotate key cells).
- **Best Fix:** Use position/length for the decision-critical comparisons and keep intensity for the overview layer [@zacksDesigningGraphsDecisionMakers2020].
