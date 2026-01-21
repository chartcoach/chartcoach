---
id: expect-centroid-like-shape-cues-to-drive-mean-judgments
title: Expect Centroid-Like Shape Cues to Drive Mean Judgments
bibliography: references.bib
description: "Design mean comparisons knowing that viewers may rely on a chart\u2019\
  s visual centroid rather than arithmetic averaging."
labels:
- chart:bar
- task:compare
- visual:position
- visual:shape
- impact:clarity
- data:categorical
- audience:general
- concept:perceptual-proxies
---

## The Rule <!-- role: advice -->

When designing side-by-side bar charts for mean comparison, check whether the chart’s overall “center of mass” (centroid) could mislead the judgment; avoid arrangements where centroid strongly favors the lower-mean series.

## The Logic <!-- role: reason -->

The paper finds the strongest evidence (in their proxy set) that centroid manipulation can increase the titer needed to correctly choose the higher mean, implying centroid (or correlated shape proxies) can drive incorrect mean judgments [@ondovRevealingPerceptualProxies2021]. This aligns with their framing that the visual system may substitute heuristic spatial features for statistics.

- **The Principle:** Center-of-mass heuristic (centroid as a proxy for average magnitude)
- **The Evidence:** Centroid showed the clearest tendency to be “deceptive” for MaxMean in their threshold modeling [@ondovRevealingPerceptualProxies2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Picking which of two groups has a higher mean from bar charts
- **Data Type:** Multi-bar series where distribution shape can vary even when mean differences are small
- **Audience:** Mixed/unknown audiences; brief viewing or dashboard scanning [@ondovRevealingPerceptualProxies2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You deliberately want to emphasize distribution shape rather than mean.
- **Reason:** Then centroid-driven impressions may be acceptable or desired.

## The Price <!-- role: costs -->

- **The Sacrifice:** Constraining shapes to avoid misleading centroids can limit faithful presentation of real distributions.
- **The Risk:** Over-correcting may reduce sensitivity to genuine structure (clusters, skew).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Only adding numeric mean labels while leaving a strongly misleading shape.
- **Why it fails:** Under rapid judgments, the perceptual proxy can dominate; the paper’s whole adversarial setup demonstrates proxy competition with the correct statistic [@ondovRevealingPerceptualProxies2021].

## How to Check <!-- role: check -->

- **Visual Sign:** One chart “feels” shifted right overall even if many bars are small (a centroid pull from a subset of bars).
- **The Test:** Compute or approximate which chart’s mass appears more right-shifted; if that conflicts with the true mean, the design is vulnerable [@ondovRevealingPerceptualProxies2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a prominent mean reference and reduce shape-induced centroid shifts (e.g., reduce dominance of extreme bars that pull the centroid).
- **Best Fix:** Validate with a brief-exposure comparison test (similar to the paper’s impression trials) to ensure centroid is not overriding mean across typical viewers [@ondovRevealingPerceptualProxies2021].
