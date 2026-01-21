---
id: assess-colormap-local-global-uniformity-with-speed-variance
title: Assess Colormap Uniformity with Speed Variance
bibliography: references.bib
description: Evaluate whether a continuous colormap changes perceptually evenly by
  measuring the standard deviation of its local and global speeds.
labels:
- chart:colormap
- task:evaluate
- visual:color
- impact:clarity
- data:quantitative
- audience:expert
- scope:continuous-colormap
---

## The Rule <!-- role: advice -->

Assess a continuous colormap’s uniformity by measuring variability in speed: use the **standard deviation of local speed** for local uniformity and the **standard deviation of global speed** for global uniformity.

## The Logic <!-- role: reason -->

- **The Principle:** A colormap is more uniform when equal steps in the encoded value correspond to equal perceived color differences, which is operationalized as (near-)constant speed; deviations in speed quantify non-uniformity.
- **The Evidence:** Local uniformity is equivalent to constant local speed and can be evaluated via the standard deviation of local speed; global uniformity corresponds to constant global speed and can be evaluated via the standard deviation of global speed [@bujackGoodBadUgly2018]. This type of structured theoretical guidance is explicitly collated for recommendation systems [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Ensuring even perceptual progression along a continuous color scale (avoiding “jumps” or “dead zones”).
- **Data Type:** Quantitative data mapped continuously to color.
- **Audience:** Visualization system builders and designers performing colormap assessment.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not evaluating a continuous colormap (e.g., nominal palettes).
- **Reason:** The framework’s uniformity measures are formulated for continuous colormap curves with sampled points [@bujackGoodBadUgly2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional computation (pairwise distances or neighbor distances) and sensitivity to the chosen ∆E metric and sampling.
- **The Risk:** A colormap may appear uniform under one metric (e.g., ∆E76) but not under another (e.g., ∆E00), so conclusions can vary by metric choice [@bujackGoodBadUgly2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming a “straight-line” looking gradient is automatically uniform without measuring.
- **Why it fails:** The paper shows uniformity depends on measured speed in a perceptual metric and can differ across metrics and across local vs global interpretations [@bujackGoodBadUgly2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Some value ranges look overly emphasized while others look compressed or flat.
- **The Test:** Compute σ of local speed (neighbor pairs) and σ of global speed (all pairs); lower values indicate higher uniformity under the chosen metric [@bujackGoodBadUgly2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap to a colormap with lower local-speed standard deviation under the same evaluation setup.
- **Best Fix:** Include local/global speed-variance thresholds as explicit evaluation constraints when selecting continuous colormaps in recommendation workflows [@zengReviewCollationGraphical2023; @bujackGoodBadUgly2018].
