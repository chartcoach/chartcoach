---
id: emphasize-distribution-means-in-proportion-to-certainty
title: Emphasize Distribution Means Proportionally to Certainty
bibliography: references.bib
description: "Overlay or scale intensity at each distribution\u2019s mean so individual\
  \ items remain locatable while uncertain ones fade."
labels:
- chart:scatter
- chart:parallel-coordinates
- task:locate
- visual:luminance
- impact:readability
- data:uncertainty
- audience:expert
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When density plots hide individual items, add mean emphasis by boosting intensity at each distribution mean, and let that emphasis naturally diminish with higher uncertainty.

## The Logic <!-- role: reason -->

For normal distributions, the peak value occurs at the mean and becomes higher as σ decreases; scaling the center intensity therefore highlights certain points more than uncertain ones, preserving identifiability without making uncertain points salient.

- **The Principle:** Certainty-weighted discrete anchors within a continuous density field
- **The Evidence:** [@fengMatchingVisualSaliency2010]

## Where to Apply <!-- role: context -->

- **User Goal:** See where individual uncertain observations sit while still benefiting from density summarization
- **Data Type:** Uncertain data where distributions have visible means (e.g., normal) and over-plotting is not extreme
- **Audience:** Analysts doing exploratory selection and follow-up investigation

## When to Break It <!-- role: exceptions -->

- **Scenario:** Extremely large datasets where many means overlap densely
- **Reason:** Mean emphasis becomes less informative; users should rely on the density summary instead [@fengMatchingVisualSaliency2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional visual complexity and potential clutter
- **The Risk:** If overdone, mean emphasis can reintroduce the very saliency you are trying to avoid for uncertain points [@fengMatchingVisualSaliency2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Emphasize all means equally (constant-bright point overlay)
- **Why it fails:** It makes uncertain points pop like reliable points, reintroducing false positives [@fengMatchingVisualSaliency2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Uncertain points’ means look as bright/sharp as certain points
- **The Test:** Compare two points with very different σ; the lower-σ mean should be noticeably more emphasized [@fengMatchingVisualSaliency2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Scale mean emphasis by a function that increases as σ decreases (e.g., proportional to peak height)
- **Best Fix:** Combine mean emphasis with the underlying PDF so the user can read both mean locations and uncertainty extent simultaneously [@fengMatchingVisualSaliency2010].
