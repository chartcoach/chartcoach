---
id: prefer-near-square-bar-marks-to-minimize-recall-bias
title: Use Near-Square Bar Marks to Minimize Position Recall Bias
bibliography: references.bib
description: Square-like bar marks show little systematic over/underestimation when
  users reproduce bar-top positions from memory.
labels:
- chart:bar
- task:read-value
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- design:mark-shape
---

## The Rule <!-- role: advice -->

When you expect users to remember and reproduce bar heights, design bars to be closer to a 1:1 (square) width:height aspect ratio rather than extremely wide or extremely tall.

## The Logic <!-- role: reason -->

Memory for bar-top position is biased toward a prototypical square: wide bars get recalled as higher (overestimation), tall bars as lower (underestimation), while square bars show no systematic bias in the same paradigm. [@cejaTruthSquareAspect2021a]

- **The Principle:** Prototype attraction toward “square” reduces directional error when already at the prototype
- **The Evidence:** [@cejaTruthSquareAspect2021a]

## Where to Apply <!-- role: context -->

- **User Goal:** Recall a previously seen bar value accurately (e.g., “What was that bar’s height?”)
- **Data Type:** Single-bar or sparse-bar displays where a specific mark must be remembered
- **Audience:** General audiences; situations where quick memory-based judgments occur

## When to Break It <!-- role: exceptions -->

- **Scenario:** The mark’s aspect ratio is itself a deliberate encoding (e.g., designs where width and height both carry meaning).
- **Reason:** Pushing everything toward “square” could undermine the intended encoding or layout constraints. (The paper motivates that some designs intentionally use width/height separately.) [@cejaTruthSquareAspect2021a]

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose density (fewer bars fit) or require larger canvases to keep bars nearer to square.
- **The Risk:** Over-constraining to squares can reduce readability for categorical comparisons if spacing becomes tight.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making bars extremely thin to “emphasize position not area.”
- **Why it fails:** Very tall/thin bars are exactly the case that showed underestimation and higher variability. [@cejaTruthSquareAspect2021a]

## How to Check <!-- role: check -->

- **Visual Sign:** Bars look like “lines” (very tall/thin) or “slabs” (very wide/flat).
- **The Test:** Identify whether bars commonly exceed clearly extreme ratios (visually far from square) in the views users must remember. [@cejaTruthSquareAspect2021a]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase bar width for thin bars, or reduce width for overly wide bars, to move typical marks toward squarer shapes.
- **Best Fix:** Adjust layout (panel size, number of categories shown at once) so bars can remain closer to square without crowding. [@cejaTruthSquareAspect2021a]
