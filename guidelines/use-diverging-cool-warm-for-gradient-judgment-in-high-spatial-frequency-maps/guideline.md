---
id: use-diverging-cool-warm-for-gradient-judgment-in-high-spatial-frequency-maps
title: Use a cool-warm diverging colormap for gradient judgment in high-spatial-frequency
  maps
bibliography: references.bib
description: For judging which region is steeper in a continuous quantitative map
  at high spatial frequency, a cool-warm colormap outperforms most tested alternatives.
labels:
- chart:heatmap
- task:aggregate
- visual:color
- impact:accuracy
- data:spatial
- audience:general
- domain:continuous-map
- condition:high-spatial-frequency
---

## Gradient comparison in complex continuous maps with cool-warm <!-- role: advice -->

Use a cool-warm diverging colormap when users must judge gradients (steepness differences) in a continuous quantitative map with high spatial frequency. Prefer it over the tested greyscale, single-hue, sequential, and spiral alternatives for this condition.

## Why cool-warm helps gradient judgment at high spatial frequency <!-- role: reason -->

Colormap choice can amplify or reduce perceptual contrast in local changes, which affects accuracy when comparing steepness between regions, especially when the underlying field has many small features (high spatial frequency).

**Mechanism:** A diverging palette can make changes around a midpoint more distinguishable, improving discrimination when comparing local gradient strength.

**Evidence:** For a gradient-perception condition represented in the extracted results (aggregate-2), the ranking places cool-warm first, followed by rainbow and blue-yellow, with cool-warm significantly outperforming multiple other colormaps in the recorded significance pairs [@redaGraphicalPerceptionContinuous2018]. This task- and condition-specific rule is included as structured evidence for visualization recommendation in the broader collation effort [@zengReviewCollationGraphical2023].

**Notes:** This is specific to the extracted gradient-perception condition and should not be generalized to all map-reading tasks.

## When to apply this rule <!-- role: context -->

- **User Goal:** Decide which of two regions has the steeper average gradient.
- **Task:** Aggregate-style comparison (steepness/gradient judgment between regions).
- **Data:** Continuous spatial field with high spatial frequency (many small features).
- **Chart Setting:** Continuous pseudocolor map where users compare two highlighted regions.
- **Audience:** General audiences with normal color vision (as screened in the study setting).
- **Success Criterion:** Higher accuracy in selecting the steeper region.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The user’s primary task is value lookup at a specific location. **Why:** The retrieve-value ranking places rainbow above cool-warm in the extracted results.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may reduce accuracy for other tasks that favor different colormaps. **Risk:** If the map does not actually have high spatial frequency, the advantage may not hold. **Mitigation:** Gate this rule on a “high spatial frequency / complex surface” detection or user-declared task mode.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Reusing a value-lookup-optimized palette for gradient judgment in complex maps. **Why it fails:** The extracted rankings for gradient judgment at high spatial frequency differ from the retrieve-value ranking.

## Quick tests <!-- role: check -->

**Failure Sign:** Readers disagree widely on which region is steeper or perform near chance on simple gradient-comparison questions. **Quick Check:** Present a few pairs of highlighted regions and see whether most readers pick the same “steeper” region. **Stronger Test:** A/B test cool-warm against your current palette on the same gradient-comparison prompts and track accuracy.

## What to do instead <!-- role: fix -->

- Use blue-yellow if you want another high-ranking option for the same extracted condition.
- Use rainbow if you must prioritize a scheme that also ranks highly in the same extracted gradient condition while aligning with your value-lookup needs.
- Provide a task toggle that switches palettes between gradient-judgment mode (cool-warm) and value-lookup mode (rainbow).
