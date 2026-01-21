---
id: encode-more-important-information-with-more-accurate-channels
title: Encode More Important Data with More Accurate Channels
bibliography: references.bib
description: Assign the highest-accuracy encodings to the most important relations
  using a lexicographic importance ordering.
labels:
- chart:any
- task:prioritize
- visual:encoding
- impact:accuracy
- data:multivariate
- audience:any
- principle:importance-ordering
- source:mackinlay-1986
---

## The Rule <!-- role: advice -->

Map your most important variables to the highest-accuracy perceptual channels, and push less important variables to lower-accuracy channels.

## The Logic <!-- role: reason -->

When multiple designs require the same set of perceptual tasks overall, you still need a decision rule; the paper extends the effectiveness ranking with a lexicographic principle: encode more important information more effectively.

- **The Principle:** Principle of Importance Ordering
- **The Evidence:** The paper’s scatter-plot comparison shows choosing which variable gets position vs area depends on importance ordering [@mackinlayAutomatingDesignGraphical1986b].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand the key relationships first while still seeing secondary variables
- **Data Type:** Multiple relations/variables (e.g., several measures per item)
- **Audience:** Any

## When to Break It <!-- role: exceptions -->

- **Scenario:** A “secondary” variable is the one users must read precisely to complete a task, even if it is conceptually secondary.
- **Reason:** Task demands can override nominal “importance” ordering; otherwise you optimize the wrong objective [@mackinlayAutomatingDesignGraphical1986b].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less important variables may be harder to read accurately.
- **The Risk:** If you mis-rank importance, you may allocate the best channels to the wrong variables and harm the task [@mackinlayAutomatingDesignGraphical1986b].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Giving every variable an equally “strong” encoding (e.g., multiple axes and heavy styling everywhere).
- **Why it fails:** It ignores perceptual limits and removes the intended prioritization, making the display harder to interpret [@mackinlayAutomatingDesignGraphical1986b].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart’s most salient encodings emphasize a variable that is not the one the viewer cares about.
- **The Test:** Write the variables in priority order, then verify the top variables use the top-ranked perceptual tasks (e.g., position over area for quantitative) [@mackinlayAutomatingDesignGraphical1986b].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap channel assignments so the top variable uses a higher-ranked perceptual task.
- **Best Fix:** Redesign the chart around the top relations first, then add secondary encodings only when they don’t conflict or degrade the primary reading [@mackinlayAutomatingDesignGraphical1986b].
