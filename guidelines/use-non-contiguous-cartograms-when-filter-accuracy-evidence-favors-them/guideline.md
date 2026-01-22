---
id: use-non-contiguous-cartograms-when-filter-accuracy-evidence-favors-them
title: Use non-contiguous cartograms when your filtering condition matches one where
  they are more accurate than contiguous
bibliography: references.bib
description: A filtering condition showed non-contiguous cartograms outperforming
  contiguous cartograms in accuracy.
labels:
- chart:cartogram
- task:filter
- visual:area
- visual:position
- impact:accuracy
- data:geospatial
- audience:general
- variant:non-contiguous
---

## Prefer non-contiguous cartograms for the filtering condition they win <!-- role: advice -->

Use a non-contiguous cartogram for filtering when your filtering question format matches a condition where non-contiguous cartograms are significantly more accurate than contiguous cartograms. Treat this as condition-specific rather than a general rule for all filtering.

## Why non-contiguous can win on accuracy for some filtering setups <!-- role: reason -->

Filtering performance can depend on how easily individual regions can be visually isolated and identified under the exact filtering prompt; separating regions can sometimes reduce confusion and improve correctness.

**Mechanism:** Increased separation between regions can reduce misidentification under certain filtering question formats.

**Evidence:** In one filtering condition, non-contiguous cartograms ranked higher than contiguous cartograms in accuracy, with a statistically significant difference reported between them [@nusratEvaluatingCartogramEffectiveness2018; @zengReviewCollationGraphical2023].

**Notes:** The same source contains other filtering conditions where the ordering differs, so the trigger is the filtering condition you match.

## When this condition-specific rule applies <!-- role: context -->

- **User Goal:** Get the most correct answers for a specific filtering prompt format.
- **Task:** Filter.
- **Data:** Regions on a map with a quantitative value encoded by area.
- **Chart Setting:** Choosing among cartogram variants for a fixed filtering question style.
- **Audience:** Users who need correctness more than adjacency fidelity.
- **Success Criterion:** Higher accuracy on the specific filtering prompt type.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your filtering prompts are closer to a filtering condition where contiguous cartograms are more accurate. **Why:** The evidence shows direction changes across filtering conditions.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may reduce the usefulness of adjacency cues for other tasks. **Risk:** Applying this outside the matching filtering condition can degrade performance. **Mitigation:** Map your prompts to the closest tested filtering condition before standardizing.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Generalizing “non-contiguous is better for filtering” without matching the filtering condition. **Why it fails:** The evidence includes multiple filtering outcomes with different winners.

## Quick tests <!-- role: check -->

**Failure Sign:** Users confuse regions or pick the wrong qualifying region under your filtering prompt. **Quick Check:** Replicate your filtering question format with both non-contiguous and contiguous cartograms and compare error rate. **Stronger Test:** A/B test the two variants in the actual product workflow and log correctness.

## What to do instead <!-- role: fix -->

- Use a contiguous cartogram if your filtering prompt aligns with the condition where contiguous ranks highest in accuracy.
- Optimize the filtering prompt wording or highlighting to reduce region confusion, then re-test.
- Offer both cartogram types and let users switch depending on the filtering question they are answering.
- If filtering is central, maintain a task-tuned default cartogram type per filtering prompt family.
