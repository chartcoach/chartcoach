---
id: keep-axes-stable-across-hops-frames
title: Keep Axes Stable Across HOPs Frames
bibliography: references.bib
description: Maintain a consistent scale and mapping across frames so viewers can
  integrate outcomes over time.
labels:
- chart:animation
- task:compare
- visual:position
- impact:clarity
- data:uncertainty
- audience:novice
- uncertainty:hops
---

## The Rule <!-- role: advice -->

Use a fixed axis range and consistent visual mapping across all HOPs frames.

## The Logic <!-- role: reason -->

HOPs require viewers to integrate information across frames; changing scales breaks perceptual comparability and increases the cognitive load of integration. The paper explicitly notes that maintaining visual stability (e.g., fixed y-axis range) reduces difficulty of visual integration across frames.

- **The Principle:** Visual stability supports temporal integration
- **The Evidence:** [@hullmanHypotheticalOutcomePlots2015]

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating frequencies/probabilities or comparing outcomes across variables over frames.
- **Data Type:** Any animated sequence of sampled outcomes (HOPs).
- **Audience:** General viewers relying on perceptual comparison and counting.

## When to Break It <!-- role: exceptions -->

- **Scenario:** None supported by this paper’s evidence.
- **Reason:** The study framing and discussion emphasize stability as a design requirement for HOPs to be interpretable. [@hullmanHypotheticalOutcomePlots2015]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less automatic “zoom-to-fit” readability for narrow distributions.
- **The Risk:** If the fixed range is too large, marks may appear compressed, potentially reducing precision for some univariate judgments. [@hullmanHypotheticalOutcomePlots2015]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Auto-scaling each frame to its own min/max to “use space better.”
- **Why it fails:** It destroys comparability, making counting/integration across time unreliable. [@hullmanHypotheticalOutcomePlots2015]

## How to Check <!-- role: check -->

- **Visual Sign:** The same numeric value appears at different pixel heights across frames.
- **The Test:** Freeze two frames and verify that identical values map to identical positions on the axis. [@hullmanHypotheticalOutcomePlots2015]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Lock the y-axis domain for the entire animation.
- **Best Fix:** Precompute a global domain for the shown distribution(s) and enforce it consistently in every frame and every variable. [@hullmanHypotheticalOutcomePlots2015]
