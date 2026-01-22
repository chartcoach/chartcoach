---
id: emphasize-distribution-means-in-density-plots-in-proportion-to-certainty
title: Emphasize each distribution mean in density plots with intensity that increases
  as uncertainty decreases
bibliography: references.bib
description: Add a mean-focused highlight to density plots so individual locations
  remain findable while still reflecting uncertainty.
labels:
- chart:scatter
- chart:parallel-coordinates
- task:locate
- visual:luminance
- impact:trust
- data:uncertain
- audience:expert
- complexity:advanced
---

## Make distribution means identifiable without reintroducing misleading saliency <!-- role: advice -->

In a density plot, add mean emphasis by increasing intensity at each distribution’s mean by a constant scale factor so that more certain samples receive stronger emphasis than uncertain ones. Keep the emphasis proportional to the distribution peak so uncertain samples do not regain strong visual saliency.

## Certainty-scaled mean emphasis preserves identifiability while keeping uncertainty blurred <!-- role: reason -->

For normal distributions, the maximum value occurs at the mean, and smaller variance increases the peak height. Scaling the distribution center therefore creates a discrete, identifiable feature that naturally fades as uncertainty grows, maintaining the goal that saliency matches confidence.

**Mechanism:** Peak-height differences convert uncertainty magnitude into contrast differences at the mean, making confident means pop out while uncertain means remain faint and hard to preattentively group.

**Evidence:** Mean emphasis helps viewers locate the contributing distribution centers while still deemphasizing uncertain values, and it is described as scaling the distribution center so certainty increases emphasis more than uncertainty does [@fengMatchingVisualSaliency2010].

**Notes:** This behaves like overlaying points whose transparency (or brightness) is tied to the distribution peak.

## When mean emphasis is useful in uncertain density plots <!-- role: context -->

- **User Goal:** Find approximate locations of individual samples while still interpreting the overall density under uncertainty.
- **Task:** Identify which samples contribute to a region of density, especially in smaller datasets.
- **Data:** Per-sample uncertainty modeled as distributions (for example, normal distributions).
- **Chart Setting:** Density plot where over-plotting is not extreme and viewers benefit from seeing individual means.
- **Audience:** Analysts doing interactive exploration who may brush or query specific regions.
- **Success Criterion:** Means are findable without creating crisp, misleading “point clusters” from uncertain samples.

## When not to use mean emphasis <!-- role: exceptions -->

**Break it when:** The dataset is so dense that many means overlap heavily. **Why:** Overlapping mean highlights reduce the benefit of identifiability and can collapse back into a bright mass that is better represented by the PDF alone [@fengMatchingVisualSaliency2010].

## Tradeoffs of mean emphasis <!-- role: costs -->

**Sacrifice:** Additional visual structure is added on top of the PDF, which can compete with density cues. **Risk:** Over-emphasis can reintroduce attention to uncertain regions if not tied to distribution peak behavior. **Mitigation:** Keep emphasis tied to the modeled distribution peak so uncertainty still reduces contrast.

## Common mistakes with mean emphasis <!-- role: mistakes -->

- **Mistake:** Overlay identical, high-contrast mean markers for all samples. **Why it fails:** It makes uncertain values as visually salient as certain ones, undermining the goal of matching saliency to confidence [@fengMatchingVisualSaliency2010].
- **Mistake:** Use mean markers without the underlying PDF. **Why it fails:** It reverts the display to a discrete plot that can encourage false positives from uncertain samples [@fengMatchingVisualSaliency2010].

## Quick checks for appropriate mean emphasis <!-- role: check -->

**Failure Sign:** Uncertain samples look as “sharp” or attention-grabbing as certain samples. **Quick Check:** Spot-check high-variance samples; their mean emphasis should be faint compared to low-variance samples [@fengMatchingVisualSaliency2010]. **Stronger Test:** Temporarily hide the PDF layer; mean emphasis alone should not create apparent clusters in regions dominated by high uncertainty.

## What to do instead if mean emphasis causes clutter <!-- role: fix -->

- Remove mean emphasis and rely on the pure PDF when mean overlap is high [@fengMatchingVisualSaliency2010].
- Show means only for a selected subset (for example, brushed distributions) while keeping the full PDF as context [@fengMatchingVisualSaliency2010].
- Use probabilistic plots to show discrete samples over time rather than persistent mean markers [@fengMatchingVisualSaliency2010].
- Provide linked detail views for sample identity rather than forcing identity into the density plot [@fengMatchingVisualSaliency2010].
